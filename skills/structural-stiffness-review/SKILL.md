---
id: mai-skill-structural-stiffness-review
title: Structural Stiffness Review
type: skill
status: active
version: 1.0.0
summary: Review sheet-metal stiffness, load paths and reinforcement concepts without pretending a simple beam model is a full panel analysis.
tags: [sheet-metal, stiffness, mechanical-design, dfma]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, relevant geometry/drawing/data, constraints, target decision
output_contract: evidence-labelled review, alternatives/risks, missing inputs and verification actions
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: structural-stiffness-review
description: Review sheet-metal stiffness, load paths and reinforcement concepts without pretending a simple beam model is a full panel analysis.
---
# Structural Stiffness Review

## Trigger
Use when a panel, door, bracket or frame bends, vibrates, sags, oil-cans or needs a reinforcement concept.

## Workflow
1. Define the functional load and allowed motion/deflection.
2. Trace the load path and identify the flexible span/interface.
3. Classify the structural idealization: beam-like, plate/shell, joint-dominated or unknown.
4. Compare geometry-first options: returns, section depth, shorter span, stiffener, support, thickness.
5. State manufacturing/assembly trade-offs and the verification method.

## Knowledge to load
- `knowledge/22-structural-stiffness-and-load-paths.md`
- `knowledge/16-design-troubleshooting-and-decision-support.md`
- `knowledge/19-manufacturing-process-selection-and-dfma.md`

## Output discipline
- Label supplied, calculated, source-backed, assumed, estimated and unknown information.
- Do not invent manufacturer, shop or certification values.
- End with the smallest useful next verification/action.
