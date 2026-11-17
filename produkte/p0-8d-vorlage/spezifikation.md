# Spezifikation – p0-8d-vorlage „8D-Report Vorlage (Excel)“

> Rolle: sqe-experte · Stand: 17.11.2026 · Version Spezifikation 1.0
> Produkttyp: kostenloser Lead-Magnet (Preis 0 €, Download nach Double-Opt-in)
> Dateiname: `dist/8D-Report-Vorlage.xlsx`

## 1. Zweck
Eine schlanke, sofort nutzbare Excel-Arbeitsmappe, mit der ein Lieferant (oder eine interne Qualitätsabteilung) eine Reklamation strukturiert nach der 8D-Methode bearbeitet und dem Kunden berichtet – inklusive Ursachenanalyse (5-Why, Ishikawa) und Maßnahmenverfolgung.

Die 8D-Methode selbst ist ein allgemein bekanntes Problemlösungsvorgehen. Die Vorlage verwendet **eigene Formulierungen, eigenes Layout und eigene Leitfragen**. Sie bildet **kein** offizielles Formblatt nach (weder das VDA-8D-Formular noch AIAG-/Kunden-Formblätter). Kundenspezifische Formulare (Customer Specific Requirements) haben Vorrang – das wird auf dem Startblatt erwähnt.

## 2. Zielnutzer
- SQE und Qualitätsingenieure beim Kunden, die 8D-Reports einfordern und bewerten
- Qualitätsverantwortliche bei Zulieferern (KMU), die 8D-Reports **schreiben** müssen
- Einsteiger (0–3 Jahre), die eine Struktur mit Leitfragen brauchen

## 3. Tabellenblätter (verbindlich)
| # | Blatt | Inhalt |
|---|---|---|
| 1 | Start | Zweck, Hyperlink-Inhaltsverzeichnis, Kurzanleitung in 6 Schritten, Farblegende, Version, Lizenzhinweis, Haftungsausschluss, Hinweis zu Normen/Kundenformularen |
| 2 | 8D-Report | Kopfdaten, Statusübersicht D0–D8 mit Fortschrittsanzeige, Abschnitte D0–D8 |
| 3 | 5-Why | Zwei getrennte Pfade: (A) Warum ist der Fehler **aufgetreten**? (B) Warum wurde er **nicht entdeckt**? |
| 4 | Ishikawa | 6M-Ursachensammlung in Tabellenform mit Bewertung + Zusammenfassung je M |
| 5 | Maßnahmentracker | Alle Maßnahmen (D3/D5/D6/D7) mit Verantwortlich, Termin, Status, Ampel bei Überfälligkeit |

Ein zusätzliches, ausgeblendetes Hilfsblatt ist **nicht** vorgesehen; Auswahllisten werden direkt als Listen in der Datenvalidierung hinterlegt (robust in Excel, LibreOffice und Google Sheets).

## 4. Blatt „8D-Report“ – Felder

### 4.1 Kopfdaten
8D-Nr. · Datum Eröffnung · Kunde · Reklamationsnr. Kunde · Lieferant · Lieferanten-Nr. · Teilenummer · Teilebezeichnung · Fehlerbezeichnung (kurz) · Betroffene Menge · Erstmeldung am · Ansprechpartner (Name, E-Mail).

### 4.2 Statusübersicht D0–D8
Spalten: Disziplin | Bezeichnung | Verantwortlich | Soll-Termin | Erledigt am | Status | Terminampel.
- Status-Dropdown: `offen`, `in Arbeit`, `erledigt`, `n. a.` (nicht anwendbar – nur für D0 sinnvoll)
- Terminampel (Formel): `erledigt` → „erledigt“; `n. a.` → „–“; kein Soll-Termin → „kein Termin“; Soll-Termin < HEUTE() → „überfällig“; Soll-Termin ≤ HEUTE()+7 → „fällig ≤ 7 T“; sonst „im Plan“.
- **Fortschritt** = Anzahl „erledigt“ / (9 − Anzahl „n. a.“) in %, dargestellt als Prozentwert mit Datenbalken und Textbalken (■□).
- Orientierungswerte für Soll-Termine (Hinweistext, keine Normvorgabe): Sofortmaßnahmen (D3) typischerweise innerhalb von 24 h, Ursache und geplante Abstellmaßnahmen (D4/D5) häufig innerhalb von 10 Arbeitstagen – **maßgeblich sind immer die Vorgaben des Kunden**. [Praxiswert, kundenabhängig]

### 4.3 Abschnitte
| Abschnitt | Felder / Tabellen | Leitfragen (eigene Formulierung) |
|---|---|---|
| **D0 Notfall-/Sofortreaktion (optional)** | Freitext: Notfallreaktion, Kunde informiert am, Sicherheits-/Gesetzesrelevanz (ja/nein/unklar) | Muss sofort etwas gestoppt, gesperrt oder gemeldet werden? |
| **D1 Team** | Tabelle: Name · Funktion/Abteilung · Rolle (Teamleiter/Teammitglied/Sponsor/Experte) · Kontakt | Wer hat Fachwissen, Entscheidungsbefugnis und Zeit? |
| **D2 Problembeschreibung** | Freitext Fehlerbild aus Kundensicht; Tabelle **5W2H** (Was, Wo, Wann, Wer, Warum relevant, Wie, Wie viele); Tabelle **Ist / Ist-nicht** (Merkmal · IST betroffen · IST NICHT betroffen, obwohl möglich · Unterschied/Auffälligkeit) | Ist das Problem so beschrieben, dass jemand Fremdes es versteht – ohne Ursache vorwegzunehmen? |
| **D3 Sofortmaßnahmen** | Tabelle: Maßnahme · Ort (Kunde/Transit/Lager/Fertigung) · Verantwortlich · Termin · Status · Wirksamkeit belegt durch · Wirksam (ja/nein/offen) | Ist der Kunde geschützt? Wurden alle Bestände (auch unterwegs) erfasst? Wie werden geprüfte Teile gekennzeichnet? |
| **D4 Ursachen** | Zwei Tabellen: **Auftreten** und **Nichtentdeckung**, je: Ursache · Nachweis/Verifizierung · verifiziert (ja/nein/offen) · Anteil/Bemerkung; Verweis auf Blätter 5-Why und Ishikawa | Lässt sich der Fehler mit der Ursache gezielt ein- und ausschalten? Warum hat die Prüfung nicht angeschlagen? |
| **D5 Abstellmaßnahmen geplant** | Tabelle: bezieht sich auf Ursache (Auftreten/Nichtentdeckung) · Maßnahme · Verantwortlich · Termin geplant · Risiko/Nebenwirkung geprüft (ja/nein) | Wirkt jede Maßnahme auf eine verifizierte Ursache? |
| **D6 Umsetzung & Wirksamkeitsnachweis** | Tabelle: Maßnahme · umgesetzt am · Wirksamkeitsnachweis (z. B. Ergebnisse über n Lose, Prüfdaten) · Nachweis bis · wirksam (ja/nein/offen) · Sofortmaßnahme aufgehoben am | Woran sehen wir objektiv, dass der Fehler nicht mehr auftritt? |
| **D7 Wiederholung verhindern / Lessons Learned** | Checkliste mit Dropdown (ja/nein/n. a.) + Bemerkung: FMEA aktualisiert, Produktionslenkungsplan aktualisiert, Arbeits-/Prüfanweisung angepasst, Mitarbeiter geschult, Übertrag auf ähnliche Produkte/Prozesse, Lessons Learned dokumentiert | Wo könnte derselbe Fehler noch auftreten? |
| **D8 Abschluss & Würdigung** | Abschlussdatum, Abschluss durch, Kundenbestätigung (ja/nein/offen), Würdigung Team (Freitext) | Hat der Kunde den Abschluss bestätigt? Wurde das Team gewürdigt? |

## 5. Blatt „5-Why“
- Kopf: Problembeschreibung (Formel-Verweis auf das Feld „Fehlerbezeichnung“ im 8D-Report, überschreibbar).
- **Pfad A – Auftreten** und **Pfad B – Nichtentdeckung**, jeweils 5 Zeilen: Nr · Warum …? · Antwort (Ursache) · Nachweis/Fakt · verifiziert (ja/nein/offen).
- Darunter je Pfad: „Grundursache (Root Cause)“ und „→ übertragen nach D4“.
- Regeln (Hinweistext): nicht bei Warum 5 stoppen müssen – stoppen, wenn eine abstellbare, verifizierte Ursache erreicht ist; keine Personen-Schuldzuweisung als Endursache („Mitarbeiter hat nicht aufgepasst“ ist keine Grundursache); jede Antwort mit Fakt belegen.
- Beispielinhalt: Pfad A und B je eine vollständige, **grau-kursive** Beispielkette (fiktiv), gekennzeichnet „Beispiel – löschen“. Abweichung von „eine Beispielzeile“ bewusst: eine Kette ist nur zusammenhängend verständlich.

## 6. Blatt „Ishikawa“
- Kopf: Wirkung/Problem (Verweis auf 8D-Report).
- Tabelle: Nr · 6M-Kategorie (Dropdown: Mensch, Maschine, Methode, Material, Messung, Mitwelt) · mögliche Ursache · Bewertung (Dropdown: wahrscheinlich, möglich, ausgeschlossen, bestätigt) · Prüfung/Nachweis · Verantwortlich · Termin.
- Zusammenfassung je M: Anzahl Ursachen gesamt, davon „bestätigt“, „wahrscheinlich“, „ausgeschlossen“ (COUNTIFS).
- Bedingte Formatierung: bestätigt = rot hinterlegt (Ursache!), wahrscheinlich = gelb, ausgeschlossen = grau.
- Hinweis: Material hier = Rohmaterial/Zukaufteile; Mitwelt = Umgebung (Temperatur, Sauberkeit, Licht …).

## 7. Blatt „Maßnahmentracker“
Spalten: Nr · 8D-Bezug (D3/D5/D6/D7/sonstige) · Maßnahme · Art (Sofortmaßnahme/Abstellmaßnahme/Vorbeugemaßnahme) · Verantwortlich · Termin · Status (offen/in Arbeit/erledigt/verworfen) · erledigt am · Wirksamkeit geprüft (ja/nein/offen) · Ampel · Tage überfällig · Bemerkung.
- Ampel (Formel mit HEUTE()): Status erledigt/verworfen → „erledigt“ (grün) bzw. „verworfen“ (grau); Termin leer → „kein Termin“; Termin < HEUTE() → „überfällig“ (rot); Termin ≤ HEUTE()+7 → „fällig ≤ 7 T“ (gelb); sonst „im Plan“ (grün).
- Tage überfällig = HEUTE() − Termin, nur wenn überfällig.
- Kopfzeile: Zähler offen / überfällig / erledigt.
- 100 vorformatierte Zeilen.

## 8. Bewertungslogik / Formeln (Zusammenfassung)
| Ort | Formel-Logik |
|---|---|
| 8D Fortschritt | `ZÄHLENWENN(Status;"erledigt") / (9 − ZÄHLENWENN(Status;"n. a."))` |
| Terminampeln | verschachteltes WENN mit HEUTE() (siehe 4.2/7) |
| Ishikawa Summen | ZÄHLENWENNS je Kategorie und Bewertung |
| Tracker Zähler | ZÄHLENWENN je Status/Ampel |
Alle Formeln ohne Makros, ohne Matrixformeln, ohne Funktionen jünger als Excel 2010 (Kompatibilität Excel/LibreOffice/Google Sheets).

## 9. Fiktive Beispieldaten
- Kunde: **Muster GmbH** (fiktiv), Lieferant: **Beispiel-Druckguss GmbH** (fiktiv)
- Teil: Halter, Aluminium-Druckguss, TN 100-2034 (fiktiv)
- Fehler: Gewindebohrung M6 fehlt (nicht gebohrt), 12 Teile in Lieferung 2026-11-03 gefunden, Liefermenge 2.400 Teile
- Ursache Auftreten (Beispiel): Bohrwerkzeug gebrochen, Werkzeugbruchkontrolle an der Bearbeitungsstation war deaktiviert nach Wartung
- Ursache Nichtentdeckung (Beispiel): Endprüfung erfolgt als Stichprobe 1×/Schicht; fehlendes Gewinde fällt bei Sichtprüfung im Durchlauf nicht auf; keine 100-%-Gewindeprüfung

## 10. Typische Anwenderfehler (werden in Anleitung/Leitfragen adressiert)
1. D2 enthält bereits die Ursache („Fehler durch Werkzeugbruch“) → Beschreibung und Ursache trennen.
2. Nur Auftretensursache, keine Nichtentdeckungsursache.
3. Sofortmaßnahme (Sortieren) wird als Abstellmaßnahme verkauft.
4. „Mitarbeiter geschult“ als einzige Maßnahme – wirkt nicht nachhaltig.
5. Wirksamkeit nicht belegt (D6 ohne Daten).
6. Sofortmaßnahmen werden nie formal aufgehoben.
7. D7 leer: FMEA und Produktionslenkungsplan nicht aktualisiert.

## 11. Rechtliches / Abgrenzung
- Keine Normtexte, keine Kopie offizieller VDA-/AIAG-/Kundenformblätter. „VDA“, „AIAG“ werden höchstens als Bezug genannt.
- Lizenz: kostenlose Nutzung im eigenen Unternehmen; Weitergabe, Weiterverkauf, Veröffentlichung untersagt; Weiterleitung des Download-Links erlaubt.
- Haftungsausschluss: Arbeitshilfe, keine Beratung; Prüfung der Eignung und der Kundenanforderungen liegt beim Anwender.

## 12. Offene Punkte / Unsicherheiten
- Orientierungsfristen (24 h / 10 Arbeitstage) sind Praxiswerte, keine allgemeingültige Vorgabe – als solche kennzeichnen.
