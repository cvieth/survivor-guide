"""Read the subset of mkdocs.yml consumed by the book and validation scripts.

MkDocs itself resolves !!python/name extension handlers through its own loader.
The scripts only need plain data (primarily nav), so that explicit known handler
tag is replaced with an inert string instead of loading arbitrary Python code.
"""
from pathlib import Path
import yaml


class _MkDocsSafeLoader(yaml.SafeLoader):
    pass


_MERMAID_FENCE_TAG = (
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format"
)
_MkDocsSafeLoader.add_constructor(
    _MERMAID_FENCE_TAG, lambda loader, node: "pymdownx.superfences.fence_code_format"
)


def load_mkdocs_config(path: Path) -> dict:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_MkDocsSafeLoader)
