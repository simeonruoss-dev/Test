# Shop-Setup-Checkliste – von null bis zur ersten Checkout-URL

> Stand: 17.11.2026 · Rolle: vertrieb-marketing · Status: **Entwurf, Freigabe Inhaber ausstehend**
> Hinweis: Keine Rechts- oder Steuerberatung. Gebühren ändern sich; alle Werte vor Vertragsabschluss auf der offiziellen Preisseite prüfen.
> Recherche-Einschränkung: Die offiziellen Preisseiten (digistore24.com, lemonsqueezy.com, gumroad.com) waren aus dieser Arbeitsumgebung nicht direkt abrufbar. Gebühren stammen aus Suchergebnissen (Quellen unten) und sind als **„prüfen“** markiert, wo nur Drittquellen vorlagen.

## 1. Ausgangslage
- 3 Produkte (`shop/produkte.json`): P0 8D-Vorlage (0 €, Lead-Magnet, kein Shop nötig – läuft über E-Mail-Tool), P1 ISO 9001 Baukasten (79 €, Hypothese), P2 Lieferanten-Toolkit (49 €, Hypothese).
- Zielgruppe DACH, überwiegend B2B (KMU), aber auch Privatpersonen (z. B. Studierende) → Verbraucherrecht muss erfüllt sein.
- Inhaber: 2 h/Woche, nebenberuflich → möglichst wenig Steuer-, Rechnungs- und Supportaufwand.
- Entscheidendes Kriterium: **Merchant of Record (MoR)/Reseller** – der Anbieter ist rechtlich Verkäufer, stellt Rechnung, schuldet und führt die EU-Umsatzsteuer ab (digitale Leistungen an Verbraucher: USt des Kundenlands). Der Inhaber verkauft nur noch an den Anbieter (eine Gutschrift/Abrechnung pro Periode).

## 2. Anbietervergleich

| Kriterium | Digistore24 | ablefy (ehem. elopage) | Gumroad | Lemon Squeezy |
|---|---|---|---|---|
| Sitz / Sprache | DE, deutschsprachig | DE, deutschsprachig | USA, Englisch | USA, Englisch |
| MoR / EU-USt | **Ja** – Reseller-Modell ist Standard [1][2] | **Optional**: Reseller-Modell gegen Aufpreis; sonst verkauft der Inhaber selbst (eigene USt-Pflichten) [6][7] | Laut Drittquellen seit 2025 MoR; Angaben widersprüchlich → **prüfen** [4][5] | **Ja**, laut eigener Preisseite (per Suchergebnis) [3] |
| Grundgebühr | Keine [1] | Ja, laut Drittquellen ab ca. 27–39 €/Monat, kein Gratistarif → **prüfen** [6][7] | Keine (laut Drittquellen) → **prüfen** [4] | Keine (laut Drittquellen) → **prüfen** [3] |
| Transaktionsgebühr | **7,9 % + 1 €** je Verkauf (Hilfe-Center/Gebührenrechner) [1][2]; bei Chargeback-Quote > 1 %: 9,9 % + 1 € [2] | 2,7 % + 0,50 € plus Reseller-Aufschlag 2,5 % + 1 € (Drittquellen, abweichende Werte) → **prüfen** [6][7] | 10 % + 0,50 $, ggf. zzgl. Zahlungsabwicklung (Drittquellen widersprüchlich) → **prüfen** [4][5] | 5 % + 0,50 $ (Preisseite per Suchergebnis); Zuschläge z. B. für internationale Karten/PayPal laut Drittquellen → **prüfen** [3] |
| Beispiel 49 € brutto | ≈ 4,87 € Gebühr (7,9 % × 49 € + 1 €), Berechnungsbasis brutto/netto **prüfen** (Gebührenrechner [2]) | **prüfen** | **prüfen** | **prüfen** |
| Auszahlung | Laut Drittquelle bis zu 4×/Monat, SEPA gebührenfrei → **prüfen** [8] | **prüfen** | **prüfen** (USD-Konto/Umrechnung beachten) | **prüfen** (USD/Umrechnung beachten) |
| Checkout DE / Zahlarten DACH | Deutsch, u. a. PayPal, Karte, SEPA, Rechnung (Zahlarten im Konto **prüfen**) | Deutsch, breite DACH-Zahlarten inkl. Klarna [9] | Englischlastig | Englischlastig, Lokalisierung **prüfen** |
| Widerruf digitale Inhalte (§ 356 Abs. 5 BGB) | Checkbox/Bestätigung im Checkout vorhanden – konkret **prüfen** | Konfigurierbar – **prüfen** | **prüfen** (US-Anbieter, DE-Verbraucherrecht nicht Standard) | **prüfen** |
| Affiliate-Programm | Ja, großer Marktplatz | Ja | Ja | Ja |
| Ruf / Risiko | Marktplatz mit vielen „Make-Money“-Angeboten → Image für B2B-QM-Produkte beachten | Seriöser B2B-Auftritt, aber Fixkosten | Einfach, aber US-Fokus | Laut Drittquelle 2024 von Stripe übernommen; Produktzukunft **prüfen** [3] |
| **DACH-Eignung (Einschätzung)** | **Hoch** | **Hoch** (ab höherem Umsatz) | Mittel | Mittel |

### Kurzbewertung
- **Digistore24:** + MoR ohne Fixkosten, deutsch, Rechnung inkl. USt durch Digistore24, DACH-Zahlarten. – Höchste prozentuale Gebühr bei kleinen Preisen (der 1-€-Fixanteil fällt bei 49 € stark ins Gewicht); Marktplatz-Image.
- **ablefy:** + professioneller Auftritt, deutsches Recht, viele Zahlarten, Reseller-Modell möglich. – Monatliche Grundgebühr lohnt erst bei regelmäßigem Umsatz (Break-even gegenüber Digistore24 laut Drittquelle grob im Bereich ab ca. 1.500 €/Monat [7] – **prüfen**).
- **Gumroad:** + sehr schnell eingerichtet. – Hohe Gebühr, USD/Englisch, MoR-Status für EU unklar.
- **Lemon Squeezy:** + MoR, niedrige Basisgebühr. – Englisch, Zuschläge, Zukunft nach Übernahme unklar, DE-Verbraucherrecht (Widerruf-Checkbox) zu prüfen.

## 3. Empfehlung
**Start mit Digistore24** (Reseller/MoR, keine Fixkosten). Begründung: In Phase 2 ist die Zahl der Verkäufe unbekannt; ohne Grundgebühr gibt es kein Kostenrisiko, und die EU-Umsatzsteuer sowie die Rechnungsstellung an Endkunden liegen beim Anbieter. Das passt zu 2 h/Woche.
**Wechsel-Trigger:** Ab nachhaltig ca. 1.500 €/Monat Umsatz oder wenn das Marktplatz-Image bei B2B-Kunden stört → ablefy (Reseller-Modell) erneut durchrechnen. Ein Wechsel ist unkritisch, weil Videos und Website nur auf die eigene Produktseite verlinken (`produkt_seite`), nie direkt auf den Checkout.
**Freigabe durch Inhaber erforderlich.**

## 4. Schritt für Schritt bis zur ersten Checkout-URL (Digistore24)
Voraussetzungen (Inhaber):
- [ ] Nebentätigkeit beim Arbeitgeber angezeigt/genehmigt (siehe `kanal/profil.md`, Kap. 9)
- [ ] Gewerbe angemeldet; Steuerberater/Finanzamt: Regelbesteuerung oder Kleinunternehmer (§ 19 UStG) – beeinflusst die Abrechnung mit dem Reseller und den Preis-Hinweis auf der Website
- [ ] Geschäftskonto (IBAN) für Auszahlungen
- [ ] Produktdateien final und geprüft (`produkte/<id>/dist/`, `review.md` = Go)
- [ ] Impressum, Datenschutz, AGB/Lizenz, Widerrufsbelehrung über Generator/Anwalt (Website-Platzhalter ersetzen)

Einrichtung:
1. [ ] Konto als **Vendor** bei Digistore24 anlegen; Identitäts- und Steuerangaben (USt-Status) hinterlegen.
2. [ ] Auszahlungsdaten (SEPA) und Auszahlungsrhythmus einstellen; aktuelle Konditionen und Sicherheitseinbehalt im Konto nachlesen und hier notieren.
3. [ ] Neues Produkt anlegen: Typ „Digitales Produkt/Download“, Name aus `shop/produkte.json`, Sprache Deutsch.
4. [ ] Preis als **Bruttopreis** (79 € bzw. 49 €) eintragen; Steuerbehandlung prüfen (Digistore24 berechnet die USt je Käuferland).
5. [ ] Lieferung: Datei hochladen oder Download-Seite hinterlegen; Thank-you-Seite (optional eigene Seite auf der Website, ohne Tracker).
6. [ ] **Widerruf digitale Inhalte:** Im Checkout die Einwilligung zur sofortigen Ausführung + Bestätigung der Kenntnis vom Erlöschen des Widerrufsrechts aktivieren (siehe Abschnitt 5). Testkauf: Checkbox sichtbar? Bestätigungsmail enthält die Erklärung?
7. [ ] Produktbeschreibung/Bild (Verkaufstext aus `produkte/<id>/verkaufstext.md`), Lizenzhinweis, „keine Zertifizierungsgarantie“ (P1).
8. [ ] Rechtstexte verknüpfen: Impressum- und Datenschutz-URL der eigenen Domain im Produkt/Konto hinterlegen.
9. [ ] Affiliate-Programm vorerst **aus** (Kontrolle über Werbeaussagen, UWG).
10. [ ] Produkt zur Freigabe einreichen (Digistore24 prüft Produkte) und Freigabe abwarten.
11. [ ] **Testkauf** (Testmodus bzw. echter Kauf mit anschließender Erstattung): Rechnung mit USt? Download funktioniert? E-Mails auf Deutsch?
12. [ ] Bestellformular-URL kopieren → `shop/produkte.json` → `checkout_url` (ersetzt `TODO_CHECKOUT_URL`).
13. [ ] Website: auf der Produktseite `data-checkout-url` ersetzen (siehe `website/README.md`) → Button wird aktiv.
14. [ ] `qualitaets-pruefer`: Abschlussprüfung Website + Checkout (Go/No-Go).

## 5. Widerrufsrecht bei digitalen Inhalten (§ 356 Abs. 5 BGB)
Verbraucher haben grundsätzlich 14 Tage Widerrufsrecht. Bei nicht auf einem körperlichen Datenträger gelieferten digitalen Inhalten **erlischt** es vorzeitig, wenn der Unternehmer mit der Vertragserfüllung begonnen hat, nachdem der Verbraucher
1. **ausdrücklich zugestimmt** hat, dass vor Ablauf der Widerrufsfrist mit der Ausführung begonnen wird,
2. seine **Kenntnis bestätigt** hat, dass er dadurch sein Widerrufsrecht verliert, und
3. der Unternehmer ihm eine **Bestätigung** des Vertrags (auf dauerhaftem Datenträger, z. B. E-Mail) zur Verfügung gestellt hat, die diese Zustimmung/Kenntnisnahme enthält (§ 312f Abs. 3 BGB).

Umsetzung:
- [ ] Nicht vorangekreuzte Checkbox im Checkout (Formulierung vom Shop-Anbieter bzw. Generator/Anwalt übernehmen, nicht selbst erfinden)
- [ ] Bestätigungsmail enthält die Erklärung
- [ ] Widerrufsbelehrung + Muster-Widerrufsformular verfügbar; bei MoR gilt die Belehrung des Anbieters – auf `website/widerruf.html` darauf verweisen
- [ ] Ohne diese Schritte: Kunde kann binnen 14 Tagen widerrufen, auch nach Download

## 6. Rechnungsstellung
- **Mit MoR (Digistore24, ablefy-Reseller, Lemon Squeezy):** Endkundenrechnung inkl. korrekter USt stellt der Anbieter. Der Inhaber erhält Gutschriften/Abrechnungen des Anbieters → an Steuerberater/Buchhaltung.
- **Ohne MoR (ablefy-Verkäufermodell):** Inhaber ist Verkäufer, muss EU-USt für Verbraucher im EU-Ausland beachten (OSS-Verfahren, Schwellenwert 10.000 €/Jahr EU-weit), B2B-Reverse-Charge prüfen → für den Start nicht empfohlen.
- B2B-Käufer (KMU) brauchen Rechnungen mit ausgewiesener USt und ggf. eigener Firmenadresse/USt-IdNr. → im Checkout „Firmenkauf“-Option prüfen.

## 7. E-Mail-Tool (Lead-Magnet, DSGVO-konform)
Anforderungen:
- [ ] **Auftragsverarbeitungsvertrag (AVV, Art. 28 DSGVO)** im Konto abschließbar
- [ ] **Serverstandort EU** (bevorzugt DE), Anbieter mit Sitz in der EU – vermeidet Drittlandübermittlung
- [ ] **Double-Opt-in** mit Protokollierung (Zeitpunkt, IP, Einwilligungstext)
- [ ] Abmeldelink in jeder Mail, Impressum in jeder Mail
- [ ] Formular-Einbindung ohne externe Skripte/Fonts (reines HTML-POST-Formular) – passt zur Website (`data-optin-url`)
- [ ] Automatisierung (Lead-Magnet-Auslieferung + 5-Mail-Sequenz `shop/email-sequenz.md`)
- [ ] Kostenloser bzw. günstiger Einstiegstarif bis ca. 300 Kontakte (Ziel `kanal/profil.md`)

Kandidaten (Angaben zu Sitz/Serverstandort/Preisen vor Entscheidung auf der jeweiligen Website **prüfen**):
| Tool | Sitz (laut Anbieter) | AVV | Hinweis |
|---|---|---|---|
| CleverReach | DE | **prüfen** | Deutscher Anbieter |
| rapidmail | DE | **prüfen** | Deutscher Anbieter |
| Brevo (ehem. Sendinblue) | FR | **prüfen** | EU-Anbieter, Automationen |
| MailerLite | LT (EU) | **prüfen** | US-Unterauftragsverarbeiter prüfen |
| Mailchimp / ConvertKit (Kit) | USA | – | Drittlandübermittlung (DPF) → für den Start nicht empfohlen |

**Empfehlung:** Ein Anbieter mit Sitz und Servern in DE/EU und Automationen im Einstiegstarif; Entscheidung nach Preisvergleich durch Inhaber. Im E-Mail-Tool die Lead-Magnet-Datei per Bestätigungs-/Willkommensmail ausliefern; Formular-URL dann in `shop/produkte.json` (P0 `checkout_url`) und `website/` (`data-optin-url`) eintragen.

## 8. KPIs nach Start
Besucher Produktseite → Opt-in-Rate → Käufer-Conversion → Umsatz pro Video (UTM `utm_campaign=<video-slug>`; Digistore24-Statistik bzw. serverseitige Hoster-Statistik ohne Cookies).

## Quellen
1. Digistore24 Hilfe-Center (Gebühren): https://help.digistore24.com/hc/en-us/articles/23694504392721 · Preisseite: https://www.digistore24.com/pricing/ (nicht direkt abrufbar, nur Suchergebnis)
2. Digistore24 Gebührenrechner: https://www.digistore24.com/extern/calculator/iframe/de · Hilfe-Center Chargebacks: https://help.digistore24.com/hc/en-us/articles/29007028838033
3. Lemon Squeezy Preisseite (per Suchergebnis): https://lemonsqueezy.com/pricing · Drittquellen: https://fungies.io/alternatives/lemon-squeezy, https://dodopayments.com/blogs/lemonsqueezy-review
4. Gumroad-Gebühren (Drittquellen): https://dodopayments.com/blogs/gumroad-fees-explained, https://schoolmaker.com/blog/gumroad-pricing.md
5. Gumroad MoR/VAT (widersprüchlich): https://getly.store/blog/gumroad-fees-2026, https://fungies.io/gumroad-vs-paddle
6. ablefy Preise: https://ablefy.io/en/preise-2/ · Vergleich: https://www.fastlancer.org/fastlancer-blog/digitale-produkte-verkaufen/
7. ablefy vs. Digistore24 (Break-even): https://quasa.io/de/media/ablefy-oder-digistore24-ab-1500-euro-umsatz-kann-die-grundgebuehr-kippen
8. Digistore24 Auszahlung (Drittquelle): https://ecom-tools.de/digistore24/
9. ablefy Klarna: https://ablefy.io/en/klarna/
