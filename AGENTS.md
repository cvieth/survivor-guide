# Agentenregeln – Survivor Guide

- Dies ist ein frei zugängliches, deutschsprachiges Krisen- und Wissenshandbuch.
- Ein Thema nach `docs/<kapitel>/<slug>.md` einordnen und `mkdocs.yml` bei neuen Artikeln aktualisieren.
- Kapitelnummern bleiben ausschließlich in Verzeichnisnamen und der internen Sortierung; in sichtbaren Seitentiteln (`# ...`) und MkDocs-Navigationslabels keine Nummernpräfixe wie `01 ·` verwenden.
- Artikelvorlage `templates/artikel.md` verwenden, Fakten belegen und Unsicherheiten kenntlich machen.
- Wissenschaftlich und sachlich schreiben; keine unbelegten Behauptungen als Gewissheiten darstellen.
- Nüchtern, natürlich und präzise formulieren. Keine werblichen Appelle, künstliche Freundlichkeit, Floskeln oder Emoticons. Gedankenstriche nicht routinemäßig als Satzverbindung verwenden; stattdessen normale Satzzeichen und kurze, klare Sätze. Notwendige Bindestriche in Fachbegriffen bleiben erlaubt.
- Medizinische, pharmakologische, chemische, elektrische und andere sicherheitskritische Anleitungen bis zur Fachprüfung deutlich als ungeprüft markieren.
- Realistische Grenzen, benötigte Ausrüstung, Gefahren und Alternativen aufzeigen.
- Besonders gefährliche Verfahren nicht improvisiert als allgemein sichere Praxis darstellen.
- Keine fremden Bilder oder geschützte längere Texte ohne nachgewiesene Nutzungsrechte übernehmen.
- `python3 scripts/check.py` prüfen und, wenn die Toolchain verfügbar ist, `make build` ausführen.
- Zusammengehörige Änderungen gesammelt in einem Commit einspielen. Nicht für jede Datei einzeln committen, da jeder Push einen neuen Website-Build auslöst.
- Eine Website-Änderung erst als veröffentlicht bezeichnen, wenn der Workflow `Publish website` erfolgreich beendet wurde und die öffentlich erreichbare `revision.txt` die betreffende Commit-SHA enthält.

- Wenn möglich und für das Verständnis hilfreich, Inhalte mit eigenständig erstellten, barrierearm beschrifteten Diagrammen, Illustrationen oder Tabellen ergänzen. Grafiken sollen sowohl im Website- als auch im PDF-Build funktionieren.
- Bei jedem dokumentierten oder veröffentlichten Artikel in der Antwort einen direkten Web-Link zur Artikelseite und einen GitHub-Quelllink nennen. Status der Veröffentlichung und eventuell offene Arbeiten transparent angeben.

- Entscheidungsbäume mit `::: decision` und `::: answer` aus Markdown erstellen, nicht als vorgerenderte Bilder. Der gemeinsame Renderer übernimmt Website, PDF und Buch. Details siehe `CONTRIBUTING.md`.

- Bei jedem **zeitkritischen oder prozeduralen Artikel** vor der Veröffentlichung prüfen: Welche beobachtbaren Kriterien führen zu unterschiedlichen Handlungen? Solche echten Entscheidungspunkte bevorzugt als wiederverwendbaren Markdown-Block (`::: decision`) unmittelbar vor den betroffenen Maßnahmen darstellen. Dies gilt besonders für die ersten 72 Stunden, medizinische Triage, Wasserqualität, Kommunikation, Hygiene und Evakuierung.
- Keine Entscheidungsdiagramme nur zur Dekoration oder bei identischem Ergebnis beider Zweige. Jede Verzweigung muss eine klare, überprüfbare Frage, unterschiedliche Konsequenzen, sichere Behandlung von Unsicherheit und gegebenenfalls einen Rückweg zur neuen Gefahrenbewertung enthalten. Die Diagramme müssen allein über Text verständlich bleiben und in Web-, A4-PDF- und Buchformat funktionieren.

- Allgemeine Diagramme als Mermaid-Codeblöcke mit `%% alt:`-Alternativtext verwenden. PDF und Buch rendern dieselbe Quelle mit `scripts/mermaid_diagrams.py` als SVG. Handlungsentscheidungskarten bleiben `::: decision`.

- **Doppelter Versorgungspfad:** Jede relevante medizinische oder andere sicherheitskritische Handlungsanleitung berücksichtigt sowohl verfügbare professionelle Hilfe als auch den vollständigen Ausfall von Telefon, Rettungsdienst, Arzt und Apotheke. „112 rufen“ darf nie der einzige Schritt sein. Im Ausfallpfad konkrete sichere Sofortmaßnahmen, Beobachtung, Entscheidungskriterien, Materialalternativen und Grenzen nennen. Akute lebensrettende Maßnahmen nicht zugunsten einer unerreichbaren externen Stelle verzögern.
- Medizinische Inhalte nach Möglichkeit symptomorientiert und laienverständlich aufbauen: Erkennen/Messen auch ohne Spezialgerät, Warnzeichen/Triage, sofortige Handlungen, Behandlung und Dosierungen nur mit überprüfbaren Voraussetzungen, Gegenanzeigen, Verlaufskontrolle, Eskalation ohne Infrastruktur. Diagnostische Unsicherheit und Grenzen improvisierter Therapien deutlich kennzeichnen. Keine pauschalen Sicherheitserklärungen für riskante Eingriffe.
- **Medizinisches Wissensnetz:** Krankheitsartikel mit dem symptomorientierten Einstieg `docs/02-medizin/beschwerden-und-mittel.md`, dem Wirkstoffregister und dem Heilpflanzenregister verknüpfen. Nur fachlich passende Mittel verlinken. Von Registereinträgen rückwärts zu vorhandenen konkreten Handlungsanleitungen verweisen. Keine toten Links; fehlende Krankheitsartikel als offen kennzeichnen. Doppelte Volltexte vermeiden.
- **Heilpflanzen:** Botanischen Namen und Pflanzenteil, traditionelle vs. klinisch belegte Anwendung, Gegenanzeigen, Wechselwirkungen, Verwechslungsgefahren und Quellen angeben. Bei unklarer Identität/Heimdosierung ausdrücklich von Eigenversuchen abraten. Pflanzenzubereitungen nicht als Ersatz für definierte Arzneimittel oder lebensrettende Maßnahmen ausgeben.

- **Bilder von Heilpflanzen:** Bevorzugt reale, gemeinfreie historische Tafeln oder belegbar frei lizenzierte Fotografien verwenden, nicht KI-Bilder als Hauptreferenz. Bildmetadaten unter `data/heilpflanzen-bilder.json` und `docs/12-nachschlagewerk/bildquellen-heilpflanzen.md` dokumentieren; Bilddateien per `make images` für Website und PDF lokal bereitstellen. Bilder mit Art, Bestimmungsmerkmalen und Grenzen versehen. Erst nach Quellen- und Lizenzprüfung aufnehmen. Nicht allein anhand einer Tafel eine Pflanze zur Selbstmedikation empfehlen.

- **Verlinkte Handlungstiefe:** Wo ein Entscheidungszweig zu einer weiterführenden Maßnahme führt (z. B. Flucht, Wasseraufbereitung, Erstversorgung), in der betroffenen Antwort **nach** der sicherheitskritischen Sofortanweisung direkt auf den einschlägigen Vertiefungsartikel verlinken. Der Kurztext muss auch ohne Öffnen des Links handlungsfähig bleiben; Links dürfen dringende Sofortmaßnahmen nicht verzögern.
- Querverweise in beide Richtungen setzen: vom Entscheidungsbaum zum Handlungsartikel und vom Artikel zurück zur übergeordneten Lageentscheidung sowie zu Material-, Register- und Grundlagenartikeln. Bestehende passende Artikel wiederverwenden statt Inhalte zu duplizieren. Keine Links auf reine Stichwort-Platzhalter als vermeintlich vollständige Anleitung.
