# 01 – Recherche: „8D-Report erklärt – alle 8 Disziplinen am Praxisbeispiel“

> Rolle: `recherche` · Stand: 17.11.2026 · Video #1 laut `kanal/content-plan.md` · Säule: Reklamation & Problemlösung
> **Methodenhinweis:** Die Recherche lief über eine echte Websuche. Der direkte Seitenabruf (WebFetch) war in dieser Sitzung für die meisten Domains gesperrt (u. a. webshop.vda.de, asq.org, en.wikipedia.org). Die Aussagen stützen sich daher auf die Treffer und Auszüge der Suchmaschine zu den genannten URLs. Deshalb ist die Belastbarkeit eine Stufe vorsichtiger angesetzt. **Inhaberaufgabe:** Die mit ⚑ markierten Quellen vor dem Upload einmal im Browser öffnen (≈ 5 Min.).

## 1. Kernfrage & Unterfragen
**Kernfrage:** „Wie schreibe ich einen 8D-Report, der fachlich trägt und beim Kunden akzeptiert wird, und was gehört in jede Disziplin?“

Unterfragen (aus Anbieter-FAQs, Schulungsbeschreibungen und Kunden-8D-Anleitungen abgeleitet):
1. Was bedeutet „8D“, und gibt es D0?
2. Woher kommt die Methode (Ford? Militär?)
3. Ist 8D Pflicht (IATF 16949, VDA), oder gibt der Kunde das Format vor?
4. Worin unterscheiden sich Sofortmaßnahme (D3) und Abstellmaßnahme (D5/D6)?
5. Warum verlangen Kunden in D4 **zwei** Ursachen (Auftreten und Nichtentdeckung)?
6. Wie weise ich nach, dass eine Ursache die richtige ist?
7. Wann darf die Sofortmaßnahme enden?
8. Was gehört in D7 (FMEA, Control Plan, Übertragung auf andere Prozesse)?
9. Welche typischen Fehler führen zur Ablehnung eines 8D?
10. Gibt es eine brauchbare deutschsprachige Vorlage?

## 2. Faktentabelle
| # | Aussage | Quelle (URL) | Datum | Belastbarkeit |
|---|---|---|---|---|
| 1 | 8D besteht aus acht Disziplinen D1–D8. Manche Organisationen stellen einen Planungsschritt **D0** voran. | ASQ: https://asq.org/quality-resources/eight-disciplines-8d ⚑ · Quality Inspection: https://qualityinspection.org/fill-out-an-8d-report-fix-problem/ | o. D. | hoch (Fachverband, übereinstimmend) |
| 2 | ASQ-Bezeichnungen (sinngemäß): D0 Planen · D1 Team · D2 Problem beschreiben · D3 vorläufige Eindämmung (Sofortmaßnahme) · D4 Grundursachen **und Escape Points** bestimmen und verifizieren · D5 Abstellmaßnahmen wählen und verifizieren · D6 umsetzen und validieren · D7 Wiederauftreten verhindern · D8 Team würdigen. | ASQ (wie #1) ⚑ · Symestic: https://www.symestic.com/de-de/was-ist/8d-report | o. D. | mittel–hoch (Suchauszug, nicht direkt geöffnet) |
| 3 | **Ursprung:** Mehrere Quellen nennen Ford als Ursprung. Belegt wird ein Ford-Handbuch „Team Oriented Problem Solving“ (TOPS) aus **1987**. | Wikipedia (EN): https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving ⚑ · All About Lean: https://www.allaboutlean.com/8d-history/ · ComplianceOnline: https://complianceonline.com/resources/8D-problem-solving-process.html | o. D. | mittel (nur Sekundärquellen, Ford-Primärdokument nicht gefunden) |
| 3a | **Gegenposition:** Wikipedia nennt die Herkunft „umstritten“. Mehrere Seiten sehen Vorläufer im US-Militärstandard **MIL-STD-1520** (Korrekturmaßnahmen). Dieser enthalte Elemente, aber nicht die 8D-Struktur. | Wikipedia (wie #3) · Elsmar: https://elsmar.com/8D/sld007.htm | o. D. | mittel |
| 4 | D0 wurde später ergänzt (Angaben schwanken: „Mitte“ bzw. „Ende der 1990er“). Ford nennt die überarbeitete Variante „Global 8D“ (G8D). | Wikipedia (wie #3) · innovation.world: https://innovation.world/8d-problem-solving/ | o. D. | **niedrig** (widersprüchlich → im Video **ohne Jahreszahl**) |
| 5 | **VDA-Band „8D – Problemlösung in 8 Disziplinen“**, Untertitel „Methode, Prozess, Bericht“, **1. Ausgabe November 2018**, im VDA-QMC-Webshop gelistet (EN-Titel „8D – Problem Solving in 8 Disciplines“). | VDA-Webshop: https://webshop.vda.de/QMC/de/8d-problem-solving-in-8-disciplines ⚑ · Kepner-Tregoe-Broschüre (zitiert „VDA: 8D – Problemlösung in 8 Disziplinen; Methode, Prozess, Bericht. Berlin 2018“): https://kepner-tregoe.com/app/uploads/2024/04/ATS-8D-Broschure-compressed.pdf | 11/2018 | mittel–hoch (zwei unabhängige Treffer; Webshop nur als Suchauszug) |
| 5a | Preis des VDA-Bands: Suchtreffer widersprechen sich (40 € bzw. 50 € zzgl. MwSt.). | wie #5 | – | **niedrig → Preis NICHT im Video nennen** |
| 6 | Laut Kepner-Tregoe legt der VDA je Disziplin überprüfbare Grundanforderungen fest. | Kepner-Tregoe (wie #5) | 2024 | mittel (Sekundär, Anbieter) |
| 7 | Separates, frei verfügbares VDA-QMC-Dokument „VDA Volume 8D V1.0“ (2017) definiert **Fehlerursachen-Kategorien** zur einheitlichen 8D-Auswertung. Es ist ein anderes Dokument als #5. | https://vda-qmc.de/wp-content/uploads/2023/01/VDA_Volume_8D__V1.0__EN__English.pdf ⚑ | 06/2017 | mittel |
| 8 | **D3 Sofortmaßnahme** schützt den Kunden, solange die Ursache offen ist, und ist keine Dauerlösung. EN: ICA (Interim Containment Action) vs. PCA (Permanent Corrective Action). Nach wirksamer Abstellmaßnahme entfällt die Sofortmaßnahme. | Symestic (wie #2) · ASQ (wie #1) | o. D. | hoch (übereinstimmend) |
| 9 | **D4 verlangt zwei Ursachen:** Warum ist der Fehler entstanden (Auftreten), und warum blieb er unentdeckt (Nichtentdeckung, „Escape Point“)? Behebt man nur das Auftreten, erreicht der nächste Fehler den Kunden ebenfalls unentdeckt. | ASQ (wie #1) · LEONI 8D Information Sheet: https://d3ga0yfowtcnef.cloudfront.net/fileadmin/group/about-us/purchasing-wsd/production-material/leoni-information-sheet-8d.pdf · All About Lean D4: https://www.allaboutlean.com/8d-d4/ | o. D. | hoch (Fachverband + Kundenanforderung eines Automobilzulieferers) |
| 10 | Ursachen müssen **verifiziert** sein. Ein anerkannter Nachweis: Den Fehler gezielt erzeugen und wieder abstellen. | Symestic (wie #2) · LEONI (wie #9) | o. D. | mittel–hoch |
| 11 | Werkzeuge in D4: 5-Why, Ishikawa, Pareto, Prozessabbildung. 5-Why getrennt für Problem- und Escape-Ursache. | QT9: https://qt9software.com/glossary/8d-report | o. D. | mittel |
| 12 | **D7:** FMEA, Control Plan (Produktionslenkungsplan) und Arbeitsanweisungen anpassen, um Wiederauftreten zu verhindern. | Symestic (wie #2) · Tacto: https://www.tacto.ai/de/einkaufer-lexikon/8d-report | o. D. | mittel–hoch |
| 13 | **IATF 16949** fordert einen definierten Problemlösungsprozess bis zur Grundursache (Abschnitt 10.2.3), schreibt aber **nicht** das 8D-Format vor. Das 8D-Format verlangen in der Praxis OEMs und Tier-1. | Certainty Software: https://www.certaintysoftware.com/?p=4252 · TÜV NORD Seminar: https://www.tuev-nord.de/de/weiterbildung/seminare/8d-report-schulung-zum-reklamationsprozess | o. D. | mittel (Sekundär; Normtext nicht zitierfähig/geschützt) |
| 14 | Kunden geben **eigene 8D-Formulare und Leitfäden** vor (z. B. BSH, Continental, Wacker Neuson). | BSH: https://media3.bsh-group.com/Documents/18957792_Anleitung_8D_Report_de.pdf · Continental ProSo Guide: https://service.supplyon.com/continental/resources/files/Continental_ProSo_Guide_8D_June2023.pdf · Wacker Neuson: https://wackerneusongroup.com/fileadmin/general/downloads-en/02_lieferanten/formulare_und_richtlinien/02_qualitaetsmanagement/qualitaetsmanagement_musterbeispiele/8d-report_sample_en_v1-1_11-2022.pdf | 2022–2023 | hoch (Primärdokumente) – **im Video keine Firmennamen nennen**, nur „viele Kunden“ |
| 15 | **Typische 8D-Fehler:** nur die „offensichtliche“ Ursache benennen, Trial-and-Error statt Hypothesen, personenbezogene statt systemischer Maßnahmen („Mitarbeiter entlassen“ nicht zielführend), 8D wird zum reinen Formular. | QZ 04/2022 „8D Reloaded“: https://res.cloudinary.com/sternwald-systems/raw/upload/v1/hugoprd/ARTIKEL_ATTACH/002EBCF3_44D172EA4CE9/d1490f9a232d68b7203a5662d3e75e0799c13f91/8D-Reloaded%20-%20QZ%2004%202022.pdf · QZ 09/2020 „A3 statt 8D?“ (Suchauszug) · VDA QMC Pressebericht 2017: https://vda-qmc.de/wp-content/uploads/2024/02/Pressebericht-2017-QZ-Gut-sortier-8D%C2%ADReport.pdf | 2017–2022 | mittel |
| 15a | Eine Quelle, die „Mitarbeiter geschult“ ausdrücklich als unzureichend bezeichnet, wurde **nicht** gefunden. | – | – | **Lücke** → im Skript als fachliche Einschätzung kennzeichnen |
| 16 | **Gasporosität** im Druckguss: runde, glatte Hohlräume durch eingeschlossene Luft, Wasserstoff, unzureichende Entlüftung, Trennmittelgase. **Schwindungsporosität:** unregelmäßige Hohlräume an dicken Querschnitten/Hotspots. | aluminium-guide.com: https://aluminium-guide.com/gas-porosity-aluminium-casting-defect/ · FDB Casting: https://www.fdbcasting.com/knowledge/aluminum-die-casting-causes-and-solutions-for-porosity-issues · Uni Leoben: https://pureadmin.unileoben.ac.at/portal/files/3145013/AC11221117n01.pdf | o. D. | mittel (teils Anbieter, Uni-Quelle stützt) |
| 17 | Vakuumunterstützter Druckguss ist ein Ansatz zur Reduzierung von Porosität. | CORDIS (EU): https://cordis.europa.eu/article/id/151594-ecofriendly-lowporosity-casting/de | o. D. | mittel |
| 18 | **Druckabfall-Dichtheitsprüfung ist stark temperaturabhängig:** Steigt die Temperatur während der Prüfung minimal, bleiben Lecks oft unerkannt. Fällt sie, entstehen „Phantom-Lecks“. | industrial-production.de: https://www.industrial-production.de/sensorik---messtechnik/alles-noch-ganz-dicht-.htm · INFICON E-Book: https://inficon.com/media/7993/download/INFICON_E-Book_Dichtheitspruefung_Automobilindustrie_vmika00de-b_1602%20%281%29.pdf?latest=1 | o. D. | mittel (Fachpresse + Prüftechnik-Anbieter, nicht neutral) |
| 19 | Für poröse Gussgehäuse haben sich laut Fachartikel Prüfgasverfahren (Helium) bewährt. | industrial-production.de (wie #18) | o. D. | niedrig–mittel (Anbieterbezug) → im Video nicht nötig |
| 20 | YouTube: Offenlegung „veränderter oder synthetischer Inhalte“ ist nötig, wenn realistisch wirkende Inhalte mit realen Personen/Orten/Ereignissen verwechselt werden könnten. Produktivitätshilfen (z. B. Skripthilfe) und offensichtlich unrealistische Grafiken fallen nicht darunter. | YouTube-Blog: https://blog.youtube/intl/de-de/news-and-events/wie-wir-creatorn-dabei-helfen-veranderte-oder-synthetische-inhalte-offenzulegen | 2024 | hoch |
| 21 | EU AI Act Art. 50 (Transparenzpflichten) gilt laut mehreren Quellen seit 02.08.2026; vom Digital Omnibus angeblich unberührt; für Art. 50 Abs. 2 (maschinenlesbare Kennzeichnung) wird teils der 02.12.2026 genannt. | Goodwin: https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force · TÜV Consulting: https://consulting.tuv.com/aktuelles/ki-im-fokus/transparenzpflichten-eu-ai-act-art-50 | 2026 | mittel (widersprüchlich bei Abs. 2; Amtsblatt nicht geprüft) – nur für Review relevant |

## 3. Wettbewerbsvideos / -inhalte
| Anbieter | Format | Winkel | Lücke |
|---|---|---|---|
| Quality Inspection, „How to complete an 8D report?“ (YouTube, 2020, ≈ 13:37 laut Docsie: https://www.docsie.io/tutorials/manufacturing/write-an-8d-report/) | Video EN | Ausfüllanleitung, Einkaufsperspektive (Asien-Sourcing) | Englisch, kein VDA-Bezug, kein durchgängiges Technikbeispiel |
| zerodefectpizza.com („What is an 8D report“) | Blog/Video EN | Praxis | Englisch |
| Lecturio, Dr. Markus Maier (8D-Vorträge) | Video DE, kostenpflichtig | Grundlagen | Bezahlschranke |
| TÜV NORD / TÜV SÜD (8D-Seminare, E-Learning) | Seminar DE | VDA-Band als Basis | teuer, keine kostenlose Vorlage |
| Asana, HubSpot, Symestic, Atlassian (Blogartikel DE) | Text | Generisch, Softwarevertrieb | Kein Automobil-/Lieferantenfall, keine Nichtentdeckungsursache am Beispiel |

*Hinweis:* Die Websuche lieferte **kein** deutschsprachiges YouTube-Video zum 8D-Report. Das ist ein Indiz, kein Beweis. **Inhaberaufgabe:** Auf YouTube „8D Report Deutsch“ manuell prüfen (5 Min.).

## 4. Content Gap & Unique Angle
1. **Ein durchgängiger technischer Fall** (Druckguss, Porosität, Dichtheitsprüfung) statt acht abstrakter Folien: Jede Disziplin baut auf der vorigen auf.
2. **Fokus auf D4 mit zwei Ursachen** (Auftreten **und** Nichtentdeckung), inklusive Nachweis „Fehler ein- und ausschalten“. Das ist der häufigste Ablehnungsgrund und in DE-Inhalten kaum am Beispiel gezeigt.
3. **Vorlage live im Video:** Jede Disziplin wird in der kostenlosen 8D-Excel-Vorlage gezeigt (Lead-Magnet p0).

## 5. Offene Punkte / Widersprüche
- **Ursprung:** Ford/TOPS 1987 ist verbreitet, aber nur sekundär belegt; Militär-Vorläufer umstritten. → Im Video: „wird meist Ford zugeschrieben … ganz unumstritten ist das nicht“.
- **D0-Jahr** widersprüchlich → keine Jahreszahl nennen.
- **Disziplin-Benennungen** variieren zwischen Quellen und Kundenformularen (z. B. D5 „Ursache korrigieren“ vs. „Maßnahmen auswählen und verifizieren“) → Hinweis „Kundenformular geht vor“.
- **Fristen** (z. B. „D3 in 24 h“) sind kundenspezifisch; keine allgemeingültige Quelle gefunden → im Video nicht als Regel nennen.
- **VDA-Band:** Existenz und Ausgabe sind über zwei Quellen belegt (⚑ vor Upload im Browser bestätigen). Er wird nur als Referenz genannt, ohne Inhalte, Abbildungen oder Formblatt-Layout.
- Lead-Magnet **p0** hat in `shop/produkte.json` den Status `in_entwicklung`. Die gezeigten Vorlagen-Ansichten müssen mit der finalen Vorlage übereinstimmen.
