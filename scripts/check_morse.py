#!/usr/bin/env python3
"""Regression test: precisely one traversable Morse tree, geometric SVG symbols."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ARTICLE = ROOT / "docs/04-kommunikation/morsealphabet.md"
SVG_DIR = ROOT / "docs/assets/kommunikation/morsezeichen"
MORSE = {
 "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
 "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
 "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
 "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
 "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
 "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
 "3": "...--", "4": "....-", "5": ".....", "6": "-....",
 "7": "--...", "8": "---..", "9": "----.",
}

def validate():
    errors = []
    content = ARTICLE.read_text(encoding="utf-8")
    fence = re.escape(chr(96) * 3)
    blocks = re.findall(r"(?ms)^" + fence + r"mermaid[ \t]*\n(.*?)^" + fence + r"[ \t]*(?:\n|$)", content)
    if len(blocks) != 1:
        return [f"Morse: expected exactly ONE Mermaid diagram, found {len(blocks)}"]
    block = blocks[0]
    if "flowchart TB" not in block or 'ROOT(("START"))' not in block:
        errors.append("Morse: graph must flow from one START node top to bottom")
    edges = re.findall(r'(?m)^\s*(ROOT|N[01]+) -->\|(kurz|lang)\| (N[01]+)\["([A-Z])"\]$', block)
    if len(edges) != 26:
        errors.append(f"Morse: expected 26 tree edges, found {len(edges)}")
    graph = {}
    for parent, direction, child, letter in edges:
        if (parent, direction) in graph:
            errors.append(f"Morse: duplicate {direction} branch at {parent}")
        graph[(parent, direction)] = (child, letter)
    for letter, code in MORSE.items():
        if letter.isdigit():
            continue
        node = "ROOT"
        for signal in code:
            item = graph.get((node, "kurz" if signal == "." else "lang"))
            if item is None:
                errors.append(f"Morse: missing branch in path to {letter}")
                break
            node, actual = item
        else:
            if actual != letter:
                errors.append(f"Morse: path for {letter} ends at {actual}")
    for letter, code in MORSE.items():
        svg_path = SVG_DIR / (letter.lower() + ".svg")
        if not svg_path.exists():
            errors.append(f"Morse: missing SVG for {letter}")
            continue
        try:
            svg = ET.parse(svg_path).getroot()
            elements = [e.tag.rsplit("}", 1)[-1] for e in svg]
            elements = [shape for shape in elements if shape in {"circle", "rect"}]
            expected = ["circle" if signal == "." else "rect" for signal in code]
            if elements != expected:
                errors.append(f"Morse: geometric symbols differ from code for {letter}")
        except ET.ParseError as e:
            errors.append(f"Morse: invalid SVG for {letter}: {e}")
        ref = f"../assets/kommunikation/morsezeichen/{letter.lower()}.svg"
        if f"]({ref})" not in content:
            errors.append(f"Morse: table does not reference {ref}")
    return errors

if __name__ == "__main__":
    errors = validate()
    if errors:
        raise SystemExit("\n".join(errors))
    print("OK: one connected Morse tree A-Z, all 36 geometric SVG symbols")
