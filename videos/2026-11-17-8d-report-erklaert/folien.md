# Folien – Video #1 „8D-Report erklärt“ (Bauanleitung für 60 Min.)

> Rolle: `skript-autor` · Stand: 17.11.2026 · v1.1 · Bezug: `02-skript.md` (F-Nummern)
> **Ziel:** Der Inhaber baut alle Folien in ≈ 60 Min. in PowerPoint oder Canva. Texte sind kopierfertig.

## Grundeinstellungen (5 Min.)
- Format 16:9 (1920×1080). Kanal-Vorlage: dunkelblau `#1F3A5F` (Titel), weiß (Hintergrund), Akzent orange `#E8730C` (Hervorhebungen), rot `#C0392B` nur für Fehler/NIO, grün `#2E8B57` für i. O.
- Schrift: eine serifenlose Schrift (z. B. Calibri/Inter), Titel 40 pt, Text ≥ 24 pt. **Max. 3 Zeilen Text pro Folie.**
- Dauer-Element ab F06 bis F25: kleines Label unten rechts **„Fiktives Beispiel“**.
- **Urheberrecht:** Keine VDA-/AIAG-/IATF-Cover, -Formblätter, -Tabellen oder -Zitate. Nur eigene Grafiken, Icons aus lizenzfreien Bibliotheken (z. B. PowerPoint-Symbole), eigene Screenshots der eigenen Vorlage.
- **Screen-Recordings (F07–F25 „Vorlage“)**: Bildschirmaufnahme der **finalen** kostenlosen 8D-Vorlage (p0) mit dem ausgefüllten Muster-GmbH-Fall. Zoom auf den jeweiligen Bereich (Excel-Zoom 150 %). Falls p0 noch nicht fertig ist: Mockup-Folie mit derselben Tabellenstruktur bauen und vor dem Upload durch echte Aufnahme ersetzen (**Abgleich Pflicht**, siehe unten).

## Voraussetzung: Aufbau der Vorlage, wie im Video gezeigt
Das Video verspricht folgende Elemente. `produkt-entwickler` und `sqe-experte` müssen sie in p0 umsetzen, sonst das Skript anpassen:
| Blatt / Bereich | Muss enthalten | Gezeigt in |
|---|---|---|
| Kopf | Reklamations-Nr., Teil/Sachnr., Kunde, Eingangsdatum, Fristen, Status | F07 |
| D1 Team | Rolle, Name, Abteilung, Teamleiter, Sponsor | F08 |
| D2 | W-Fragen + zwei Spalten **IST / IST NICHT** | F10 |
| D3 | Tabelle Ort (Kunde/Transport/Lager/Fertigung) · Maßnahme · Menge · Verantwortlich · Datum · Ergebnis; Zeile Kennzeichnung/Clean Point | F12 |
| D4 / 5-Why | **Zwei getrennte 5-Why-Spalten (Auftreten / Nichtentdeckung)**, je Feld „Nachweis“; leere Nichtentdeckungs-Spalte wird **rot** (bedingte Formatierung) | F15, F17, F19 |
| D5 | Ursache · Abstellmaßnahme · Verifikation, getrennt nach Auftreten/Nichtentdeckung | F20 |
| D6 | umgesetzt am · Wirksamkeitsnachweis · Ergebnis · Sofortmaßnahme beendet am | F22 |
| D7 | Checkliste FMEA · Control Plan · Wartungsplan · Arbeitsanweisung · Übertragung auf ähnliche Prozesse | F24 |
| D8 | Abschluss Kunde · Datum · Würdigung; **Statusampel je Disziplin** | F25 |
| Beispielblatt | Muster-GmbH-Fall ausgefüllt (Daten aus `praxisbeispiel.md`) | F07–F25 |

---

## Folien

| F | Zeit | Typ | Titel / Text auf der Folie | Bild / Gestaltung |
|---|---|---|---|---|
| F01 | 00:00 | Grafik | **„Reklamation: undicht“** | Eigene einfache Grafik: Halter (graues Rechteck mit Bohrung) + blauer Tropfen; roter Rahmen. Alternativ KI-Bild aus Thumbnail-Prompt (ohne Text) |
| F02 | 00:18 | Fahrplan | D0 → D1 → … → D8 (Zeitstrahl) | Neun Kreise, Kreis D4 orange hervorgehoben; rechts unten Mini-Screenshot der Vorlage |
| F03 | 00:34 | Text | **8D = 8 Disziplinen** · D1–D8 · *+ D0 Planung (optional)* | Neun Kästchen nebeneinander, D0 gestrichelt |
| F04 | 00:45 | Zeitleiste | „1987: Ford-Handbuch *Team Oriented Problem Solving* (verbreitete Angabe)“ · klein: „Herkunft umstritten, Vorläufer in US-Militärnorm diskutiert“ | Einfache Linie mit einem Punkt; **kein Ford-Logo** (Markenrecht) |
| F05 | 00:59 | 3 Kästen | ① „VDA-Band *8D – Problemlösung in 8 Disziplinen* (2018): Referenz“ ② „IATF 16949: definierter Problemlösungsprozess, kein 8D-Zwang“ ③ **„Kundenformular geht vor“** | Nur Text in Kästen. **Kein Cover, kein Inhalt, keine Gliederung des VDA-Bands** |
| F06 | 01:21 | Steckbrief | **Fall: Muster GmbH** · Halter Kühlmittelpumpe (Alu-Druckguss) · Kunde: 6 von 1.200 Modulen undicht an Dichtfläche | Schnittskizze: Halter mit Kanal (blau) und Dichtfläche (orange Linie); Label „Fiktives Beispiel“ groß |
| F07 | 01:42 | Vorlage | Bereich „Kopf / D0“ | Screen-Recording: Felder werden ausgefüllt (oder im Schnitt beschleunigt) |
| F08 | 01:59 | Vorlage | Bereich „D1 Team“ | Recording; Rollen sichtbar, Namen fiktiv („A. Beispiel“) |
| F09 | 02:20 | Liste | **W-Fragen:** Was? · Wo? · Wann? · Wie viele? · Was ist *nicht* betroffen? | Letzte Zeile orange |
| F10 | 02:35 | Vorlage | D2 „IST / IST NICHT“ | Recording; Zellen „Werkzeug 2“ und „nach Wartung“ orange markieren (Rahmen im Schnitt) |
| F11 | 03:01 | Icons | **Wo liegen fehlerhafte Teile?** Kunde · Transport · Lager · Fertigung | Vier Icons in einer Reihe |
| F12 | 03:21 | Vorlage + Einblendung | D3-Tabelle; Einblendung: **„Erst Prüfmethode absichern, dann sortieren“** | Recording; danach Zeile „Kennzeichnung / Clean Point“ hervorheben (bis 04:06) |
| F13 | 04:06 | 2 Spalten | links **„Auftreten: Warum entstanden?“** · rechts **„Nichtentdeckung: Warum durchgerutscht?“** | Groß, mittig; Spalten in Orange/Dunkelblau |
| F14 | 04:26 | Schema | „Gaspore: rund, glatt“ vs. „Schwindungslunker: zerklüftet“ | Zwei selbst gezeichnete Formen (Kreis vs. unregelmäßige Form). **Keine Fremd-Schliffbilder** |
| F15 | 04:45 | Vorlage | 5-Why, Spalte „Auftreten“ (5 Zeilen, letzte „systemisch“ markiert) | Zeilen nacheinander einblenden (Animation „Erscheinen“ oder Recording) |
| F16 | 05:16 | Diagramm | „Druck über Zeit“: Linie *Leck* (fällt) + Linie *Erwärmung* (steigt) = Linie *Anzeige* (fast flach) → „scheinbar dicht“ | Drei Linien, **keine Zahlenwerte/Achsenskala** (schematisch) |
| F17 | 05:39 | Vorlage | 5-Why, Spalte „Nichtentdeckung“ inkl. Zeile „Referenzteil-Check wöchentlich + kalt“ | Recording |
| F18 | 05:58 | Text | **Nachweis = Fehler ein- und ausschalten** ✔ Auftreten: Kanäle gereinigt → keine Poren ✔ Nichtentdeckung: Leckteil warm ✗ / kalt ✔ | Zwei Zeilen mit Häkchen |
| F19 | 06:19 | Vorlage | Leere Nichtentdeckungs-Spalte färbt sich rot | Recording: Spalte leeren → rot → wieder füllen → weiß |
| F20 | 06:36 | Vorlage | D5-Tabelle (zwei Zeilen: Auftreten / Nichtentdeckung) | Recording |
| F21 | 07:12 | Stempel | ~~„Mitarbeiter geschult“~~ → **„System ändern“** | Roter durchgestrichener Stempel, grüner Pfeil |
| F22 | 07:29 | Vorlage | D6: umgesetzt am · Wirksamkeitsnachweis · Ergebnis | Recording |
| F23 | 07:45 | Pfeil | **„Sofortmaßnahme beenden – erst nach Wirksamkeitsnachweis“** | Pfeil von „D6“ zurück zu „D3“ |
| F24 | 07:54 | Vorlage | D7-Checkliste; Häkchen „Übertragung auf ähnliche Prozesse“ zuletzt | Recording |
| F25 | 08:19 | Vorlage | D8 + Statusampel aller Disziplinen grün | Recording, Zoom auf Ampel |
| F26 | 08:32 | 3 Takeaways | ① Sofortmaßnahme schützt – Abstellmaßnahme beseitigt ② D4: zwei Ursachen, beide nachgewiesen ③ Sofortmaßnahme endet erst nach Wirksamkeitsnachweis | Nacheinander einblenden (08:32 / 08:41 / 08:49) |
| F27 | 08:55 | Endkarte | **„Kostenlose 8D-Vorlage – Link in der Beschreibung“** · klein: „Eigenes Produkt · kostenlos“ | Mockup der Vorlage (Laptop-Rahmen); rechte Hälfte frei für YouTube-Endkarte (Video + Abo-Button), 15–20 s |

## Zeitplan für den Inhaber (≈ 60 Min.)
| Schritt | Min. |
|---|---|
| Kanal-Vorlage öffnen, Farben/Schrift, Label „Fiktives Beispiel“ | 5 |
| Textfolien F03, F04, F05, F09, F11, F13, F18, F21, F23, F26, F27 (Text kopieren) | 20 |
| Grafiken F01, F02, F06, F14, F16 (einfache Formen) | 15 |
| Screen-Recordings der Vorlage F07–F25 in **einer** Aufnahme (Bereiche nacheinander anfahren, im Schnitt teilen) | 15 |
| Kontrolle gegen Skript | 5 |
