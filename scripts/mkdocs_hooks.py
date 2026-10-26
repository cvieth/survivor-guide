"""MkDocs hook for Markdown decision diagrams."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from decision_blocks import render_html

def on_page_markdown(markdown, page, config, files):
    return render_html(markdown)
