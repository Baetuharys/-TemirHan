#!/usr/bin/env python3
"""Build Claude-uploadable skill packages and Project knowledge.

Output (generated, never edit by hand):
  dist/claude-skills/<name>.zip            one ZIP per skill: <name>/SKILL.md (+ references/)
  dist/claude-project-knowledge/*          files to upload to a Claude Project

SKILL.md in the package keeps only `name` and `description` in the front matter and rewrites
repository paths (knowledge/..., reference/...) to the bundled references/ folder.
"""
import re, shutil, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SK = DIST / "claude-skills"
PK = DIST / "claude-project-knowledge"
CPK = DIST / "claude-project-compact"
for d in (SK, PK, CPK):
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)

REF = re.compile(r"(?<![\w/])((?:knowledge|reference|sources)/[A-Za-z0-9_.\-]+\.(?:md|csv|json))")

def split(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l and not l.startswith(" "))
    return meta, m.group(2)

count = 0
for sd in sorted((ROOT / "skills").iterdir()):
    sm = sd / "SKILL.md"
    if not sm.exists(): continue
    meta, body = split(sm.read_text(encoding="utf-8"))
    name, desc = meta["name"], meta["description"]
    refs = {}
    def repl(m):
        rel = m.group(1)
        src = ROOT / rel
        if src.exists():
            refs[rel] = src
            return "references/" + src.name
        return rel
    body = REF.sub(repl, body)
    body = body.replace("Paths are relative to the repository root.", "Reference files are bundled in `references/`.")
    body = body.replace("`workflows/default-workflow.md`", "`references/workflows-default-workflow.md`")
    body = body.replace("`examples/example.md`", "`references/examples-example.md`")
    body = body.replace(", `tests/smoke.md`", "")
    out = f"---\nname: {name}\ndescription: {desc}\n---\n{body}"
    zpath = SK / f"{name}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{name}/SKILL.md", out)
        for rel, src in sorted(refs.items()):
            z.write(src, f"{name}/references/{src.name}")
        for sub in ("workflows", "examples"):
            for f in sorted((sd / sub).glob("*.md")) if (sd / sub).exists() else []:
                z.write(f, f"{name}/references/{sub}-{f.name}")
    count += 1

# Project knowledge: topic files + key reference/source files
for f in sorted((ROOT / "knowledge").glob("[0-9]*.md")):
    shutil.copy(f, PK / f.name)
for n in ("glossary-sacmetal.md", "standards-map.md", "ip-codes.md", "sheet-metal-formulas.md", "solidworks-ui-labels.csv"):
    p = ROOT / "reference" / n
    if p.exists(): shutil.copy(p, PK / n)
for rel in ("sources/registry.md", "sources/README.md"):
    p = ROOT / rel
    if p.exists(): shutil.copy(p, PK / p.name)
# Compact Project pack: reuse thematic bundles generated for ChatGPT, but use Claude instructions.
chat_pack = DIST / "chatgpt-knowledge"
if chat_pack.exists():
    for f in chat_pack.iterdir():
        if f.name != "00-INSTRUCTIONS-COPY.txt" and f.is_file(): shutil.copy(f, CPK / f.name)
(CPK / "00-INSTRUCTIONS-COPY.txt").write_text((ROOT / "training/system-prompts/claude-project-instructions.md").read_text(encoding="utf-8"), encoding="utf-8")
print(f"Built {count} skill ZIPs; {len(list(PK.iterdir()))} full Project files; {len(list(CPK.iterdir()))} compact Project files")
