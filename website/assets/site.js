/* QM-Klartext – minimales Vanilla-JS (optional; alle Seiten funktionieren auch ohne JS).
 *
 * 1) MARKE: Arbeitsmarke an EINER Stelle änderbar. Alle Elemente mit [data-marke]
 *    und der Seitentitel werden beim Laden ersetzt. Für SEO/No-JS zusätzlich im HTML
 *    ersetzen (siehe website/README.md, Abschnitt „Marke ändern“).
 *
 * 2) Kauf-Buttons: Jeder Button trägt data-checkout-url (Wert aus shop/produkte.json).
 *    Solange der Wert mit „TODO“ beginnt, bleibt der Button deaktiviert („Bald verfügbar“).
 *    Sobald dort eine echte https-URL steht, wird er automatisch zum aktiven Kauf-Link.
 *
 * 3) Opt-in-Formular: dasselbe Prinzip über data-optin-url (kein externer Dienst eingebunden).
 */
(function () {
  "use strict";

  var MARKE = "QM-Klartext"; // <- Arbeitsmarke (Platzhalter) hier ändern
  var MARKE_IM_HTML = "QM-Klartext"; // Wert, der aktuell im HTML steht

  if (MARKE !== MARKE_IM_HTML) {
    document.querySelectorAll("[data-marke]").forEach(function (el) { el.textContent = MARKE; });
    document.title = document.title.split(MARKE_IM_HTML).join(MARKE);
  }

  function istEchteUrl(url) {
    return typeof url === "string" && /^https:\/\//i.test(url) && url.indexOf("TODO") === -1;
  }

  // Kauf-Buttons aktivieren, sobald eine echte checkout_url eingetragen ist
  document.querySelectorAll("[data-checkout-url]").forEach(function (btn) {
    var url = btn.getAttribute("data-checkout-url");
    if (!istEchteUrl(url)) return;
    var a = document.createElement("a");
    a.className = btn.className;
    a.href = url;
    a.rel = "noopener";
    a.textContent = btn.getAttribute("data-label-aktiv") || "Jetzt kaufen";
    btn.replaceWith(a);
    var hint = document.getElementById(btn.getAttribute("aria-describedby"));
    if (hint && hint.hasAttribute("data-nur-wenn-inaktiv")) hint.hidden = true;
  });

  // Opt-in-Formular aktivieren, sobald eine echte Opt-in-URL eingetragen ist
  document.querySelectorAll("form[data-optin-url]").forEach(function (form) {
    var url = form.getAttribute("data-optin-url");
    if (!istEchteUrl(url)) {
      form.addEventListener("submit", function (e) { e.preventDefault(); });
      return;
    }
    form.action = url;
    form.method = "post";
    form.querySelectorAll("[disabled]").forEach(function (el) { el.disabled = false; });
    var btn = form.querySelector("button[type=submit]");
    if (btn && btn.getAttribute("data-label-aktiv")) btn.textContent = btn.getAttribute("data-label-aktiv");
    var hint = form.querySelector("[data-nur-wenn-inaktiv]");
    if (hint) hint.hidden = true;
  });
})();
