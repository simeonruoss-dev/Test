# Testbericht – p0-8d-vorlage · Version 1.0

> Rolle: produkt-entwickler · Datum: 17.11.2026 · Datei: `dist/8D-Report-Vorlage.xlsx`
> Reproduzierbar mit: `python3 build.py --test` (openpyxl 3.1.5, Python 3.13, LibreOffice headless)

## Ergebnis: ✅ bestanden

| # | Test | Ergebnis |
|---|---|---|
| 1 | Datei mit openpyxl neu laden | ✅ 5 Blätter in Sollreihenfolge: Start, 8D-Report, 5-Why, Ishikawa, Maßnahmentracker |
| 2 | Inventar | 406 Formeln · 34 Datenvalidierungen (Dropdowns/Datum) · 20 bedingte Formatierungsbereiche |
| 3 | Hyperlink-Inhaltsverzeichnis | ✅ 5 interne Links (`'Blatt'!A1`); jedes Blatt hat „← Start“ |
| 4 | Seiteneinrichtung | ✅ alle Blätter A4 (paperSize 9) quer, auf Seitenbreite eingepasst, Druckbereich + Wiederholungszeilen gesetzt |
| 5 | Fixierte Kopfzeilen | ✅ 8D-Report/5-Why A3, Ishikawa A11, Maßnahmentracker A5 |
| 6 | Makrofreiheit | ✅ kein `vbaProject.bin` im Archiv |
| 7 | LibreOffice-Neuberechnung Originaldatei | ✅ **0 Fehlerwerte** (#REF!, #NAME?, #DIV/0!, #VALUE!, #N/A, #NUM!, Err:) |
| 8 | Beispielzeile Tracker | ✅ Ampel „überfällig“, Tage überfällig > 0; Zähler oben = 0 (Beispiel korrekt ausgeschlossen) |
| 9 | Fortschritt leer | ✅ 0 % und leerer Textbalken (kein #DIV/0!) |
| 10 | Funktionstest mit Testdaten (Kopie, neu berechnet) | ✅ siehe unten |

### Funktionstest (Test 10) – Soll/Ist
| Prüfling | Eingabe | Soll | Ist |
|---|---|---|---|
| Terminampel D0–D8 | n. a. / 3× erledigt / in Arbeit (−3 T) / offen (+3 T) / offen (+30 T) / 2× ohne Termin | –, erledigt ×3, überfällig, fällig ≤ 7 T, im Plan, kein Termin ×2 | identisch ✅ |
| Fortschritt | 3 erledigt, 1 n. a. | 3/8 = 37,5 %, „3 von 8 erledigt“, ■■■■□□□□□□ | identisch ✅ |
| Tracker-Ampel | überfällig (−5 T) / +2 T / erledigt / ohne Termin / +30 T | überfällig, fällig ≤ 7 T, erledigt, kein Termin, im Plan | identisch ✅ |
| Tage überfällig | Termin −5 T | 5 | 5 ✅ |
| Laufende Nr. | 5 Einträge | 1–5 | 1–5 ✅ |
| Tracker-Zähler | s. o. | offen/in Arbeit 4 · überfällig 1 · ≤ 7 T 1 · erledigt 1 | identisch ✅ |
| Verweis Problem → 5-Why | „Testfehler“ | „Testfehler“ | ✅ |
| Ishikawa-Übersicht | Methode bestätigt, Messung ausgeschlossen | Methode bestätigt = 1, Messung Anzahl = 1 | ✅ |

## Visuelle Prüfung
PDF-Export via LibreOffice (15 Seiten A4 quer) gesichtet: Kopfzeilen dunkelblau, Tabellenköpfe schiefergrau, Beispielinhalte grau-kursiv, Ampelfarben sichtbar, keine abgeschnittenen Spalten.

## Hinweise / Einschränkungen
- openpyxl meldet beim Lesen der LibreOffice-Ausgabe „Conditional Formatting extension is not supported“ – betrifft nur das Wieder-Einlesen der von LibreOffice gespeicherten Testkopie (Datenbalken-Erweiterung), nicht die ausgelieferte Datei.
- Nicht getestet: Microsoft Excel und Google Sheets (nicht in der Build-Umgebung verfügbar). Verwendete Funktionen (IF, COUNTIF(S), SUM, REPT, ROUND, TEXT, TODAY, IFERROR, COUNTA, ISNUMBER/SEARCH) sind seit Excel 2007 verfügbar. **Empfehlung: Sichtprüfung in Excel durch den Inhaber vor Veröffentlichung.**
- Die Ampelwerte hängen von HEUTE() ab; der Test nutzt deshalb relative Datumswerte.
- Status in `shop/produkte.json` wurde laut Auftrag **nicht** geändert (Soll: `bereit_fuer_review`).
