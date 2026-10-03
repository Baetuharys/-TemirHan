# Compact Knowledge Bundle — 07-mechanical-design-stiffness-hardware.md


---

## SOURCE FILE: `knowledge/16-design-troubleshooting-and-decision-support.md`

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


---

## SOURCE FILE: `knowledge/22-structural-stiffness-and-load-paths.md`

---
id: mai-knowledge-structural-stiffness-load-paths
title: Structural Stiffness and Load Paths for Sheet-Metal Designs
category: mechanical-design
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [service loads, boundary conditions, material properties, allowable deflection/stress, analysis or test method]
maturity: implemented
source_ids: []
---

# Structural Stiffness and Load Paths for Sheet-Metal Designs

## Start with function, not thickness
When a panel feels weak, first identify **what must not move and under which load**. Increasing thickness is only one option. Returns, beads, ribs, hat sections, shorter unsupported spans, different supports and better load paths can add stiffness with less mass.

## Load-path checklist
Trace the force from where it enters the design to where it reacts. For a cabinet this may be: door equipment → inner panel/stiffener → hinge → frame → shell/base → anchor/floor. A strong local feature does not help if the next interface is flexible.

## Questions before calculation
- Load magnitude/direction and whether static, impact, cyclic or transport-related.
- Support/boundary condition.
- Span and section geometry.
- Material and actual temper/grade.
- Deflection limit and permanent-deformation criterion.
- Connections: spot weld, seam weld, screw, rivet, clinch, adhesive.
- Whether the sheet behaves like a beam, plate or shell.

## Practical stiffness levers
1. Add depth to the section before adding thickness where packaging allows.
2. Put returns/stiffeners along the load path, not decoratively.
3. Break large unsupported panels into smaller effective spans.
4. Avoid abrupt stiffness transitions that concentrate load.
5. Keep stiffeners manufacturable: bend sequence, weld access, coating and drainage still matter.

## Calculation discipline
Simple beam equations are useful only for beam-like members with known boundary conditions. Broad cabinet faces are plates/shells; use an appropriate plate calculation, FEA or physical test when deformation matters. Do not report a beam idealization as exact panel behavior.

## Release evidence
Record the load case, model assumptions, inputs, result, acceptance criterion and verification method. An FEA screenshot without boundary conditions and material definition is not a release record.


---

## SOURCE FILE: `knowledge/23-joints-fasteners-hinges-and-hardware.md`

---
id: mai-knowledge-joints-fasteners-hardware
title: Joints, Fasteners, Hinges and Hardware
category: mechanical-design
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [joint loads, material/thickness, hardware manufacturer data, installation method, access and service conditions]
maturity: implemented
source_ids: []
---

# Joints, Fasteners, Hinges and Hardware

## Choose a joint by function
A joint may locate, clamp, carry shear/tension, transmit torque, seal, conduct/bond, allow service or permanently join. State which functions matter before choosing screws, PEM hardware, rivets, welds or adhesives.

## Selection questions
- Permanent or serviceable?
- One-sided access or two-sided access?
- Parent sheet thickness and material?
- Static, cyclic, vibration or impact load?
- Corrosion/galvanic environment?
- Is electrical bonding required?
- Appearance constraints?
- Installation equipment available?
- How many assembly cycles?

## Sheet-metal hardware checks
For self-clinching or rivet hardware, use the **manufacturer's current datasheet** for minimum sheet thickness, hole preparation, edge distance, installation force and material compatibility. Do not generalize values between families.

## Hinges and latches
Treat hinges and latches as part of the structural and sealing system. Check door center of gravity, opening angle, interference, sag, fastener load path, service removal, latch compression distribution and gasket reaction. More latches may improve compression distribution but also increase cost and user effort.

## Welded vs mechanical joint trade-offs
Welding can reduce part count but introduces heat distortion, finishing effort and repair difficulty. Mechanical fastening improves serviceability but adds holes, hardware, assembly time and possible ingress paths. Compare the complete system rather than unit hardware cost.

## Verification
Use manufacturer ratings and project load cases. For unfamiliar hardware, prototype pull-out/torque/service-cycle behavior in the actual sheet stack before release.


---

## SOURCE FILE: `knowledge/30-engineering-sanity-checks-and-calculation-discipline.md`

---
id: mai-knowledge-engineering-sanity-checks
title: Engineering Sanity Checks and Calculation Discipline
category: engineering-method
evidence: calculation-practice
last_reviewed: 2026-10-02
verify_before_release: [units, input provenance, boundary conditions, independent check where critical]
maturity: implemented
source_ids: []
---

# Engineering Sanity Checks and Calculation Discipline

## Before trusting a result
1. Write units on every input.
2. Label each input SUPPLIED, SOURCE-BACKED, ASSUMED or ESTIMATED.
3. State the model: beam, plate approximation, heat balance, bend model, tolerance stack, cost rollup, etc.
4. Check order of magnitude and limiting cases.
5. Keep more precision internally than you report; do not imply false accuracy.
6. Compare with a second method, known part or prototype when the decision is costly.

## Common AI calculation failures
- mixing mm and m;
- confusing margin and markup;
- applying 90° bend shortcuts at other angles;
- treating K-factor as a material constant;
- summing tolerances by RSS without a statistical basis;
- using air-flow heat balance while ignoring pressure drop/recirculation;
- turning image-derived estimates into manufacturing dimensions.

## Output format
For consequential calculations report: formula/model, inputs with provenance, result, sensitivity to uncertain inputs, assumptions, and verification action. If a missing input dominates the result, ask for it instead of manufacturing a precise number.
