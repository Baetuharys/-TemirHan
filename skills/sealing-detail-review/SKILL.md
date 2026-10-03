---
id: mai-skill-sealing-detail-review
title: Sealing Detail Review
type: skill
status: active
version: 1.0.0
summary: Review gasket paths, compression, corners, seams, latches, cable entries and drainage against an enclosure ingress target.
tags: [enclosure, gasket, ip, sealing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, relevant geometry/drawing/data, constraints, target decision
output_contract: evidence-labelled review, alternatives/risks, missing inputs and verification actions
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: sealing-detail-review
description: Review gasket paths, compression, corners, seams, latches, cable entries and drainage against an enclosure ingress target.
---
# Sealing Detail Review

## Trigger
Use for door sealing, gasket compression, leakage paths or IP-target design questions.

## Workflow
1. Draw/describe one closed seal boundary.
2. List every seam, corner, opening and hardware penetration.
3. Use supplier gasket compression/environment data rather than a guessed universal value.
4. Check door/frame stiffness and latch distribution.
5. Separate design review from IP conformity; specify prototype/test evidence.

## Knowledge to load
- `knowledge/24-sealing-gaskets-and-ingress-details.md`
- `knowledge/05-enclosures-ip-ik.md`
- `design_patterns/enclosures/door-gasket-path.md`

## Output discipline
- Label supplied, calculated, source-backed, assumed, estimated and unknown information.
- Do not invent manufacturer, shop or certification values.
- End with the smallest useful next verification/action.
