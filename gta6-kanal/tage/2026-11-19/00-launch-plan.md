# Launch-Tag 19.11.2026 – Startpaket

## Executive Summary
GTA 6 erscheint heute (PS5/Xbox Series, regional gestaffelt ab 00:00 Ortszeit). In den ersten 72 h ist die **Suchnachfrage nach Einsteiger-Tipps am höchsten**, während das deutschsprachige Angebot noch dünn ist. Die Strategie lautet deshalb: **schnelle, nützliche Tipp-Shorts aus eigenem Gameplay**, keine Spoiler.

## Heute: 3 Shorts + Kanal-Setup
| # | Zeit | Format | Aufnahme-Auftrag (selbst spielen) | Overlay-Hook | Titel-Entwurf |
|---|---|---|---|---|---|
| 1 | 12:00 | Tipp | Erste 30 Min.: 1 Einstellung/Mechanik, die man sofort ändern/kennen sollte (z. B. Steuerung, Kamera, Karte) | „Ändere DAS sofort“ | GTA 6: Diese Einstellung sofort ändern! |
| 2 | 16:00 | Physik/Fail | Lustigster physikalischer Moment (Fahrzeug, Wasser, NPC-Reaktion) – **ohne** Gewalt in den ersten 7 s | „Das hat GTA 5 nicht“ | GTA 6 Physik ist absurd 😂 |
| 3 | 19:00 | Detail/Easter Egg | Ein Detail in der offenen Welt, das man leicht übersieht (Schild, NPC-Verhalten, Wetter) | „99 % übersehen das“ – **nur wenn belegbar selten**, sonst „Hast du das gesehen?“ | GTA 6: Dieses Detail ist verrückt |

Konkrete Spielinhalte trägt der Inhaber nach der Aufnahme ein. Spielfakten sind bis dahin `[UNBELEGT]`.

## Kanal-Setup (30 Min.)
- [ ] Kanalname final (ohne „Rockstar“/Logo), Handle sichern, auch auf TikTok/Instagram
- [ ] Profilbild + Banner: eigenes Design, **keine** offiziellen Key-Arts (Urheberrecht)
- [ ] Kanalinfo: „Täglich die besten GTA-6-Tipps & Momente auf Deutsch.“ + Impressum-Link
- [ ] YouTube Studio: Standard-Upload-Einstellungen (Kategorie Gaming, Spiel „Grand Theft Auto VI“ zuordnen, Sprache Deutsch, „Nicht speziell für Kinder“)
- [ ] Musikspur-Regel: Radio im Spiel leise/aus während der Aufnahme

## Workflow nach der Aufnahme
```bash
python3 gta6-kanal/tools/clip.py analyse gta6-kanal/rohmaterial/2026-11-19/session1.mp4 > schnittliste.csv
# Zeiten prüfen/anpassen, titel+overlay eintragen
python3 gta6-kanal/tools/clip.py render schnittliste.csv --out gta6-kanal/clips/2026-11-19
```
Danach: `gta-packaging` → `gta-compliance` → Upload durch den Inhaber.

## Standard-Beschreibung
```
<1 Satz, was man im Clip lernt/sieht>
🔔 Täglich neue GTA-6-Clips auf Deutsch – abonnieren!
Was soll ich als Nächstes testen? Schreib's in die Kommentare.
#gta6 #gtavi #gta6deutsch
Impressum: <Link>
```
