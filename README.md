# Survivor Guide

**Das offene Handbuch für Krisenbewältigung, Überleben und Wiederaufbau.**

> **Version 0.1: Grundgerüst.** Die meisten Kapitel sind noch Themenpläne, keine fachlich geprüften Anleitungen.

## Lesen
- [Online-Handbuch](https://cvieth.github.io/survivor-guide/) (nach erstmaligem Pages-Deployment)
- [PDF-Download](https://cvieth.github.io/survivor-guide/downloads/survivor-guide.pdf) (nach erstmaligem Build)

## Ziele
Wissen öffentlich dokumentieren, offline bewahren und gemeinschaftlich fachlich prüfen. Die drei Zeithorizonte sind **akutes Überleben**, **Stabilisierung** und **langfristiger Wiederaufbau**.

## Architektur
- Eine Markdown-Quelle in `docs/` für Website und PDF
- MkDocs Material für Website, Suche und Navigation
- Pandoc und XeLaTeX für A4-PDF und 6×9-Zoll-Druckvorlage
- GitHub Actions für Qualitätsprüfung und Website-Deployment
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

## GitHub Pages
Im Repository unter **Settings → Pages → Build and deployment** als Quelle **GitHub Actions** einstellen. Der Workflow `Publish website and PDF` übernimmt danach den Build und das Deployment.

## Mitarbeit
Siehe [CONTRIBUTING.md](CONTRIBUTING.md), [AGENTS.md](AGENTS.md), [ROADMAP.md](ROADMAP.md) sowie [Qualitätsregeln](docs/redaktion/qualitaet.md). Neue Artikel anhand `templates/artikel.md` schreiben.

**Lizenz:** Texte CC BY-SA 4.0, Build-Code MIT. Für Drittmaterial separate Rechte prüfen.
