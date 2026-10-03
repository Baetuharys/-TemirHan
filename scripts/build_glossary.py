#!/usr/bin/env python3
"""Regenerate reference/glossary-sacmetal.md from reference/glossary.csv."""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / "reference/glossary.csv").open(encoding="utf-8")))
cats = []
for r in rows:
    if r["category"] not in cats:
        cats.append(r["category"])
out = ["# Sacmetal ve Mühendislik Sözlüğü (EN ↔ TR)", "",
       "Kaynak veri: `reference/glossary.csv` (bu dosya `scripts/build_glossary.py` ile üretilir; elle düzenleme).", "",
       "**Okuma kuralı.** \"Atölye terimi\" sütunu yaygın kullanılan Türkçe karşılıktır. SolidWorks arayüz etiketleri bu sözlükte **iddia edilmez**; etiketler için `reference/solidworks-ui-labels.csv` ve `knowledge/04-solidworks-turkish-ui-and-terminology.md` kullanılır. Terim seçim sırası: `docs/terminology-policy.md`.", ""]
for c in cats:
    out += [f"## {c}", "", "| EN | TR (atölye/yaygın) | Not |", "|---|---|---|"]
    out += [f"| {r['en']} | {r['tr_shop']} | {r['note']} |" for r in rows if r["category"] == c]
    out.append("")
(ROOT / "reference/glossary-sacmetal.md").write_text("\n".join(out), encoding="utf-8")
print(f"Generated glossary ({len(rows)} terms)")
