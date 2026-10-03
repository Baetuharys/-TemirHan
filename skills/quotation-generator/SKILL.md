---
id: mai-skill-quotation-generator
title: Manufacturing Quotation Generator
type: skill
status: active
version: 0.3.0
summary: Convert a reviewed manufacturing scope and cost basis into a structured technical-commercial quotation without inventing commercial assumptions.
tags: [quotation, cost, commercial, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: quotation-generator
description: Turn a reviewed scope and cost basis into a structured technical-commercial quotation with assumptions and exclusions. Use for teklif hazırlama, iş teklifi dokümanı, Incoterms, geçerlilik ve ödeme koşulları.
---
# Manufacturing Quotation Generator
## Workflow
1. Extract scope, quantities, materials, processes, finish, inspection, packaging, delivery, and customer-provided items.
2. Build a cost basis from available material, laser, marking, bending, welding, assembly, finishing, scrap, labor, tooling, and overhead inputs.
3. Separate calculated cost from commercial price and explicitly identify margin/contingency assumptions if provided.
4. State inclusions, exclusions, validity, lead time basis, payment terms, and technical assumptions only when supplied or approved.
5. Cross-check quantity, revision, part identity, and process route against the engineering release.
6. Generate a customer-facing quotation with a concise technical scope and a traceable internal cost summary when requested.

## Guardrail
Never invent a price, delivery date, margin, tax treatment, payment term, material grade, or production capability. Mark unavailable commercial inputs as pending.

## Output
Return quotation draft, assumptions/exclusions, pricing basis, and approval checklist.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/11-quotation-and-commercial.md`
- `knowledge/12-cost-analysis.md`

## Required checks
- Quantities and totals recomputed; line totals add up.
- Drawing revisions priced are stated.
- Any value from an estimate (not a supplier quote) is visibly flagged as not final.
- Delivery time, payment terms and validity are never filled from memory; missing ones become open items.
- Every exclusion assumed in the cost analysis appears in the exclusions section.
- Markup vs margin is labelled; tax/legal wording is marked "to be checked by finance/legal".

## Failure modes
- Inventing a customer, price, delivery date or clause.
- Presenting an illustrative cost-model rate as a quoted price.
- Leaving out the assumptions and exclusions block.

## Self-test
1. Prices and terms fully supplied → complete document, no open items.
2. No validity period given → listed as an open item.
3. Scope mentions a finish that the cost analysis did not price → the gap is flagged.
