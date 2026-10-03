#!/usr/bin/env python3
"""Resolve depends_on recursively and print one paste-ready prompt.
Usage: python scripts/compose_prompt.py <id> [--lang en|tr] [--with-master]"""
from pathlib import Path
import argparse, re, sys
ROOT = Path(__file__).resolve().parents[1]

def index(lang):
    base = ROOT / ("tr/prompts" if lang == "tr" else "prompts")
    out = {}
    for f in base.rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        m = re.search(r"^id:\s*(\S+)", t, re.M)
        if m:
            out[m.group(1)] = (f, t)
    return out

def deps(text):
    m = re.search(r"^depends_on:\s*\[(.*?)\]", text, re.M)
    return [x.strip() for x in m.group(1).split(",") if x.strip()] if m else []

def body(text):
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) == 3 else text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--with-master", action="store_true")
    a = ap.parse_args()
    idx = index(a.lang)
    if a.id not in idx:
        sys.exit(f"Unknown id: {a.id}")
    order, seen = [], set()
    def visit(i):
        if i in seen or i not in idx:
            return
        seen.add(i)
        for d in deps(idx[i][1]):
            visit(d)
        order.append(i)
    if a.with_master:
        visit("mai-master-mechanical-ai-library-orchestrator")
    visit(a.id)
    chunks = [f"<!-- {i} -->\n{body(idx[i][1])}" for i in order]
    print("\n\n".join(chunks))

if __name__ == "__main__":
    main()
