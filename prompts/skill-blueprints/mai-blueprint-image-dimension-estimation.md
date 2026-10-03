---
id: mai-blueprint-image-dimension-estimation
title: Image Dimension Estimation
type: blueprint
status: draft
version: 0.2.0
summary: Estimate part dimensions from a photo using a reference object and report error ranges.
tags: [visual-analysis, measurement]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-uncertainty-management, mai-module-image-measurement]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Image Dimension Estimation

## Scope
Photo -> dimension estimate with classes and error range. Not a replacement for a measurement when the part is going to manufacture.

## Required inputs
The photo, the feature(s) to estimate, a reference of known size visible in the photo (or a known standard part), camera angle if known.

## Workflow
1. Check the photo: is the reference on the same plane as the feature? is the view roughly straight-on? is anything cropped?
2. State the reference and its size. If the size is assumed, class results as Scaled estimate with the assumption named.
3. Compute scale = known mm / known px. Apply only to features on that plane.
4. For each feature give value, class, and +/- error (main source named: pixel reading, tilt, lens, reference size).
5. List what would tighten the numbers: a straight-on photo, a ruler in frame, one measured dimension from the user.
6. If the stated purpose is manufacturing, say clearly that a measurement is needed before cutting.

## Required checks
- No dimension without a class. - No single number without a range. - Reference named. - Perspective warning given when tilt is visible.

## Output format
Table: feature | value | class | reference | error range; then "what would improve this".

## Test cases
1. Part photographed with a ruler beside it, straight-on: Scaled estimates with small error.
2. Part photographed obliquely, no reference: model must refuse numbers and ask for a reference.
3. Features at different depth than the reference: model must warn and widen the range.
