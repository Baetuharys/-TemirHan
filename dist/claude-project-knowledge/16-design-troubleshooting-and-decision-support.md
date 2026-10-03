---
id: mai-knowledge-design-troubleshooting
title: Design Troubleshooting and Decision Support
category: cad-engineering
evidence: practice
last_reviewed: 2026-10-02
verify_before_release: [project requirements, interface dimensions, manufacturing capability, safety-critical assumptions]
maturity: implemented
source_ids: []
---

# Design Troubleshooting and Decision Support

This file defines how the assistant should help when the user is **stuck**, not only when a formula is requested.

## 1. Start from the failure mode, not the CAD command
Translate “this design feels wrong” into one or more observable problems:
- interference / collision;
- weak or flexible panel;
- impossible bend sequence;
- hole/slot distortion near a bend;
- inaccessible fastener or tool;
- door/gasket compression inconsistency;
- water/dust ingress path;
- assembly stack-up mismatch;
- excessive part count or welding;
- hard-to-inspect datum scheme;
- cost driven by process rather than material.

## 2. Five-layer diagnosis
1. **Requirement:** what must the part do and what is non-negotiable?
2. **Geometry:** dimensions, interfaces, envelopes, clearances, datums.
3. **Material/process:** thickness, grade, bend/weld/laser/coating constraints.
4. **Assembly/service:** sequence, tool access, replaceability, cable/airflow access.
5. **Verification:** how will the requirement be measured or tested?

Do not jump from symptom to one “best” design. Generate 2–4 viable alternatives when the trade-off is real.

## 3. Option format
For each concept state:
- what changes;
- which problem it addresses;
- new risks introduced;
- manufacturing impact;
- drawing/CAD changes required;
- what must be verified before release.

## 4. Common sheet-metal rescue patterns
Use as **patterns**, not automatic answers:
- add return flange/bead/rib instead of only increasing thickness;
- move or resize bend-adjacent features;
- split a collision-prone one-piece body into controlled subassemblies;
- use tabs/slots or locators to control weld assembly;
- change fastener direction or captive hardware for service access;
- isolate gasket compression from weld distortion;
- add drip/labyrinth geometry so sealing is not dependent on a single edge;
- change datum selection to match functional interfaces and inspection setup.

## 5. “I don’t know what to ask” intake
If the user only provides a screenshot or rough idea, recover the task with at most three high-value questions: intended function/environment, key dimensions/material/process, and what outcome is currently failing. Then continue with a provisional analysis rather than blocking the conversation.

## 6. Decision rule
Prefer a design that satisfies the stated requirement with the **fewest hidden process assumptions**. If two concepts are both viable, explain the trade-off instead of declaring a winner without the user’s priorities.
