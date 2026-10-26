"""Shared Markdown decision blocks rendered for MkDocs, PDF and book."""
from dataclasses import dataclass
from html import escape
import re
import shlex
import subprocess
import yaml

START = re.compile(r"^::: decision\s*$")
ANSWER = re.compile(r"^::: answer\s+(.+?)\s*$")
END = "::: enddecision"
KINDS = {"danger", "protect", "neutral"}

@dataclass
class Answer:
    kind: str
    choice: str
    title: str
    body: str

@dataclass
class Decision:
    label: str
    question: str
    hint: str
    answers: list[Answer]

def parse_blocks(source):
    lines = source.splitlines()
    parts, raw, i = [], [], 0
    fence = None
    while i < len(lines):
        line = lines[i]
        fm = re.match(r"^\s{0,3}(\x60{3,}|~{3,})", line)
        if fm:
            marker = fm.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
        if fence is None and START.match(line):
            if raw:
                parts.append(("\n".join(raw), False))
                raw = []
            begin, metadata, answers = i + 1, [], []
            i += 1
            while i < len(lines) and lines[i] != END:
                am = ANSWER.match(lines[i])
                if am:
                    try:
                        args = shlex.split(am.group(1))
                    except ValueError as exc:
                        raise ValueError(f"Zeile {i+1}: {exc}") from exc
                    if len(args) != 3 or args[0] not in KINDS:
                        raise ValueError(f"Zeile {i+1}: Erwartet ::: answer <danger|protect|neutral> \"JA\" \"Titel\"")
                    i += 1
                    body = []
                    while i < len(lines) and lines[i] != END and not ANSWER.match(lines[i]):
                        if START.match(lines[i]):
                            raise ValueError(f"Zeile {i+1}: Verschachtelte Entscheidung")
                        body.append(lines[i])
                        i += 1
                    if not "\n".join(body).strip():
                        raise ValueError(f"Zeile {i+1}: Leere Antwort")
                    answers.append(Answer(*args, "\n".join(body).strip()))
                elif answers:
                    raise ValueError(f"Zeile {i+1}: Text außerhalb einer Antwort")
                else:
                    metadata.append(lines[i])
                    i += 1
            if i >= len(lines):
                raise ValueError(f"Zeile {begin}: ::: enddecision fehlt")
            try:
                meta = yaml.safe_load("\n".join(metadata))
            except yaml.YAMLError as exc:
                raise ValueError(f"Zeile {begin}: YAML ungültig: {exc}") from exc
            if not isinstance(meta, dict) or not isinstance(meta.get("question"), str) or not meta["question"].strip():
                raise ValueError(f"Zeile {begin}: question: erforderlich")
            if not 2 <= len(answers) <= 3:
                raise ValueError(f"Zeile {begin}: Zwei oder drei Antworten erforderlich")
            parts.append((Decision(str(meta.get("label", "ENTSCHEIDUNG")), meta["question"],
                                   str(meta.get("hint", "")), answers), True))
        elif fence is None and (line == END or ANSWER.match(line)):
            raise ValueError(f"Zeile {i+1}: Entscheidungsmarkierung außerhalb eines Blocks")
        else:
            raw.append(line)
        i += 1
    if raw:
        parts.append(("\n".join(raw), False))
    return parts

def render_html(source):
    import markdown
    output = []
    for item, is_decision in parse_blocks(source):
        if not is_decision:
            output.append(item)
            continue
        cards = []
        for ans in item.answers:
            body = markdown.markdown(ans.body, extensions=["extra", "admonition", "pymdownx.superfences"])
            cards.append(
                f'<section class="sg-decision__answer sg-decision__answer--{ans.kind}">'
                f'<div class="sg-decision__choice">{escape(ans.choice)}</div>'
                f'<h3>{escape(ans.title)}</h3>{body}</section>'
            )
        output.append(
            '<div class="sg-decision" role="group" aria-label="Entscheidungsbaum">'
            '<div class="sg-decision__question">'
            f'<div class="sg-decision__label">{escape(item.label)}</div>'
            f'<div class="sg-decision__prompt">{escape(item.question)}</div>'
            + (f'<p>{escape(item.hint)}</p>' if item.hint else '')
            + '</div><div class="sg-decision__arrow" aria-hidden="true">↓</div>'
            + f'<div class="sg-decision__answers">{"".join(cards)}</div></div>'
        )
    return "\n\n".join(output)

def latex_inline(text):
    return subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--wrap=none"],
                          input=text, text=True, capture_output=True, check=True).stdout.strip()

def render_latex(source, *, print_layout=False):
    output = []
    for item, is_decision in parse_blocks(source):
        if not is_decision:
            output.append(item)
            continue
        question = (
            f"\\begin{{sgdecisionquestion}}\n\\raggedright\n\\textbf{{{latex_inline(item.label)}}}\\par\n"
            f"\\medskip\n{{\\large\\bfseries {latex_inline(item.question)}}}\\par\n"
        )
        if item.hint:
            question += "\\smallskip\n" + latex_inline(item.hint) + "\n"
        output.append(question + "\\end{sgdecisionquestion}\n\\begin{center}$\\Downarrow$\\end{center}")
        side = not print_layout and len(item.answers) == 2
        cards = []
        for ans in item.answers:
            style = {"danger": "sgdecisiondanger", "protect": "sgdecisionprotect",
                     "neutral": "sgdecisionneutral"}[ans.kind]
            cards.append(
                f"\\begin{{tcolorbox}}[{style}{'' if side else ',breakable'},title={{{latex_inline(ans.choice)}}}]\n"
                f"\\raggedright\n\\textbf{{{latex_inline(ans.title)}}}\\par\n\\smallskip\n"
                f"{latex_inline(ans.body)}\n\\end{{tcolorbox}}"
            )
        if side:
            # No blank line between cells, otherwise they occupy separate rows.
            output.append("\\begin{tcbraster}[raster columns=2,raster equal height,raster column skip=3mm]\n"
                          + "\n".join(cards) + "\n\\end{tcbraster}")
        else:
            output.append("\n\n".join(cards))
    return "\n\n".join(output)
