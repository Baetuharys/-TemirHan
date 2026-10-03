---
id: mai-blueprint-cost-analysis
title: Cost Analysis
type: blueprint
status: draft
version: 0.2.0
summary: Build a transparent unit cost for a sheet-metal part with tagged inputs and a sensitivity note.
tags: [cost-analysis, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-cost-model, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Cost Analysis

## Scope
Unit and batch cost estimate for sheet-metal parts or assemblies. Output is an estimate, not a quotation.

## Required inputs
Part list or drawing, material and price per kg (supplied), quantity, process list (laser, bend, weld, finish), shop rates if available, price date and currency.

## Workflow
1. Compute blank size and mass (see `reference/sheet-metal-formulas.md`); apply the scrap factor and state its source.
2. Fill each cost line from the cost model. Tag every number Supplied / Assumed / Calculated.
3. Missing rates: do not invent. Ask, or mark Assumed with a reason and a replacement path.
4. Separate unit cost from setup/tooling and show the quantity assumed for spreading it.
5. Compute total and the sensitivity of the two inputs that move it most.
6. List what must be confirmed before the number goes into a quotation.

## Required checks
- Every price has a date and currency. - Formulas visible. - Assumed values listed together at the end.

## Output format
Cost table, total, sensitivity, "to confirm" list.

## Test cases
1. Fully supplied rates: all rows Supplied/Calculated, no Assumed.
2. No bending rate: model must ask or mark Assumed, not fill from memory.
3. Quantity changes from 10 to 1000: model must show how setup cost per piece changes.
