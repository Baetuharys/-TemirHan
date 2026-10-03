#!/usr/bin/env python3
"""Generate catalog/skills.md from skills/*/SKILL.md (name + description)."""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
rows = []
for d in sorted((ROOT / "skills").iterdir()):
    s = d / "SKILL.md"
    if not s.exists(): continue
    fm = re.match(r"^---\n(.*?)\n---\n", s.read_text(encoding="utf-8"), re.S).group(1)
    meta = dict(l.split(": ", 1) for l in fm.splitlines() if ": " in l and not l.startswith(" "))
    n_ex = len(list((d / "examples").glob("*.md"))); n_t = len(list((d / "tests").glob("*.md")))
    rows.append((d.name, meta.get("status", ""), meta.get("version", ""), meta.get("description", ""), n_ex, n_t))
out = ["# Skill Catalog (generated — do not edit)", "",
       f"{len(rows)} skills. Source: `skills/*/SKILL.md`. Regenerate with `python scripts/generate_skill_catalog.py`.", "",
       "| Skill | Status | Version | Description | Ex. | Tests |", "|---|---|---|---|---|---|"]
for n, st, v, de, e, t in rows:
    out.append(f"| `{n}` | {st} | {v} | {de.replace('|','/')} | {e} | {t} |")
(ROOT / "catalog/skills.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"Generated catalog/skills.md ({len(rows)} skills)")
