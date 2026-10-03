#!/usr/bin/env python3
"""Flag files that are still boilerplate stubs. Warn by default; fail with --strict."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
MARKERS = [
    "Reusable workflow blueprint for",
    "Intake the request and identify the required output.",
    "Identify the task, constraints, missing information, and assumptions before acting.",
    "Prompt: Perform a preliminary",
    "This skill covers",          # generic scope.md line
    "TODO",
    "Yeniden kullanılabilir iş akışı taslağı:",
]
GROUPS = {"prompts": "prompts", "tr": "tr/prompts", "skills": "skills"}
total = 0; report = {}
for g, d in GROUPS.items():
    for f in sorted((ROOT / d).rglob("*.md")):
        total += 1
        text = f.read_text(encoding="utf-8")
        hits = [m for m in MARKERS if m in text]
        if hits: report.setdefault(g, []).append(f.relative_to(ROOT))
n = sum(len(v) for v in report.values())
if not n:
    print(f"OK: no stub markers in {total} files"); sys.exit(0)
print(f"WARN: {n}/{total} files contain stub markers")
for g, items in report.items():
    print(f"  [{g}] {len(items)}")
    for it in items[:40]: print(f"    - {it}")
sys.exit(1 if "--strict" in sys.argv else 0)
