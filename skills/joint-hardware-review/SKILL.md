---
id: mai-skill-joint-hardware-review
title: Joint and Hardware Review
type: skill
status: active
version: 1.0.0
summary: Select and review welds, screws, rivets, self-clinching hardware, hinges and latches from function, access, load and service requirements.
tags: [fasteners, hardware, joints, hinges, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, relevant geometry/drawing/data, constraints, target decision
output_contract: evidence-labelled review, alternatives/risks, missing inputs and verification actions
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: joint-hardware-review
description: Select and review welds, screws, rivets, self-clinching hardware, hinges and latches from function, access, load and service requirements.
---
# Joint and Hardware Review

## Trigger
Use when choosing or troubleshooting a fastener, hinge, latch, weld or serviceable joint.

## Workflow
1. State joint functions: locate, clamp, load, seal, bond, service.
2. Capture sheet stack, access, load, cycles and environment.
3. Compare viable joint families and installation needs.
4. Require current manufacturer data for family-specific sheet/edge/hole requirements.
5. Check assembly, service, corrosion and verification.

## Knowledge to load
- `knowledge/23-joints-fasteners-hinges-and-hardware.md`
- `knowledge/14-welding-fasteners-finishing.md`
- `knowledge/28-supplier-fabricator-rfq-and-handoff.md`

## Output discipline
- Label supplied, calculated, source-backed, assumed, estimated and unknown information.
- Do not invent manufacturer, shop or certification values.
- End with the smallest useful next verification/action.
