---
id: mai-skill-tolerance-stack-analysis
title: Tolerance Stack Analysis
type: skill
status: active
version: 1.0.0
summary: Build and review 1-D tolerance chains, worst-case or justified RSS calculations, datum implications and functional clearances. Use for assembly gaps, stack-up, fits and tolerance allocation.
tags: [gdt, tolerancing, stack-up, assembly]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: tolerance-stack-analysis
description: Build and review 1-D tolerance chains, worst-case or justified RSS calculations, datum implications and functional clearances. Use for assembly gaps, stack-up, fits and tolerance allocation.
---
# Tolerance Stack Analysis

## Trigger
Use for stack-up, clearance/interference, tolerance allocation, fit risk or assembly variation.

## Workflow
1. Define the functional result and stack direction.
2. Create the signed dimension chain and identify each tolerance source.
3. Use worst-case by default unless a statistical model is justified.
4. Check whether bend/weld/coating effects are missing from a nominal dimension-only stack.
5. Review datum scheme and inspection feasibility.
6. Return nominal, bounds, contributors and recommended controls.

## Knowledge to load
- `knowledge/17-tolerance-stack-and-fits.md`
- `knowledge/07-gdt-and-tolerancing.md`
- `reference/gdt-symbols.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
