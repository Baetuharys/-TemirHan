# Image-to-CAD Roadmap

## Implemented in v3.0
- grayscale/threshold/edge preprocessing
- line and circle detection
- duplicate-line reduction
- parallel/perpendicular/horizontal/vertical/concentric inference
- two-point scale calibration
- four-point planar perspective helper
- JSON, SVG and ASCII DXF output
- caller-supplied manufacturing minimum checks
- synthetic-image regression test

## Next
1. Contour-based rectangle/slot recognition with topology IDs.
2. Endpoint healing and closed-loop graph reconstruction.
3. Lens calibration profiles and uncertainty propagation.
4. Dimension/text OCR as an optional, separately validated module.
5. Native parametric sketch recipe and SolidWorks macro/API bridge.
6. Bend-line recognition from drawings and flat-pattern semantics.
7. Evaluation dataset with photographed parts and ground-truth CAD.
