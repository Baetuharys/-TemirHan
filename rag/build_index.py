#!/usr/bin/env python3
"""Build a dependency-free BM25 index from training/rag/chunks.jsonl."""
from pathlib import Path
from collections import Counter
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rag.tokenize import tokens


def build(chunks_path=None, out_path=None):
    chunks_path = Path(chunks_path or ROOT / "training/rag/chunks.jsonl")
    out_path = Path(out_path or ROOT / "rag/index.json")
    docs = []
    df = Counter()
    for n, line in enumerate(chunks_path.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        r = json.loads(line)
        text = r.get("text") or r.get("content") or r.get("chunk") or ""
        toks = tokens(text)
        tf = Counter(toks)
        for term in tf:
            df[term] += 1
        docs.append({
            "id": r.get("id", f"chunk-{n+1:04d}"),
            "source": r.get("source"),
            "title": r.get("title"),
            "section": r.get("section"),
            "category": r.get("category"),
            "evidence": r.get("evidence"),
            "text": text,
            "len": len(toks),
            "tf": dict(tf),
        })
    avg = sum(d["len"] for d in docs) / max(len(docs), 1)
    idx = {
        "version": 1,
        "method": "BM25",
        "k1": 1.5,
        "b": 0.75,
        "doc_count": len(docs),
        "avgdl": avg,
        "df": dict(df),
        "docs": docs,
    }
    out_path.write_text(json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Built {out_path.relative_to(ROOT)}: {len(docs)} docs, {len(df)} terms")
    return idx


if __name__ == "__main__":
    build()
