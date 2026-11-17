# Organigramm – „QM-Klartext“ (Arbeitstitel)

**Geschäftsmodell:** Kostenlose YouTube-Videoanleitungen (Lieferantenqualität & QM für KMU) → kostenloser Lead-Magnet → Verkauf digitaler Excel-Vorlagen über die eigene Website.

```
                         Inhaber (Freigaben, Stimme, Upload, Verträge)
                                          │
                              Geschäftsführer = Orchestrator (CLAUDE.md)
        ┌───────────────┬───────────────┼────────────────┬──────────────────┐
   STRATEGIE        FACHBEREICH       PRODUKT            MEDIEN            VERTRIEB & WEB
 kanal-stratege    sqe-experte     produkt-entwickler  recherche         vertrieb-marketing
                                                       skript-autor      web-entwickler
                                                       packaging
                                    └──────────── qualitaets-pruefer (Fakten, Recht, Go/No-Go) ─┘
```

| Agent | Sinn / Verantwortung | Liefert | Befehl |
|---|---|---|---|
| Geschäftsführer (Hauptsitzung) | Priorisiert, delegiert, holt Freigaben ein | Wochenplan, Status | `/wochenplan` |
| `kanal-stratege` | Positionierung, Content-Plan | `kanal/*.md` | `/kanal-setup` |
| `sqe-experte` | Fachliche Instanz: Inhalte korrekt, praxisnah, normkonform (ohne Normtext zu kopieren) | Fachspezifikationen, Praxisbeispiele, Fachfreigabe | – |
| `produkt-entwickler` | Baut verkaufsfähige Excel-Vorlagen inkl. Anleitung | `produkte/<id>/` | `/neues-produkt` |
| `recherche`, `skript-autor`, `packaging` | Videoproduktion; Packaging setzt Produktlinks | `videos/<slug>/` | `/neues-video` |
| `vertrieb-marketing` | Produkttexte, Preise, Linkblöcke, E-Mail-Sequenz, Shop-Anbindung | `shop/`, Texte | – |
| `sprecher` | KI-Voice-over (Piper, Stimme „Thorsten“, CC0) inkl. Aussprache-Lexikon | `videos/<slug>/voiceover/` | – |
| `folien-designer` | Folieninhalte & Layout je Satz | `schnittplan.json` | – |
| `ton-meister` | Stimme, Aussprache, Abmischung, −14 LUFS | `ton-bericht.md` | – |
| `video-produzent` | Automatischer Schnitt → fertiges MP4, Untertitel, Thumbnail | `export/` | – |
| `video-pruefer` | Endabnahme, Längencheck, Korrekturschleife | `abnahme.md` | – |
| `web-entwickler` | Statische Website (Start, Produkte, Videos, Rechtliches) | `website/` | `/website-update` |
| `qualitaets-pruefer` | Faktencheck, Recht (UrhG, UWG, Widerruf, Impressum), Go/No-Go | `*review.md` | – |

## Wertschöpfungskette
1. Content-Plan wählt Thema **mit Produktbezug**
2. `sqe-experte` spezifiziert → `produkt-entwickler` baut Vorlage → `qualitaets-pruefer`
3. Video-Pipeline erklärt die Methode, zeigt die Vorlage → `packaging` setzt Links aus `shop/produkte.json`
4. `web-entwickler` + `vertrieb-marketing` veröffentlichen Produktseite
5. Inhaber: Voice-over, Schnitt, Upload, Checkout-Link im Shop anlegen
6. `/video-analyse` → Learnings → nächster Zyklus

## Was die Agenten NICHT können (Inhaberaufgaben)
- Shop-, Domain-, Hosting-, YouTube-Konten anlegen; Zahlungen; Verträge
- Fertiges Video ansehen und freigeben, Upload (API-Automatisierung als spätere Ausbaustufe möglich)
- Rechtsverbindliche Prüfung (Impressum/AGB/Datenschutz → Generator wie eRecht24 oder Anwalt)
