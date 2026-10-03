---
id: mai-skill-gdt-selection
title: GD&T Selection
type: skill
status: active
version: 1.0.0
summary: Select and explain GD&T controls based on functional requirements without inventing tolerances.
tags: [technical-drawing, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: gdt-selection
description: Select ISO 1101 / ASME Y14.5 geometric tolerances and datums based on function and inspectability; ISO 2768 general tolerances. Use for geometrik toleranslandırma, datum seçimi, konum/düzlemsellik/diklik, aşırı toleranslandırmayı önleme.
---
# GD&T Selection

## Purpose
Choose geometric tolerances and datums that express function and are inspectable; avoid over-tolerancing. Not a replacement for the standard text.

## Trigger
Select ISO 1101 / ASME Y14.5 geometric tolerances and datums based on function and inspectability; ISO 2768 general tolerances. Use for geometrik toleranslandırma, datum seçimi, konum/düzlemsellik/diklik, aşırı toleranslandırmayı önleme.

## Required inputs
Part function, mating parts, assembly method, inspection method, process capability, governing standard (ISO 1101 or ASME Y14.5), existing drawing if any.

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

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

## Output contract
Table: feature · function · characteristic · tolerance · datums · modifier · inspection note.

## Failure modes
- Referencing undefined datums.
- Tolerances tighter than the process can hold.
- MMC without a clearance check.
- Datums on non-rigid, unsupported flanges.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/07-gdt-and-tolerancing.md`
- `knowledge/06-technical-drawing.md`
- `reference/standards-map.md`

## Self-test
1. Mounting plate with 4 holes → position with ⌀ zone to datums A|B|C; MMC only if clearance fits.
2. Request "flatness 0.05 on 1 m × 1.5 mm sheet" → flagged as unrealistic/non-rigid; asks function and restraint.
3. Drawing with frame referencing datum "D" not defined → flagged as Error.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
