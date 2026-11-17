# Spezifikation – p1-iso9001-baukasten

> Rolle: sqe-experte · Stand: 17.11.2026 · Status: Entwurf v1.0 (Grundlage für Build v1.0)
> Produkt: **ISO 9001 Baukasten für KMU (Excel)** · Preis: 79 € (**Hypothese**, siehe `shop/produkte.json`)

## 1. Produktsteckbrief

| Feld | Inhalt |
|---|---|
| Zweck | Eine Excel-Arbeitsmappe, mit der ein KMU die wesentlichen Bausteine eines QM-Systems nach der Kapitelstruktur 4–10 strukturiert aufbauen, pflegen und für ein Audit nachvollziehbar machen kann. |
| Zielnutzer | KMU mit 10–250 Mitarbeitenden: Geschäftsführung, QMB (oft nebenberuflich), Assistenz QM. Typisch: Fertigungsbetrieb vor der Erstzertifizierung oder mit „gewachsenem“ QM-Handbuch. |
| Nutzenversprechen | Ein Ort statt 15 Einzeldateien; Kennzahlen laufen automatisch im Cockpit zusammen; Gap-Analyse zeigt Erfüllungsgrad je Kapitel; praxisnahe Leitfragen statt Normtext. |
| Nicht-Ziele | Kein Normersatz (Norm muss der Kunde selbst erwerben), keine Zertifizierungsgarantie, keine Software mit Workflow/Rechteverwaltung, keine IATF-16949-Spezifika (z. B. Kundenspezifische Anforderungen, Core Tools). |
| Format | `.xlsx`, **keine Makros/VBA**, keine externen Verknüpfungen. |
| Beispielfirma | **Muster Metallbau GmbH** (fiktiv; Ähnlichkeiten mit realen Unternehmen sind zufällig): ca. 45 MA, ein Standort „Musterstadt“, Schweiß- und Montagebaugruppen (Rahmen, Konsolen) für Landmaschinen- und Anlagenbauer. Lieferant im Beispiel: „Beispiel-Stahlhandel GmbH“ (fiktiv). |

## 2. Versions-, Urheber- und Haftungshinweise (verbindlich im Produkt)

- **Versionshinweis (wörtlich auf Blatt „Start“ und in der Anleitung):**
  „Strukturiert nach Harmonized Structure (Kap. 4–10); erstellt auf Basis ISO 9001:2015; Abgleich mit ISO 9001:2026 (Veröffentlichung Sept. 2026 berichtet, nicht verifiziert) vor Verkauf erforderlich.“
- **Urheberrecht:** Keine Normzitate, keine Paraphrasen in Normnähe. Zulässig sind nur Kapitelnummern, die kurzen Kapitelüberschriften (Kontext der Organisation, Führung, Planung, Unterstützung, Betrieb, Bewertung der Leistung, Verbesserung) und **eigene** praxisnahe Leitfragen. Kein Nachbau offizieller Formblätter.
- **Haftung:** „Die Vorlagen sind eine Arbeitshilfe. Sie ersetzen weder den Normtext noch Beratung oder ein Zertifizierungsaudit. Eine Zertifizierung hängt von der gelebten Umsetzung im Unternehmen ab; ein Zertifizierungserfolg wird nicht zugesichert.“
- **Lizenz:** Nutzung im eigenen Unternehmen (alle Standorte einer juristischen Person); keine Weitergabe, kein Weiterverkauf, keine Veröffentlichung der Vorlage oder abgeleiteter Leervorlagen. Eigene ausgefüllte Inhalte gehören dem Kunden.

## 3. Design- und Technikvorgaben (für produkt-entwickler)

| Thema | Vorgabe |
|---|---|
| Farben | Dunkelblau `1F3864` (Titel/Kopfzeilen, weiße Schrift), Mittelblau `2F5496` (Abschnittsüberschriften), Grau `D9D9D9`/`F2F2F2` (Hilfsflächen). Formelzellen hell blau-grau `E9EEF5`, Eingabezellen weiß mit dünnem grauen Rahmen. |
| Beispielzeile | Je Tabelle genau **eine** Zeile, grau hinterlegt (`EDEDED`), graue kursive Schrift; Spalte A = „Beispiel“ + Kommentar „Beispiel – löschen oder überschreiben“. **Zeilen mit „Beispiel“ in Spalte A werden in Kennzahlen (Blatt 12, 13, Zusammenfassungen) nicht mitgezählt.** Ausnahme: Blatt Start und Blatt 12 (reines Auswertungsblatt) haben keine Beispielzeile. |
| Blattkopf | Zeile 1 Titel, Zeile 2 Kapitelbezug + Leitfragen, Zeile 3 Link „← Inhaltsverzeichnis“ + Legende. |
| Fixierung | Einzeltabellen: Fixierung unterhalb der Kopfzeile. Blätter mit mehreren Abschnitten: Fixierung der Zeilen 1–3 (bzw. Matrixkopf bei 06). |
| Dropdowns | DataValidation (Listen inline, max. 255 Zeichen; Zahlenbereiche als Ganzzahl-Validierung). |
| Ampeln | Bedingte Formatierung: Grün `C6EFCE`, Gelb `FFEB9C`, Rot `FFC7CE`. |
| Druck | A4 quer, auf Seitenbreite skaliert, Kopfzeile der Tabelle als Wiederholungszeile, Fußzeile mit Blattname und Seite x von y. |
| Formeln | Nur Funktionen, die in Excel 2010+, LibreOffice Calc und Google Sheets vorhanden sind: IF, IFERROR, AND, OR, COUNTIF(S), SUMIFS, AVERAGEIFS, SUMPRODUCT, INDEX, MATCH, EDATE, EOMONTH, TODAY, ROUND, LEN, NOT, ISNUMBER, COUNT, SUM. **Nicht** verwenden: IFS, MAXIFS, FILTER, XLOOKUP, TEXTJOIN, LET, dynamische Arrays. |
| Leerzeilen | Formeln in allen Datenzeilen vorbelegt und liefern `""`, solange die Zeile leer ist (keine Fehlerwerte in leeren Zeilen). |

## 4. Blattstruktur (verbindlich – Website nutzt diese Liste)

| # | Blattname (exakt) | Kapitelbezug | Zweck in einem Satz |
|---|---|---|---|
| – | `Start` | – | Zweck, Hyperlink-Inhaltsverzeichnis, Kurzanleitung, Version, Haftung, Lizenz, Firmenname |
| 01 | `01 Kontext & Parteien` | 4.1 / 4.2 | Interne/externe Themen und interessierte Parteien mit Relevanz, Umgang und Prüftermin |
| 02 | `02 Geltungsbereich & Prozesse` | 4.3 / 4.4 | Geltungsbereich, automatische Prozesslandkarte, Prozesstabelle |
| 03 | `03 Politik & Ziele` | 5.2 / 6.2 | Qualitätspolitik (Freigabe, Bekanntmachung) und messbare Qualitätsziele mit Zielerreichung |
| 04 | `04 Risiken & Chancen` | 6.1 | Risiko-/Chancenregister, Bewertung W×A mit Ampel, Maßnahmen, Neubewertung, 5×5-Matrix |
| 05 | `05 Rollen & Verantwortung` | 5.3 | Rollenliste mit Stellvertretung und Verantwortungsmatrix (V/D/M/I) |
| 06 | `06 Kompetenzmatrix` | 7.2 | Ist-/Soll-Qualifikation je Person, Lückenanzeige, Schulungsplan mit Wirksamkeit |
| 07 | `07 Dokumentenlenkung` | 7.5 | Dokumentenliste mit Version, Freigabe, Prüfintervall und Fälligkeit |
| 08 | `08 Lieferantenbewertung` | 8.4 | Punktebewertung → Klasse A/B/C, Freigabestatus, Maßnahmen |
| 09 | `09 NK & Korrekturmaßnahmen` | 8.7 / 10.2 | Fehler-/Reklamationsregister mit Ursache, Korrekturmaßnahme, Wirksamkeit, Status |
| 10 | `10 Internes Audit` | 9.2 | Auditprogramm (Jahresplan) und Auditcheckliste mit eigenen Leitfragen |
| 11 | `11 Managementbewertung` | 9.3 | Eingaben mit automatisch übernommenen Kennzahlen, Beschlüsse, Gesamtaussage |
| 12 | `12 KPI-Cockpit` | 9.1 | Kennzahlen per Formel aus 03, 04, 06, 07, 08, 09, 10, 13 mit Zielwert und Status, Diagramme |
| 13 | `13 Gap-Analyse` | 4–10 | Selbstbewertung mit Erfüllungsgrad je Kapitel in % und Umsetzungsplan |

Summe: **14 Blätter** (Start + 13 Arbeitsblätter). Keine zusätzlichen (auch keine ausgeblendeten) Hilfsblätter; Hilfsspalten nur innerhalb eines Blattes.

## 5. Blattdetails

Legende Typ: **E** = Eingabe, **D** = Dropdown, **F** = Formel, **Z** = Zahl mit Validierung.

### Start
- Titel, Untertitel mit Version „1.0“ und Stand.
- Eingabefelder: Unternehmen (wird auf 02 und 11 übernommen), QMB, Stand der Bearbeitung.
- Zweck (3–4 Sätze), Inhaltsverzeichnis: Blattname als **Hyperlink**, Kapitelbezug, Kurzbeschreibung.
- „So gehen Sie vor“ in 8 Schritten (Start mit 13 Gap-Analyse → 01/02 → 03/04/05 → 06/07/08 → 09/10 laufend → 12 → 11 jährlich).
- Farblegende (Eingabe, Formel, Beispiel, Ampel), Versionshinweis (wörtlich, s. Abschnitt 2), Haftungsausschluss, Lizenzhinweis.

### 01 Kontext & Parteien (4.1/4.2)
Leitfragen (eigene): Welche Entwicklungen außerhalb des Betriebs (Markt, Technik, Gesetze, Kunden) entscheiden mit darüber, ob Sie gute Qualität liefern? Welche internen Stärken oder Schwachstellen (Personal, Maschinen, Wissen) spielen hinein? Wer hat Erwartungen an Ihre Produkte und Abläufe – und welche davon machen Sie sich verbindlich zu eigen? Wann haben Sie das zuletzt überprüft?

| Spalte | Typ | Inhalt / Logik |
|---|---|---|
| Nr. | E | laufende Nummer |
| Kategorie | D | Externes Thema / Internes Thema / Interessierte Partei |
| Thema / Partei | E | |
| Beschreibung bzw. Erwartung | E | |
| Relevanz für QMS | D | Hoch / Mittel / Gering (Ampel rot/gelb/grün = Aufmerksamkeitsbedarf) |
| Umgang / Maßnahme | E | |
| Weiterverfolgt in | D | 03 Ziele / 04 Risiken & Chancen / 07 Dokumentenlenkung / 08 Lieferanten / Keine Maßnahme nötig |
| Verantwortlich | E | |
| Zuletzt geprüft | E (Datum) | |
| Nächste Prüfung | F | `=EDATE(Zuletzt;12)` |
| Prüfstatus | F | Überfällig / Fällig ≤30 Tage / Aktuell (Ampel) |

Beispiel: Interessierte Partei „Hauptkunde Landmaschinenbau“ – erwartet Liefertreue ≥ 95 % und Erstmusterprüfbericht bei Zeichnungsänderung; Relevanz Hoch; weiterverfolgt in 03 Ziele.

### 02 Geltungsbereich & Prozesse (4.3/4.4)
Leitfragen: Welche Standorte, Produkte und Leistungen gehören dazu – und gibt es begründete Ausnahmen? Welche Abläufe braucht es, damit aus einer Kundenanfrage ein zufriedener Kunde wird? Wer ist für jeden Ablauf verantwortlich, und woran messen Sie, dass er funktioniert?
- **A) Geltungsbereich**: Unternehmen (`=Start`), Standorte, Produkte/Leistungen, nicht zutreffende Anforderungen + Begründung, ausgelagerte Prozesse, Freigabe am/von. Beispieltexte grau kursiv.
- **B) Prozesslandkarte (automatisch)**: drei Bänder Führungs-, Kern-, Unterstützungsprozesse mit je 8 Feldern; links „Kundenanforderungen →“, rechts „→ Kundenzufriedenheit“. Befüllung per `INDEX/MATCH` über ausgeblendete Hilfsspalte `Prozessart|laufende Nr.` (keine dynamischen Arrays). Zeigt auch die Beispielzeile, bis sie überschrieben wird.
- **C) Prozesstabelle**: Nr. · Prozess · Prozessart (D: Führungsprozess/Kernprozess/Unterstützungsprozess) · Prozesseigner (D aus Rollenliste Blatt 05, Freitext erlaubt) · Input · Output · Kennzahl · Zielwert · Dokumentation/Vorgabe · Risiken (Verweis 04). Vorbelegt mit 9 typischen KMU-Prozessen (nur Name + Art) als anpassbare Vorschläge.
- Beispiel: „Fertigung (Schweißen & Montage)“, Kernprozess, Eigner Fertigung, Input Fertigungsauftrag + Material, Output geprüfte Baugruppe, Kennzahl interne Fehlerquote, Ziel < 1 %.

### 03 Politik & Ziele (5.2/6.2)
Leitfragen: Wofür soll Ihr Unternehmen bei Kunden in Sachen Qualität stehen? Passt das zur Strategie? Woran erkennen Sie in einem Jahr, dass Sie besser geworden sind – in Zahlen?
- **A) Qualitätspolitik**: großes Textfeld (Beispieltext grau, ausdrücklich „eigenen Text formulieren“), Freigegeben von/am, Bekanntgemacht über (D: Aushang/Intranet/Unterweisung/Website/Mehrere Wege), Nächste Überprüfung.
- **B) Qualitätsziele**:

| Spalte | Typ | Logik |
|---|---|---|
| Nr., Qualitätsziel, Bezug (Politik/Prozess), Kennzahl, Einheit | E | |
| Ausgangswert, Zielwert, Ist-Wert | E (Zahl) | |
| Richtung | D | Höher ist besser / Niedriger ist besser |
| Zielerreichung | F | höher: Ist/Ziel; niedriger: Ziel/Ist (Ist = 0 → 100 %); Fehler → leer |
| Status | F | ≥ 100 % Erreicht (grün), ≥ 90 % Knapp verfehlt (gelb), sonst Nicht erreicht (rot) |
| Maßnahmen, Verantwortlich, Termin, Stand vom | E | |

Beispiel: Liefertreue erhöhen, Ausgang 88 %, Ziel 95 %, Ist 92 % → 97 % „Knapp verfehlt“.

### 04 Risiken & Chancen (6.1)
Leitfragen: Was könnte schiefgehen, sodass Kunden falsche, fehlerhafte oder verspätete Ware bekommen? Wo liegen Chancen (neue Kunden, Automatisierung, Know-how)? Welche drei Punkte gehen Sie zuerst an, und hat die Maßnahme das Risiko wirklich gesenkt?

| Spalte | Typ | Logik |
|---|---|---|
| Nr., Typ (D: Risiko/Chance), Prozess/Bereich, Beschreibung, Ursache/Auslöser, Mögliche Auswirkung | E/D | |
| W (1–5) | Z | Wahrscheinlichkeit: 1 kaum denkbar · 2 selten (alle paar Jahre) · 3 gelegentlich (jährlich) · 4 häufig (mehrmals jährlich) · 5 fast sicher/laufend |
| A (1–5) | Z | Auswirkung: 1 kaum spürbar · 2 interner Mehraufwand · 3 Kunde bemerkt es (Reklamation) · 4 erheblicher Schaden/Lieferstopp · 5 existenzbedrohend/Kundenverlust |
| W×A | F | Produkt (1–25) |
| Einstufung | F | ≥ 10 Hoch (rot) · 5–9 Mittel (gelb) · ≤ 4 Gering (grün). Für Chancen = Priorität, einheitlich hellgrün markiert |
| Maßnahme, Verantwortlich, Termin | E | |
| Status | D | Offen / In Umsetzung / Umgesetzt / Wirksam bestätigt |
| W neu, A neu | Z | Neubewertung nach Maßnahme |
| W×A neu | F | |
| Wirksamkeit geprüft am | E | |

Rechts neben der Tabelle: **5×5-Risikomatrix** (Anzahl Risiken je Feld per `COUNTIFS`, ohne Beispielzeile), Felder nach Zone eingefärbt, darunter Skalenlegende.
Beispiel: Ausfall des einzigen Lieferanten für verzinkte Bleche, W 3 × A 4 = 12 Hoch → Zweitlieferant qualifizieren, Sicherheitsbestand; neu 2 × 3 = 6.
Fachhinweis: Schwellen 5/10 sind eine bewusst einfache KMU-Konvention, keine Normvorgabe; anpassbar.

### 05 Rollen & Verantwortung (5.3)
Leitfragen: Weiß jede Schlüsselperson, wofür sie geradesteht – und wer sie im Urlaub vertritt? Gibt es Aufgaben, für die sich niemand oder gleich mehrere zuständig fühlen?
- **A) Rollen**: Nr. · Rolle · Kürzel · Stelleninhaber/in · Stellvertretung · Befugnisse/Kernaufgaben. 10 Zeilen, 8 vorbelegt (Geschäftsführung GF, QMB, Vertrieb VT, Einkauf EK, Arbeitsvorbereitung AV, Fertigung FE, Lager & Versand LV, Personal PE), 2 frei.
- **B) Verantwortungsmatrix**: Aufgabe/Prozess · Kap. · 10 Rollenspalten (Kopf per Formel = Kürzel bzw. Rollenname aus A) mit D: **V** verantwortlich, **D** durchführend, **M** mitwirkend, **I** informiert · Anzahl V (F) · Prüfung (F): genau 1 V → „OK“, 0 → „Kein V“, > 1 → „Mehrere V“ (Ampel). 16 typische QM-Aufgaben vorbelegt.
- Beispiel: Wareneingangsprüfung (8.6): QMB V, LV D, EK I.

### 06 Kompetenzmatrix (7.2)
Leitfragen: Welche Fähigkeiten braucht jede Tätigkeit – und wer hat sie nachweislich? Wo hängt Wissen an einer einzigen Person? Hat die letzte Schulung tatsächlich etwas verändert?
- Kopfzeile mit 10 editierbaren Qualifikationen (vorbelegt: Schweißen MAG, Zeichnungslesen, Messen & Prüfen, Fehlerkennzeichnung/Sperren, Arbeitssicherheit, QM-Grundlagen, Problemlösung/8D, Internes Audit, ERP-Bedienung, Staplerschein).
- Zeile „Soll-Niveau“ je Qualifikation (0–4).
- Je Person: Name, Bereich, Funktion, Ist-Niveau 0–4 (Z) je Qualifikation. **Leer = für diese Person nicht relevant; 0 = erforderlich, aber nicht vorhanden.** Skala: 0 nicht vorhanden · 1 in Einarbeitung (nur unter Aufsicht) · 2 selbstständig · 3 sicher auch bei Sonderfällen · 4 kann schulen.
- Erfüllungsgrad (F) = Anteil relevanter Qualifikationen mit Ist ≥ Soll; Anzahl Lücken (F); nächste Schulung (E). Zellen-Ampel Ist < Soll rot, Ist ≥ Soll grün.
- Abschnitt **Schulungsplan**: Maßnahme · Teilnehmende · Durchgeführt von · Geplant am · Durchgeführt am · Status (F: Durchgeführt/Überfällig/Geplant) · Wirksamkeit (D: Wirksam/Teilweise wirksam/Nicht wirksam/Noch offen) · Nachweis.

### 07 Dokumentenlenkung (7.5)
Leitfragen: Findet jede Person am Arbeitsplatz immer die gültige Fassung? Wer prüft und gibt frei – und sind das zwei verschiedene Personen? Welche Nachweise bewahren Sie wie lange auf?

Spalten: Dok.-Nr. · Titel · Art (D: Verfahrensanweisung/Arbeitsanweisung/Formblatt/Vorlage/Prüfplan/Externe Vorgabe/Aufzeichnung/Nachweis) · Kap.-Bezug · Version · Erstellt von · Geprüft von · Freigegeben von · Freigabe am · Prüfintervall Monate (Z 1–60) · Nächste Überprüfung (F `EDATE`) · Status (D: Entwurf/In Prüfung/Freigegeben/Zurückgezogen) · Ablageort · Aufbewahrung Jahre · Fälligkeit (F, Ampel; leer bei „Zurückgezogen“) · Hinweis (F: „Ersteller = Freigeber prüfen“, wenn identisch).

### 08 Lieferantenbewertung (8.4)
Leitfragen: Nach welchen Kriterien wählen Sie Lieferanten aus? Wie oft und anhand welcher Fakten bewerten Sie sie? Was passiert konkret mit einem schlecht bewerteten Lieferanten?

| Spalte | Typ | Logik |
|---|---|---|
| Lief.-Nr., Lieferant, Warengruppe/Leistung, Zeitraum | E | |
| Bedeutung | D | Hoch (produktkritisch) / Mittel / Gering |
| Lieferungen, davon termingerecht | E | |
| Liefertreue | F | termingerecht / Lieferungen |
| Gelieferte Teile, Beanstandete Teile | E | |
| ppm | F | beanstandet / geliefert × 1 000 000 |
| Reklamationen (Anzahl) | E | |
| Pkt. Qualität (0–10) | F | ppm ≤ 100 → 10 · ≤ 500 → 8 · ≤ 1 000 → 6 · ≤ 5 000 → 4 · darüber 2 |
| Pkt. Liefertreue (0–10) | F | ≥ 98 % → 10 · ≥ 95 % → 8 · ≥ 90 % → 6 · ≥ 80 % → 4 · darunter 2 |
| Pkt. Kommunikation/Reaktion (0–10) | Z | Einschätzung Einkauf/QM |
| Pkt. QM-System/Nachweise (0–10) | Z | z. B. 10 = gültiges Zertifikat und vollständige Nachweise, 5 = Selbstauskunft, 0 = keine |
| Gesamtpunkte (0–100) | F | gewichtete Summe × 10; Gewichte in Zeile über der Kopfzeile (Vorschlag 40/30/15/15 %), Summenprüfung „= 100 %“ |
| Klasse | F | ≥ 80 A (grün) · 60–79 B (gelb) · < 60 C (rot) |
| Freigabestatus | D | Freigegeben / Bedingt freigegeben / Gesperrt / In Prüfung |
| Maßnahme/Vereinbarung, Bewertet am, Bewertet von | E | |

Wichtig: „A/B/C“ ist hier eine **Leistungsklasse**, keine ABC-Analyse nach Einkaufsvolumen. ppm-Schwellen sind branchenabhängig (Automotive deutlich strenger als z. B. Stahlbau-Handel) – im Blatt als anpassbar kennzeichnen. Beispiel: Beispiel-Stahlhandel GmbH, 48 Lieferungen / 45 pünktlich (93,8 % → 6), 750 ppm (→ 6), Kommunikation 7, QM-System 10 → 67,5 Punkte = B.

### 09 NK & Korrekturmaßnahmen (8.7/10.2)
Leitfragen: Was passiert in der ersten Stunde nach Entdeckung eines Fehlers? Wurde die eigentliche Ursache gefunden oder nur das Symptom behoben? Wie weisen Sie nach, dass der Fehler nicht wiederkommt?

Spalten: NK-Nr. · Erfasst am · Quelle (D: Kundenreklamation/Lieferantenreklamation/Interner Fehler/Auditfeststellung/Prozessabweichung/Sonstiges) · Prozess/Bereich · Teil/Auftrag · Beschreibung · Betroffene Menge · Sofortmaßnahme · Ursache · Ursachenkategorie (D: Mensch/Maschine/Material/Methode/Messung/Mitwelt) · Korrekturmaßnahme · Verantwortlich · Termin · Erledigt am · Wirksamkeit (D: Wirksam/Nicht wirksam/Noch nicht geprüft) · Risiken/QMS angepasst? (D: Ja/Nein/Nicht nötig) · Fehlerkosten € · **Status (F)**: Abgeschlossen (erledigt + wirksam) / Erledigt – Wirksamkeit prüfen / Überfällig (Termin < heute) / Offen · Durchlaufzeit Tage (F, erledigt − erfasst).
Beispiel: Kundenreklamation Rahmen RT-200, Schweißnaht nicht durchgeschweißt, Ursache Parameter nach Drahtwechsel nicht angepasst (Methode), Parametertabelle am Platz + Erststückprüfung, wirksam, 1 850 €.

### 10 Internes Audit (9.2)
Leitfragen: Werden alle Prozesse in einem sinnvollen Rhythmus angeschaut – häufiger dort, wo es brennt? Prüft niemand seinen eigenen Bereich? Werden Feststellungen als NK in Blatt 09 weiterverfolgt?
- **A) Auditprogramm**: Audit-Nr. · Prozess/Bereich · Kapitelbezug · Auditor · Unabhängig (D: Ja/Nein; „Nein“ rot) · Geplant (Monat) · Durchgeführt am · Status (F: Durchgeführt/Überfällig ab Monatsende/Geplant) · Abweichungen (Anzahl) · Verbesserungspotenziale (Anzahl) · NK-Nr. (Verweis 09) · Bericht/Ablage.
- **B) Auditcheckliste**: Feld „gehört zu Audit-Nr.“; Spalten Nr. · Leitfrage (Praxis) · Kap. · Gesehene Nachweise · Bewertung (D: Erfüllt/Teilweise/Nicht erfüllt/Nicht anwendbar) · Punkte (F 2/1/0/leer) · NK-Nr. · Notiz. Erfüllungsgrad der Checkliste = Punkte / (2 × bewertete Fragen). Vorbelegt mit **31 eigenen Leitfragen** (Fragenkatalog in Abschnitt 6), identisch mit Blatt 13.

### 11 Managementbewertung (9.3)
Leitfragen: Funktioniert das QM-System – und woran sehen Sie das? Reichen die Ressourcen? Welche drei Entscheidungen treffen Sie für das nächste Jahr?
- Kopf: Unternehmen (=Start), Berichtszeitraum, Datum, Teilnehmende, Protokoll von.
- **A) Eingaben**: Thema (eigene Formulierung) · Kap. · Quelle im Baukasten (Hyperlink) · Kennzahl · Wert (**F**, aus Blatt 12 bzw. Blatt 11 B) · Erkenntnis/Bewertung · Trend (D: Verbessert/Unverändert/Verschlechtert/Erstmals erhoben) · Handlungsbedarf (D: Ja/Nein). 12 Themen vorbelegt: Umsetzung früherer Beschlüsse; Veränderungen im Umfeld; Kundenrückmeldungen; Qualitätsziele; Prozessleistung/Produktkonformität; NK & Korrekturmaßnahmen; Kennzahlen-Überwachung; Auditergebnisse; Lieferantenleistung; Ressourcen/Kompetenz; Wirksamkeit Risikomaßnahmen; Verbesserungsmöglichkeiten.
- **B) Beschlüsse**: Beschluss/Maßnahme · Art (D: Verbesserung/Änderung am QM-System/Ressourcenbedarf/Sonstiges) · Verantwortlich · Termin · Status (D: Offen/In Arbeit/Erledigt) · Bemerkung.
- **C) Gesamtaussage** der Geschäftsführung zur Eignung/Wirksamkeit (Freitext) + Datum/Unterschrift.

### 12 KPI-Cockpit (9.1)
Reines Auswertungsblatt. Spalten: Nr. · Kennzahl · Quelle (Hyperlink) · Ist-Wert (F) · Zielwert (E, Vorschlagswerte vorbelegt) · Bewertungsrichtung (D: Max/Min/Nur Info) · Status (F: Im Ziel/Abweichung/–, Ampel) · Berechnung.
Kennzahlen (alle **ohne Beispielzeilen**):
- 03: Anteil erreichter Qualitätsziele
- 04: erfasste Risiken · hohe Risiken · hohe Risiken ohne „Wirksam bestätigt“ · erfasste Chancen · überfällige Maßnahmen
- 06: Mitarbeitende mit Qualifikationslücke
- 07: Dokumente mit überfälliger Überprüfung
- 08: bewertete Lieferanten · Anzahl A/B/C · Anteil C · Liefertreue gesamt · ppm gesamt · Lieferantenreklamationen
- 09: NK gesamt · davon Kundenreklamationen · nicht abgeschlossen · überfällig · Wirksamkeitsquote · Ø Durchlaufzeit · Fehlerkosten
- 10: geplante/durchgeführte Audits · Umsetzungsquote · überfällige Audits · Abweichungen · nicht unabhängige Auditoren · Erfüllungsgrad Checkliste
- 13: Erfüllungsgrad Gap-Analyse gesamt
Division durch 0 → „k. A.“ (kein Fehlerwert). Darunter Hilfstabellen + Diagramme: NK nach Quelle, Lieferanten nach Klasse.

### 13 Gap-Analyse (4–10)
- **A) Zusammenfassung**: je Kapitel 4–10: Kapitelüberschrift (kurz), Fragen bewertet, Erfüllungsgrad % = Punkte / (2 × bewertete Fragen), Status (≥ 80 % „Weitgehend erfüllt“ grün · ≥ 50 % „Teilweise erfüllt“ gelb · < 50 % „Große Lücke“ rot · keine Bewertung „Noch nicht bewertet“), Gesamtzeile; Balkendiagramm.
- **B) Fragen & Umsetzungsplan**: Nr. · Leitfrage · Kap. (Z 4–10) · Abschnitt · Bewertung (D: Vollständig umgesetzt/Teilweise umgesetzt/Nicht umgesetzt/Nicht anwendbar) · Punkte (F 2/1/0/leer) · Maßnahme · Verantwortlich · Termin · Status (D: Offen/In Arbeit/Erledigt) · Werkzeug im Baukasten (Hyperlink auf passendes Blatt).
- „Nicht anwendbar“ zählt weder im Zähler noch im Nenner.

## 6. Fragenkatalog (eigene Formulierungen; Blatt 10 B und 13 B)

| Kap. | Abschnitt | Leitfrage | Werkzeug |
|---|---|---|---|
| 4 | 4.1 | Woran merken Sie, wenn sich Markt, Kunden oder gesetzliche Vorgaben ändern – und wo wird das festgehalten? | 01 |
| 4 | 4.2 | Wer sind Ihre wichtigsten Anspruchsgruppen, und welche ihrer Erwartungen haben Sie als verbindlich übernommen? | 01 |
| 4 | 4.3 | Ist schriftlich festgelegt, welche Standorte, Produkte und Leistungen das QM-System umfasst – und sind Ausnahmen begründet? | 02 |
| 4 | 4.4 | Gibt es eine aktuelle Prozessübersicht mit Verantwortlichen, Schnittstellen und Kennzahlen? | 02 |
| 5 | 5.1 | Wie zeigt die Geschäftsführung im Alltag, dass Qualität Chefsache ist (z. B. Teilnahme an Besprechungen, Ressourcenentscheidungen)? | 11 |
| 5 | 5.1 | Wie oft sind Kundenanforderungen und Kundenzufriedenheit Thema in Führungsrunden? | 11 |
| 5 | 5.2 | Ist die Qualitätspolitik aktuell, passt sie zur Strategie, und können Mitarbeitende sie sinngemäß erklären? | 03 |
| 5 | 5.3 | Wissen alle Schlüsselpersonen, wofür sie verantwortlich sind und wer sie vertritt? | 05 |
| 6 | 6.1 | Liegt eine bewertete Liste von Risiken und Chancen vor, und haben hohe Risiken Maßnahmen mit Termin? | 04 |
| 6 | 6.2 | Sind Qualitätsziele messbar, terminiert und mit Verantwortlichen hinterlegt – und wird der Stand verfolgt? | 03 |
| 6 | 6.3 | Werden größere Änderungen (neue Maschine, neuer Standort, Personalwechsel) vorab geplant und bewertet? | 04 |
| 7 | 7.1 | Reichen Personal, Maschinen und Infrastruktur, um die Aufträge in der geforderten Qualität abzuarbeiten? | 11 |
| 7 | 7.1.5 | Sind Mess- und Prüfmittel eindeutig gekennzeichnet, kalibriert bzw. überprüft, und ist der Status erkennbar? | 07 |
| 7 | 7.2 | Gibt es für jede Tätigkeit festgelegte Qualifikationsanforderungen und Nachweise, dass sie erfüllt sind? | 06 |
| 7 | 7.3 | Kennen die Mitarbeitenden die Auswirkungen ihrer Arbeit auf Produktqualität und Kunden? | 06 |
| 7 | 7.4 | Ist geregelt, wer was wann an wen kommuniziert – intern und gegenüber Kunden und Lieferanten? | 05 |
| 7 | 7.5 | Finden Mitarbeitende am Arbeitsplatz immer die gültige Version einer Vorgabe – und sind alte Versionen aus dem Umlauf? | 07 |
| 7 | 7.5 | Ist festgelegt, welche Aufzeichnungen wie lange aufbewahrt werden und wer darauf zugreifen darf? | 07 |
| 8 | 8.2 | Werden Anfragen und Aufträge vor Annahme auf Machbarkeit (Termin, Technik, Kapazität) geprüft, und ist das nachvollziehbar? | 02 |
| 8 | 8.3 | Falls Sie selbst entwickeln: Gibt es Freigabepunkte und dokumentierte Ergebnisse in Entwicklungsprojekten? | 02 |
| 8 | 8.4 | Werden Lieferanten nach festgelegten Kriterien ausgewählt, regelmäßig bewertet, und folgen bei schlechter Leistung Maßnahmen? | 08 |
| 8 | 8.5 | Haben die Mitarbeitenden in der Fertigung die nötigen Zeichnungen, Arbeitsanweisungen und Prüfvorgaben am Platz? | 07 |
| 8 | 8.5 | Ist jederzeit erkennbar, ob ein Teil geprüft, freigegeben oder gesperrt ist, und lässt sich nachverfolgen, woher es stammt? | 09 |
| 8 | 8.6 | Wer gibt Produkte vor der Auslieferung frei, und wie ist das dokumentiert? | 05 |
| 8 | 8.7 | Werden fehlerhafte Teile sofort gekennzeichnet und abgesondert, und wird über ihre Verwendung nachvollziehbar entschieden? | 09 |
| 9 | 9.1 | Welche Kennzahlen zeigen, ob Ihre Prozesse funktionieren – und wer schaut sie wie oft an? | 12 |
| 9 | 9.1 | Wie erfahren Sie systematisch, wie zufrieden Ihre Kunden sind? | 12 |
| 9 | 9.2 | Gibt es ein Auditprogramm, das alle Prozesse in einem sinnvollen Zeitraum abdeckt, mit unabhängigen Auditoren? | 10 |
| 9 | 9.3 | Hat die Geschäftsführung das QM-System im letzten Jahr bewertet, und sind daraus Beschlüsse mit Terminen entstanden? | 11 |
| 10 | 10.2 | Werden bei Reklamationen und internen Fehlern Ursachen analysiert und die Wirksamkeit der Maßnahmen geprüft? | 09 |
| 10 | 10.3 | Wie werden Verbesserungsideen von Mitarbeitenden erfasst und umgesetzt? | 13 |

Fachhinweis: Die Fragen sind bewusst als Prüf-Impulse formuliert und decken die Kapitel nicht abschließend ab. Für ein Zertifizierungsaudit ist der Abgleich mit dem Normtext durch den Anwender erforderlich.

## 7. Typische Anwenderfehler (in Anleitung aufnehmen)
1. Beispielzeile stehen lassen und „mitzählen“ wollen → wird bewusst ignoriert; überschreiben oder löschen.
2. Risiken nur einmalig bewerten → Neubewertung (W/A neu) und Status „Wirksam bestätigt“ pflegen.
3. Ziele ohne Zahl („Qualität verbessern“) → Kennzahl, Einheit, Zielwert, Richtung immer ausfüllen.
4. Lieferanten nur nach Gefühl bewerten → Lieferungen/ppm aus ERP bzw. Wareneingang eintragen.
5. NK „erledigt“ ohne Wirksamkeitsprüfung → Status bleibt „Erledigt – Wirksamkeit prüfen“.
6. Auditor prüft eigenen Bereich → Spalte „Unabhängig“ = Nein wird rot.
7. Ersteller gibt eigenes Dokument frei → Hinweis in Blatt 07.
8. Spalten/Zeilen mitten in Tabellen einfügen bricht Formelbereiche nicht, aber Zeilen **unterhalb** der letzten Tabellenzeile werden nicht ausgewertet → vorhandene Leerzeilen nutzen, ggf. Zeilen innerhalb der Tabelle einfügen.
9. Blattnamen ändern ist möglich (Formeln passen sich an), Hyperlinks im Inhaltsverzeichnis müssen dann aber neu gesetzt werden.

## 8. Abnahmekriterien (Fachfreigabe)
- 14 Blätter, Namen exakt wie Abschnitt 4.
- Kein Normtext, nur Kapitelnummern/-überschriften und eigene Leitfragen.
- Versionshinweis wörtlich auf Start und in Anleitung; Haftung/Lizenz vorhanden; keine Zertifizierungsgarantie.
- Alle Formeln ohne Fehlerwerte – leer und mit Testdaten.
- Beispielzeile je Tabelle grau und in Kennzahlen ausgeschlossen.
- Beispieldaten fiktiv (Muster Metallbau GmbH, Beispiel-Stahlhandel GmbH).

## 9. Offene Punkte / Unsicherheiten
- **ISO 9001:2026:** Veröffentlichung im Sept. 2026 nur berichtet, nicht verifiziert. Kapitelzuordnungen (v. a. Unterabschnitte wie 7.1.5, 8.5.2) vor Verkauf gegen die gültige Ausgabe prüfen; ggf. neue Themen (berichtet u. a. stärkere Betonung von Qualitätskultur/Ethik – **nicht verifiziert**) in Leitfragen ergänzen.
- Bewertungsschwellen (Risiko 5/10, Lieferanten-ppm, A/B/C 80/60, Gap 80/50 %) sind Praxis-Konventionen, keine Normvorgaben – als anpassbar kommunizieren.
- Funktionstest mit Microsoft Excel und Google Sheets steht aus (Build-Umgebung: LibreOffice).
