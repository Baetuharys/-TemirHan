---
id: mai-skill-requirements-and-risk-review
title: Requirements and Risk Review
type: skill
status: active
version: 1.0.0
summary: Turn vague design goals into traceable, testable requirements; maintain assumption and lightweight risk registers; connect design changes to verification and release artifacts.
tags: [requirements, risk, verification, change-control]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: requirements-and-risk-review
description: Turn vague design goals into traceable, testable requirements; maintain assumption and lightweight risk registers; connect design changes to verification and release artifacts.
---
# Requirements and Risk Review

## Trigger
Use at project start, before release, or after a major design change when requirements/assumptions are unclear.

## Workflow
1. Extract requirements and assign stable IDs.
2. For each requirement capture source, priority and verification method.
3. Record ASSUMED/ESTIMATED/UNKNOWN items in an assumption register.
4. Identify failure modes and closure actions without inventing a company risk score.
5. Trace design changes to CAD/drawing/DXF/BOM/cost/test/document impacts.
6. Return open items that prevent release.

## Knowledge to load
- `knowledge/21-requirements-risk-and-release.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
