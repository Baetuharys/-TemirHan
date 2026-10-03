---
id: mai-blueprint-technical-document-generator
title: Technical Document Generator
type: blueprint
status: draft
version: 1.0.0
summary: Produce structured technical documents from supplied facts, with open items instead of invented data.
tags: [documentation, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: document type, audience, language, facts, template
output_contract: skeleton, full document, open items
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Technical Document Generator

## Scope
Produce technical documents (design description, specification, datasheet, work instruction, inspection plan, test procedure, calculation note, quotation annex) from supplied facts.

## Required inputs
Document type, audience, language, purpose, supplied facts/drawings, template or company format, revision data.

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

## Output format
Skeleton → full document → list of open items.

## Test cases
1. Work instruction without torque values → inserts [OPEN] for torque, does not invent.
2. Datasheet requested with unknown IP rating → states "not rated / not tested" or asks.
3. Long spec → skeleton shown first.
