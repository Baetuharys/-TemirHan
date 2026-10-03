---
id: mai-skill-flat-pattern-workflow
title: Flat Pattern Workflow
type: skill
status: active
version: 1.0.0
summary: Transform a sheet-metal model into a manufacturing-ready flat-pattern workflow without assuming machine-specific settings.
tags: [sheet-metal, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: flat-pattern-workflow
description: Build and verify a sheet-metal flat pattern: K-factor or bend-table consistency, relief, bend lines, bounding box, test-bend recommendation. Use for açınım, düz açınım, flat length, DXF öncesi kontrol.
---
# Flat Pattern Workflow

## Purpose
From a bent sheet-metal model to a trustworthy flat pattern and DXF. Covers flatten checks, K-factor/bend table consistency, relief, bend lines, bounding box.

## Trigger
Build and verify a sheet-metal flat pattern: K-factor or bend-table consistency, relief, bend lines, bounding box, test-bend recommendation. Use for açınım, düz açınım, flat length, DXF öncesi kontrol.

## Required inputs
Model or drawing, material and thickness, inside radii, bend method (K-factor / bend table / allowance), cutting process, sheet format.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Confirm material, thickness, radii, and the bend method used by the **shop**, not only by CAD.
2. Flatten and check for errors (overlaps, failed bends, missing relief, closed corners).
3. Check feature-to-bend distances (see `knowledge/01`, `knowledge/02`).
4. Compute the expected flat length by hand for one or two bends as a sanity check (`knowledge/02`).
5. Verify bounding box against the sheet format and nesting.
6. Prepare bend lines on a separate layer; decide marking geometry.
7. Record method and revision in the drawing note; export DXF; open and inspect.
8. Recommend a test bend before series release.

## Required checks
- K-factor or bend table source recorded.
- Units mm, scale 1:1.
- Bend lines are not cut lines.
- Hole/slot distortion near bends considered.

## Output contract
Findings table (item · status · note) · expected flat dimensions · open items.

## Failure modes
- Presenting a flat length as verified without a K-factor source.
- Mixing inside/outside dimension conventions.
- Leaving bend lines on the cut layer.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/02-bending-and-flat-pattern.md`
- `knowledge/03-solidworks-sheet-metal.md`
- `knowledge/01-sheet-metal-fundamentals.md`
- `reference/sheet-metal-formulas.md`

## Self-test
1. No K-factor given → asks for source; offers labelled estimate range.
2. Hole 3 mm from a 2 mm-thick bend → flagged as risk with distance rule.
3. DXF with bend lines on the cut layer → flagged as Error.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
