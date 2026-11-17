# Anleitung – 8D-Report Vorlage (Excel) · Version 1.0

Kostenlose Arbeitsmappe zur strukturierten Reklamationsbearbeitung nach der 8D-Methode. Keine Makros, keine externen Verknüpfungen.

## 1. Voraussetzungen
- Microsoft Excel 2010 oder neuer, LibreOffice Calc oder Google Sheets (beim Import nach Google Sheets kann die Darstellung, z. B. Datenbalken, leicht abweichen).
- Speichern Sie die Datei **je Reklamation** als Kopie, z. B. `8D_2026-017_TN100-2034.xlsx`.

## 2. Aufbau
| Blatt | Wofür |
|---|---|
| **Start** | Inhaltsverzeichnis (Klick springt zum Blatt), Kurzanleitung, Farblegende, Lizenz, Haftungsausschluss |
| **8D-Report** | Kopfdaten, Statusübersicht D0–D8 mit Terminampel und Fortschrittsbalken, Abschnitte D0–D8 mit Leitfragen |
| **5-Why** | Zwei getrennte Warum-Ketten: Pfad A „Warum aufgetreten?“, Pfad B „Warum nicht entdeckt?“ |
| **Ishikawa** | Ursachensammlung nach 6M (Mensch, Maschine, Methode, Material, Messung, Mitwelt) in Tabellenform; Übersicht zählt Ursachen je M und Bewertung |
| **Maßnahmentracker** | Alle Maßnahmen mit Verantwortlich, Termin, Status, Ampel und Tagen Überfälligkeit |

Jedes Blatt hat oben rechts einen Link „← Start“.

## 3. Farben und Felder
- **Weiß mit Rahmen:** Eingabe.
- **Hellgrau:** Formel bzw. feste Beschriftung – nicht überschreiben.
- **Grau-kursiv:** fiktives Beispiel (Muster GmbH / Beispiel-Druckguss GmbH). In Tabellen ist die erste Zeile mit „Beispiel – löschen“ markiert: Zeile löschen (Rechtsklick → Zeilen löschen) oder überschreiben – sobald in der ersten Spalte nicht mehr „Beispiel“ steht, verschwindet die graue Formatierung. Die Spalten „Beispiel (fiktiv)“ in Kopfdaten, 5W2H und 5-Why dienen nur zur Orientierung; Sie können sie stehen lassen oder ausblenden.
- **Ampel:** rot = überfällig, gelb = fällig in ≤ 7 Tagen oder kein Termin gesetzt, grün = im Plan/erledigt, grau = nicht anwendbar/verworfen.

## 4. Schritt für Schritt
1. **Kopfdaten** (8D-Report) ausfüllen. Die „Fehlerbezeichnung (kurz)“ erscheint automatisch auf den Blättern 5-Why und Ishikawa.
2. **Statusübersicht:** Für jede Disziplin Verantwortliche und Soll-Termin eintragen. Die Terminampel vergleicht den Soll-Termin mit dem heutigen Datum (Funktion HEUTE()). Status per Dropdown: offen · in Arbeit · erledigt · n. a.
   Fortschritt = erledigte Disziplinen ÷ anwendbare Disziplinen (Disziplinen mit „n. a.“ zählen nicht mit – sinnvoll vor allem für D0).
   Fristen: Viele Kunden erwarten Sofortmaßnahmen sehr schnell (oft innerhalb von 24 h) und Ursache/Abstellmaßnahmen innerhalb weniger Arbeitstage (häufig 10). Das sind Praxiswerte – **maßgeblich sind die Vorgaben Ihres Kunden.**
3. **D0** nur, wenn eine Notfallreaktion nötig ist (z. B. Sicherheitsrelevanz); sonst Status „n. a.“.
4. **D1 Team:** Teamleiter, Mitglieder, Sponsor; Rolle per Dropdown.
5. **D2 Problembeschreibung:** Fehlerbild aus Kundensicht, dann 5W2H und Ist/Ist-nicht. Noch **keine Ursache** nennen.
6. **D3 Sofortmaßnahmen:** Maßnahmen mit Ort, Termin, Status und Wirksamkeitsbeleg. In der Bestandstabelle alle Bestände (Kunde, Transit, Lager, Fertigung, Unterlieferant) erfassen; die Summenzeile berechnet den Fehleranteil in ppm.
7. **D4 Ursachen:** Analysieren Sie auf den Blättern **5-Why** (beide Pfade!) und **Ishikawa**. Übertragen Sie nur **verifizierte** Ursachen in die zwei D4-Tabellen „Auftreten“ und „Nichtentdeckung“.
8. **D5:** Für jede verifizierte Ursache mindestens eine Abstellmaßnahme planen; Bezug (Auftreten/Nichtentdeckung) per Dropdown.
9. **D6:** Umsetzung und objektiven Wirksamkeitsnachweis dokumentieren; erst danach Sofortmaßnahmen aufheben (Datum eintragen).
10. **D7:** Checkliste (ja/nein/n. a.) – FMEA, Produktionslenkungsplan, Anweisungen, Unterweisung, Übertrag auf ähnliche Produkte, Lessons Learned.
11. **D8:** Abschluss, Kundenbestätigung, Würdigung des Teams.
12. **Maßnahmentracker:** Alle Maßnahmen aus D3–D7 zusätzlich hier führen. Nummer, Ampel und „Tage überfällig“ rechnen automatisch; die Zähler oben ignorieren die Beispielzeile. Autofilter in der Kopfzeile nutzen, um z. B. nur „überfällig“ anzuzeigen.

## 5. Typische Fehler – und wie die Vorlage hilft
| Fehler | Gegenmittel in der Vorlage |
|---|---|
| Ursache steht schon in D2 | Leitfrage in D2; 5W2H/Ist-Ist-nicht ohne Ursachenfeld |
| Nur Auftretensursache analysiert | 5-Why mit Pflichtpfad B, D4 mit zwei getrennten Tabellen |
| Sortieren als Abstellmaßnahme | D3 und D5 getrennt; „Art“ im Tracker |
| „Mitarbeiter geschult“ als einzige Maßnahme | Hinweis auf 5-Why-Blatt; D7-Checkliste |
| Wirksamkeit nicht belegt | D6-Spalte „Wirksamkeitsnachweis“, Tracker-Spalte „Wirksamkeit geprüft“ |
| Sofortmaßnahmen nie aufgehoben | D6-Spalte „Sofortmaßn. aufgehoben am“ |

## 6. Drucken
Alle Blätter sind auf A4 quer, Seitenbreite eingepasst, eingerichtet; Tabellenköpfe wiederholen sich auf jeder Seite. Die Fußzeile zeigt Blattname und Seitenzahl.

## 7. Grenzen
- Die Vorlage ersetzt kein Kundenformular: Schreibt Ihr Kunde ein eigenes 8D-Formular vor, übertragen Sie die Inhalte dorthin.
- Keine Mehrbenutzer-Funktion, keine automatische Verknüpfung zwischen D3–D7 und dem Tracker (bewusst einfach gehalten – Einträge bitte doppelt führen bzw. Nr. im Tracker in D5 eintragen).
- HEUTE() wird bei jedem Öffnen bzw. Neuberechnen aktualisiert; die Ampeln ändern sich deshalb mit der Zeit.

## 8. Lizenz und Haftung
Siehe Blatt „Start“: Nutzung im eigenen Unternehmen, keine Weitergabe/kein Weiterverkauf der Datei; Arbeitshilfe ohne Gewähr, ersetzt keine Beratung.
