---
id: mai-skill-image-dimension-estimation
title: Image Dimension Estimation
type: skill
status: active
version: 1.0.0
summary: Estimate dimensions from images only when a scale/reference is available, and report uncertainty.
tags: [visual-analysis, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: image-dimension-estimation
description: Estimate dimensions from photos using a reference object, with error range and confidence, never presented as manufacturing data. Use for görselden ölçü tahmini, fotoğraftan boy/ölçü, referans nesne, ölçek hesabı.
---
# Image Dimension Estimation

## Purpose
Photo -> dimension estimate with classes and error range. Not a replacement for a measurement when the part is going to manufacture.

## Trigger
Estimate dimensions from photos using a reference object, with error range and confidence, never presented as manufacturing data. Use for görselden ölçü tahmini, fotoğraftan boy/ölçü, referans nesne, ölçek hesabı.

## Required inputs
The photo, the feature(s) to estimate, a reference of known size visible in the photo (or a known standard part), camera angle if known.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Check the photo: is the reference on the same plane as the feature? is the view roughly straight-on? is anything cropped?
2. State the reference and its size. If the size is assumed, class results as Scaled estimate with the assumption named.
3. Compute scale = known mm / known px. Apply only to features on that plane.
4. For each feature give value, class, and +/- error (main source named: pixel reading, tilt, lens, reference size).
5. List what would tighten the numbers: a straight-on photo, a ruler in frame, one measured dimension from the user.
6. If the stated purpose is manufacturing, say clearly that a measurement is needed before cutting.

## Required checks
- No dimension without a class. - No single number without a range. - Reference named. - Perspective warning given when tilt is visible.

## Output contract
Table: feature | value | class | reference | error range; then "what would improve this".

## Failure modes
- Giving a single exact number without range and confidence.
- Reference object not in the same plane.
- Using an estimate for manufacturing.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/08-image-dimension-estimation.md`

## Self-test
1. Part photographed with a ruler beside it, straight-on: Scaled estimates with small error.
2. Part photographed obliquely, no reference: model must refuse numbers and ask for a reference.
3. Features at different depth than the reference: model must warn and widen the range.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
