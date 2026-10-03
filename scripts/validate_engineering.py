#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errs = []
reg = json.loads((ROOT / "sources/registry.json").read_text(encoding="utf-8"))
source_ids = {x["id"] for x in reg["sources"]}
for f in sorted((ROOT / "knowledge").glob("[0-9]*.md")):
    t = f.read_text(encoding="utf-8")
    fm = t.split("---", 2)[1] if t.startswith("---") else ""
    m = re.search(r"^source_ids:\s*\[(.*?)\]\s*$", fm, re.M)
    if m:
        ids = [x.strip() for x in m.group(1).split(",") if x.strip()]
        for sid in ids:
            if sid not in source_ids:
                errs.append(f"{f.name}: unknown source_id {sid}")
for rel in [
    "engineering_core/evidence.py",
    "schemas/sheet-metal-part.schema.json",
    "rag/retrieve.py",
    "engines/image_to_cad/pipeline.py",
    "agents/orchestrator.md",
    "tools/calculators/engineering_calc.py",
    "project-profiles/example-fabricator-profile.json",
    "design_patterns/enclosures/README.md",
    "docs/DESIGN-HELP.md",
]:
    if not (ROOT / rel).exists():
        errs.append(f"missing required v3 component: {rel}")
try:
    profile = json.loads((ROOT / "project-profiles/example-fabricator-profile.json").read_text(encoding="utf-8"))
    if not profile.get("profile_id") or profile.get("units") not in ("mm", "inch"):
        errs.append("invalid example fabricator profile")
except Exception as e:
    errs.append(f"cannot read example fabricator profile: {e}")
if len(list((ROOT / "knowledge").glob("[0-9]*.md"))) < 30:
    errs.append("v3 requires at least 30 numbered knowledge topics")
if len([p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists()]) < 46:
    errs.append("v3 requires at least 46 skills")

if errs:
    print("\n".join("ERROR: " + x for x in errs))
    sys.exit(1)
print(f"OK: engineering architecture; {len(source_ids)} registered sources")
