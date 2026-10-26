# Mitmachen beim Survivor Guide

1. Bestehende Artikel und Issues prüfen, um Doppelarbeit zu vermeiden.
2. Themen über die Issue-Vorlage vorschlagen.
3. In einem Branch unter `docs/` schreiben, Vorlage `templates/artikel.md`.
4. Fakten mit nachvollziehbaren Quellen belegen; Unsicherheit offen kennzeichnen.
5. Medizin, Pharmazie, Chemie, Elektrizität und Sicherheit erfordern fachliche Prüfung. Risiken, Kontraindikationen und Grenzen dokumentieren.
6. `make check` und nach Möglichkeit `make build` ausführen, Pull Request eröffnen.
7. Nur selbst erstellte oder korrekt lizenzierte Inhalte beitragen. Mit dem PR bestätigt der Beitragende die Freigabe seiner Textbeiträge unter CC BY-SA 4.0.

**Sprache:** Deutsch; **Ton:** sachlich, konkret, nachvollziehbar; **Quellen:** Autor, Titel, Datum, ggf. DOI und URL.


## Entscheidungsdiagramme aus Markdown

Entscheidungsbäume als wiederverwendbaren Markdown-Block formulieren. Beispiel (vier Leerzeichen nur zur Darstellung in diesem Dokument):

    ::: decision
    label: PHASE 0
    question: Ist das Gebäude akut gefährlich?
    hint: Warnungen beachten.
    ::: answer danger "JA" "Gebäude verlassen"
    Einen **sicheren** Fluchtweg wählen.
    ::: answer neutral "NEIN" "Weitere Gefahr prüfen"
    Die **nächste Schutzfrage** beantworten.
    ::: enddecision

Die Typen sind `danger` (rot), `protect` (blau) und `neutral` (neutral). Erlaubt sind zwei oder drei Antwortkarten. Der Text jeder Karte ist normales Markdown. Inhalte müssen auch ohne Farben verständlich sein. Keine verschachtelten Blöcke; für Folgeschritte einen weiteren Block schreiben.

Das PDF verwendet für zwei Antworten auf A4 zwei nebeneinanderliegende Karten. Im schmalen Buchformat stehen die Karten untereinander und werden für Schwarzweißdruck ausgegeben. Website-Karten sind responsiv.
