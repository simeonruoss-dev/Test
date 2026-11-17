#!/usr/bin/env python3
"""Vollautomatische Videoproduktion aus schnittplan.json.
Aufruf: python3 tools/video/produziere.py videos/<slug> [--tempo 1.0] [--nur ton|folien|schnitt|qc]
Stufen: 1 Ton (Piper-TTS je Segment) -> 2 Folien (Playwright) -> 3 Schnitt (ffmpeg) -> 4 Mastering (-14 LUFS)
        -> 5 Untertitel (SRT) -> 6 Qualitätsprüfung (qc-bericht.md)
"""
import argparse, json, re, subprocess, sys, wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "tts"))
from vertonen import lexikon_anwenden, STD_STIMME  # noqa: E402

FPS = 25
PAD_VOR, PAD_NACH = 0.35, 0.55  # Atempausen je Folie (s)
LUFS_ZIEL, TP_ZIEL = -14.0, -1.5


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"Fehler: {' '.join(map(str, cmd))[:300]}\n{r.stderr[-1500:]}")
    return r


def wav_dauer(p):
    with wave.open(str(p), "rb") as w:
        return w.getnframes() / w.getframerate()


def stufe_ton(d, plan, tempo):
    from piper import PiperVoice, SynthesisConfig
    stimme = PiperVoice.load(str(STD_STIMME)); cfg = SynthesisConfig(length_scale=tempo)
    roh = d / "build" / "ton"; roh.mkdir(parents=True, exist_ok=True)
    timing, t = {}, 0.0
    for s in plan["segmente"]:
        p = roh / f"{s['id']}.wav"
        with wave.open(str(p), "wb") as wf:
            stimme.synthesize_wav(lexikon_anwenden(s["sprechtext"]), wf, syn_config=cfg)
        sprech = wav_dauer(p)
        dauer = round((sprech + PAD_VOR + PAD_NACH) * FPS) / FPS  # auf Frames gerundet -> exakte Synchronität
        timing[s["id"]] = {"start": round(t, 3), "dauer": dauer, "sprech": round(sprech, 3)}
        t += dauer
    (d / "build" / "timing.json").write_text(json.dumps({"gesamt": round(t, 3), "segmente": timing}, indent=1))
    print(f"[Ton] {len(timing)} Segmente, {t/60:.1f} Min.")


def stufe_folien(d):
    sh(["node", str(ROOT / "tools/video/folien.mjs"), str(d)]); print("[Folien] gerendert")


def stufe_schnitt(d, plan):
    b = d / "build"; tm = json.loads((b / "timing.json").read_text())["segmente"]
    clips = b / "clips"; clips.mkdir(exist_ok=True)
    # Video: je Folie ein Clip mit sanftem Zoom (Ken-Burns) + kurzer Einblendung
    for s in plan["segmente"]:
        du = tm[s["id"]]["dauer"]; n = int(round(du * FPS))
        vf = (f"scale=3840:-1,zoompan=z='1+0.025*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d={n}:s=1920x1080:fps={FPS},fade=t=in:st=0:d=0.25:color=0xF7F8FA,format=yuv420p")
        sh(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(b / "folien" / f"{s['id']}.png"),
            "-vf", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
            str(clips / f"{s['id']}.mp4")])
    (b / "clips.txt").write_text("".join(f"file 'clips/{s['id']}.mp4'\n" for s in plan["segmente"]))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(b / "clips.txt"), "-c", "copy", str(b / "bild.mp4")])
    # Ton: Segmente mit Pausen exakt auf Clipdauer
    teile = []
    for s in plan["segmente"]:
        t = tm[s["id"]]; ziel = b / "ton" / f"{s['id']}-pad.wav"
        sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(b / "ton" / f"{s['id']}.wav"), "-af",
            f"adelay={int(PAD_VOR*1000)},apad,atrim=0:{t['dauer']}", "-ar", "48000", "-ac", "1", str(ziel)])
        teile.append(ziel)
    (b / "ton.txt").write_text("".join(f"file 'ton/{p.name}'\n" for p in teile))
    sh(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(b / "ton.txt"), str(b / "stimme-roh.wav")])
    print("[Schnitt] Bild- und Tonspur montiert")


def stufe_mastering(d):
    b = d / "build"
    kette = "highpass=f=80,lowpass=f=11000,deesser=i=0.4,acompressor=threshold=-20dB:ratio=3:attack=10:release=200:makeup=2"
    r = sh(["ffmpeg", "-y", "-i", str(b / "stimme-roh.wav"), "-af", f"{kette},loudnorm=I={LUFS_ZIEL}:TP={TP_ZIEL}:LRA=7:print_format=json", "-f", "null", "-"])
    m = json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}") + 1])
    ln = (f"loudnorm=I={LUFS_ZIEL}:TP={TP_ZIEL}:LRA=7:measured_I={m['input_i']}:measured_TP={m['input_tp']}"
          f":measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(b / "stimme-roh.wav"), "-af", f"{kette},{ln}", "-ar", "48000", "-ac", "2", str(b / "ton-master.wav")])
    # Nachmessung + Feinkorrektur (loudnorm unterschätzt bei Sprachpausen) mit True-Peak-Begrenzer
    e = sh(["ffmpeg", "-nostats", "-i", str(b / "ton-master.wav"), "-af", "ebur128", "-f", "null", "-"]).stderr
    ist = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); gain = LUFS_ZIEL - ist
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(b / "ton-master.wav"), "-af",
        f"volume={gain:.2f}dB,alimiter=limit={10 ** (TP_ZIEL / 20):.3f}:level=disabled", "-ar", "48000", str(b / "ton-final.wav")])
    out = d / "export"; out.mkdir(exist_ok=True)
    sh(["ffmpeg", "-y", "-loglevel", "error", "-i", str(b / "bild.mp4"), "-i", str(b / "ton-final.wav"), "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out / "video.mp4")])
    sh(["cp", str(b / "thumbnail.png"), str(out / "thumbnail.png")])
    print("[Mastering] Ton zweistufig auf -14 LUFS normalisiert, Export erstellt")


def ts(x):
    h, r = divmod(x, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)) % 1000:03d}"


def stufe_untertitel(d, plan):
    tm = json.loads((d / "build" / "timing.json").read_text())["segmente"]; zeilen, i = [], 1
    for s in plan["segmente"]:
        t = tm[s["id"]]; text = re.sub(r"\s+", " ", s["sprechtext"]).strip()
        saetze = [x for x in re.split(r"(?<=[.!?:])\s+", text) if x]
        bloecke = []
        for sz in saetze:  # lange Sätze an Kommas teilen (max. ~84 Zeichen)
            while len(sz) > 84:
                k = sz.rfind(",", 0, 84); k = k if k > 30 else sz.rfind(" ", 0, 84)
                bloecke.append(sz[:k + 1].strip()); sz = sz[k + 1:].strip()
            bloecke.append(sz)
        gesamt = sum(len(x) for x in bloecke); start = t["start"] + PAD_VOR
        for bl in bloecke:
            dauer = t["sprech"] * len(bl) / gesamt
            zeilen.append(f"{i}\n{ts(start)} --> {ts(start + dauer)}\n{bl}\n"); i += 1; start += dauer
    (d / "export" / "untertitel-de.srt").write_text("\n".join(zeilen), encoding="utf-8")
    print(f"[Untertitel] {i-1} Einträge")


def stufe_qc(d, plan):
    v = d / "export" / "video.mp4"; befunde = []
    probe = json.loads(sh(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,duration,width,height", "-of", "json", str(v)]).stdout)
    dur = {s["codec_type"]: float(s["duration"]) for s in probe["streams"]}
    lo, hi = plan.get("ziel_minuten", [8, 11]); minuten = dur["video"] / 60
    befunde.append(("Länge", f"{minuten:.1f} Min. (Ziel {lo}–{hi})", "🟢" if lo <= minuten <= hi else "🟡"))
    diff = abs(dur["video"] - dur["audio"])
    befunde.append(("Bild/Ton-Synchronität", f"Differenz {diff:.2f} s", "🟢" if diff < 0.1 else "🔴"))
    e = sh(["ffmpeg", "-nostats", "-i", str(v), "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])
    befunde.append(("Lautheit (YouTube-Referenz ≈ -14 LUFS)", f"{I:.1f} LUFS", "🟢" if abs(I - LUFS_ZIEL) <= 1 else "🟡"))
    befunde.append(("True Peak", f"{TP:.1f} dBTP", "🟢" if TP <= -1.0 else "🟡"))
    s = sh(["ffmpeg", "-nostats", "-i", str(v), "-af", "silencedetect=n=-45dB:d=2.5", "-f", "null", "-"]).stderr
    stille = re.findall(r"silence_start: ([\d.]+)", s)
    befunde.append(("Stille > 2,5 s", f"{len(stille)} Stellen {stille[:5]}", "🟢" if not stille else "🟡"))
    bl = sh(["ffmpeg", "-nostats", "-i", str(v), "-vf", "blackdetect=d=0.5:pix_th=0.1", "-an", "-f", "null", "-"]).stderr
    schwarz = re.findall(r"black_start:([\d.]+)", bl)
    befunde.append(("Schwarzbilder > 0,5 s", f"{len(schwarz)}", "🟢" if not schwarz else "🔴"))
    tm = json.loads((d / "build" / "timing.json").read_text())["segmente"]
    lang = [(k, x["dauer"]) for k, x in tm.items() if x["dauer"] > 40]
    kurz = [(k, x["dauer"]) for k, x in tm.items() if x["dauer"] < 4]
    befunde.append(("Folien-Standzeit (4–40 s)", f"zu lang: {lang or '–'}; zu kurz: {kurz or '–'}", "🟢" if not (lang or kurz) else "🟡"))
    w = sum(len(x["sprechtext"].split()) for x in plan["segmente"])
    befunde.append(("Sprechtempo", f"{w} Wörter / {minuten:.1f} Min. = {w/minuten:.0f} Wörter/Min. (Richtwert 130–150)", "🟢" if 120 <= w / minuten <= 160 else "🟡"))
    gesamt = "🔴" if any(x[2] == "🔴" for x in befunde) else ("🟡" if any(x[2] == "🟡" for x in befunde) else "🟢")
    kap = []
    for x in plan["segmente"]:
        if not kap or kap[-1][1] != x["kapitel"]:
            kap.append((tm[x["id"]]["start"], x["kapitel"]))
    kapitel = "\n".join(f"{int(a//60):02d}:{int(a%60):02d} {k}" for a, k in kap)
    (d / "export" / "kapitel.txt").write_text(kapitel + "\n", encoding="utf-8")
    md = [f"# QC-Bericht – {plan['titel']}", "", f"**Gesamtampel: {gesamt}**", "", "| Prüfpunkt | Messwert | Ampel |", "|---|---|---|"]
    md += [f"| {a} | {b} | {c} |" for a, b, c in befunde]
    md += ["", "## Kapitelmarken (aus tatsächlichem Timing, für die Videobeschreibung)", "```", kapitel, "```"]
    (d / "export" / "qc-bericht.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("ordner"); ap.add_argument("--tempo", type=float, default=0.95, help="<1 schneller")
    ap.add_argument("--nur", choices=["ton", "folien", "schnitt", "qc"])
    a = ap.parse_args(); d = Path(a.ordner).resolve(); plan = json.loads((d / "schnittplan.json").read_text())
    if a.nur in (None, "ton"): stufe_ton(d, plan, a.tempo)
    if a.nur in (None, "folien"): stufe_folien(d)
    if a.nur in (None, "schnitt"):
        stufe_schnitt(d, plan); stufe_mastering(d); stufe_untertitel(d, plan)
    if a.nur in (None, "qc"): stufe_qc(d, plan)


if __name__ == "__main__":
    main()
