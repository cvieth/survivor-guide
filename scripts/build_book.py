#!/usr/bin/env python3
"""Build screen or print PDF from the MkDocs navigation order."""
from pathlib import Path
import argparse
import posixpath
import re
import subprocess
import yaml
from decision_blocks import render_latex

ROOT=Path(__file__).resolve().parent.parent
DOCS=ROOT/"docs"

def flatten(node):
    if isinstance(node,list):
        for item in node: yield from flatten(item)
    elif isinstance(node,dict):
        for label,value in node.items():
            if isinstance(value,str): yield label,value
            else: yield from flatten(value)

def chapter_id(path):
    return "chapter-"+re.sub(r"[^a-z0-9]+","-",path.lower()).strip("-")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True)
    parser.add_argument("--format",choices=["screen","print"],default="screen")
    args=parser.parse_args()
    conf=yaml.safe_load((ROOT/"mkdocs.yml").read_text(encoding="utf-8"))
    chapters=list(flatten(conf["nav"]))
    destinations={path:chapter_id(path) for _,path in chapters}
    parts=["---\ntitle: 'SURVIVOR GUIDE'\nsubtitle: 'Das offene Handbuch für Krisenbewältigung, Überleben und Wiederaufbau'\nlang: de-DE\n---\n\n"]
    for label,page in chapters:
        body=(DOCS/page).read_text(encoding="utf-8")
        body=re.sub(r"\A\s*#\s+[^\n]+\n","",body,count=1)
        # Nach dem Zusammenführen müssen Bildpfade relativ zu docs/ gelten.
        def images(m):
            alt, target, attrs = m.group(1), m.group(2), m.group(3) or ""
            if target.startswith(("http:", "https:", "data:", "/")):
                return m.group(0)
            new_target = posixpath.normpath(posixpath.join(posixpath.dirname(page), target))
            return "![" + alt + "](" + new_target + ")" + attrs
        body=re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)(\{[^}\n]*\})?', images, body)
        def callout(m):
            lines=[line[4:] for line in m.group(2).rstrip("\n").splitlines()]
            return "> **"+m.group(1)+"**\n>\n"+"\n".join("> "+line for line in lines)+"\n\n"
        body=re.sub(r'(?m)^!!!\s+\w+\s+"([^"]+)"\s*\n((?:[ ]{4}[^\n]*\n?)+)',callout,body)
        def links(m):
            title,target=m.group(1),m.group(2)
            if target.startswith(("http:","https:","mailto:","#","/")): return m.group(0)
            dest=posixpath.normpath((Path(page).parent/target.split("#",1)[0]).as_posix())
            if dest in destinations:return "["+title+"](#"+destinations[dest]+")"
            if target=="downloads/survivor-guide.pdf":return title
            return m.group(0)
        body=re.sub(r"(?<!!)\[([^\]]+)\]\(([^\s)]+)\)",links,body)
        body=render_latex(body, print_layout=(args.format=="print"))
        parts.append("# "+label+" {#"+destinations[page]+"}\n\n"+body.strip()+"\n\n\\newpage\n\n")
    build=ROOT/"build"
    build.mkdir(exist_ok=True)
    assembled=build/"survivor-guide-assembled.md"
    assembled.write_text("".join(parts),encoding="utf-8")
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    cmd=["pandoc",str(assembled),"-f","markdown+yaml_metadata_block","--resource-path",str(DOCS),"--pdf-engine=xelatex","-H",str(ROOT/"templates/decision-boxes.tex"),"--toc","--toc-depth=1","-V","mainfont=DejaVu Sans","-V","fontsize=10pt","-V","colorlinks=true","-V","linkcolor=teal","-V","urlcolor=teal","-o",str(out)]
    if args.format=="screen":cmd+=["-V","papersize=a4","-V","geometry:margin=20mm"]
    else:cmd+=["-H",str(ROOT/"templates/decision-boxes-print.tex"),"-V","classoption=twoside","-V","geometry:paperwidth=6in","-V","geometry:paperheight=9in","-V","geometry:inner=0.85in","-V","geometry:outer=0.65in","-V","geometry:top=0.7in","-V","geometry:bottom=0.7in"]
    subprocess.run(cmd,cwd=ROOT,check=True)
    print("Created:",out)

if __name__=="__main__":
    main()
