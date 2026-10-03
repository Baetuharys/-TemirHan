#!/usr/bin/env python3
"""Validate reference CSV files. A UI label may be level V only with version and source."""
import csv, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
errs = []
ui = list(csv.DictReader((ROOT / "reference/solidworks-ui-labels.csv").open(encoding="utf-8")))
for i, r in enumerate(ui, 2):
    lv = r["level"].strip()
    if lv not in {"V", "C", "U"}:
        errs.append(f"ui-labels row {i}: level must be V, C or U")
    if lv == "V" and not (r["sw_version"].strip() and r["source"].strip() and r["tr_label"].strip()):
        errs.append(f"ui-labels row {i}: level V needs tr_label, sw_version and source")
    if lv == "U" and r["tr_label"].strip():
        errs.append(f"ui-labels row {i}: level U must not carry a Turkish label (use C or V after evidence)")
gl = list(csv.DictReader((ROOT / "reference/glossary.csv").open(encoding="utf-8")))
seen = set()
for i, r in enumerate(gl, 2):
    k = (r["category"], r["en"].lower())
    if k in seen:
        errs.append(f"glossary row {i}: duplicate {k}")
    seen.add(k)
    if not r["en"].strip() or not r["tr_shop"].strip():
        errs.append(f"glossary row {i}: empty term")
if errs:
    print("\n".join(errs)); sys.exit(1)
print(f"OK: {len(ui)} UI-label rows, {len(gl)} glossary rows")
