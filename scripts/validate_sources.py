#!/usr/bin/env python3
"""Validate source registry shape and high-risk lifecycle notes."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "sources/registry.json"
try:
    data = json.loads(p.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERROR: cannot read {p}: {e}")
    sys.exit(1)

errs = []
ids = set()
urls = set()
for i, s in enumerate(data.get("sources", []), 1):
    for k in ("id", "type", "organization", "title", "status", "url", "use_for"):
        if k not in s or s[k] in ("", None, []):
            errs.append(f"row {i}: missing {k}")
    sid = s.get("id")
    if sid in ids:
        errs.append(f"duplicate id: {sid}")
    ids.add(sid)
    url = s.get("url", "")
    if url in urls:
        errs.append(f"duplicate url: {url}")
    urls.add(url)
    if url and not url.startswith("https://"):
        errs.append(f"{sid}: non-https url")
if errs:
    print("\n".join("ERROR: " + e for e in errs))
    sys.exit(1)
watch = [
    s["id"] for s in data["sources"]
    if any(x in s["status"] for x in ("draft", "under-publication", "pending-replacement", "to-be-revised"))
]
print(f"OK: {len(ids)} source records; lifecycle-watch={len(watch)}" + (f" ({', '.join(watch)})" if watch else ""))
