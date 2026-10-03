---
id: mai-skill-weight-analysis
title: Weight Analysis
type: skill
status: active
version: 1.0.0
summary: Estimate or calculate part/assembly weight from geometry, material and density with explicit assumptions.
tags: [analysis, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: weight-analysis
description: Compute and cross-check plate, blank, finished-part and CAD mass with stated density sources. Use for ağırlık hesabı, kg/m², levha ağırlığı, CAD kütle karşılaştırması.
---
# Weight Analysis

## Purpose
Compute and sanity-check the mass of sheet/plate parts and assemblies: blank mass for purchasing, finished mass for shipping, CAD mass properties comparison.

## Trigger
Compute and cross-check plate, blank, finished-part and CAD mass with stated density sources. Use for ağırlık hesabı, kg/m², levha ağırlığı, CAD kütle karşılaştırması.

## Required inputs
Material and grade (density source), thickness, geometry (area or dimensions), cut-outs, hardware, coating, quantity.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

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

## Output contract
Table: item · formula · inputs · result · label. Then notes and open items.

## Failure modes
- Assuming stainless density equals steel.
- Mixing mm and m.
- Reporting blank mass as finished mass.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/15-materials-reference.md`
- `knowledge/09-cad-engineering-practice.md`
- `reference/sheet-metal-formulas.md`

## Self-test
1. 1 m × 2 m × 3 mm steel plate → 47.1 kg `[CALCULATED]`.
2. Same in 1.4301 → ≈ 47.6 kg with ρ ≈ 7930 kg/m³; states density source.
3. "Part is 5 kg" vs CAD 4.2 kg → asks configuration, density, hardware, coating.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
