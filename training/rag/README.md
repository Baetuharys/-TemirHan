# RAG Notes

- `chunks.jsonl` is generated: `python training/scripts/build_rag_chunks.py` (never edit by hand).
- Chunk size ≈ 2200 characters; split at `##` headings; tables and code fences are not split; each chunk starts with `Title › Section`.
- Retrieval tips: embed `text`; filter on `category` when the task family is known (e.g. `enclosures`, `sheet-metal`, `gdt`); return `source` + `section` so the answer can cite `knowledge/05 › Leakage paths`.
- Keep Turkish and English terms in the same chunks (the knowledge files already do) — multilingual embeddings handle this well; test with Turkish queries such as "büküm payı" and "IP65 kablo girişi".
- Re-run after every knowledge change; commit the regenerated file.
- Do not index customer data (see `../DATA-GOVERNANCE.md`).
