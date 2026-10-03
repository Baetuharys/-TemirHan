#!/usr/bin/env python3
"""Generate a human/RAG readable source registry from sources/registry.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "sources/registry.json").read_text(encoding="utf-8"))
rows = [
    "# External Source Registry (generated — do not edit)",
    "",
    f"Reviewed: {data.get('reviewed_on', '')}",
    "",
    data.get("policy", ""),
    "",
    "| ID | Organization | Status | Edition/version | Title | Official URL |",
    "|---|---|---|---|---|---|",
]
for s in data["sources"]:
    ev = s.get("edition") or s.get("version") or ""
    title = s["title"].replace("|", "/")
    rows.append(f"| `{s['id']}` | {s['organization']} | {s['status']} | {ev} | {title} | {s['url']} |")
rows += ["", "## Lifecycle notes", ""]
for s in data["sources"]:
    if s.get("note"):
        rows.append(f"- **{s['id']}** — {s['note']}")
(ROOT / "sources/registry.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Generated sources/registry.md ({len(data['sources'])} records)")
