#!/usr/bin/env python3
"""Cache rights-reviewed, historic botanical plates for offline website/PDF builds.

The versioned manifest holds the canonical Commons file titles and attributions.
Images are cached at docs/assets/heilpflanzen; never hotlinked in published output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data/heilpflanzen-bilder.json"
CREDITS = ROOT / "docs/12-nachschlagewerk/bildquellen-heilpflanzen.md"
MIN_JPEG_SIZE = 12_000
MAX_JPEG_SIZE = 7_000_000
USER_AGENT = "SurvivorGuide/1.0 (offline-education; github.com/cvieth/survivor-guide)"


def commons_page(name: str) -> str:
    return "https://commons.wikimedia.org/wiki/File:" + quote(name.replace(" ", "_"), safe="()-_.~")


def original_file(name: str) -> str:
    normalized = name.replace(" ", "_")
    digest = hashlib.md5(normalized.encode("utf-8")).hexdigest()  # Wikimedia storage sharding, not a security hash
    return ("https://upload.wikimedia.org/wikipedia/commons/"
            + digest[0] + "/" + digest[:2] + "/" + quote(normalized, safe="()-_.~"))


def check_jpeg(path: Path) -> bool:
    if not path.is_file() or not MIN_JPEG_SIZE <= path.stat().st_size <= MAX_JPEG_SIZE:
        return False
    with path.open("rb") as fp:
        if fp.read(2) != b"\xff\xd8":
            return False
        fp.seek(-2, 2)
        return fp.read() == b"\xff\xd9"


def credits_page(media: list[dict]) -> str:
    lines = [
        "# Bildquellen: Heilpflanzen",
        "",
        "Alle hier dokumentierten Tafeln sind historische botanische Abbildungen,",
        "die laut der verlinkten Wikimedia-Commons-Dateiseite gemeinfrei sind",
        "(Public Domain Mark 1.0). Bildrechte sind von der CC-BY-SA-Lizenz",
        "der Handbuchtexte getrennt zu betrachten. Die Links führen zur",
        "jeweiligen Originalquelle mit Versionshistorie und Nutzungsinformationen.",
        "Quellenprüfung: 26. Oktober 2026.",
        "",
        "**Hinweis:** Historische Tafeln zeigen exemplarische Arten, teilweise",
        "vergrößerte Details und idealisierte Merkmale. Eine einzelne Abbildung",
        "reicht nicht zur sicheren Bestimmung oder medizinischen Anwendung.",
        "Bei Unklarheit niemals sammeln oder einnehmen.",
        "",
        "Die Originaldateien werden anhand des versionierten",
        "[Medienmanifests](https://github.com/cvieth/survivor-guide/blob/main/data/heilpflanzen-bilder.json)",
        "für die Website und den PDF-Build lokal zwischengespeichert. Damit",
        "sind die veröffentlichten Ausgaben unabhängig von externen Bildservern nutzbar.",
        "",
    ]
    for d in media:
        lines.extend([
            "## " + d["name"] + " {#" + d["slug"] + "}",
            "",
            "- **Abgebildete Art:** *" + d["taxon"] + "*",
            "- **Historische Quelle:** " + d["work"] + " (" + d["year"] + ")",
            "- **Autor / Zuschreibung:** " + d["author"] + " (Angaben nach Wikimedia Commons)",
            "- **Dateiseite:** [" + d["commons_filename"] + "](" + commons_page(d["commons_filename"]) + ")",
            "- **Rechtestatus laut Commons:** Public Domain Mark 1.0, gemeinfrei; [" +
              "Lizenzhinweis](https://creativecommons.org/publicdomain/mark/1.0/)",
            "- **Lokale Ausgabedatei:** `" + d["local_path"] + "`",
            "",
        ])
    return "\n".join(lines)


def download(d: dict) -> None:
    target = ROOT / d["local_path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    if check_jpeg(target):
        print("Cached:", target.relative_to(ROOT))
        return
    url = original_file(d["commons_filename"])
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "image/jpeg"})
    error = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=35) as response:
                body = response.read(MAX_JPEG_SIZE + 1)
                if response.headers.get("Content-Type", "").split(";")[0] not in ("image/jpeg", "application/octet-stream"):
                    raise ValueError("Unexpected content type for " + url)
            if not MIN_JPEG_SIZE <= len(body) <= MAX_JPEG_SIZE:
                raise ValueError("Unexpected image size: " + str(len(body)) + " bytes")
            if not body.startswith(b"\xff\xd8") or not body.endswith(b"\xff\xd9"):
                raise ValueError("Invalid JPEG data")
            tmp = target.with_suffix(".part")
            tmp.write_bytes(body)
            tmp.replace(target)
            print("Fetched:", target.relative_to(ROOT), len(body), "bytes")
            return
        except (OSError, ValueError) as exc:
            error = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Could not fetch {d['slug']} from {url}: {error}") from error


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credits-only", action="store_true", help="Write credits without accessing the network")
    ap.add_argument("--verify-only", action="store_true", help="Require all cached image files; do not download")
    args = ap.parse_args()
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    media = data["media"]
    assert len(media) == len({d["slug"] for d in media}), "Duplicate image slug"
    assert len(media) == 12, "Review changed register size"
    CREDITS.parent.mkdir(parents=True, exist_ok=True)
    content = credits_page(media)
    if CREDITS.exists() and CREDITS.read_text(encoding="utf-8") != content:
        # Allow deterministic refresh after updating source metadata.
        CREDITS.write_text(content, encoding="utf-8")
    elif not CREDITS.exists():
        CREDITS.write_text(content, encoding="utf-8")
    if args.credits_only:
        return
    for item in media:
        file_path = ROOT / item["local_path"]
        if args.verify_only:
            if not check_jpeg(file_path):
                raise RuntimeError("Missing or invalid local image: " + str(file_path))
        else:
            download(item)
    print("OK:", len(media), "historical images ready for offline publication")


if __name__ == "__main__":
    main()
