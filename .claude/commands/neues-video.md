---
description: Komplette Videoproduktion (Recherche → Skript → Packaging → Review)
argument-hint: <Thema oder Nummer aus content-plan.md>
---
Produziere ein Video zum Thema: $ARGUMENTS

1. Lies `kanal/profil.md`. Ist es nicht ausgefüllt → abbrechen und `/kanal-setup` empfehlen.
2. Lege `videos/<heutiges Datum JJJJ-MM-TT>-<kurzer-slug>/` an.
3. Führe die Pipeline sequenziell mit den Subagenten aus. Nach jedem Schritt: 3-Zeilen-Zusammenfassung und Freigabe einholen (außer der Nutzer hat „durchlaufen lassen" geschrieben).
   a. `recherche` → `01-recherche.md`
   b. `skript-autor` → `02-skript.md`
   c. `packaging` → `03-packaging.md`
   d. `qualitaets-pruefer` → `04-review.md`
   e. `folien-designer` → `schnittplan.json`
   f. `ton-meister` → Aussprache/Tempo, `--nur ton`
   g. `video-produzent` → `python3 tools/video/produziere.py videos/<slug>` → `export/`
   h. `video-pruefer` → `export/abnahme.md`; Korrekturschleife bis 🟢 (max. 2 Runden)
4. Bei 🟡/🔴 im Review: Fixes umsetzen lassen und erneut prüfen (max. 2 Iterationen).
5. Abschluss: Upload-Paket (video.mp4, thumbnail.png, untertitel-de.srt, Titel, Beschreibung mit Kapiteln und Links), Ampel.
