---
id: mai-skill-design-troubleshooter
title: Design Troubleshooter
type: skill
status: active
version: 1.0.0
summary: Diagnose a mechanical or sheet-metal design problem when the user is stuck. Converts symptoms into requirements, geometry/process causes, alternative concepts, risks and verification actions without inventing missing engineering inputs.
tags: [cad, design-review, troubleshooting, dfma]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: design-troubleshooter
description: Diagnose a mechanical or sheet-metal design problem when the user is stuck. Converts symptoms into requirements, geometry/process causes, alternative concepts, risks and verification actions without inventing missing engineering inputs.
---
# Design Troubleshooter

## Trigger
Use when the user says a design does not work, asks what to change, wants alternatives, or is unsure how to proceed.

## Workflow
1. State the observable problem and intended function.
2. Extract hard constraints and unresolved inputs; ask at most three high-value questions if necessary.
3. Run the five-layer diagnosis: requirement, geometry, process, assembly/service, verification.
4. Offer 2–4 viable concepts when trade-offs exist.
5. For each concept show benefit, new risk, manufacturing effect and verification need.
6. End with the smallest next action that will reduce uncertainty.

## Knowledge to load
- `knowledge/16-design-troubleshooting-and-decision-support.md`
- `knowledge/09-cad-engineering-practice.md`
- `knowledge/19-manufacturing-process-selection-and-dfma.md`
- `knowledge/21-requirements-risk-and-release.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
