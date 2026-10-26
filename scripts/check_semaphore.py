#!/usr/bin/env python3
"""Check Semaphore documentation against the authoritative A-Z position table."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ARTICLE = ROOT / "docs/04-kommunikation/flaggenalphabet.md"
DIR = ROOT / "docs/assets/kommunikation/semaphore"
ANGLES = ("12", "1:30", "3", "4:30", "6", "7:30", "9", "10:30")
CODES = {
    "A": ("6", "7:30"), "B": ("6", "9"), "C": ("6", "10:30"),
    "D": ("6", "12"), "E": ("1:30", "6"), "F": ("3", "6"),
    "G": ("4:30", "6"), "H": ("7:30", "9"), "I": ("7:30", "12"),
    "J": ("3", "12"), "K": ("12", "7:30"), "L": ("1:30", "7:30"),
    "M": ("3", "7:30"), "N": ("4:30", "7:30"), "O": ("10:30", "9"),
    "P": ("12", "9"), "Q": ("1:30", "9"), "R": ("3", "9"),
    "S": ("4:30", "9"), "T": ("12", "10:30"), "U": ("1:30", "10:30"),
    "V": ("4:30", "12"), "W": ("3", "1:30"), "X": ("4:30", "1:30"),
    "Y": ("3", "10:30"), "Z": ("3", "4:30"),
    "ZAHL": ("1:30", "12"), "ANNULL": ("4:30", "10:30"),
}

def validate():
    errors = []
    content = ARTICLE.read_text(encoding="utf-8")
    fence = re.escape(chr(96) * 3)
    diagrams = re.findall(r"(?ms)^" + fence + r"mermaid[ \t]*\n(.*?)^" + fence + r"[ \t]*(?:\n|$)", content)
    if len(diagrams) != 1:
        return [f"Semaphore: expected ONE decoder graph, found {len(diagrams)}"]
    graph = diagrams[0]
    if 'START(["START: linker Arm des Senders"])' not in graph:
        errors.append("Semaphore: missing single start node")
    root_edges = re.findall(r'(?m)^\s*START -->\|(.+?)\| L([0-7])\[', graph)
    expected_roots = set(left for left, _ in CODES.values())
    if set(a.replace(" Uhr", "") for a, _ in root_edges) != expected_roots:
        errors.append("Semaphore: root branches do not cover all left-arm positions")
    second = re.findall(r'(?m)^\s*L([0-7]) -->\|rechts: (.+?) Uhr\| C_([A-Z]+)\["', graph)
    if len(second) != 28:
        errors.append(f"Semaphore: graph must have 28 signals, got {len(second)}")
    seen = set()
    for left_index, right, letter in second:
        if letter not in CODES:
            errors.append(f"Semaphore: invalid graph signal {letter}")
            continue
        left = ANGLES[int(left_index)]
        if (left, right) != CODES[letter]:
            errors.append(f"Semaphore: incorrect graph path for {letter}: {left}, {right}")
        if letter in seen:
            errors.append(f"Semaphore: duplicate graph leaf for {letter}")
        seen.add(letter)
    if seen != set(CODES):
        errors.append("Semaphore: missing or unexpected decoder characters")
    for character, (left, right) in CODES.items():
        svg_path = DIR / (character.lower() + ".svg")
        if not svg_path.is_file():
            errors.append(f"Semaphore: missing SVG {character}")
            continue
        try:
            svg = ET.parse(svg_path).getroot()
            if svg.attrib.get("data-sender-left") != left or svg.attrib.get("data-sender-right") != right:
                errors.append(f"Semaphore: incorrect direction attributes for {character}")
            shapes = [e.tag.rsplit("}", 1)[-1] for e in svg.iter()]
            if shapes.count("polygon") != 4 or shapes.count("line") != 4:
                errors.append(f"Semaphore: expected two poles and two colored flags for {character}")
        except ET.ParseError as exc:
            errors.append(f"Semaphore: invalid SVG {character}: {exc}")
        if f"../assets/kommunikation/semaphore/{character.lower()}.svg" not in content:
            errors.append(f"Semaphore: unlinked SVG {character}")
    for old in ("flaggenalphabet-a-m.svg", "flaggenalphabet-n-z.svg"):
        if old in content:
            errors.append(f"Semaphore: obsolete full-page chart still used ({old})")
    for link in ("morsealphabet.md", "funkzeitfenster-333-regel.md", "sirenensignale.md", "../00-grundlagen/erste-72-stunden.md"):
        if f"]({link}" not in content and f"]({link}#" not in content:
            errors.append(f"Semaphore: missing cross-reference to {link}")
    return errors

if __name__ == "__main__":
    errors = validate()
    if errors:
        raise SystemExit("\n".join(errors))
    print("OK: Semaphore A-Z, mode signals, SVG table and one connected decoder")
