# Agentenregeln – Survivor Guide

- Dies ist ein frei zugängliches, deutschsprachiges Krisen- und Wissenshandbuch.
- Ein Thema nach `docs/<kapitel>/<slug>.md` einordnen und `mkdocs.yml` bei neuen Artikeln aktualisieren.
- Kapitelnummern bleiben ausschließlich in Verzeichnisnamen und der internen Sortierung; in sichtbaren Seitentiteln (`# ...`) und MkDocs-Navigationslabels keine Nummernpräfixe wie `01 ·` verwenden.
- Artikelvorlage `templates/artikel.md` verwenden, Fakten belegen und Unsicherheiten kenntlich machen.
- Wissenschaftlich und sachlich schreiben; keine unbelegten Behauptungen als Gewissheiten darstellen.
- Medizinische, pharmakologische, chemische, elektrische und andere sicherheitskritische Anleitungen bis zur Fachprüfung deutlich als ungeprüft markieren.
- Realistische Grenzen, benötigte Ausrüstung, Gefahren und Alternativen aufzeigen.
- Besonders gefährliche Verfahren nicht improvisiert als allgemein sichere Praxis darstellen.
- Keine fremden Bilder oder geschützte längere Texte ohne nachgewiesene Nutzungsrechte übernehmen.
- `python3 scripts/check.py` prüfen und, wenn die Toolchain verfügbar ist, `make build` ausführen.
- Keine Änderung als veröffentlicht bezeichnen, bevor die Veröffentlichung verifiziert wurde.

- Wenn möglich und für das Verständnis hilfreich, Inhalte mit eigenständig erstellten, barrierearm beschrifteten Diagrammen, Illustrationen oder Tabellen ergänzen. Grafiken sollen sowohl im Website- als auch im PDF-Build funktionieren.
- Bei jedem dokumentierten oder veröffentlichten Artikel in der Antwort einen direkten Web-Link zur Artikelseite und einen GitHub-Quelllink nennen. Status der Veröffentlichung und eventuell offene Arbeiten transparent angeben.

- Entscheidungsbäume mit `::: decision` und `::: answer` aus Markdown erstellen, nicht als vorgerenderte Bilder. Der gemeinsame Renderer übernimmt Website, PDF und Buch. Details siehe `CONTRIBUTING.md`.

- Bei jedem **zeitkritischen oder prozeduralen Artikel** vor der Veröffentlichung prüfen: Welche beobachtbaren Kriterien führen zu unterschiedlichen Handlungen? Solche echten Entscheidungspunkte bevorzugt als wiederverwendbaren Markdown-Block (`::: decision`) unmittelbar vor den betroffenen Maßnahmen darstellen. Dies gilt besonders für die ersten 72 Stunden, medizinische Triage, Wasserqualität, Kommunikation, Hygiene und Evakuierung.
- Keine Entscheidungsdiagramme nur zur Dekoration oder bei identischem Ergebnis beider Zweige. Jede Verzweigung muss eine klare, überprüfbare Frage, unterschiedliche Konsequenzen, sichere Behandlung von Unsicherheit und gegebenenfalls einen Rückweg zur neuen Gefahrenbewertung enthalten. Die Diagramme müssen allein über Text verständlich bleiben und in Web-, A4-PDF- und Buchformat funktionieren.
