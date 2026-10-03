# Training, Retrieval and Evaluation Guide

The goal is not to make an AI sound like an engineer; it is to make it **behave predictably around evidence, calculations, uncertainty and release decisions**.

## Use the lightest mechanism that solves the problem
| Level | Purpose | Repository |
|---|---|---|
| 1. System prompt + skills | Behavior, workflow, abstention, routing | `training/system-prompts/`, `skills/` |
| 2. Knowledge + retrieval | Facts, explanations, source-linked context | `knowledge/`, `reference/`, `sources/`, `rag/` |
| 3. Deterministic tools | Arithmetic and repeatable transformations | `tools/`, `engineering_core/`, `engines/` |
| 4. Fine-tuning | Persistent behavior/style gaps only | `training/datasets/` |

Facts should normally **not** be frozen into a fine-tune. Update knowledge/source metadata and retrieval instead.

## Current seed assets (v3.0.0)
- **47 SFT** examples.
- **20 preference** pairs.
- **63 eval** cases.
- **49 gold responses** for harness regression; 14 eval cases intentionally require future/manual/model responses.
- **263 RAG chunks** in the current generated build (rebuild after knowledge edits).

Counts are validated by `python training/scripts/validate_dataset.py`; generated RAG counts may change as the library grows.

## Retrieval
```bash
python training/scripts/build_rag_chunks.py
python rag/build_index.py
python rag/retrieve.py "IP65 gasket latch compression" -k 5
```
The included retrieval baseline is local BM25 with no external service. It is transparent and works offline. A semantic embedding/reranker can be added later, but must be evaluated against the same cases rather than assumed better.

## Evaluation
```bash
python training/scripts/run_eval.py --template answers.jsonl
# run the prompts through the target AI and put responses in the file
python training/scripts/run_eval.py --responses answers.jsonl

# harness self-test with supplied gold subset
python training/scripts/run_eval.py --responses training/eval/gold-sample-responses.jsonl --min-pass 1.0
```
Automatic regex/number checks catch gross failures only. The human rubric remains important for engineering quality.

## Fine-tuning
Use only when prompt + knowledge/retrieval + tools still show a stable behavior gap. Keep eval prompts out of training data. Anonymize all examples and never train on customer/confidential data. Provider model availability changes; check current provider documentation before committing to a tuning workflow.

## Provider packs
Run:
```bash
python scripts/mai.py rebuild
```
Generated outputs include:
- compact ChatGPT knowledge pack;
- full and compact Claude Project knowledge packs;
- one Claude skill ZIP per skill;
- provider-neutral source files remain the source of truth.

## Data governance
See `DATA-GOVERNANCE.md` and `docs/KNOWLEDGE-GOVERNANCE.md`. Every release-relevant value should be traceable to supplied/project data, deterministic calculation, a named source, or a clearly labelled assumption/estimate.
