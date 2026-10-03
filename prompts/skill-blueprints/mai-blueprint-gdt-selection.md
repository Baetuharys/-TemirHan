---
id: mai-blueprint-gdt-selection
title: GD&T Selection
type: blueprint
status: draft
version: 1.0.0
summary: Select function-based geometric tolerances and datums that are inspectable and not over-specified.
tags: [technical-drawing, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: function, mating parts, process capability, standard
output_contract: table of frames with datums, modifiers and inspection notes
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# GD&T Selection

## Scope
Choose geometric tolerances and datums that express function and are inspectable; avoid over-tolerancing. Not a replacement for the standard text.

## Required inputs
Part function, mating parts, assembly method, inspection method, process capability, governing standard (ISO 1101 or ASME Y14.5), existing drawing if any.

## Workflow
1. Identify the function of each critical feature (seal, fit, mount, alignment).
2. Choose the **datum scheme** from how the part is mounted and measured (stable surfaces, hole patterns); state restraint for thin non-rigid parts.
3. Map each requirement to a characteristic (flatness, parallelism, perpendicularity, position, profile…) using `knowledge/07`.
4. Choose the loosest tolerance that works; compare with process capability (laser ±0.1–0.2 mm, bend angle ±0.5°–1°).
5. Decide whether a modifier (MMC/LMC/free state) is justified.
6. Check ISO 2768 general tolerance consequences.
7. Check that the inspection method exists.
8. Output the frames in text form with datum references.

## Required checks
- Every referenced datum is defined.
- Datum order is justified.
- No tolerance tighter than the process can hold without a note.
- Standard (ISO/ASME) is named; edition to verify.

## Output format
Table: feature · function · characteristic · tolerance · datums · modifier · inspection note.

## Test cases
1. Mounting plate with 4 holes → position with ⌀ zone to datums A|B|C; MMC only if clearance fits.
2. Request "flatness 0.05 on 1 m × 1.5 mm sheet" → flagged as unrealistic/non-rigid; asks function and restraint.
3. Drawing with frame referencing datum "D" not defined → flagged as Error.
