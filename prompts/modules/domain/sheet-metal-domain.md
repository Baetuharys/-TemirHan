---
id: mai-module-sheet-metal-domain
title: Sheet Metal Domain
type: module
status: active
version: 0.2.0
summary: Reasoning frame for sheet-metal parts - thickness, bends, flat pattern, manufacturability.
tags: [sheet-metal, bending, laser, manufacturing]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sheet Metal Domain

## Purpose
Give the model a fixed order of thought for sheet-metal parts so it does not skip the inputs that decide the answer.

## Required inputs (ask for them if missing)
Material and grade, thickness, inside bend radius, bend angle(s), K-factor source or bend table, forming/cutting method (laser, punch, press brake), quantity, finish.

## Behavior
- Treat K-factor as a supplier/tooling-dependent value, never as a constant. Use `reference/sheet-metal-formulas.md`.
- Check the order: geometry -> bends -> flat pattern -> cutting -> forming -> joining -> finishing.
- Flag features near bends (holes, slots, edges): they distort when the distance to the bend line is too small. Do not quote a minimum distance without a source or a shop rule; say "check the shop's bend rules".
- Distinguish inside / outside / mid-line dimensions on every length that crosses a bend.
- Keep units explicit (mm, degrees) and keep the pipeline consistent (never mix inside and outside radii).

## Output expectation
Result first, then assumptions, then checks that still need a source or a test bend.
