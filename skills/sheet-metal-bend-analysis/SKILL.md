---
id: mai-skill-sheet-metal-bend-analysis
title: Sheet Metal Bend Analysis
type: skill
status: active
version: 0.2.0
summary: Analyze sheet-metal bends, inputs, manufacturability constraints, and calculation requirements without inventing missing data.
tags: [sheet-metal, bending, manufacturability]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: material, thickness, bend geometry, bend radius, tooling/process data when available, desired output
output_contract: bend assessment, calculations or required inputs, assumptions, verification status, manufacturing risks
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: sheet-metal-bend-analysis
description: Analyse bends: bend allowance, bend deduction, K-factor, flat length, press-brake feasibility (V-die, minimum flange, springback). Use for büküm hesabı, bükme payı, K faktörü, kenar boyu, abkant uygunluğu.
---
# Sheet Metal Bend Analysis
## Trigger
Use for bend feasibility, bend allowance, K-factor, bend deduction, radius, or manufacturability questions.
## Workflow
1. Extract material, thickness, inside radius, angle, flange lengths, bend direction, and process.
2. Separate supplied values from inferred values; never invent K-factor, tooling, or material data.
3. Identify whether the task is geometric, manufacturing, SolidWorks-specific, or combined.
4. Calculate only when required inputs are available.
5. Check units and dimensional plausibility.
6. Check flange/edge distances, hole-to-bend relations, collision, sequence, and tooling access when applicable.
7. Report missing inputs and the next concrete action.
## Rules
- Label exact values and estimates separately.
- Flag values dependent on tooling, temper, machine, or shop practice.
- Distinguish engineering calculations from SolidWorks settings.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/02-bending-and-flat-pattern.md`
- `knowledge/01-sheet-metal-fundamentals.md`
- `knowledge/15-materials-reference.md`
- `reference/sheet-metal-formulas.md`
