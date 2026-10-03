#!/usr/bin/env python3
"""Run every validator and repository integrity check. Exit 1 on any failure."""
import re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
errors = []

def run(cmd):
    r = subprocess.run([sys.executable] + cmd, cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    last = out[-1] if out else ""
    print(("OK   " if r.returncode == 0 else "FAIL ") + " ".join(cmd) + (f"  -> {last}" if last else ""))
    if r.returncode != 0:
        errors.append(" ".join(cmd) + "\n" + "\n".join(out[-15:]))

for c in (["scripts/generate_catalog.py"], ["scripts/generate_skill_catalog.py"], ["scripts/validate_metadata.py"], ["scripts/validate_catalog.py"],
          ["scripts/check_missing_links.py"], ["scripts/validate_localization.py"], ["scripts/validate_reference.py"],
          ["scripts/validate_content.py"], ["scripts/generate_source_reference.py"], ["scripts/validate_sources.py"], ["scripts/validate_engineering.py"],
          ["training/scripts/validate_dataset.py"], ["tests/core/test_evidence.py"], ["tests/tools/test_calculators.py"],
          ["tests/rag/test_retrieval.py"], ["engines/image_to_cad/tests/test_synthetic.py"]):
    run(c)

def check(name, ok, msg=""):
    print(("OK   " if ok else "FAIL ") + name + (f"  -> {msg}" if msg and not ok else ""))
    if not ok: errors.append(f"{name}: {msg}")

# --- version consistency
ver = (ROOT / "VERSION").read_text().strip()
cl = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
m = re.search(r"^#+\s*v?(\d+\.\d+\.\d+)", cl, re.M)
check("CHANGELOG top entry == VERSION", bool(m) and m.group(1) == ver, f"VERSION={ver}, changelog top={m.group(1) if m else None}")
rd = (ROOT / "README.md").read_text(encoding="utf-8")
check("README mentions current version", f"v{ver}" in rd or ver in rd, f"README lacks {ver}")

# --- skills
bad = []
for d in sorted((ROOT / "skills").iterdir()):
    if not d.is_dir(): continue
    s = (d / "SKILL.md")
    if not s.exists(): bad.append(f"{d.name}: no SKILL.md"); continue
    fm = re.match(r"^---\n(.*?)\n---\n", s.read_text(encoding="utf-8"), re.S)
    meta = dict(l.split(": ", 1) for l in fm.group(1).splitlines() if ": " in l and not l.startswith(" ")) if fm else {}
    if meta.get("name") != d.name: bad.append(f"{d.name}: name != folder ({meta.get('name')})")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", d.name) or len(d.name) > 64: bad.append(f"{d.name}: invalid skill name")
    desc = meta.get("description", "")
    if not desc or len(desc) > 1024: bad.append(f"{d.name}: description missing or >1024 chars")
    for sub in ("examples", "tests"):
        if not any((d / sub).glob("*.md")): bad.append(f"{d.name}: no {sub}/*.md")
check("skills: name/description/examples/tests", not bad, "; ".join(bad[:8]))

# --- knowledge front matter
kb = []
for f in sorted((ROOT / "knowledge").glob("[0-9]*.md")):
    t = f.read_text(encoding="utf-8")
    for k in ("id:", "title:", "category:", "evidence:", "last_reviewed:", "verify_before_release:"):
        if k not in t.split("---", 2)[1]: kb.append(f"{f.name}: missing {k}")
check("knowledge front matter", not kb, "; ".join(kb[:6]))

# --- internal path references in markdown
ROOTS = ("knowledge/", "reference/", "skills/", "training/", "docs/", "catalog/", "prompts/", "scripts/", "templates/", "adapters/", "cases/", "workflows/", "dist/", "tr/", "sources/", "rag/", "agents/", "engines/", "engineering_core/", "schemas/", "tools/")
rx = re.compile(r"`((?:%s)[A-Za-z0-9_./\-]+\.(?:md|csv|jsonl|py|json|yml))`" % "|".join(re.escape(r) for r in ROOTS))
missing = []
SKIP_PARTS = ("XXX", "<", "*", "dist/", "training/export", "training/eval/runs", "chunks.jsonl", "answers.jsonl", "responses.jsonl")
for f in list(ROOT.glob("*.md")) + list((ROOT / "knowledge").glob("*.md")) + list((ROOT / "skills").rglob("*.md")) + \
         list((ROOT / "training").rglob("*.md")) + list((ROOT / "docs").rglob("*.md")) + list((ROOT / "catalog").glob("*.md")) + list((ROOT / "adapters").rglob("*.md")):
    if "releases" in f.parts: continue
    for p in rx.findall(f.read_text(encoding="utf-8")):
        if any(s in p for s in SKIP_PARTS): continue
        if not (ROOT / p).exists() and not (f.parent / p).exists():
            missing.append(f"{f.relative_to(ROOT)} -> {p}")
check("markdown path references resolve", not missing, "; ".join(missing[:10]) + (f" (+{len(missing)-10} more)" if len(missing) > 10 else ""))

# --- empty directories
empties = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_dir() and not any(p.iterdir()) and ".git" not in p.parts]
check("no empty directories", not empties, ", ".join(empties[:8]))

if errors:
    print("\n=== FAILURES ===\n" + "\n\n".join(errors)); sys.exit(1)
print("\nALL CHECKS PASSED")
