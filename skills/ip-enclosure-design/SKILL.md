---
id: mai-skill-ip-enclosure-design
title: IP Enclosure Design
type: skill
status: active
version: 1.0.0
summary: Analyze enclosure design requirements against a requested IP rating and identify sealing, joints, entries and testing considerations.
tags: [design, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: ip-enclosure-design
description: Analyse sheet-metal enclosure design against an IP/IK target: leakage paths, gaskets, glands, vents, drainage, thermal, test plan. Use for sac kabin, pano, IP54/IP65/IP66, IK, NEMA karşılaştırması.
---
# IP Enclosure Design

## Purpose
Design review of a sheet-metal cabinet against a target IP code. Output is design risk, not certification.

## Trigger
Analyse sheet-metal enclosure design against an IP/IK target: leakage paths, gaskets, glands, vents, drainage, thermal, test plan. Use for sac kabin, pano, IP54/IP65/IP66, IK, NEMA karşılaştırması.

## Required inputs
Target IP code, environment, mounting, door/seam description or model/drawing, list of cut-outs and cable entries, purchased parts' own ratings (glands, switches, fans).

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Restate the target and what each digit demands (`reference/ip-codes.md`).
2. List every opening and seam. For each: sealing method, owner (design / purchased part), risk.
3. Check the weakest element: the rating of the whole enclosure is limited by its weakest opening.
4. Check door seal: gasket type, compression stop, overlap or labyrinth, hinge side, lock pull-in.
5. Check weld/seam closure, drain/vent decisions, and how they change the rating.
6. List test or evidence needed (lab test, supplier certificates) and what the design can and cannot claim.

## Required checks
- Never states a rating as achieved. - Every opening listed. - Purchased parts' ratings taken from supplied data, not assumed.

## Output contract
Table: opening | risk | sealing method | owner | open question. Then verdict wording that stays at "targets".

## Failure modes
- Stating that an IP rating is guaranteed from geometry.
- Forgetting cable glands, vents and mounting holes as leakage paths.
- Treating NEMA types as identical to IP codes.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/05-enclosures-ip-ik.md`
- `knowledge/14-welding-fasteners-finishing.md`
- `reference/ip-codes.md` (quick card)

## Self-test
1. IP65 target with a vent fan: model must flag that the fan rating limits the enclosure.
2. Stitch-welded seam in an IPx5 target: model must flag.
3. User asks "is this IP66?": model must answer in terms of design intent and required test.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
