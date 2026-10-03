# Release v2.0.0 — Consolidation and Training Release

## Why v2.0.0
The 16 archives supplied (ChatGPT line v0.1 → v1.3, ChatGPT v0.3.0 variants, Claude line v0.9) were audited. Findings:

| Finding in v1.3.0 | Consequence | Resolution in v2.0.0 |
|---|---|---|
| `knowledge/` empty at repository root | The "library" had no facts, only prompts | 15 knowledge files + reference data |
| 8 modules were empty skeletons, 8 blueprints were stubs | Skills inherited generic text | Real content, EN + TR |
| 10 of 22 skills used one generic template body | No domain behaviour | Rewritten from blueprints with failure modes, examples, tests |
| Claude-line assets (IP codes, formulas, standards map, glossary, cost/IP/image modules) absent from v1.x | Best content lost during the line switch | Restored and extended |
| `VERSION` 1.2.0 vs README 1.1.0, CHANGELOG out of order | Unreliable release state | Single version, enforced by `validate_all.py` |
| No training assets | Nothing to "train an AI" with | `training/` (prompts, SFT, DPO, eval, RAG, governance) |
| Claude-Skills front matter (`name`/`description`) absent or Turkish-only | Poor triggering | Bilingual descriptions for all 32 skills |
| Existing validators only checked structure | Empty content passed | Content/stub validator, dataset validator, path checker |

## What was merged
Structure and MergenHan compatibility from the ChatGPT line v1.3.0 · concrete content and reference data from the Claude line v0.9.0 · all earlier archives were diffed file-by-file against these two: the only unique content found was a quotation blueprint in one v0.3.0 variant, whose checks and test cases were merged into `quotation-generator`; the rest were generated files and caches.

## Verification performed
All validators pass (`python scripts/validate_all.py`); eval harness self-test 31/31 gold responses; every numeric example recomputed by code. The ISO 2768-1 tables, IK/IP tables and other standard-derived values were reviewed from general knowledge only — no copy of the standards was available — so **verify them against the standards before sending anything to customers**.

## Not done (needs the owner)
Real Turkish SolidWorks label capture · shop capability data · real model eval runs for Claude and ChatGPT · LICENSE · fine-tuning runs.
