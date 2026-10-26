#!/usr/bin/env python3
"""Render top-level Mermaid Markdown fences as SVG assets for PDF and print."""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "build" / "diagrams"
TICKS = chr(96) * 3
FENCE = re.compile(r"(?ms)^" + TICKS + r"mermaid[ \t]*\r?\n(.*?)^" + TICKS + r"[ \t]*(?:\r?\n|$)")
ALT = re.compile(r"(?m)^%%[ \t]*alt:[ \t]*(.+)$")


def render_for_pdf(markdown: str) -> str:
    """Replace Mermaid fences with vector SVG references rendered from their source."""
    def replace(match: re.Match[str]) -> str:
        code = match.group(1).strip() + "\n"
        digest = hashlib.sha256(code.encode("utf-8")).hexdigest()[:20]
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        source = OUTPUT_DIR / f"{digest}.mmd"
        target = OUTPUT_DIR / f"{digest}.svg"
        source.write_text(code, encoding="utf-8")
        if not target.exists():
            local_cli = ROOT / "node_modules" / ".bin" / "mmdc"
            executable = str(local_cli) if local_cli.is_file() else shutil.which("mmdc")
            if not executable:
                raise RuntimeError("Mermaid CLI missing: run 'npm install' before building PDF or print")
            subprocess.run(
                [executable, "-i", str(source), "-o", str(target),
                 "-t", "neutral", "-b", "white"],
                cwd=ROOT,
                check=True,
            )
        alt_match = ALT.search(code)
        alt = alt_match.group(1).strip() if alt_match else "Diagramm"
        alt = alt.replace("[", "").replace("]", "")
        return f"![{alt}](diagrams/{digest}.svg){{ width=100% }}\n"

    return FENCE.sub(replace, markdown)
