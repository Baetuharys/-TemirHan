---
id: mai-skill-metrology-inspection-planning
title: Metrology and Inspection Planning
type: skill
status: active
version: 1.0.0
summary: Turn critical drawing requirements into measurable inspection characteristics, datum setups and prototype/production checks.
tags: [quality, drawing, gdt, inspection, metrology]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, relevant geometry/drawing/data, constraints, target decision
output_contract: evidence-labelled review, alternatives/risks, missing inputs and verification actions
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: metrology-inspection-planning
description: Turn critical drawing requirements into measurable inspection characteristics, datum setups and prototype/production checks.
---
# Metrology and Inspection Planning

## Trigger
Use when deciding how a dimension/GD&T item will be measured or preparing an inspection/FAI plan.

## Workflow
1. Identify function-critical characteristics.
2. Define the drawing datum/measurement setup.
3. Select a realistic measurement method and note flexible-part restraint.
4. State frequency/recording/reaction expectations from project quality rules.
5. Verify measurement capability before tightening tolerances.

## Knowledge to load
- `knowledge/26-metrology-inspection-and-quality-planning.md`
- `knowledge/06-technical-drawing.md`
- `knowledge/07-gdt-and-tolerancing.md`

## Output discipline
- Label supplied, calculated, source-backed, assumed, estimated and unknown information.
- Do not invent manufacturer, shop or certification values.
- End with the smallest useful next verification/action.
