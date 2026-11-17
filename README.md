# YouTube-Kanal-Agent (Claude)

## Executive Summary
Ein Multi-Agenten-Setup, das die **Wissensarbeit** eines YouTube-Kanals übernimmt: Strategie, Recherche, Skript, Packaging (Titel/Thumbnail/SEO) und Qualitätsprüfung. **Nicht** automatisiert: Aufnahme, Schnitt, Upload. Das ist bewusst so (siehe „Grenzen & Risiken").

Zwei Nutzungswege:
| Weg | Für wen | Aufwand |
|---|---|---|
| **A. claude.ai-Projekt** | Ohne Programmierung, im Browser/App | 5 Min. |
| **B. Claude Code** (dieses Repo) | Echte Subagenten, Dateiablage pro Video, versioniert | 15 Min. |

## Architektur
```
            /kanal-setup                 /neues-video <Thema>
                 │                               │
          kanal-stratege              ┌──────────┴───────────┐
                 │                    ▼                      │
        kanal/profil.md ──────► recherche → skript-autor → packaging → qualitaets-pruefer
        kanal/content-plan.md     01-…md      02-…md        03-…md        04-review.md (Go/No-Go)
                                                                              │
                                    /video-analyse ◄── echte YouTube-Kennzahlen
                                         │
                                  kanal/learnings.md  (Feedback-Schleife)
```

## Weg A – claude.ai-Projekt
1. claude.ai → **Projekte** → Neues Projekt.
2. Inhalt von `prompts/claude-project-systemprompt.md` als **Projektanweisungen** einfügen.
3. Websuche aktivieren. Mit `SETUP` beginnen, Ergebnis als `profil.md` ins Projektwissen hochladen.
4. Pro Video: `RECHERCHE <Thema>` → `SKRIPT` → `PACKAGING` → `REVIEW`.

## Weg B – Claude Code
```bash
git clone <dieses Repo> && cd <Repo>
claude
> /kanal-setup Ich bin MBA-Student und arbeite im Controlling
> /neues-video 3
> /video-analyse videos/2026-11-20-xyz CTR 4,1 %, Ø Wiedergabedauer 38 %, Einbruch bei 0:45
```
| Datei | Zweck |
|---|---|
| `CLAUDE.md` | Orchestrator-Regeln (Pipeline, Human-in-the-loop, Faktenpflicht) |
| `.claude/agents/*.md` | 5 Subagenten mit eigenem System-Prompt und Tool-Rechten |
| `.claude/commands/*.md` | Slash-Befehle `/kanal-setup`, `/neues-video`, `/video-analyse` |
| `kanal/profil.md` | Positionierung – Single Source of Truth |
| `videos/` | Ein Ordner pro Video |

## Mögliche Ausbaustufen
1. **Upload-Automatisierung** über die YouTube Data API v3 (OAuth 2.0). Hinweise: begrenztes Tageskontingent (Standard 10.000 Einheiten; ein Upload kostet nach meinem Kenntnisstand ca. 1.600 – aktuell prüfen); Uploads aus nicht auditierten API-Projekten werden auf „privat" gesetzt.
2. **Analytics-Anbindung** (YouTube Analytics API) für `/video-analyse` statt manueller Kennzahlen.
3. **Voice-over/Video-Generierung** (TTS, KI-Video) – rechtlich und monetarisierungsseitig sensibel (s. u.).
4. **Eigenständiger Agent** mit dem Claude Agent SDK, z. B. wöchentlich per Zeitplan Ideen + Recherche vorbereiten.

## Grenzen & Risiken (kritische Einordnung)
| Risiko | Einordnung | Gegenmaßnahme |
|---|---|---|
| **Monetarisierung** | YouTube schließt massenhaft produzierte, repetitive („inauthentic") Inhalte vom Partnerprogramm aus. Voll-automatisierte „Faceless AI"-Kanäle sind genau davon betroffen. | Agent als *Co-Pilot*, eigene Expertise/Stimme/Perspektive als Differenzierung. |
| **Halluzinationen** | LLMs erzeugen plausible, aber falsche Fakten – Reputations- und Haftungsrisiko, v. a. bei YMYL-Themen (Finanzen, Gesundheit, Recht). | Quellenpflicht, `[UNBELEGT]`-Marker, Review-Agent, **finale menschliche Prüfung**. |
| **KI-Transparenz** | YouTube verlangt Offenlegung realistisch wirkender synthetischer Inhalte; EU AI Act Art. 50 regelt Transparenzpflichten für Deepfakes (Anwendung gestaffelt – aktuellen Stand prüfen). | Offenlegungs-Checkbox im Upload, Hinweis in Beschreibung. |
| **Recht DACH** | Impressumspflicht (DDG, ggf. MStV) bei geschäftsmäßigem Kanal; Werbekennzeichnung (UWG); Urheberrecht; ggf. Nebentätigkeitsanzeige beim Arbeitgeber. | Vor Start klären; keine Rechtsberatung durch den Agenten. |
| **Strategisch** | Ein KI-Workflow ist leicht kopierbar → kein nachhaltiger Wettbewerbsvorteil (vgl. Barney, Ressourcenbasierter Ansatz/VRIO). | Vorteil muss aus Expertise, Persönlichkeit und Community entstehen, nicht aus dem Tool. |

> Plattformregeln und Kennzahlen ändern sich häufig. Alle Zahlen in diesem Dokument vor Entscheidungen mit den offiziellen YouTube-Hilfeseiten abgleichen.
