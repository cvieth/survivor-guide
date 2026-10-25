#!/usr/bin/env python3
"""Generate the markdown register from the machine-readable JSON source."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data/medikamente.json").read_text(encoding="utf-8"))
sources, entries = data["quellen"], data["eintraege"]
header = "# Wirkstoffregister – Offline-Nachschlagewerk\n\n!!! warning \"Entwurf – fachliche Prüfung ausstehend\"\n    Die Wirkstoffsteckbriefe sind eine Orientierung zur **Identifizierung von Arzneimitteln**, keine Therapie-, Dosierungs- oder Verschreibungsanleitung. Stand: 25. Oktober 2026.\n\nDieses Register wird aus einer [maschinenlesbaren JSON-Datei](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json) erzeugt und ist auch im Gesamt-PDF enthalten. Die Stufen beschreiben **Szenario-Prioritäten, keine allgemeingültige medizinische Rangliste**.\n\n- **1:** Persönlicher lebenswichtiger Bedarf und spezielle Notfallmittel.\n- **2:** Häufig benötigte Basisversorgung.\n- **3:** Antibiotika, deren Wahl eine passende bakterielle Indikation voraussetzt.\n- **4:** Ergänzende symptomatische Mittel.\n- **5:** Injektionsmedikamente für qualifiziertes Personal.\n\n**Für alle Mittel:** Originalverpackung, Wirkstärke, Darreichungsform, Beipackzettel, Allergien, Schwangerschaft, Alter, Nieren-/Leberfunktion, Wechselwirkungen und Lagerbedingungen prüfen. Unbekannte oder zweifelhaft gelagerte Medikamente nicht als sicher betrachten. Antibiotika wirken nicht gegen Viren; die Liste ersetzt weder Diagnostik noch Prüfung von Resistenzen oder Behandlungsdauer.\n\nSiehe [Apotheke – Schnellpriorisierung](../03-pharmazie/apotheke-prioritaeten.md).\n\n"
sections = {"1":"1 · Persönlicher Bedarf und Notfall","2":"2 · Basisversorgung","3":"3 · Antibiotika – indikationsgebunden","4":"4 · Ergänzende Mittel","5":"5 · Fachpersonal und Infrastruktur"}
labels = [["aufschrift","Auf der Packung suchen"],["einsatz","Typischer Einsatz"],["wirkung","Wirkung/Abdeckung"],["nicht_geeignet","Grenzen"],["risiken","Risiken/Gegenanzeigen"],["alternativen","Alternativen"],["voraussetzungen","Voraussetzungen"]]
output = header
for step in ("1", "2", "3", "4", "5"):
    output += "## " + sections[step] + "\n\n"
    for d in [item for item in entries if item["stufe"] == step]:
        output += "### " + d["name"] + "\n\n"
        for key, label in labels:
            output += "- **" + label + ":** " + d[key] + "\n"
        output += "- **Quellen:** " + ", ".join(
            "[" + code + "](" + sources[code]["url"] + ")" for code in d["quellen"]
        ) + "\n"
        output += "- **Lagerung:** Produktindividuelle Vorgaben; keine pauschale Haltbarkeitszusage.\n\n"
output += (
    "## Datenpflege\n\n"
    "- **Einzige Datenquelle:** [data/medikamente.json](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json).\n"
    "- **Seite neu generieren:** `python3 scripts/generate_medications.py`.\n"
    "- **Redaktionsstand:** Entwurf, medizinische und pharmazeutische Fachprüfung ausstehend.\n"
)
dest = ROOT / "docs/12-nachschlagewerk/wirkstoffregister.md"
dest.write_text(output, encoding="utf-8")
print("Updated", dest.relative_to(ROOT))
