---
id: mai-skill-image-to-cad-reconstruction
title: Image to CAD Reconstruction
type: skill
status: active
version: 1.0.0
summary: Guide and execute draft image-to-CAD reconstruction using scale calibration, perspective control, geometry confidence and DXF/JSON review. Never treats photo-derived geometry as manufacturing truth.
tags: [image, cad, dxf, geometry, reconstruction]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: task context, available drawings/CAD/images/data, constraints, desired decision or deliverable
output_contract: evidence-labelled engineering analysis, risks, unresolved inputs, verification actions, next step
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: image-to-cad-reconstruction
description: Guide and execute draft image-to-CAD reconstruction using scale calibration, perspective control, geometry confidence and DXF/JSON review. Never treats photo-derived geometry as manufacturing truth.
---
# Image to CAD Reconstruction

## Trigger
Use for tracing parts/drawings/photos into editable draft geometry or evaluating whether a reference image is adequate for CAD reconstruction.

## Workflow
1. Determine whether the image is a drawing, scan, orthographic photo or perspective photo.
2. Find an authoritative scale reference or restrict output to proportions.
3. Correct perspective when a planar reference is available.
4. Run or emulate the geometry-engine pipeline and retain confidence/provenance.
5. Review topology/constraints and compare against known dimensions.
6. Export draft DXF/JSON only with an explicit CAD-review release gate.

## Knowledge to load
- `knowledge/20-image-to-cad-geometry-reconstruction.md`
- `knowledge/08-image-dimension-estimation.md`

## Output discipline
- Distinguish facts, calculations, practice, assumptions, estimates and unknowns.
- Do not upgrade a draft analysis into a certification or release claim.
- Prefer a concrete next action over generic advice.
