#!/usr/bin/env python3
"""Vertont einen Sprechtext mit Piper TTS (lokal, kostenlos).

Aufruf:  python3 tools/tts/vertonen.py <sprechtext.txt> [--stimme PFAD.onnx] [--tempo 1.0]
Eingabe: ein Absatz pro Folie (Leerzeile als Trenner).
Ausgabe: im Ordner der Eingabe: teil-NN.wav je Absatz + voiceover-komplett.wav
"""
import argparse, json, re, wave
from pathlib import Path

HIER = Path(__file__).resolve().parent
STD_STIMME = HIER / "stimmen" / "de_DE-thorsten-high.onnx"
PAUSE_S = 0.6  # Pause zwischen Absätzen/Folien


def lexikon_anwenden(text: str) -> str:
    regeln = json.loads((HIER / "aussprache.json").read_text(encoding="utf-8"))["ersetzungen"]
    for alt in sorted(regeln, key=len, reverse=True):
        neu = regeln[alt]
        muster = re.escape(alt)
        if alt[0].isalnum():
            muster = r"(?<![\w-])" + muster
        if alt[-1].isalnum():
            muster += r"(?![\w])"
        text = re.sub(muster, neu, text)
    return re.sub(r"[ \t]+", " ", text).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("eingabe")
    ap.add_argument("--stimme", default=str(STD_STIMME))
    ap.add_argument("--tempo", type=float, default=1.0, help=">1 langsamer, <1 schneller")
    a = ap.parse_args()

    from piper import PiperVoice, SynthesisConfig
    stimme = PiperVoice.load(a.stimme)
    cfg = SynthesisConfig(length_scale=a.tempo)

    eingabe = Path(a.eingabe)
    absaetze = [p.strip() for p in re.split(r"\n\s*\n", eingabe.read_text(encoding="utf-8")) if p.strip()]
    ziel = eingabe.parent
    teile = []
    for i, absatz in enumerate(absaetze, 1):
        datei = ziel / f"teil-{i:02d}.wav"
        with wave.open(str(datei), "wb") as wf:
            stimme.synthesize_wav(lexikon_anwenden(absatz), wf, syn_config=cfg)
        teile.append(datei)

    gesamt = ziel / "voiceover-komplett.wav"
    with wave.open(str(teile[0]), "rb") as w0:
        params = w0.getparams()
    stille = b"\x00" * int(params.framerate * PAUSE_S) * params.sampwidth * params.nchannels
    dauer = 0.0
    with wave.open(str(gesamt), "wb") as out:
        out.setparams(params)
        for t in teile:
            with wave.open(str(t), "rb") as w:
                frames = w.readframes(w.getnframes())
                dauer += w.getnframes() / w.getframerate()
            out.writeframes(frames + stille)
    print(f"{len(teile)} Teile, Gesamtdauer ca. {dauer/60:.1f} Min. -> {gesamt}")


if __name__ == "__main__":
    main()
