---
description: Neues digitales Produkt entwickeln (Spezifikation → Bau → Verkaufstext → Review → Produktseite)
argument-hint: <Produkt-ID aus shop/produkte.json oder neue Produktidee>
---
Produkt: $ARGUMENTS
1. Falls neu: Eintrag in `shop/produkte.json` anlegen (Preis als Hypothese) und Freigabe holen.
2. `sqe-experte` → `produkte/<id>/spezifikation.md`
3. `produkt-entwickler` → `build.py`, `dist/*.xlsx`, `Anleitung.md`, `testbericht.md`
4. `sqe-experte` → Fachfreigabe; `vertrieb-marketing` → `verkaufstext.md`
5. `qualitaets-pruefer` → `review.md` (Go/No-Go)
6. `web-entwickler` → Produktseite aktualisieren
