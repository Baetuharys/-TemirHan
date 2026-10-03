---
id: mai-skill-cost-analysis
title: Cost Analysis
type: skill
status: active
version: 1.0.0
summary: Build a transparent manufacturing cost estimate from supplied quantities, rates and process assumptions.
tags: [analysis, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: cost-analysis
description: Estimate and explain sheet-metal part cost (material, cutting, bending, welding, finishing, setup, overhead, margin) with a transparent model and sensitivity. Use for maliyet analizi, birim fiyat, parti etkisi, kâr marjı vs markup, cost reduction ideas.
---
# Cost Analysis

## Purpose
Unit and batch cost estimate for sheet-metal parts or assemblies. Output is an estimate, not a quotation.

## Trigger
Estimate and explain sheet-metal part cost (material, cutting, bending, welding, finishing, setup, overhead, margin) with a transparent model and sensitivity. Use for maliyet analizi, birim fiyat, parti etkisi, kâr marjı vs markup, cost reduction ideas.

## Required inputs
Part list or drawing, material and price per kg (supplied), quantity, process list (laser, bend, weld, finish), shop rates if available, price date and currency.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Compute blank size and mass (see `reference/sheet-metal-formulas.md`); apply the scrap factor and state its source.
2. Fill each cost line from the cost model. Tag every number Supplied / Assumed / Calculated.
3. Missing rates: do not invent. Ask, or mark Assumed with a reason and a replacement path.
4. Separate unit cost from setup/tooling and show the quantity assumed for spreading it.
5. Compute total and the sensitivity of the two inputs that move it most.
6. List what must be confirmed before the number goes into a quotation.

## Required checks
- Every price has a date and currency. - Formulas visible. - Assumed values listed together at the end.

## Output contract
Cost table, total, sensitivity, "to confirm" list.

## Failure modes
- Using illustrative rates as if they were market prices.
- Confusing markup with margin.
- Costing the finished part mass instead of the blank for material.
- Ignoring batch size in setup amortisation.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/12-cost-analysis.md`
- `knowledge/15-materials-reference.md`
- `knowledge/01-sheet-metal-fundamentals.md`

## Self-test
1. Fully supplied rates: all rows Supplied/Calculated, no Assumed.
2. No bending rate: model must ask or mark Assumed, not fill from memory.
3. Quantity changes from 10 to 1000: model must show how setup cost per piece changes.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
