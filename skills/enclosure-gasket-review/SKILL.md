---
id: mai-skill-enclosure-gasket-review
title: Sheet Metal Enclosure Gasket Review
type: skill
status: active
version: 0.3.0
summary: Review gasket, cover, flange, cable-entry, ventilation, drainage, and joint features against an enclosure sealing requirement.
tags: [enclosure, ip, gasket, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: enclosure-gasket-review
description: Review gasket, sealing line, compression and fastening of a sheet-metal enclosure door or cover. Use for conta seçimi/sıkışma, kapak sızdırmazlığı, IP kaçak yolu, gasket groove vs flat gasket.
---
# Sheet Metal Enclosure Gasket Review
## Workflow
1. State the required enclosure protection level and the environment; do not infer an IP requirement from appearance.
2. Identify sealing interfaces: door/cover perimeter, removable panels, cable entries, ventilation elements, and service openings.
3. Check gasket continuity, compression concept, corner transitions, flange width, fastener spacing concept, and assembly accessibility.
4. Check whether bends, welds, seams, and fasteners create leak paths or local gasket discontinuities.
5. Treat cable glands, vents, filters, drains, locks, and hinges as part of the enclosure boundary.
6. Separate standard-backed requirements from engineering practice and supplier-specific recommendations.
7. Define how compliance would be verified; design intent alone is not test evidence.

## Output
Return boundary map, risk points, missing inputs, design actions, and verification/test plan.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/05-enclosures-ip-ik.md`
- `knowledge/14-welding-fasteners-finishing.md`
- `reference/ip-codes.md` (quick card)
