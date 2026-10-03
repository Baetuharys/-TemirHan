---
id: mai-skill-enclosure-thermal-review
title: Enclosure Thermal Review
type: skill
status: active
version: 1.0.0
summary: Review first-pass thermal architecture for electrical/mechanical enclosures while preserving IP intent. Uses supplied heat load, ambient limits and airflow constraints without inventing fan performance.
tags: [enclosure, thermal, airflow, ip]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: enclosure-thermal-review
description: Review first-pass thermal architecture for electrical/mechanical enclosures while preserving IP intent. Uses supplied heat load, ambient limits and airflow constraints without inventing fan performance.
---
# Enclosure Thermal Review

## Trigger
Use for hot cabinets, fan/filter sizing inputs, passive-vs-active cooling choices, thermal/IP trade-offs.

## Workflow
1. Collect heat load, ambient range, allowable internal temperature, enclosure geometry and IP target.
2. Separate first-pass heat balance from component/fan selection.
3. Calculate airflow only from stated heat and ΔT inputs.
4. Check pressure-drop, contamination, altitude and service assumptions.
5. Review every new opening against ingress-boundary logic.
6. Return architecture, assumptions and measurement/test plan.

## Knowledge to load
- `knowledge/18-enclosure-thermal-management.md`
- `knowledge/05-enclosures-ip-ik.md`
- `knowledge/21-requirements-risk-and-release.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
