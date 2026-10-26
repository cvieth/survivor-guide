# Survivor Guide

**Das offene Handbuch für Krisenbewältigung, Überleben und Wiederaufbau.**

> **Version 0.1: Grundgerüst.** Die meisten Kapitel sind noch Themenpläne, keine fachlich geprüften Anleitungen.

## Lesen
- [Online-Handbuch](https://cvieth.github.io/survivor-guide/)
- [Aktuelles veröffentlichtes PDF (A4)](https://github.com/cvieth/survivor-guide/releases/latest/download/survivor-guide.pdf)
- [Druckvorlage (6 × 9 Zoll, Entwurf)](https://github.com/cvieth/survivor-guide/releases/latest/download/survivor-guide-print-interior.pdf)
- [Alle versionierten Ausgaben](https://github.com/cvieth/survivor-guide/releases)
- [PDF-Vorschau des aktuellen Entwicklungsstands (Actions-Artefakt)](https://github.com/cvieth/survivor-guide/actions/workflows/publish.yml)

## Ziele
Wissen öffentlich dokumentieren, offline bewahren und gemeinschaftlich fachlich prüfen. Die drei Zeithorizonte sind **akutes Überleben**, **Stabilisierung** und **langfristiger Wiederaufbau**.

## Architektur
- Eine Markdown-Quelle in `docs/` für Website und PDF
- MkDocs Material für Website, Suche und Navigation
- Pandoc und XeLaTeX für A4-PDF und 6×9-Zoll-Druckvorlage
- GitHub Actions für Qualitätsprüfung, Website-Deployment und versionierte PDF-Releases
- Community über Issues und Pull Requests

## Lokal entwickeln
Voraussetzungen: Python 3.11+, Pandoc, XeLaTeX (z. B. texlive-xetex und texlive-latex-extra), DejaVu-Schrift.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make check
make build
make serve
```

Mit `make print` entsteht `build/survivor-guide-print-interior.pdf` als **unverbindlicher Druckentwurf**, noch nicht bereit für Amazon KDP.

## Veröffentlichung

Der Workflow `Publish website and PDF` veröffentlicht bei jedem Push auf `main` die Website auf GitHub Pages und stellt ein unversioniertes Vorschau-PDF als herunterladbares GitHub-Actions-Artefakt bereit. Unter **Settings → Pages → Build and deployment** muss dazu **GitHub Actions** als Quelle eingestellt sein.

Der separate Workflow [`Publish versioned PDF releases`](.github/workflows/release.yml) erzeugt bei einem neuen Versionstag **beide PDF-Dateien** und veröffentlicht sie als Assets eines GitHub Releases. Die Dateinamen bleiben innerhalb der Releases gleich, ältere Versionen sind über [alle Releases](https://github.com/cvieth/survivor-guide/releases) abrufbar.

Neue Version veröffentlichen:

```bash
git tag v0.2.0
git push origin v0.2.0
```

Alternativ unter **Actions → Publish versioned PDF releases → Run workflow** die gewünschte Versionsnummer (z. B. `v0.2.0`) eintragen. Der erste Release `v0.1.0` wird bei Einführung des Release-Workflows auf `main` automatisch erstellt. Bereits existierende Releases werden nicht überschrieben.

## Mitarbeit
Siehe [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), [ROADMAP.md](ROADMAP.md) sowie [Qualitätsregeln](docs/redaktion/qualitaet.md). Neue Artikel anhand `templates/artikel.md` schreiben.

**Lizenz:** Texte CC BY-SA 4.0, Build-Code MIT. Für Drittmaterial separate Rechte prüfen.
