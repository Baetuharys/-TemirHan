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
