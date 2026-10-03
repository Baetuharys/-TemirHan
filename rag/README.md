# Retrieval Layer

`training/rag/chunks.jsonl` is the content corpus. This directory makes it **actually searchable** with a dependency-free BM25 baseline.

```bash
python training/scripts/build_rag_chunks.py
python rag/build_index.py
python rag/retrieve.py "IP65 kapı contası sızıntı yolu" -k 5
```

## Why lexical first?

A transparent baseline is useful for engineering evaluation: it is deterministic, inspectable and works offline. Production deployments can add embeddings and reranking, but the lexical score remains a good fallback and a regression reference.

## Recommended production retrieval

1. Parse query into task/domain/constraints.
2. BM25 retrieve 15–30 chunks.
3. Optional semantic retrieval over the same chunk IDs.
4. Merge with reciprocal-rank fusion.
5. Rerank against the actual engineering question.
6. Keep only chunks with traceable `source` metadata.
7. Answer with evidence labels and cite the file/source IDs used.
8. If retrieval does not support a release-critical claim, mark it `UNKNOWN` or research it; do not fill the gap from model intuition.

`rag/index.json` is generated and may be rebuilt at any time.
