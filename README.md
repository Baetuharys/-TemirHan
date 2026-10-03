# Mechanical AI Engineering — v3.0.0

**Provider-neutral mechanical engineering knowledge, design-support, retrieval, calculation and release framework for ChatGPT, Claude, Codex and generic LLMs.**

Primary focus: **sheet metal / sac levha, SolidWorks, cabinets/enclosures, IP/IK-oriented design, technical drawing, GD&T, image measurement / Image→CAD, manufacturing, documentation, costing and quotation.**

> This project is designed to help when you are stuck on a design **without letting the AI hide uncertainty behind confident wording**. It separates supplied facts, deterministic calculations, source-backed facts, practice, assumptions, estimates and unknowns.

## What v3 contains

| Layer | Current build | Purpose |
|---|---:|---|
| Engineering knowledge | **30** topic files | Sheet metal → enclosure → inspection → supplier handoff |
| Task skills | **46** skills | Reusable design/review/calculation/document workflows |
| Evaluation | **63** cases | Regression for hallucination, calculations and engineering behavior |
| Gold harness | **49** responses | Current automatic self-test subset |
| SFT seed | **47** examples | Behavior/style training seed |
| Preference seed | **20** pairs | Good-vs-bad engineering behavior |
| RAG | **263** generated chunks | Offline knowledge retrieval baseline |
| Source registry | **12** authoritative metadata records | Standards/software provenance and lifecycle watch |
| Executable tools | calculators + Image→CAD | Deterministic arithmetic and draft 2D reconstruction |
| Provider adapters | ChatGPT / Claude / Codex / generic | Thin runtime-specific packaging |

Generated counts are checked by the repository validators; RAG/package counts change as the library grows.

---

## What you can ask it

You can write normally in Turkish. You do not need to know the engineering term first.

Examples:

```text
/design Bu kabin kapısı kilidi kapatınca ortadan esniyor. Kalınlığı artırmadan ne yapabilirim?
/enclosure IP65 hedefli kapı-conta detayımı gözden geçir.
/bend 2 mm sacın açınımını hesaplayalım; bend table'ımı birazdan vereceğim.
/gdt Bu delik paterni için datum ve tolerans stratejisi öner.
/review Bu teknik resmi üretici gözüyle Blocker/Risk/Improvement/Open item şeklinde incele.
/imagecad Bu fotoğraftan yaklaşık geometri çıkar; hangi ölçüyü referans vermem lazım?
/solidworks Bu parçayı SolidWorks Sheet Metal olarak en temiz nasıl modellemeliyim?
/macro Açık çizimleri PDF'e export edecek güvenli makro taslağı hazırla.
/cost Lazer + büküm + kaynak + boya maliyet modelini kur.
/quote Bu BOM ve maliyetlerden profesyonel teklif iskeleti oluştur.
/release Bu drawing/DXF paketi üretime çıkmadan önce ne eksik?
```

The `/...` prefixes are **conversational shortcuts**, not required syntax. Full guide: `docs/DESIGN-HELP.md`.

---

## The trust model

Every release-relevant value should be classifiable as:

- `[VERİLEN] / SUPPLIED`
- `[HESAPLANAN] / CALCULATED`
- `[KAYNAKLI] / SOURCE-BACKED`
- `[UYGULAMA] / PRACTICE`
- `[VARSAYIM] / ASSUMED`
- `[TAHMİN] / ESTIMATED`
- `[AÇIK] / UNKNOWN`

This prevents common AI failures such as inventing a K-factor, claiming an enclosure “is IP65” from CAD alone, fabricating a Turkish SolidWorks menu path, treating a photo estimate as a manufacturing dimension, or mixing markup with margin.

### Non-negotiable engineering rules
1. **No invented production inputs.** Material, thickness, tolerance, K/BD, machine capability, price, standard clause and customer fact must be supplied, calculated, sourced or labelled unresolved.
2. **K-factor is not a universal material constant.** Production flat patterns use real shop bend data / trial validation.
3. **IP/IK claims need the applicable evidence/test.** CAD can be reviewed against a target; it cannot certify itself.
4. **Image-derived geometry stays estimated** until scale, perspective and authoritative dimensions are validated.
5. **SolidWorks UI/API is version-sensitive.** Turkish labels and API members are verified against the installed/versioned environment before release use.
6. **Macros start safe.** Read-only first, null/error checks, copies/test files, no silent overwrite/deletion.
7. **Electrical safety values are not guessed.** Creepage/clearance and similar requirements come from the governing electrical authority/standard/component data.
8. **A calculation states its model and limits.** A simple beam calculation is not presented as exact sheet/plate behavior.

---

## Best first setup

### 1. Give the AI the library
Run:

```bash
python scripts/mai.py rebuild
```

Then use:
- ChatGPT: `training/system-prompts/chatgpt-custom-gpt-instructions.md` + `dist/chatgpt-knowledge/`
- Claude, compact: `training/system-prompts/claude-project-instructions.md` + `dist/claude-project-compact/`
- Claude, full: `dist/claude-project-knowledge/`
- Claude task skills: `dist/claude-skills/*.zip`
- Code/agent runtimes: load the repo and follow `AGENTS.md` / adapter mapping.

Product upload limits and features change, so the repo provides both **compact thematic packs** and full source files instead of hardcoding a platform limit.

### 2. Give it your real shop once
Copy:

```text
project-profiles/example-fabricator-profile.yaml
```

and fill whatever you actually know: SolidWorks version/language, stocked materials, laser constraints, press-brake tooling, bend table/K-factor source, weld/finish capability, hardware families and cost rates.

**This is one of the highest-value steps in the whole project.** Real shop data outranks generic rules of thumb.

### 3. Ask normally
If you know little, start with:

> “Şunu tasarlıyorum, elimde bunlar var, burada takıldım.”

The system should recover requirements and ask no more than a few high-value questions before helping.

Beginner guide: `docs/GETTING-STARTED-NOVICE.md`.

---

## Repository architecture

```text
knowledge/            30 engineering knowledge topics
reference/            quick cards, glossary, UI/standards maps
sources/              provenance/source registry
skills/               46 task skills with examples/tests
agents/               specialist roles + orchestrator + verifier
workflows/            end-to-end design/release flows
design_patterns/      reusable enclosure/sheet-metal concept patterns
project-profiles/     real shop/project capability data
engineering_core/     evidence model + shared engineering data model
schemas/              machine-readable schemas
tools/                deterministic engineering calculators
engines/image_to_cad/ executable 2D image→geometry pipeline
rag/                  local BM25 retrieval/index
training/             system prompts, SFT, preference, eval and RAG chunks
adapters/             ChatGPT / Claude / Codex / generic mappings
templates/            requirements, review, release, quotation/document templates
mh-compat/            MergenHan-inspired content lifecycle compatibility layer
dist/                 generated provider packages; do not hand-edit
```

Architecture details: `docs/ARCHITECTURE.md`.

---

## Executable tools

### One entry point

```bash
python scripts/mai.py validate
python scripts/mai.py search "door gasket latch IP65"
python scripts/mai.py calc bend --t 2 --r 2 --angle 90 --k 0.40
python scripts/mai.py calc gasket --free 10 --compressed 7.5
python scripts/mai.py calc tolerance --plusminus 0.2 0.1 0.15 --method worst
python scripts/mai.py image-cad image.png --out output --ref-p1 10 20 --ref-p2 410 20 --ref-mm 200
python scripts/mai.py rebuild
```

Windows wrappers:

```powershell
.\mai.ps1 validate
.\mai.ps1 search "sac kabin kapı stiffener"
```

See `docs/SETUP-WINDOWS.md`.

### Deterministic calculation modules
- bend allowance / outside setback / bend deduction;
- mass;
- margin vs markup / cost rollup;
- worst-case and RSS 1-D tolerance stack;
- first-pass sensible-heat airflow;
- gasket geometric compression;
- simple beam sanity-check idealizations.

The calculators deliberately keep caller-supplied/process-specific inputs visible instead of hiding them as constants.

### Image→CAD engine
Current executable scope:
- grayscale/threshold/edge preprocessing;
- Hough line/circle detection;
- two-point scale calibration;
- four-point perspective correction utility;
- horizontal/vertical/parallel/perpendicular/concentric constraint inference;
- JSON, SVG and dependency-light ASCII DXF export;
- first-pass geometry/manufacturing checks;
- synthetic regression test.

It is **not yet a universal 3D inverse-CAD system** and does not claim native `.SLDPRT` generation. Real-photo ground-truth benchmarking remains a release-development item.

---

## Design-support coverage

Beyond the original sheet-metal/SolidWorks scope, v3 adds practical help for:
- finding why a design is failing rather than only suggesting a thicker sheet;
- stiffness/load paths and reinforcement concepts;
- hinges, latches, joints and self-clinching/rivet hardware decisions;
- continuous gasket paths and compression reasoning;
- thermal enclosure trade-offs;
- corrosion/coating/material compatibility;
- inspection/metrology and flexible formed-part measurement;
- BOM/revision/PDM/change control;
- supplier/fabricator RFQ and manufacturing handoff;
- mechanical layout/serviceability of electrical enclosures without inventing electrical-code values;
- requirements, assumptions, risk and release control.

Coverage/maturity map: `catalog/topic-coverage.md`.

---

## RAG and AI training

The repo no longer stops at “Markdown chunks”. It includes an offline BM25 build/retrieval path:

```bash
python training/scripts/build_rag_chunks.py
python rag/build_index.py
python rag/retrieve.py "ISO 5459 datum strategy" -k 5
```

Training strategy is intentionally:

```text
Prompt/skills → knowledge + retrieval → deterministic tools → eval → fine-tune only if still needed
```

Current datasets: 47 SFT, 20 preference pairs, 63 eval cases. `training/eval/gold-sample-responses.jsonl` currently exercises 49 of those cases as a harness self-test; the remaining cases are left for real model/manual evaluation rather than pretending to have run a model that was not run.

See `training/README.md` and `training/DATA-GOVERNANCE.md`.

---

## Source and standards governance

`sources/registry.json` stores source IDs, organization, edition/status metadata, official links and intended use. The repository references standards; it does **not** redistribute protected standard text.

Release-critical standard/software claims are re-checked against the governing project requirements and the current authoritative source. Some records are intentionally on lifecycle watch because revisions/replacements are in progress.

See `sources/README.md` and `docs/KNOWLEDGE-GOVERNANCE.md`.

---

## Validation / release

Run:

```bash
python scripts/validate_all.py
python training/scripts/run_eval.py --responses training/eval/gold-sample-responses.jsonl --min-pass 1.0
```

A full release can be built reproducibly with:

```bash
python scripts/build_release.py
```

The release builder validates metadata/links/localization/sources/datasets/calculators/RAG/Image→CAD, rebuilds retrieval/provider packs, runs the gold harness, creates a file SHA-256 manifest and produces a versioned ZIP.

---

## What still requires real-world validation

This repo is deliberately explicit about the boundary between a strong engineering assistant and a certified production system. Before relying on it for real release work, the most valuable remaining validation is:

1. your actual fabricator capability + bend table/tooling data;
2. your installed SolidWorks version and Turkish UI labels;
3. real SolidWorks macro regression on controlled copies;
4. real Image→CAD photo/drawing benchmark against ground-truth CAD;
5. your company/customer drawing, revision, quotation and approval rules;
6. real ChatGPT/Claude runs over the eval set;
7. applicable physical testing/certification where required.

The maturity model is in `docs/maturity-model.md`; the project intentionally does not label every topic “complete”.

---

## Licensing

No repo-wide open-source license is selected automatically. Review `docs/LICENSING.md` and `THIRD_PARTY_NOTICE.md` before public redistribution.
