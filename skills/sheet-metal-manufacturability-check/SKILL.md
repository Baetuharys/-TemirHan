---
id: mai-skill-sheet-metal-manufacturability-check
title: Sheet Metal Manufacturability Check
type: skill
status: active
version: 1.0.0
summary: Review sheet-metal geometry for common fabrication risks before release.
tags: [sheet-metal, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: sheet-metal-manufacturability-check
description: Design-for-manufacturing review of sheet-metal parts: cutting, forming, joining, finishing, inspection and cost drivers with Error/Risk/Suggestion findings. Use for üretilebilirlik kontrolü, DFM, imalat uygunluğu.
---
# Sheet Metal Manufacturability Check

## Purpose
Design-for-manufacturing review of a sheet-metal part or assembly before release or quotation. Finds features the shop will reject, re-quote or struggle with.

## Trigger
Design-for-manufacturing review of sheet-metal parts: cutting, forming, joining, finishing, inspection and cost drivers with Error/Risk/Suggestion findings. Use for üretilebilirlik kontrolü, DFM, imalat uygunluğu.

## Required inputs
Model/drawing, material and thickness, quantity, process (laser/punch/bend/weld/finish), tolerance class, shop capability data if available.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Cutting: min hole/slot, web, corner radii, edge distances, nesting friendliness.
2. Forming: radius vs tooling, flange length, hole-to-bend, relief, bend sequence and collisions, springback, grain direction.
3. Joining: weld access and distortion, hardware datasheet limits, galvanised/stainless considerations.
4. Finishing: coating thickness vs fits, masking, hanging marks, drain holes.
5. Assembly/inspection: tolerance stack, datum accessibility.
6. Cost drivers: extra setups, special tools, secondary operations.
7. Classify each finding as **Error / Risk / Suggestion**, cite location, give a fix.

## Required checks
- Rules of thumb are labelled *typical*; shop values override.
- No finding without a location.
- The first process that could reject the part is named.

## Output contract
Findings table: # · location · class · finding · proposed fix · cost/time effect.

## Failure modes
- Quoting rules of thumb as universal limits.
- Findings without a location.
- Not naming the first process that may reject the part.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/01-sheet-metal-fundamentals.md`
- `knowledge/02-bending-and-flat-pattern.md`
- `knowledge/14-welding-fasteners-finishing.md`

## Self-test
1. 3 mm thick part with 8 mm flange → Error: flange shorter than tooling minimum (typical).
2. Slot 2 mm from a bend → Risk with distance rule.
3. Request without material → asks material and thickness before judging.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
