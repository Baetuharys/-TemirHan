#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rag.tokenize import tokens


def load_index(path=None):
    p = Path(path or ROOT / "rag/index.json")
    if not p.exists():
        from rag.build_index import build
        return build(out_path=p)
    return json.loads(p.read_text(encoding="utf-8"))


def search(query, k=5, category=None, index=None):
    idx = index or load_index()
    n_docs = idx["doc_count"]
    avg = idx["avgdl"] or 1
    k1 = idx["k1"]
    b = idx["b"]
    q = tokens(query)
    scores = []
    for d in idx["docs"]:
        if category and d.get("category") != category:
            continue
        score = 0.0
        for term in q:
            tf = d["tf"].get(term, 0)
            if not tf:
                continue
            df = idx["df"].get(term, 0)
            idf = math.log(1 + (n_docs - df + 0.5) / (df + 0.5))
            denom = tf + k1 * (1 - b + b * d["len"] / avg)
            score += idf * (tf * (k1 + 1)) / denom
        meta = " ".join(str(d.get(x) or "") for x in ("title", "section", "category")).lower()
        score += sum(0.15 for term in q if term in meta)
        if score > 0:
            scores.append((score, d))
    scores.sort(key=lambda x: x[0], reverse=True)
    return [
        {
            "score": round(score, 4),
            **{key: d.get(key) for key in ("id", "source", "title", "section", "category", "evidence", "text")},
        }
        for score, d in scores[:k]
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-k", type=int, default=5)
    ap.add_argument("--category")
    a = ap.parse_args()
    for r in search(a.query, a.k, a.category):
        print(f"[{r['score']}] {r['source']} :: {r['section'] or r['title']}")
        print((r["text"] or "")[:500].replace("\n", " "))
        print()


if __name__ == "__main__":
    main()
