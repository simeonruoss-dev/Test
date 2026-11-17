# Automatische Videoproduktion (0 €)

```bash
python3 tools/video/produziere.py videos/<slug>            # alle Stufen
python3 tools/video/produziere.py videos/<slug> --nur qc   # einzelne Stufe: ton | folien | schnitt | qc
```
Abhängigkeiten: `piper-tts` + Stimme (siehe `tools/tts/README.md`), ffmpeg, Node + Playwright (Chromium), Schrift „Inter“.

## Pipeline
| Stufe | Agent | Ergebnis |
|---|---|---|
| Schnittplan | folien-designer | `schnittplan.json` |
| 1 Ton (TTS je Segment) | ton-meister | `build/ton/*.wav`, `build/timing.json` |
| 2 Folien 1920×1080 + Thumbnail | video-produzent | `build/folien/*.png`, `build/thumbnail.png` |
| 3 Schnitt: Ken-Burns-Zoom, Einblendung, frame-genaue Synchronität | video-produzent | `build/bild.mp4`, `build/stimme-roh.wav` |
| 4 Mastering: Hochpass 80 Hz, De-Esser, Kompressor, 2-Pass-loudnorm −14 LUFS / −1,5 dBTP | ton-meister | `export/video.mp4` |
| 5 Untertitel | video-produzent | `export/untertitel-de.srt` |
| 6 QC: Länge, Sync, Lautheit, Stille, Schwarzbild, Standzeit, Sprechtempo, Kapitel | video-pruefer | `export/qc-bericht.md`, `export/kapitel.txt` |

## schnittplan.json – Layouts
`titel` {ueberschrift, unterzeile, badge?} · `punkte` {ueberschrift, punkte[≤4], hinweis?} · `zwei_spalten` {ueberschrift, links/rechts {titel, punkte[≤3], farbe rot|gruen|blau|orange|grau}} · `zeitstrahl` {ueberschrift, schritte[{label,text}], aktiv} · `tabelle` {ueberschrift, blatt, spalten[≤6], zeilen[≤6], markiert[], hinweis?} · `karten` {ueberschrift, karten[{titel,text}≤4]} · `cta` {ueberschrift, text, button}
Segment: {id, folie, kapitel, fiktiv, sprechtext, layout, daten}; optional Wurzel: `thumbnail` {zeile1, zeile2, badge}.
