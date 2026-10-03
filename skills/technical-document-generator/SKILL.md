---
id: mai-skill-technical-document-generator
title: Technical Document Generator
type: skill
status: active
version: 1.0.0
summary: Generate structured technical documentation from supplied engineering facts while separating missing data from assumptions.
tags: [documentation, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: technical-document-generator
description: Produce structured engineering documents (specification, datasheet, work instruction, inspection plan, calculation note, test procedure) from supplied facts with open items instead of invented data. Use for teknik doküman, iş talimatı, şartname, hesap föyü.
---
# Technical Document Generator

## Purpose
Produce technical documents (design description, specification, datasheet, work instruction, inspection plan, test procedure, calculation note, quotation annex) from supplied facts.

## Trigger
Produce structured engineering documents (specification, datasheet, work instruction, inspection plan, calculation note, test procedure) from supplied facts with open items instead of invented data. Use for teknik doküman, iş talimatı, şartname, hesap föyü.

## Required inputs
Document type, audience, language, purpose, supplied facts/drawings, template or company format, revision data.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Confirm type, audience, language, and template (`knowledge/10`).
2. Build the skeleton first (sections, tables) and confirm for long documents.
3. Fill from supplied facts only; insert `[OPEN]` for any mandatory missing item.
4. Separate facts, calculations, assumptions; add evidence labels.
5. Add references with edition, revision history, document number.
6. Review against the checklist in `knowledge/10`; fix numbers/units consistency.
7. Deliver in the requested format; keep a Markdown source.

## Required checks
- No invented standards, certificates, signatures or test results.
- Units and numbers consistent across text and tables.
- Requirements use shall/should/may and are verifiable.

## Output contract
Skeleton → full document → list of open items.

## Failure modes
- Inventing standards, test results, torque values or signatures.
- Skipping the skeleton on long documents.
- Inconsistent units between text and tables.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/10-engineering-documentation.md`

## Self-test
1. Work instruction without torque values → inserts [OPEN] for torque, does not invent.
2. Datasheet requested with unknown IP rating → states "not rated / not tested" or asks.
3. Long spec → skeleton shown first.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
