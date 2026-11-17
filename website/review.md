# Review Website – QM-Klartext (Arbeitsmarke)

> Stand: 17.11.2026 · Rolle: qualitaets-pruefer · Prüfgegenstand: `website/` (9 Seiten, `assets/style.css`, `assets/site.js`) und `shop/setup-checkliste.md`
> Hinweis: Keine Rechtsberatung. Rechtliche Punkte sind Risikohinweise; verbindliche Prüfung durch Generator/Anwalt.

## Ampel: 🔴 No-Go für Livegang · 🟢 Go als interner Entwurf / Vorschau

Technisch und inhaltlich ist die Website sauber. **Livegang ist blockiert**, weil Impressum, Datenschutz, AGB und Widerrufsbelehrung bewusst Platzhalter sind (Regel: Platzhalter = 🔴 vor Livegang). Zusätzlich fehlen Marke, Domain, Shop- und E-Mail-Anbindung. Die Kauf-Buttons sind korrekt deaktiviert, es kann also nichts versehentlich verkauft werden.

## Befunde

| # | Stelle | Problem | Schwere | Konkreter Fix |
|---|---|---|---|---|
| 1 | `impressum.html` | Platzhalter, keine Anbieterkennzeichnung (§ 5 DDG) | 🔴 Blocker | Mit Generator (z. B. eRecht24) oder Anwalt erstellen, Platzhalter ersetzen |
| 2 | `datenschutz.html` | Platzhalter; Hoster, E-Mail-Tool, Shop noch nicht festgelegt | 🔴 Blocker | Nach Wahl von Hoster/E-Mail-Tool/Shop per Generator erstellen; Drittlandübermittlung (GitHub/Netlify = USA) behandeln |
| 3 | `agb.html`, `widerruf.html` | Platzhalter; Vertragspartner (MoR oder Inhaber) offen | 🔴 Blocker | Shop-Entscheidung treffen (`shop/setup-checkliste.md`), dann AGB/Lizenz und Widerruf erstellen bzw. auf MoR-Bedingungen verweisen |
| 4 | Checkout (noch nicht vorhanden) | Erlöschen des Widerrufsrechts nach § 356 Abs. 5 BGB erst mit Zustimmung + Bestätigung + Vertragsbestätigung | 🔴 vor erstem Verkauf | Beim Testkauf prüfen (Checkliste Abschnitt 5, Schritt 6/11) |
| 5 | Preise (alle Seiten) | USt-Hinweis „inkl. MwSt.“ ist Platzhalter, Steuerstatus offen (PAngV) | 🟡 | Nach Entscheidung Regelbesteuerung/§ 19 UStG Fußnote finalisieren; Kleinunternehmer-Variante steht als Kommentar am Preis |
| 6 | Opt-in-Formulare | Nicht funktionsfähig (bewusst, kein Dienst angebunden); Einwilligungstext vorläufig | 🟡 | E-Mail-Tool mit AVV + EU-Server wählen, `data-optin-url` setzen, Einwilligungstext mit Datenschutzerklärung abstimmen; Kopplung Download ↔ Newsletter rechtlich prüfen lassen |
| 7 | Marke „QM-Klartext“ | Arbeitstitel, Marken-/Domainprüfung fehlt; weicht von Kanalnamen-Kandidaten in `kanal/profil.md` ab | 🟡 | DPMA/EUIPO + Handle prüfen; dann per README-Befehl ersetzen |
| 8 | Lizenzhinweis Produktseiten | „Geplante Lizenz“ noch nicht final | 🟡 | Lizenz festlegen, in AGB/Produktdatei aufnehmen |
| 9 | Produktseiten | Screenshot-Platzhalter, „Über uns“ mit TODO für Inhaber-Hintergrund | 🟡 | Screenshots aus fertigen Vorlagen (mit Alt-Text); 2–3 Sätze ohne Arbeitgeberbezug |
| 10 | Produktinhalte | Blattlisten entsprechen den verbindlichen Vorgaben; Produkte sind noch „in Entwicklung“ | 🟡 | Nach Fertigstellung mit `produkte/<id>/dist/` abgleichen (Blattnamen, ppm-Logik P2) |
| 11 | P1 ISO 9001 | Hinweise vorhanden: Kap. 4–10, Basis 2015, Abgleich 2026 in Arbeit, keine Zertifizierungsgarantie, keine Normtexte, Norm bei DIN Media | 🟢 | – |
| 12 | Externe Ressourcen | Keine (Playwright: 0 externe Requests); YouTube nur als Link vorgesehen | 🟢 | – |
| 13 | UWG | Keine Testimonials, Kundenzahlen, Verknappung oder Rabatt-Countdowns; eigene Produkte klar als solche erkennbar | 🟢 | – |
| 14 | Indexierung | `noindex, nofollow` auf allen Seiten | 🟢 (gewollt) | Vor Livegang entfernen |
| 15 | `shop/setup-checkliste.md` | Gebühren teils nur aus Drittquellen, offizielle Seiten nicht abrufbar; korrekt als „prüfen“ markiert | 🟡 | Vor Vertragsabschluss Preisseiten direkt prüfen und Werte nachtragen |

## Technische Prüfung (Playwright/Chromium)
| Prüfung | Ergebnis |
|---|---|
| 9 Seiten × 1280 px / 390 px × hell / dunkel (36 Screenshots) | 🟢 visuell geprüft |
| Horizontales Scrollen | 🟢 keines |
| Interne Links und Anker | 🟢 alle gültig |
| JS-Fehler | 🟢 keine |
| Kauf-Button-Aktivierung (Test mit Beispiel-URL) | 🟢 Button wird zu Link, Hinweis ausgeblendet |
| Barrierearmut | 🟢 semantisches HTML, Skip-Link, Labels, Fokusrahmen, Mindest-Klickfläche 44 px; 🟡 Kontraste nicht maschinell gemessen |

## Rubrik (1–5)
| Kriterium | Score | Begründung |
|---|---|---|
| Nutzenversprechen / Klarheit | 4 | Zielgruppe KMU/SQE klar, Problem → Lösung je Produkt; ohne Screenshots noch abstrakt |
| Ehrlichkeit / Compliance | 5 | Status „in Entwicklung“, keine Garantie-, Zahlen- oder Verknappungsaussagen |
| Struktur / Navigation | 4 | Logisch; mobile Navigation umbricht auf drei Zeilen (akzeptabel) |
| Technik / Performance | 5 | Kein Framework, keine externen Requests, eine CSS-Datei |
| Livegang-Reife | 1 | Rechtstexte, Shop, E-Mail-Tool, Marke offen |

## Nächste Schritte (Inhaber)
1. Shop-Anbieter freigeben (Empfehlung Digistore24) → Checkout-URLs.
2. E-Mail-Tool wählen (AVV, EU-Server) → Opt-in-URL.
3. Rechtstexte per Generator/Anwalt, Marke/Domain prüfen.
4. Danach erneute Prüfung durch `qualitaets-pruefer` → Ziel 🟢.
