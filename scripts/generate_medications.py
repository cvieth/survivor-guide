#!/usr/bin/env python3
"""Generate the markdown register from the machine-readable JSON source."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data/medikamente.json").read_text(encoding="utf-8"))
sources, entries = data["quellen"], data["eintraege"]
header = "# Wirkstoffregister – Offline-Nachschlagewerk\n\n!!! warning \"Entwurf – fachliche Prüfung ausstehend\"\n    Die Wirkstoffsteckbriefe sind eine Orientierung zur **Identifizierung von Arzneimitteln**, keine Therapie-, Dosierungs- oder Verschreibungsanleitung. Stand: 26. Oktober 2026.\n\nDieses Register wird aus einer [maschinenlesbaren JSON-Datei](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json) erzeugt und ist auch im Gesamt-PDF enthalten. Die Stufen beschreiben **Szenario-Prioritäten, keine allgemeingültige medizinische Rangliste**.\n\n- **1:** Persönlicher lebenswichtiger Bedarf und spezielle Notfallmittel.\n- **2:** Häufig benötigte Basisversorgung.\n- **3:** Antibiotika, deren Wahl eine passende bakterielle Indikation voraussetzt.\n- **4:** Ergänzende symptomatische Mittel.\n- **5:** Injektionsmedikamente für qualifiziertes Personal.\n- **X:** Häufig verwechselte oder für Wunden ungeeignete Stoffe, **keine Bevorratungs- oder Anwendungsempfehlung**.\n\n**Für alle Mittel:** Originalverpackung, Wirkstärke, Darreichungsform, Beipackzettel, Allergien, Schwangerschaft, Alter, Nieren-/Leberfunktion, Wechselwirkungen und Lagerbedingungen prüfen. Unbekannte oder zweifelhaft gelagerte Medikamente nicht als sicher betrachten. Antibiotika wirken nicht gegen Viren; die Liste ersetzt weder Diagnostik noch Prüfung von Resistenzen oder Behandlungsdauer.\n\nSiehe [Apotheke – Schnellpriorisierung](../03-pharmazie/apotheke-prioritaeten.md).\n\nBeschwerden zuerst im [Symptomverzeichnis](../02-medizin/beschwerden-und-mittel.md) einordnen. Zu ausgewählten Anwendungsgebieten gibt es ein eigenes [Heilpflanzenregister](heilpflanzenregister.md); dessen Einträge sind keine pauschal gleichwertigen Ersatzmittel.\n\n"
sections = {"1":"1 · Persönlicher Bedarf und Notfall","2":"2 · Basisversorgung","3":"3 · Antibiotika – indikationsgebunden","4":"4 · Ergänzende Mittel","5":"5 · Fachpersonal und Infrastruktur", "X":"X · Warnhinweise und nicht empfohlene Anwendungen"}
labels = [["aufschrift","Auf der Packung suchen"],["einsatz","Typischer Einsatz"],["wirkung","Wirkung/Abdeckung"],["nicht_geeignet","Grenzen"],["risiken","Risiken/Gegenanzeigen"],["alternativen","Alternativen"],["voraussetzungen","Voraussetzungen"]]
RELATED = {
    "Orale Rehydratationssalze (ORS)": "[Durchfall und Erbrechen](../02-medizin/beschwerden-und-mittel.md#magen-und-darm); [Trinkwassersicherheit](../01-versorgung/oberflaechenwasser-aufbereiten.md); Heilpflanzen ersetzen ORS nicht.",
    "Natriumchlorid 0,9 % (sterile Spüllösung)": "[Kleine Wunden: Reinigung und Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); reinigt mechanisch, desinfiziert nicht.",
    "Paracetamol": "[Fieberanleitung](../02-medizin/fieber-erkennen-und-versorgen.md); [Weidenrinde](heilpflanzenregister.md#weidenrinde) hat andere Risiken und ist kein dosierbarer Ersatz.",
    "Ibuprofen": "[Fieberanleitung](../02-medizin/fieber-erkennen-und-versorgen.md); [Weidenrinde](heilpflanzenregister.md#weidenrinde) kann zusätzliche salicylatbezogene Risiken bergen.",
    "Octenidin": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); [Ringelblume](heilpflanzenregister.md#ringelblumenblueten) ersetzt keine Antiseptik.",
    "Polihexanid (PHMB)": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll).",
    "Povidon-Iod": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); [Ringelblume](heilpflanzenregister.md#ringelblumenblueten) ersetzt keine Antiseptik.",
    "Wasserstoffperoxid": "[Wundversorgung: warum Wasserstoffperoxid nicht erste Wahl ist](../02-medizin/wunden-mehrtaegige-versorgung.md#warum-wasserstoffperoxid-keine-gute-routineoption-ist); nicht als Wundmittel bevorraten.",
    "Loperamid": "[Durchfall und Austrocknung](../02-medizin/beschwerden-und-mittel.md#magen-und-darm); [Eichenrinde](heilpflanzenregister.md#eichenrinde) ersetzt keine Rehydratation.",
}

output = header
for step in ("1", "2", "3", "4", "5", "X"):
    output += "## " + sections[step] + "\n\n"
    for d in [item for item in entries if item["stufe"] == step]:
        output += "### " + d["name"] + "\n\n"
        for key, label in labels:
            output += "- **" + label + ":** " + d[key] + "\n"
        output += "- **Quellen:** " + ", ".join(
            "[" + code + "](" + sources[code]["url"] + ")" for code in d["quellen"]
        ) + "\n"
        output += "- **Lagerung:** Produktindividuelle Vorgaben; keine pauschale Haltbarkeitszusage.\n"
        if d["name"] in RELATED:
            output += "- **Weiterführend:** " + RELATED[d["name"]] + "\n"
        output += "\n"
output += (
    "## Datenpflege\n\n"
    "- **Einzige Datenquelle:** [data/medikamente.json](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json).\n"
    "- **Seite neu generieren:** `python3 scripts/generate_medications.py`.\n"
    "- **Redaktionsstand:** Entwurf, medizinische und pharmazeutische Fachprüfung ausstehend.\n"
)
dest = ROOT / "docs/12-nachschlagewerk/wirkstoffregister.md"
dest.write_text(output, encoding="utf-8")
print("Updated", dest.relative_to(ROOT))
