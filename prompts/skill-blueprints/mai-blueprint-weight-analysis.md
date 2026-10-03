---
id: mai-blueprint-weight-analysis
title: Weight Analysis
type: blueprint
status: draft
version: 1.0.0
summary: Compute and cross-check blank, finished and CAD mass with stated density sources.
tags: [analysis, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: material, thickness, geometry, cut-outs, hardware, coating
output_contract: table of formulas, inputs, results and labels
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Weight Analysis

## Scope
Compute and sanity-check the mass of sheet/plate parts and assemblies: blank mass for purchasing, finished mass for shipping, CAD mass properties comparison.

## Required inputs
Material and grade (density source), thickness, geometry (area or dimensions), cut-outs, hardware, coating, quantity.

## Workflow
1. Identify what is wanted: blank mass, finished part mass, assembly mass, shipping mass.
2. Pick density with a stated source (`knowledge/15`); never assume stainless = steel.
3. Compute `m = V·ρ` (V in m³, ρ in kg/m³) or `m = A·T·ρ`; show the substituted numbers.
4. Subtract cut-outs; add hardware, welds, coating separately and label them estimates.
5. Compare with CAD mass properties; explain differences (density, configuration, coating).
6. Apply order-of-magnitude check (kg/m² per mm: steel ≈ 7.85).
7. Give result with units and an uncertainty note.

## Required checks
- Units consistent (mm vs m).
- Density grade matches the real grade.
- Blank vs finished mass is not confused.

## Output format
Table: item · formula · inputs · result · label. Then notes and open items.

## Test cases
1. 1 m × 2 m × 3 mm steel plate → 47.1 kg `[CALCULATED]`.
2. Same in 1.4301 → ≈ 47.6 kg with ρ ≈ 7930 kg/m³; states density source.
3. "Part is 5 kg" vs CAD 4.2 kg → asks configuration, density, hardware, coating.
