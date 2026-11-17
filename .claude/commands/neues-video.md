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
   e. `sprecher` → `voiceover/` (nur bei 🟢/🟡 nach Fixes; KI-Stimme, Hinweis in Beschreibung)
4. Bei 🟡/🔴 im Review: Fixes umsetzen lassen und erneut prüfen (max. 2 Iterationen).
5. Abschluss: Ampel, empfohlener Titel, Thumbnail-Konzept, geschätzte Videolänge, offene To-dos für die Produktion.
