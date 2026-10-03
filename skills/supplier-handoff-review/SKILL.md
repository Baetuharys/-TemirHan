---
id: mai-skill-supplier-handoff-review
title: Supplier and Fabricator Handoff Review
type: skill
status: active
version: 1.0.0
summary: Prepare and review a revision-controlled manufacturing/RFQ package and capture real fabricator capabilities back into the project profile.
tags: [supplier, rfq, manufacturing, release, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, relevant geometry/drawing/data, constraints, target decision
output_contract: evidence-labelled review, alternatives/risks, missing inputs and verification actions
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: supplier-handoff-review
description: Prepare and review a revision-controlled manufacturing/RFQ package and capture real fabricator capabilities back into the project profile.
---
# Supplier and Fabricator Handoff Review

## Trigger
Use before sending parts for quotation, prototype or production.

## Workflow
1. Confirm revision, quantity, material, finish and process scope.
2. Assemble drawing/CAD/DXF/BOM and critical requirements.
3. List quote assumptions and exclusions requiring clarification.
4. Capture supplier-specific bend/tooling/material/process capability.
5. Run release verification and create a manifest.

## Knowledge to load
- `knowledge/28-supplier-fabricator-rfq-and-handoff.md`
- `knowledge/21-requirements-risk-and-release.md`
- `knowledge/27-bom-revision-pdm-and-change-control.md`

## Output discipline
- Label supplied, calculated, source-backed, assumed, estimated and unknown information.
- Do not invent manufacturer, shop or certification values.
- End with the smallest useful next verification/action.
