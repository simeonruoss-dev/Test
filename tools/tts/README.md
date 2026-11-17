# KI-Voice-over mit Piper (0 €)

| Punkt | Wert |
|---|---|
| Engine | [Piper TTS](https://github.com/OHF-Voice/piper1-gpl) (`pip install piper-tts`), läuft lokal, keine Cloud |
| Stimme | `de_DE-thorsten-high` (Hugging Face `rhasspy/piper-voices`) |
| Lizenz Stimme | Datensatz Thorsten-Voice: **CC0** (laut Model Card) → kommerzielle Nutzung möglich |
| Lizenz Engine | Aktuelle Piper-Version steht unter GPL; betrifft Weitergabe der Software, nicht die erzeugten Audiodateien (Einschätzung, keine Rechtsberatung) |

## Einrichtung (einmalig, auch auf dem eigenen PC)
```bash
pip install piper-tts
mkdir -p tools/tts/stimmen && cd tools/tts/stimmen
for f in de_DE-thorsten-high.onnx de_DE-thorsten-high.onnx.json; do
  curl -L -O "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/high/$f"; done
```
Die Stimmdateien (~110 MB) sind per `.gitignore` vom Repo ausgeschlossen.

## Nutzung
```bash
python3 tools/tts/vertonen.py videos/<slug>/voiceover/sprechtext.txt --tempo 1.05
```
Aussprache von Fachbegriffen: `aussprache.json` erweitern.
