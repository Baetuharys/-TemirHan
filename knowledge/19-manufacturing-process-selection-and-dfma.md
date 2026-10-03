---
id: mai-knowledge-manufacturing-process-selection
title: Manufacturing Process Selection and DFMA
category: manufacturing
evidence: practice
last_reviewed: 2026-10-02
verify_before_release: [quantity, tolerances, material/finish, supplier capability, inspection plan]
maturity: implemented
source_ids: []
---

# Manufacturing Process Selection and DFMA

## 1. Do not optimize a part before knowing volume
Prototype, 20-piece batch and 20,000-piece production can justify different tooling and joining strategies. Always capture quantity, repeat demand and acceptable setup cost.

## 2. Process routing questions
For every feature ask:
- which operation creates it?
- does the feature survive the next operation?
- does it need a secondary setup?
- can it be inspected after forming/welding/coating?
- is there tool access and fixture access?
- does it create a special tool, manual rework or hidden setup cost?

## 3. Sheet-metal route
Typical route may include laser/turret → deburr → form → weld/insert hardware → grind/clean → finish → assemble → inspect. The actual route is supplier-specific; use it to identify risk and cost, not as a fixed universal sequence.

## 4. DFMA review
Look for:
- unnecessary unique thicknesses/material grades;
- mirrored parts that can be commonized;
- features requiring special punches/tools without volume justification;
- welds that exist only because locating features are absent;
- inaccessible nuts/screws;
- hardware inserted too early for coating;
- cosmetic surfaces exposed to grinding/handling;
- tolerances tighter than the functional need;
- drawings that mix process instructions with design requirements ambiguously.

## 5. Supplier capability profile
Maintain a project profile containing available material sizes, laser limits, tooling, preferred inside radii, bend table/K data, press-brake envelope, welding capability, finishes, insertion hardware and inspection tools. These project values override generic heuristics.
