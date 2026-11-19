#!/usr/bin/env python3
"""GTA-6-Clip-Werkzeug: Highlights finden und 9:16-Shorts rendern.

  python3 clip.py analyse <video> [--top 10]
      Schlägt Highlight-Zeitstempel vor (Lautstärkespitzen + Szenenwechsel).

  python3 clip.py render <schnittliste.csv> [--out DIR]
      CSV-Spalten: datei,start,ende,titel,overlay,mute_music
      start/ende in Sekunden oder mm:ss. mute_music=1 schaltet Ton stumm
      (In-Game-Radio, Content-ID-Risiko).

Ausgabe: 1080x1920, H.264/AAC, unscharfer Hintergrund, Overlay oben, -14 LUFS.
"""
import argparse, csv, os, re, subprocess, sys

def sek(t: str) -> float:
    t = t.strip()
    if ":" in t:
        m, s = t.split(":", 1)
        return int(m) * 60 + float(s)
    return float(t)

def dauer(datei: str) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", datei], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())

def analyse(datei: str, top: int) -> None:
    # Lautheit pro 0,5 s (Momentary Loudness) aus ebur128
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", datei, "-af", "ebur128=peak=none",
                        "-f", "null", "-"], capture_output=True, text=True)
    pegel = [(float(t), float(m)) for t, m in
             re.findall(r"t:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)", r.stderr)]
    # Szenenwechsel
    s = subprocess.run(["ffmpeg", "-hide_banner", "-i", datei, "-vf", "select='gt(scene,0.35)',showinfo",
                        "-an", "-f", "null", "-"], capture_output=True, text=True)
    szenen = [float(x) for x in re.findall(r"pts_time:([\d.]+)", s.stderr)]
    if not pegel and not szenen:
        sys.exit("Keine Analysedaten – Datei prüfen.")
    # Score je 1-s-Fenster: Lautheit + Bonus für Szenenwechsel
    fenster = {}
    for t, m in pegel:
        fenster[int(t)] = max(fenster.get(int(t), -99.0), m)
    for t in szenen:
        fenster[int(t)] = fenster.get(int(t), -40.0) + 6
    gesamt = dauer(datei)
    vorschlaege, belegt = [], []
    for t, score in sorted(fenster.items(), key=lambda x: -x[1]):
        if any(abs(t - b) < 20 for b in belegt):
            continue
        belegt.append(t)
        start, ende = max(0, t - 8), min(gesamt, t + 17)  # Höhepunkt nach ~8 s, Clip ~25 s
        vorschlaege.append((start, ende, score))
        if len(vorschlaege) >= top:
            break
    print("datei,start,ende,titel,overlay,mute_music")
    for start, ende, score in sorted(vorschlaege):
        print(f"{datei},{start:.0f},{ende:.0f},TODO,TODO,1  # score {score:.1f}")
    print("\nHinweis: Vorschläge sind maschinell – jeden Clip ansehen, Zeiten anpassen, "
          "Kommentare (# …) entfernen, als schnittliste.csv speichern.", file=sys.stderr)

def esc(txt: str) -> str:
    return txt.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\u2019").replace("%", "\\%")

def render(csvdatei: str, out: str) -> None:
    os.makedirs(out, exist_ok=True)
    with open(csvdatei, newline="", encoding="utf-8") as f:
        zeilen = [z for z in csv.DictReader(f) if z.get("datei") and not z["datei"].startswith("#")]
    for i, z in enumerate(zeilen, 1):
        start, ende = sek(z["start"]), sek(z["ende"])
        if not 5 <= ende - start <= 60:
            print(f"[{i}] übersprungen: Länge {ende-start:.1f}s (5–60 s erlaubt)"); continue
        slug = re.sub(r"[^a-z0-9]+", "-", z.get("titel", f"clip{i}").lower()).strip("-")[:40] or f"clip{i}"
        ziel = os.path.join(out, f"{i:02d}-{slug}.mp4")
        overlay = esc(z.get("overlay", "").strip())
        vf = ("[0:v]split[a][b];"
              "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2,eq=brightness=-0.15[bg];"
              "[b]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2")
        if overlay and overlay != "TODO":
            vf += (f",drawtext=text='{overlay}':fontcolor=white:fontsize=72:borderw=6:bordercolor=black:"
                   "x=(w-text_w)/2:y=260:font=Sans:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
        vf += ",fps=30,format=yuv420p[v]"
        stumm = z.get("mute_music", "0").strip() == "1"
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", str(start), "-to", str(ende),
               "-i", z["datei"]]
        if stumm:
            cmd += ["-f", "lavfi", "-t", str(ende - start), "-i", "anullsrc=r=48000:cl=stereo"]
            amap = "1:a"; af = []
        else:
            amap = "0:a?"; af = ["-af", "loudnorm=I=-14:TP=-1.5:LRA=11"]
        cmd += ["-filter_complex", vf, "-map", "[v]", "-map", amap, *af,
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                "-ar", "48000", "-shortest", "-movflags", "+faststart", ziel]
        subprocess.run(cmd, check=True)
        print(f"[{i}] {ziel} ({ende-start:.0f}s{', stumm' if stumm else ''})")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("analyse"); a.add_argument("video"); a.add_argument("--top", type=int, default=10)
    r = sp.add_parser("render"); r.add_argument("csv"); r.add_argument("--out", default="clips/neu")
    args = p.parse_args()
    analyse(args.video, args.top) if args.cmd == "analyse" else render(args.csv, args.out)
