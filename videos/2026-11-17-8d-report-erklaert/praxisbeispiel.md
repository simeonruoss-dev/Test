# Praxisbeispiel 8D – „Muster GmbH: Undichter Druckgusshalter“

> Rolle: `sqe-experte` · Stand: 17.11.2026 · **Vollständig fiktiv.** Firmen, Teile, Nummern, Mengen und Termine sind erfunden und dienen nur der Veranschaulichung. Ähnlichkeiten mit realen Fällen sind nicht beabsichtigt. Im Video als „fiktives Beispiel“ einblenden.
> Fachliche Grundlagen: Quellen-# aus `01-recherche.md` in eckigen Klammern. Alles ohne Quelle ist **fachliche Praxiseinschätzung (SQE)** und als solche gekennzeichnet.

## Ausgangslage
| Feld | Inhalt (fiktiv) |
|---|---|
| Lieferant | **Muster GmbH**, Aluminium-Druckgießerei mit mechanischer Bearbeitung, Waschanlage und 100 %-Dichtheitsprüfung (Druckabfall) |
| Kunde | fiktiver Automobilhersteller (OEM), im Video nur „der Kunde“ |
| Teil | **Halter Kühlmittelpumpe**, Sachnr. MG-4711, Aluminium-Druckguss, vakuumunterstützt gegossen [17], mit integriertem Kühlmittelkanal und bearbeiteter Dichtfläche |
| Werkzeuge | 2 Druckgießwerkzeuge (W1, W2) |
| Reklamation | Kunde meldet beim End-of-Line-Dichtheitstest des Pumpenmoduls **6 undichte Module von 1.200**; Leckage an der Dichtfläche des Halters |

## D0 – Planung
- Bewertung: Kundenauswirkung + Ursache unbekannt → 8D erforderlich.
- Kundenformular/-portal und Fristen klären; Kundenformat geht vor [14]. *(Konkrete Fristen sind kundenspezifisch; keine allgemeine Regel [Recherche, offene Punkte].)*

## D1 – Team
Teamleiter: Leiter Qualität (Entscheidungsbefugnis) · Gießereimeister · Werkzeugbau/-wartung · Verantwortlicher Dichtheitsprüfung · Prozessingenieur Bearbeitung · Sponsor: Werkleiter. *(Praxis: Team mit Produkt- und Prozesswissen [2]; „Sponsor“ = SQE-Praxis.)*

## D2 – Problembeschreibung (W-Fragen + Ist / Ist nicht)
| Frage | IST | IST NICHT |
|---|---|---|
| Was? | Kühlmittelleckage an bearbeiteter Dichtfläche | Leckage an Rohgussflächen, Maßfehler |
| Wo (Herkunft)? | ausschließlich **Werkzeug W2** | Werkzeug W1 |
| Wann? | Teile gegossen **nach Werkzeugwartung W2** (Fertigungstage T-12 bis T-5) | Teile vor der Wartung |
| Wie viele? | 6 von 1.200 verbauten Modulen beim Kunden | – |
| Wie entdeckt? | Kunden-End-of-Line-Test | nicht bei Muster GmbH (eigene 100 %-Prüfung „i. O.“) |

## D3 – Sofortmaßnahmen (Containment) [8]
| Ort | Maßnahme | Verantwortlich | Ergebnis (fiktiv) |
|---|---|---|---|
| Kunde | Sperrung, 100 %-Sortierung durch Sortierdienstleister auf Kosten Muster GmbH | Qualität | 3 weitere NIO-Teile gefunden |
| Transit | Sendungen identifiziert und gesperrt | Logistik | 2 Paletten zurückgeholt |
| Lager Muster GmbH | Sperrung, erneute Dichtheitsprüfung **nach Abkühlung auf Raumtemperatur**, abgesichert mit Leck-Referenzteil | Prüffeld | 11 NIO |
| Fertigung | W2 gestoppt, Produktion auf W1 | Gießerei | – |
| Kennzeichnung | Zusatzkennzeichnung geprüfter Teile; erste saubere Lieferung („Clean Point“) dem Kunden gemeldet | Versand | – |

**Wichtiger Praxispunkt:** Bevor sortiert wird, prüft das Team mit einem bekannten Leck-Referenzteil, ob die eigene Prüfung das Leck überhaupt findet. Ergebnis: Ist das Referenzteil warm, wird es **nicht** erkannt, ist es abgekühlt, schon. Deshalb wird nur an abgekühlten Teilen sortiert. *(Fachliche Einschätzung: Eine Sortierung ist nur so gut wie die Prüfmethode; Temperatureffekt belegt durch [18].)*

## D4 – Ursachenanalyse: Auftreten **und** Nichtentdeckung [9][10][11]

### a) Auftretensursache (Warum ist der Fehler entstanden?)
Befund: Schliffbild/CT der NIO-Teile zeigt **runde, glatte Poren** unter der Dichtfläche → typisch für **Gasporosität** (eingeschlossene Luft/Gas, unzureichende Entlüftung) [16], nicht für unregelmäßige Schwindungslunker.

5-Why (Auftreten):
1. Warum undicht? → Bearbeitung hat eine Pore an der Dichtfläche angeschnitten.
2. Warum Pore? → Luft/Gas beim Gießen im Werkzeug eingeschlossen [16].
3. Warum eingeschlossen? → Entlüftungs- und Vakuumkanäle von W2 teilweise mit Trennmittelrückständen zugesetzt, das Vakuum wurde nicht vollständig erreicht.
4. Warum zugesetzt? → Bei der Wartung wurden die Kanäle nicht gereinigt.
5. Warum nicht gereinigt? → **Wartungsplan enthielt die Reinigung der Entlüftung nicht; der Vakuumwert wurde nicht überwacht (kein Alarm).** ← systemische Auftretensursache

Nachweis (Fehler ein-/ausschalten [10]): Abgüsse W2 vor Reinigung → Poren im CT; nach Reinigung der Kanäle → keine relevanten Poren; Vakuumwert-Aufzeichnung bestätigt den Unterschied.

### b) Nichtentdeckungsursache (Warum blieb der Fehler unentdeckt?)
5-Why (Nichtentdeckung):
1. Warum hat die 100 %-Prüfung das Leck nicht erkannt? → Druckabfallprüfung zeigte „i. O.“.
2. Warum „i. O.“? → Teile kamen **warm** aus der Waschanlage; die eingefüllte Prüfluft erwärmte sich während der Messzeit, der Druckanstieg überdeckte den Druckverlust durch das Leck [18].
3. Warum warm geprüft? → Keine Abkühlstrecke, keine Temperaturmessung vor der Prüfung.
4. Warum nicht vorgesehen? → **Prüfplan legte keine Teiletemperatur fest; die PFMEA bewertete die Entdeckung ohne Temperatureinfluss als sicher.** ← systemische Nichtentdeckungsursache
5. Ergänzend: Der Leckteil-Check erfolgte nur wöchentlich und mit **kaltem** Referenzteil, er konnte das Problem also nicht zeigen.

Nachweis: Leck-Referenzteil warm geprüft → „i. O.“ (nicht erkannt); abgekühlt → „n. i. O.“ (erkannt). Reproduzierbar.

> **Merksatz (fachliche Einschätzung):** Auftretensursache = Warum ist der Fehler *entstanden*? Nichtentdeckungsursache = Warum ist er *durchgerutscht*? Beide brauchen eine eigene, nachgewiesene Ursache und eigene Maßnahmen.

## D5 – Abstellmaßnahmen festlegen und verifizieren
| Ursache | Abstellmaßnahme | Verifikation |
|---|---|---|
| Auftreten | Reinigung der Entlüftungs-/Vakuumkanäle als Pflichtpunkt in jeder Wartung; Vakuumwert-Überwachung je Schuss mit Grenzwert und automatischer Ausschleusung | Versuchsserie W2: CT-Stichproben ohne relevante Poren; künstlich verschlechtertes Vakuum → Teil wird ausgeschleust |
| Nichtentdeckung | Abkühlstrecke vor der Prüfung; Temperaturmessung mit Verriegelung (Prüfung startet nur im Temperaturfenster); Leck-Referenzteil-Check zu **jedem Schichtbeginn** | Referenzteil warm und kalt → beide Male erkannt bzw. Prüfung gesperrt |

*Fachliche Einschätzung:* „Mitarbeiter geschult“ ist allein keine Abstellmaßnahme, weil sie das System nicht ändert, das den Fehler zugelassen hat. Systemische statt personenbezogener Maßnahmen: [15]; eine direkte Quelle speziell zu „Schulung“ fehlt [15a].

## D6 – Umsetzen und Wirksamkeit bestätigen
- Umsetzung abgeschlossen an T+15 (fiktiv).
- Wirksamkeit: 4 Wochen Serienbeobachtung, CT-Stichproben, Vakuum- und Temperaturdaten in Ordnung, **0 weitere Befunde beim Kunden**.
- **Erst danach** und in Abstimmung mit dem Kunden: Sortierung (D3) beendet, Zusatzkennzeichnung entfällt [8].

## D7 – Wiederauftreten verhindern [12]
- PFMEA aktualisiert (Ursache „Entlüftung zugesetzt“, Entdeckung „Prüftemperatur“ neu bewertet)
- Produktionslenkungsplan/Prüfplan: Temperaturfenster, Referenzteil-Check je Schicht
- Wartungsplan aller Druckgießwerkzeuge, Prüfanweisung Dichtheitsprüfplatz
- **Übertragung** auf alle Werkzeuge und **alle** Druckabfall-Prüfplätze im Werk, auch dort, wo noch kein Fehler aufgetreten ist (SQE-Praxis)
- Lessons Learned an Konstruktion/Planung (Abkühlstrecke bei künftigen Linien einplanen)

## D8 – Abschluss & Würdigung [2]
Kunde bestätigt den Abschluss, Bericht archiviert, Team wird gewürdigt (z. B. im Werks-Meeting).

## Häufige Anwenderfehler (für Video und Vorlage)
1. Nur eine Ursache in D4 (Nichtentdeckung fehlt) [9]
2. Ursache vermutet, nicht nachgewiesen [10][15]
3. Sofortmaßnahme als Abstellmaßnahme ausgegeben (z. B. „100 % Sortieren“ in D5) [8]
4. Sofortmaßnahme vor Wirksamkeitsnachweis beendet
5. Personenbezogene Maßnahmen („Mitarbeiter geschult/ermahnt“) statt Systemänderung [15]
6. D7 vergessen: FMEA/Control Plan nicht aktualisiert, keine Übertragung [12]
