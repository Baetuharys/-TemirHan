---
id: mai-skill-design-review-orchestrator
title: Design Review Orchestrator
type: skill
status: active
version: 1.0.0
summary: Route a mechanical design review across requirements, CAD, sheet metal, enclosure/IP, drawing/GD&T, manufacturing, cost and release checks, then consolidate blockers and next actions.
tags: [orchestration, design-review, release, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: design-review-orchestrator
description: Route a mechanical design review across requirements, CAD, sheet metal, enclosure/IP, drawing/GD&T, manufacturing, cost and release checks, then consolidate blockers and next actions.
---
# Design Review Orchestrator

## Trigger
Use for broad “review this design” requests, release readiness, or when several domains interact.

## Workflow
1. Run engineering task intake and identify applicable domains.
2. Create a review matrix with requirement/function/process/release columns.
3. Route only relevant specialist skills; avoid loading everything.
4. Consolidate duplicate findings and preserve evidence labels.
5. Separate blockers, warnings, optimizations and optional ideas.
6. End with release state and ordered closure actions.

## Knowledge to load
- `knowledge/21-requirements-risk-and-release.md`
- `knowledge/16-design-troubleshooting-and-decision-support.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
