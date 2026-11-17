# Linkblock – Video #1 „8D-Report erklärt“

> Rolle: `vertrieb-marketing` · Stand: 17.11.2026 · Quelle aller Links: `shop/produkte.json` (nicht geändert)
> Video-Slug für UTM: `8d-report-erklaert`
> URL-Schema: `domain` + `produkt_seite` + `?utm_source=youtube&utm_medium=video&utm_campaign=8d-report-erklaert`

## Linkblock (kopierfertig für die YouTube-Beschreibung, direkt nach den ersten 2 Zeilen)

```
📥 Kostenlose 8D-Report-Vorlage (Excel) aus dem Video – Eigenes Produkt, kostenlos (E-Mail-Anmeldung):
https://www.DEINE-DOMAIN.de/produkte/8d-vorlage.html?utm_source=youtube&utm_medium=video&utm_campaign=8d-report-erklaert

🧰 Lieferantenmanagement-Toolkit (Excel) für Einkauf & QM – Eigenes Produkt, kostenpflichtig:
https://www.DEINE-DOMAIN.de/produkte/lieferanten-toolkit.html?utm_source=youtube&utm_medium=video&utm_campaign=8d-report-erklaert

📘 Optional – ISO 9001 Baukasten für KMU (Excel) – Eigenes Produkt, kostenpflichtig:
https://www.DEINE-DOMAIN.de/produkte/iso-9001-baukasten.html?utm_source=youtube&utm_medium=video&utm_campaign=8d-report-erklaert
```

## Begründung der Auswahl
| Position | Produkt (id) | Warum |
|---|---|---|
| 1 | `p0-8d-vorlage` (Lead-Magnet) | Wird im Video Schritt für Schritt gezeigt und ist der einzige CTA im Sprechtext. Ziel: E-Mail-Liste (wichtigster KPI Phase 1). |
| 2 | `p2-lieferanten-toolkit` | Zielgruppe deckt sich (SQE, Einkauf/QM): Wer 8Ds von Lieferanten bewertet, braucht Lieferantenbewertung und Eskalation. |
| 3 (optional) | `p1-iso9001-baukasten` | Schwächerer Bezug (ISO 9001 fordert Korrekturmaßnahmen, Kap. 10.2), passt zur KMU-Käufergruppe. **Empfehlung: zunächst weglassen**, um die Beschreibung fokussiert zu halten. Erst aufnehmen, wenn die Produktseite live ist. |

## Regeln & Hinweise
- **Kennzeichnung:** Alle drei sind eigene Produkte und als „Eigenes Produkt“ benannt. Keine Drittwerbung, kein Affiliate. Keine Preise in der Beschreibung (Preise sind Hypothesen; werden auf der Produktseite inkl. USt-Hinweis nach PAngV angegeben).
- **Verlinkt wird immer die Produktseite**, nie `checkout_url` (bleibt bei Shopwechsel gültig).
- **Keine** Verknappung, keine Kundenzahlen, keine Testimonials (UWG).

## Blocker vor Upload (Inhaber)
1. `domain` in `shop/produkte.json` ist der Platzhalter `https://www.DEINE-DOMAIN.de` → echte Domain eintragen; Linkblock dann per Suchen/Ersetzen aktualisieren.
2. Produktseite `/produkte/8d-vorlage.html` muss live sein, mit funktionierendem Double-Opt-in (`checkout_url` von p0 ist noch `TODO_EMAIL_OPTIN_URL`).
3. p1/p2 haben den Status `in_entwicklung`. Ist die jeweilige Produktseite beim Upload nicht live, Zeile weglassen oder als „Warteliste“ formulieren. **Keine toten Links.**
4. Nach dem Upload alle Links einmal anklicken; UTM-Parameter in der Web-Analyse prüfen (falls eingesetzt, nur mit Einwilligung/Consent).

## KPI-Tracking für dieses Video
Aufrufe → Klicks auf Link 1 (UTM `8d-report-erklaert`) → Opt-ins → Klicks Link 2 → Käufe. Auswertung über `/video-analyse` nach 28 Tagen.
