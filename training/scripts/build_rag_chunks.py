#!/usr/bin/env python3
"""Build RAG chunks (JSONL) from knowledge/, reference/ and docs/terminology-policy.md.

Chunks are split at '##' headings, keep the document title as a breadcrumb, and carry metadata
(source path, section, category, evidence, last_reviewed). Tables are never split.
Output: training/rag/chunks.jsonl
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
MAX = 2200  # characters per chunk (about 550 tokens)
OUT = ROOT / "training/rag/chunks.jsonl"

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text

def split_blocks(body):
    """Split into paragraph blocks keeping tables/code fences together."""
    blocks, cur, in_code = [], [], False
    for line in body.split("\n"):
        if line.startswith("```"): in_code = not in_code
        if not in_code and not line.strip():
            if cur: blocks.append("\n".join(cur)); cur = []
        else:
            cur.append(line)
    if cur: blocks.append("\n".join(cur))
    return blocks

def chunks_for(path):
    text = path.read_text(encoding="utf-8")
    meta, body = fm(text)
    title = meta.get("title") or (re.search(r"^# (.+)$", body, re.M) or [None, path.stem])[1]
    parts = re.split(r"(?m)^## ", body)
    pre, secs = parts[0], parts[1:]
    out = []
    items = [("Overview", pre)] + [(s.split("\n", 1)[0].strip(), s.split("\n", 1)[1] if "\n" in s else "") for s in secs]
    for sec, content in items:
        content = content.strip()
        if len(content) < 40: continue
        buf = ""
        pieces = []
        for b in split_blocks(content):
            if len(buf) + len(b) + 2 > MAX and buf:
                pieces.append(buf); buf = b
            else:
                buf = (buf + "\n\n" + b) if buf else b
        if buf: pieces.append(buf)
        for n, p in enumerate(pieces, 1):
            out.append({
                "id": f"{path.relative_to(ROOT).as_posix()}#{re.sub(r'[^a-z0-9]+','-',sec.lower()).strip('-')}-{n}",
                "source": path.relative_to(ROOT).as_posix(),
                "title": title, "section": sec,
                "category": meta.get("category", path.parent.name),
                "evidence": meta.get("evidence", ""),
                "last_reviewed": meta.get("last_reviewed", ""),
                "text": f"{title} › {sec}\n\n{p}",
            })
    return out

def main():
    files = sorted((ROOT / "knowledge").glob("*.md")) + sorted((ROOT / "reference").glob("*.md")) + [ROOT / "docs/terminology-policy.md", ROOT / "sources/README.md", ROOT / "sources/registry.md", ROOT / "docs/maturity-model.md"]
    files = [f for f in files if f.name != "README.md" and f.exists()]
    rows = []
    for f in files: rows += chunks_for(f)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for r in rows: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Wrote {len(rows)} chunks from {len(files)} files -> {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
