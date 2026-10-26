#!/usr/bin/env python3
"""Generate the markdown register from the machine-readable JSON source."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data/medikamente.json").read_text(encoding="utf-8"))
sources, entries = data["quellen"], data["eintraege"]
header = "# Wirkstoffregister – Offline-Nachschlagewerk\n\n!!! warning \"Entwurf – fachliche Prüfung ausstehend\"\n    Die Wirkstoffsteckbriefe sind eine Orientierung zur **Identifizierung von Arzneimitteln**, keine individuelle Therapie- oder Verschreibungsanleitung. Angegebene **Leitlinien-Referenzdosierungen** sind nur für die passende Indikation bei Erwachsenen gedacht. Stand: 26. Oktober 2026.\n\nDieses Register wird aus einer [maschinenlesbaren JSON-Datei](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json) erzeugt und ist auch im Gesamt-PDF enthalten. Die Stufen beschreiben **Szenario-Prioritäten, keine allgemeingültige medizinische Rangliste**.\n\n- **1:** Persönlicher lebenswichtiger Bedarf und spezielle Notfallmittel.\n- **2:** Häufig benötigte Basisversorgung.\n- **3:** Antibiotika, deren Wahl eine passende bakterielle Indikation voraussetzt.\n- **4:** Ergänzende symptomatische Mittel.\n- **5:** Injektionsmedikamente für qualifiziertes Personal.\n- **X:** Häufig verwechselte oder für Wunden ungeeignete Stoffe, **keine Bevorratungs- oder Anwendungsempfehlung**.\n\n**Für alle Mittel:** Originalverpackung, Wirkstärke, Darreichungsform, Beipackzettel, Allergien, Schwangerschaft, Alter, Nieren-/Leberfunktion, Wechselwirkungen und Lagerbedingungen prüfen. Unbekannte oder zweifelhaft gelagerte Medikamente nicht als sicher betrachten. Antibiotika wirken nicht gegen Viren; die Liste ersetzt weder Diagnostik noch Prüfung von Resistenzen oder Behandlungsdauer.\n\nSiehe [Apotheke – Schnellpriorisierung](../03-pharmazie/apotheke-prioritaeten.md), [Antibiotikagruppen](antibiotikagruppen.md) und [Wundinfektionen](../02-medizin/wundinfektionen-antibiotika.md).\n\nBeschwerden zuerst im [Symptomverzeichnis](../02-medizin/beschwerden-und-mittel.md) einordnen. **Haushaltsreiniger, Natriumhypochlorit und andere Hygienestoffe** sind im gesonderten [Hygienemittelregister](hygienemittel-register.md) dokumentiert, **nicht** als Arzneimittel. Zu ausgewählten Anwendungsgebieten gibt es ein eigenes [Heilpflanzenregister](heilpflanzenregister.md); dessen Einträge sind keine pauschal gleichwertigen Ersatzmittel.\n\n"
sections = {"1":"1 · Persönlicher Bedarf und Notfall","2":"2 · Basisversorgung","3":"3 · Antibiotika – indikationsgebunden","4":"4 · Ergänzende Mittel","5":"5 · Fachpersonal und Infrastruktur", "X":"X · Warnhinweise und nicht empfohlene Anwendungen"}
labels = [["aufschrift","Auf der Packung suchen"],["einsatz","Typischer Einsatz"],["wirkung","Wirkung/Abdeckung"],["nicht_geeignet","Grenzen"],["risiken","Risiken/Gegenanzeigen"],["alternativen","Alternativen"],["voraussetzungen","Voraussetzungen"]]
RELATED = {
    "Orale Rehydratationssalze (ORS)": "[Durchfall und Austrocknung: ORS und Warnzeichen](../02-medizin/durchfall-austrocknung.md#orale-rehydratationsloesung-ors); [Handhygiene](../01-versorgung/handhygiene-ohne-leitungswasser.md); [Trinkwassersicherheit](../01-versorgung/oberflaechenwasser-aufbereiten.md); Heilpflanzen ersetzen ORS nicht.",
    "Natriumchlorid 0,9 % (sterile Spüllösung)": "[Kleine Wunden: Reinigung und Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); reinigt mechanisch, desinfiziert nicht.",
    "Paracetamol": "[Fieberanleitung](../02-medizin/fieber-erkennen-und-versorgen.md); [Weidenrinde](heilpflanzenregister.md#weidenrinde) hat andere Risiken und ist kein dosierbarer Ersatz.",
    "Ibuprofen": "[Fieberanleitung](../02-medizin/fieber-erkennen-und-versorgen.md); [Weidenrinde](heilpflanzenregister.md#weidenrinde) kann zusätzliche salicylatbezogene Risiken bergen.",
    "Octenidin": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); [Ringelblume](heilpflanzenregister.md#ringelblumenblueten) ersetzt keine Antiseptik.",
    "Polihexanid (PHMB)": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll).",
    "Povidon-Iod": "[Wundversorgung und Entscheidung zur Antiseptik](../02-medizin/wunden-mehrtaegige-versorgung.md#reinigung-oder-antiseptik-was-ist-sinnvoll); [Ringelblume](heilpflanzenregister.md#ringelblumenblueten) ersetzt keine Antiseptik.",
    "Wasserstoffperoxid": "[Wundversorgung: warum Wasserstoffperoxid nicht erste Wahl ist](../02-medizin/wunden-mehrtaegige-versorgung.md#warum-wasserstoffperoxid-keine-gute-routineoption-ist); nicht als Wundmittel bevorraten.",
    "Loperamid": "[Durchfall und Austrocknung](../02-medizin/durchfall-austrocknung.md); [Eichenrinde](heilpflanzenregister.md#eichenrinde) ersetzt keine Rehydratation.",
}

output = header
for step in ("1", "2", "3", "4", "5", "X"):
    output += "## " + sections[step] + "\n\n"
    for d in [item for item in entries if item["stufe"] == step]:
        output += "### " + d["name"] + (" {#" + d["anchor"] + "}" if d.get("anchor") else "") + "\n\n"
        for key, label in labels:
            output += "- **" + label + ":** " + d[key] + "\n"
        if d.get("gruppe"):
            g = next(g for g in data["antibiotikagruppen"] if g["id"] == d["gruppe"])
            output += "- **Antibiotikagruppe:** [" + g["name"] + "](antibiotikagruppen.md#" + g["id"] + ")\n"
        if d.get("wunddosis"):
            output += "- **Leitlinien-Referenzdosierung (Erwachsene, indikationsgebunden):** " + d["wunddosis"] + "\n"
        if d.get("wundgrenzen"):
            output += "- **Wundspezifische Grenzen:** " + d["wundgrenzen"] + "\n"
        output += "- **Quellen:** " + ", ".join(
            "[" + code + "](" + sources[code]["url"] + ")" for code in d["quellen"]
        ) + "\n"
        output += "- **Lagerung:** Produktindividuelle Vorgaben; keine pauschale Haltbarkeitszusage.\n"
        if d["name"] in RELATED:
            output += "- **Weiterführend:** " + RELATED[d["name"]] + "\n"
        if d.get("gruppe"):
            output += "- **Wundinfektionen:** [Klinische Einordnung](../02-medizin/wundinfektionen-antibiotika.md).\n"
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

# Generate the antibiotic class index from the same structured dataset.
group_page = "# Antibiotikagruppen: Wirkweise und Grenzen\n\n!!! warning \"Entwurf, medizinische Fachprüfung ausstehend\"\n    Keine individuelle Dosierungs- oder Behandlungsfreigabe.\n\nVom [Wundinfektions-Entscheidungsweg](../02-medizin/wundinfektionen-antibiotika.md) zur passenden Wirkstoffklasse und zum [zentralen Wirkstoffregister](wirkstoffregister.md).\n\n"
for g in data["antibiotikagruppen"]:
    group_page += "## " + g["name"] + " {#" + g["id"] + "}\n\n"
    group_page += "- **Wirkprinzip:** " + g["wirkprinzip"] + "\n"
    group_page += "- **Geeignete Einsatzgebiete:** " + g["eignung"] + "\n"
    group_page += "- **Grenzen und Gegenanzeigen:** " + g["grenzen"] + "\n"
    choices = []
    for n in g["wirkstoffe"]:
        m = next((m for m in entries if m["name"] == n), None)
        if m is None:
            raise ValueError("Missing antibiotic drug: " + n)
        slug = m.get("anchor", n.lower().replace(" ", "-"))
        choices.append("[" + n + "](wirkstoffregister.md#" + slug + ")")
    group_page += "- **Wirkstoffsteckbriefe:** " + ", ".join(choices) + "\n"
    group_page += "- **Quellen:** " + ", ".join("[" + key + "](" + sources[key]["url"] + ")" for key in g["quellen"]) + "\n\n"
group_page += "## Zurück zu den Handlungsanleitungen\n\n[Wundinfektionen](../02-medizin/wundinfektionen-antibiotika.md) · [Wundreinigung](../02-medizin/wunden-mehrtaegige-versorgung.md) · [Apothekenprioritäten](../03-pharmazie/apotheke-prioritaeten.md).\n\nQuelle der Klassendaten: [data/medikamente.json](https://github.com/cvieth/survivor-guide/blob/main/data/medikamente.json).\n"
(ROOT / "docs/12-nachschlagewerk/antibiotikagruppen.md").write_text(group_page, encoding="utf-8")
print("Updated docs/12-nachschlagewerk/antibiotikagruppen.md")
