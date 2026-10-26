#!/usr/bin/env python3
"""Check navigation references and local Markdown links."""
from pathlib import Path
from urllib.parse import unquote, urlparse
import re
import sys
import yaml
from decision_blocks import parse_blocks

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NAV = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))["nav"]

def flatten(node):
    if isinstance(node, list):
        for item in node:
            yield from flatten(item)
    elif isinstance(node, dict):
        for label, value in node.items():
            if isinstance(value, str):
                yield label, value
            else:
                yield from flatten(value)

def main():
    errors = []
    items = list(flatten(NAV))
    paths = [path for _, path in items]
    if len(paths) != len(set(paths)):
        errors.append("Duplicate navigation paths")
    for label, path in items:
        if not (DOCS / path).is_file():
            errors.append(f"Missing nav target: {label}: {path}")
    files = list(DOCS.rglob("*.md"))
    regex = re.compile(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)|!\[[^\]]*\]\(([^\s)]+)\)')
    for doc in files:
        content = doc.read_text(encoding="utf-8")
        try:
            parse_blocks(content)
        except ValueError as exc:
            errors.append(f"Invalid decision block in {doc.relative_to(ROOT)}: {exc}")
        if not re.search(r"(?m)^#\s+\S+", content):
            errors.append(f"Missing H1: {doc.relative_to(ROOT)}")
        for m in regex.finditer(content):
            raw = m.group(1) or m.group(2)
            parsed = urlparse(raw)
            if parsed.scheme or parsed.netloc or raw.startswith(("#","mailto:","/")):
                continue
            target = unquote(parsed.path)
            if not target or target == "downloads/survivor-guide.pdf":
                continue
            resolved = (doc.parent / target).resolve()
            if not resolved.is_relative_to(DOCS.resolve()):
                errors.append(f"Link outside docs: {doc.relative_to(ROOT)} -> {raw}")
            elif not resolved.is_file():
                errors.append(f"Broken link: {doc.relative_to(ROOT)} -> {raw}")
    if errors:
        for e in errors: print("ERROR:",e,file=sys.stderr)
        return 1
    print(f"OK: {len(files)} Markdown pages, {len(items)} navigation entries")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
