# Website – QM-Klartext (Arbeitsmarke)

Statische Website: reines HTML, eine CSS-Datei (`assets/style.css`), ein kleines optionales Skript (`assets/site.js`). Kein Framework, kein Build-Schritt, keine externen Ressourcen (Systemschriften, keine Fonts/CDNs/Tracker). Mobil zuerst, hell/dunkel automatisch über `prefers-color-scheme`.

> **Status: nicht livefähig.** Impressum, Datenschutz, AGB und Widerrufsbelehrung sind Platzhalter (siehe `review.md`, Ampel 🔴). Alle Seiten tragen deshalb `<meta name="robots" content="noindex, nofollow">` – vor Livegang entfernen.

## Seiten
| Datei | Inhalt |
|---|---|
| `index.html` | Hero, 3 Produktkarten, Lead-Magnet-Box, geplante Videos, Über uns, FAQ |
| `produkte/8d-vorlage.html` | P0, kostenlos – Opt-in-Formular (Platzhalter) |
| `produkte/iso-9001-baukasten.html` | P1, 79 € – Kauf-Button deaktiviert |
| `produkte/lieferanten-toolkit.html` | P2, 49 € – Kauf-Button deaktiviert |
| `videos.html` | Videos 1–6 aus `kanal/content-plan.md` als „demnächst“ |
| `impressum.html`, `datenschutz.html`, `agb.html`, `widerruf.html` | Platzhalter mit TODO-Hinweis |

Produktdaten (Namen, Preise, Seitenpfade, `checkout_url`) stammen aus `shop/produkte.json` und sind beim Bau in die Seiten übernommen worden. **Bei Preisänderungen** in `produkte.json` die Preise in `index.html` und der jeweiligen Produktseite mitändern (`grep -rn "79 €" website/`).

## Häufige Änderungen

### Kauf-Button aktivieren
1. Checkout im Shop anlegen (siehe `shop/setup-checkliste.md`), URL in `shop/produkte.json` → `checkout_url` eintragen.
2. Auf der Produktseite im Button das Attribut ersetzen:
   `data-checkout-url="TODO_CHECKOUT_URL"` → `data-checkout-url="https://…"`
3. Fertig: `assets/site.js` macht daraus beim Laden einen aktiven Link „Jetzt kaufen – 49 €“ und blendet den Hinweis „Verkauf startet in Kürze“ aus.
   (Ohne JS bleibt der Button deaktiviert. Wer das vermeiden will, ersetzt den `<button>` direkt durch `<a class="btn btn-block" href="https://…">Jetzt kaufen</a>`.)

### Opt-in-Formular (Lead-Magnet) aktivieren
Formulare auf `index.html` und `produkte/8d-vorlage.html` tragen `data-optin-url="TODO_EMAIL_OPTIN_URL"`. Durch die Formular-Endpunkt-URL des E-Mail-Tools ersetzen (Double-Opt-in im Tool aktivieren, AV-Vertrag abschließen). `site.js` setzt dann `action`/`method` und aktiviert die Felder. Feldnamen (`email`, `vorname`) ggf. an das Tool anpassen. Alternativ das vom Tool erzeugte HTML-Formular einsetzen – aber **ohne** externe Skripte/Fonts des Tools.

### Marke ändern („QM-Klartext“ ist Platzhalter)
- Schnell (sichtbarer Text): Konstante `MARKE` in `assets/site.js`.
- Sauber (Titel, SEO, ohne JS): im HTML ersetzen und danach `MARKE_IM_HTML` in `site.js` angleichen:
  ```bash
  grep -rl "QM-Klartext" website | xargs sed -i 's/QM-Klartext/Neue Marke/g'
  ```
  Logo-Kürzel „QM“ steht in `.brand-mark` im Header.

### Videos veröffentlichen
In `videos.html` (und `index.html`, Abschnitt „Neueste Videos“) den Platzhalter durch einen **Link** auf YouTube ersetzen. Keine direkte Einbettung; falls doch, nur als 2-Klick-Lösung (lokales Vorschaubild, Hinweis, erst nach Klick `iframe` von `youtube-nocookie.com`).

### Preisangabe
Unter jedem Preis steht ein HTML-Kommentar mit der Kleinunternehmer-Variante (§ 19 UStG). Der Fußnotentext steht im Footer jeder Seite (`id="preis-hinweis"`).

## Lokal ansehen
```bash
cd website && python3 -m http.server 8000   # http://localhost:8000
```

## Deploy

### Option A: GitHub Pages

> ⚠️ **Für den Livegang nicht empfohlen:** Die GitHub-Nutzungsbedingungen untersagen GitHub Pages als kostenloses Hosting für ein Online-Geschäft bzw. E-Commerce (aktuellen Wortlaut prüfen). Für die Vorschau unkritisch; live → Option B (Netlify) oder Cloudflare Pages. Siehe `firma/entscheidungen.md`.
1. Repo auf GitHub (kann privat sein, Pages für private Repos erfordert je nach Plan ein kostenpflichtiges Konto – prüfen).
2. Da die Website im Unterordner liegt, per GitHub Actions veröffentlichen: *Settings → Pages → Source: GitHub Actions*, Workflow `.github/workflows/pages.yml`:
   ```yaml
   name: Pages
   on: { push: { branches: [main], paths: ["website/**"] }, workflow_dispatch: {} }
   permissions: { contents: read, pages: write, id-token: write }
   jobs:
     deploy:
       runs-on: ubuntu-latest
       environment: { name: github-pages }
       steps:
         - uses: actions/checkout@v4
         - uses: actions/upload-pages-artifact@v3
           with: { path: website }
         - uses: actions/deploy-pages@v4
   ```
3. Eigene Domain: *Settings → Pages → Custom domain* `www.deine-domain.de` eintragen (legt eine `CNAME`-Datei im Artefakt an; alternativ Datei `website/CNAME` mit dem Domainnamen anlegen). Beim Domain-Anbieter:
   - `www` → **CNAME** auf `<github-benutzer>.github.io`
   - Apex `deine-domain.de` → **A**-Records auf die GitHub-Pages-IPs (aktuelle Liste in der GitHub-Doku „Managing a custom domain for your GitHub Pages site“) oder Weiterleitung auf `www`.
   - Domain in den GitHub-Kontoeinstellungen verifizieren (Schutz vor Domain-Übernahme), dann *Enforce HTTPS* aktivieren.

### Option B: Netlify
1. Netlify-Konto → *Add new site → Import from Git* → Repo wählen.
2. Build command: leer; **Publish directory: `website`**.
3. *Domain management → Add custom domain*: `www.deine-domain.de`; DNS beim Anbieter: `www` → CNAME auf `<site-name>.netlify.app`, Apex per ALIAS/ANAME bzw. A-Record laut Netlify-Anzeige. HTTPS (Let's Encrypt) wird automatisch aktiviert.
4. Netlify Forms **nicht** nutzen, solange sie nicht in der Datenschutzerklärung beschrieben sind.

### Vor Livegang (Pflicht)
- [ ] Impressum, Datenschutz, AGB, Widerruf über Generator/Anwalt erstellen und Platzhalter ersetzen
- [ ] Hoster (GitHub/Netlify) in der Datenschutzerklärung nennen; Drittlandübermittlung (USA) prüfen
- [ ] Marke/Domain final, `domain` in `shop/produkte.json` eintragen
- [ ] `noindex`-Meta-Tag aus allen Seiten entfernen
- [ ] USt-Hinweis bei Preisen final (Regelbesteuerung vs. § 19 UStG)
- [ ] Screenshots der Vorlagen einfügen (mit Alt-Text)

## Prüfung (Stand 17.11.2026)
Playwright/Chromium, alle 9 Seiten bei 1280 px und 390 px, hell und dunkel: kein horizontales Scrollen, alle internen Links und Anker gültig, keine externen Requests, keine JS-Fehler. Aktivierungslogik des Kauf-Buttons mit Test-URL geprüft.
