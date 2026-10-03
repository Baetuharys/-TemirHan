---
id: mai-knowledge-image-to-cad
title: Image to CAD Geometry Reconstruction
category: image-cad
evidence: method
last_reviewed: 2026-10-02
verify_before_release: [scale calibration, perspective, geometry review, drawing dimensions, manufacturing release]
maturity: implemented
source_ids: []
---

# Image → CAD Geometry Reconstruction

The repository includes an executable engine under `engines/image_to_cad/`. Its purpose is **draft reconstruction**, not dimensional certification.

## Pipeline
1. preprocess raster;
2. detect lines/circles;
3. de-duplicate geometry;
4. infer geometric relations (parallel/perpendicular/horizontal/vertical/concentric);
5. optionally calibrate pixels to mm using a known reference;
6. validate basic geometry/manufacturing limits supplied by the user;
7. export JSON/SVG/DXF;
8. review in CAD before release.

## Scale hierarchy
Best to worst:
1. dimension explicitly printed on a drawing;
2. calibration target in the same plane;
3. known component with verified size in the same plane;
4. multiple consistent references;
5. perspective-corrected estimate;
6. no reference → proportions only, no mm claim.

## Uncertainty
Calibration error, pixel selection, perspective, lens distortion and edge ambiguity all contribute. If the result is image-derived, use `ESTIMATED` until checked against authoritative dimensions.

## Native CAD
A DXF created from detected geometry is not equivalent to a parametric SolidWorks model. Preserve the JSON model so a future SolidWorks adapter can reconstruct constraints/features while retaining provenance.

## Release gate
No image-derived dimension should become a manufacturing dimension merely because it looks plausible. Require a drawing, measurement, supplier model, or explicit user validation for release-critical geometry.
