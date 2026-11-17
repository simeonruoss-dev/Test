# Entscheidungslog

| Datum | Entscheidung | Begründung | Konsequenz |
|---|---|---|---|
| 17.11.2026 | **Shop: Digistore24** | Merchant of Record: stellt Endkunden-Rechnungen, führt EU-USt ab, keine Fixkosten | Kauf-Links (`checkout_url`) in `shop/produkte.json` nach Produktfreigabe eintragen |
| 17.11.2026 | **0-€-Fixkosten-Prinzip** bis zum Funktionsnachweis | Erst Zahlungsbereitschaft validieren | Nur Werkzeuge mit kostenlosem Tarif (s. u.); einzige empfohlene Ausnahme: Domain |
| 17.11.2026 | Bestehendes Gewerbe nutzen | Bereits angemeldet | Ummeldung (neuer Wohnsitz) + Tätigkeit „Verkauf digitaler Produkte/Online-Inhalte“ ergänzen |
| 17.11.2026 | **Anrede „Sie“** in allen Kundentexten (Website, Produkte, E-Mails, Videos) | B2B-Zielgruppe (Geschäftsführung, QMB in KMU) | Website umgestellt; Teams informiert |
| 17.11.2026 | **KI-Stimme statt eigener Stimme** (Piper, „Thorsten“) | Inhaber möchte nicht selbst sprechen; 0 € | Agent `sprecher`; Hinweis „Sprecherstimme KI-generiert“ in jeder Beschreibung |

## 0-€-Stack (Startphase)
| Funktion | Werkzeug | Kosten | Hinweis |
|---|---|---|---|
| Verkauf, Rechnung, USt | Digistore24 | 0 € fix, Gebühr pro Verkauf (7,9 % + 1 €) | Erzeugt Endkunden-Rechnungen; Vendor erhält Abrechnungen/Gutschriften (Format im Konto prüfen) |
| Website-Hosting | **Netlify** oder **Cloudflare Pages** (kostenloser Tarif) | 0 € | **Nicht GitHub Pages:** GitHub-Nutzungsbedingungen untersagen den Betrieb als kommerzielle Online-Geschäfts-/E-Commerce-Seite (aktuellen Wortlaut prüfen) |
| Domain | z. B. deutscher Registrar | ca. 1 €/Monat (Schätzung) | Optional; kostenlose Subdomain (`*.netlify.app`) geht, wirkt bei KMU weniger seriös |
| E-Mail-Liste / Lead-Magnet | Brevo oder MailerLite (kostenloser Tarif, EU-Anbieter) | 0 € | Limits des Gratistarifs prüfen; AV-Vertrag abschließen; Double-Opt-in |
| KI-Stimme | **Piper TTS** (Open Source, lokal) mit deutscher Stimme, z. B. „Thorsten“ | 0 € | Lizenz der jeweiligen Stimme für kommerzielle Nutzung prüfen; Qualität unter kommerziellen Anbietern |
| Folien / Schnitt | PowerPoint bzw. Canva (Free), DaVinci Resolve | 0 € | – |
| Thumbnails | Canva (Free) | 0 € | Bildlizenzen beachten |
| Buchhaltung | EÜR in Excel; Digistore24-Abrechnungen als Beleg | 0 € | Steuerberater erst bei Wachstum |

## Steuerliche Klärungspunkte (keine Steuerberatung)
- **Kleinunternehmerregelung (§ 19 UStG)** gilt für das **gesamte Unternehmen** des Inhabers: Umsätze aus dem bestehenden Gewerbe und dem neuen Geschäft werden zusammengerechnet.
- Bei Digistore24 verkauft der Inhaber an Digistore24 (inländische Leistung), nicht an Endkunden. Ob die Abrechnung mit oder ohne USt erfolgt, hängt vom Kleinunternehmer-Status ab und wird im Digistore24-Konto hinterlegt.
- Wohnsitzwechsel kann die Zuständigkeit des Finanzamts ändern; neue Tätigkeit dem Finanzamt mitteilen.
