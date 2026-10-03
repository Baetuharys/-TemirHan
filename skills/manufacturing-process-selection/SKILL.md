---
id: mai-skill-manufacturing-process-selection
title: Manufacturing Process Selection
type: skill
status: active
version: 1.0.0
summary: Select and review manufacturing routes for mechanical and sheet-metal parts using quantity, material, tolerance, finish, tooling and assembly constraints. Focuses on DFMA and supplier capability.
tags: [manufacturing, dfma, sheet-metal, process]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: manufacturing-process-selection
description: Select and review manufacturing routes for mechanical and sheet-metal parts using quantity, material, tolerance, finish, tooling and assembly constraints. Focuses on DFMA and supplier capability.
---
# Manufacturing Process Selection

## Trigger
Use when deciding laser/turret/form/weld/hardware/finish/assembly routes or simplifying a design for manufacture.

## Workflow
1. Capture quantity, material/thickness, finish, tolerances and critical features.
2. Map each feature to an operation and setup.
3. Identify special tooling, secondary operations and inspection bottlenecks.
4. Look for part commonization, locator features and service-friendly joining.
5. Compare feasible routes without declaring a best option until priorities are known.
6. Feed route assumptions to cost and drawing/release skills.

## Knowledge to load
- `knowledge/19-manufacturing-process-selection-and-dfma.md`
- `knowledge/01-sheet-metal-fundamentals.md`
- `knowledge/14-welding-fasteners-finishing.md`
- `knowledge/12-cost-analysis.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
