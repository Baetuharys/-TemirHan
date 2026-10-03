# Changelog

## 3.0.0 — 2026-10-02

Professional consolidation release built from the three supplied repositories. SV2 is the base; unique Claude-v2 engineering/tooling assets were salvaged; the Image→CAD scaffold was converted into an executable first-pass engine.

### Added — engineering platform
- Shared evidence/data model and release validation in `engineering_core/` + JSON schemas.
- Official-source provenance registry, lifecycle validation and generated source reference.
- Deterministic calculators for bending, mass, cost, tolerances, thermal airflow, gasket compression and simple beam sanity checks.
- Real offline BM25 RAG build/retrieval path instead of chunk generation only.
- Executable Image→CAD 2D pipeline: preprocessing, line/circle detection, scale/perspective utilities, constraint inference, JSON/SVG/DXF export and synthetic regression.
- Agent/orchestrator/verification layer and end-to-end design/release workflows.
- Project/fabricator profiles so real shop capability overrides generic heuristics.
- Enclosure and sheet-metal design pattern cards.

### Expanded — domain knowledge
- Knowledge grew from 15 to **30** main topics, adding design troubleshooting, tolerance stacks, thermal management, DFMA, image→CAD, requirements/release, structural stiffness/load paths, hardware/joints/hinges, sealing/gaskets, corrosion/finishing, metrology, BOM/PDM/change control, supplier handoff, electrical-enclosure mechanical layout and calculation discipline.
- Skills grew to **46**, including design troubleshooting/orchestration, source verification, tolerance/thermal/process/image→CAD, structural stiffness, hardware, sealing, metrology and supplier-handoff reviews.

### Expanded — AI quality
- **47 SFT**, **20 preference pairs**, **63 eval cases**.
- **49/49** supplied gold responses pass the automatic harness; 14 eval cases remain intentionally outside the gold subset for real/manual model evaluation.
- Generated RAG baseline currently contains **263 chunks**; current count is rebuild-dependent.
- ChatGPT/Claude/Codex/generic adapters; compact thematic packs for upload-limited environments.

### Changed
- Topic coverage now uses maturity states instead of misleading “Complete”.
- `dist/` is generated from source-of-truth content.
- Provider prompts explicitly prefer real project/shop profiles and deterministic tools.
- Release-critical assumptions/estimates/unknowns are prevented from silently becoming facts.

### Known real-world validation still open
- Populate actual fabricator bend/tooling/capability data.
- Verify Turkish SolidWorks UI labels in the installed version.
- Execute macro regression in real SolidWorks.
- Benchmark Image→CAD on real ground-truth parts.
- Run target ChatGPT/Claude configurations against all eval cases.
- Physical/certification tests remain external evidence, not AI claims.

## 2.0.0 — 2026-10-02

Consolidation release. Merges the ChatGPT-built line (v0.1 → v1.3) with the Claude-built line (v0.9) and turns a mostly structural library into a *usable* one.

### Added — knowledge (15 files, ≈12 500 words)
- `knowledge/01–15`: sheet-metal fundamentals, bending/flat pattern with computed examples, SolidWorks sheet-metal, SolidWorks Turkish UI (V/C/U confidence levels), enclosures/IP/IK, technical drawing, GD&T + ISO 2768 tables, image-based dimension estimation, CAD practice, engineering documentation, quotation, cost analysis (worked example), macros/API, welding/fasteners/finishing, materials (generated weight table).
- `reference/`: IP codes, standards map, sheet-metal formulas, glossary (164 EN↔TR terms, CSV source + generated MD), SolidWorks UI-label table (41 rows, levels V/C/U).
- `docs/terminology-policy.md` (Turkish term-selection order).

### Added — training (new `training/`)
- System prompts for Claude (Project) and ChatGPT (Custom GPT) from one core prompt.
- SFT seed set (35 records, numbers computed by code), preference set (12 pairs), exporters for OpenAI and Claude formats.
- Evaluation: 45 cases with automatic checks, offline runner, gold self-test (100 %), protocol.
- RAG chunk builder (≈160 chunks with metadata).
- Data-governance rules and training strategy (prompt → RAG → fine-tune).

### Added — skills
- `cad-engineering-practice`, `sheet-metal-terminology`, `ai-training-curator`.
- Every skill now has `name` + bilingual `description` (Claude-Skills compatible), knowledge pointers, failure modes, example and smoke test.

### Changed
- 8 empty skeleton modules and 8 stub blueprints (EN + TR) replaced with real content; Claude-line blueprints (bend analysis, image estimation, Turkish UI, drawing review, cost, macros, enclosure review) restored over v1.x templates.
- 10 template skills rewritten from their blueprints; scope files, workflows, examples and smoke tests are real, not placeholders.
- Adapters rewritten (Claude Project/Skills/Code, ChatGPT Custom GPT/Project/API).
- Old release notes moved to `docs/releases/`.

### Fixed
- `VERSION` (1.2.0) disagreed with README (1.1.0) and CHANGELOG ordering; now enforced by `scripts/validate_all.py`.
- Empty `knowledge/`, `templates/`, `tone/`, `archived/` directories (now populated or `.gitkeep`).
- Numeric corrections found in review: ISO 2768-1 "v" column, V-die ratios, rounding in worked examples.

### Tooling
- `scripts/validate_all.py` (version consistency, skill front matter, knowledge front matter, path references, empty dirs + all validators), `scripts/validate_content.py` (stub detector), `scripts/validate_reference.py`, `scripts/build_glossary.py`, `scripts/generate_skill_catalog.py`, `scripts/export_claude_skills.py`, `scripts/export_chatgpt.py`, GitHub Actions workflow (optional).

### Known limits
- Turkish SolidWorks UI labels are **unverified** (level U) until filled from a real installation.
- *Typical* design values are rules of thumb, not a shop's capability data.
- No real model run of the eval set is included (needs API access/manual run); the gold self-test only checks the harness.
- LICENSE not chosen.

## 1.3.0 and earlier
See `docs/releases/` and the version history of the source repository (v1.3: visual generation skills; v1.2: MergenHan compatibility layer; v1.1: market intelligence; v1.0: first stable structure).
