# Image → CAD Geometry Engine

This is the implemented successor to the earlier scaffold. It converts a raster image into **draft engineering geometry**: preprocessing → Hough line/circle detection → de-duplication → constraint inference → optional real-world calibration → DXF/SVG/JSON export → simple manufacturing checks.

## Important boundary

The engine does **not** claim that a photo is a manufacturing drawing. Geometry extracted from images is tagged `ESTIMATED` until a known scale/reference and CAD review exist. Perspective, lens distortion, hidden geometry and ambiguous edges can create large errors.

## Quick use

```bash
pip install -r engines/image_to_cad/requirements.txt
python -m engines.image_to_cad.cli part.png --out out
python -m engines.image_to_cad.cli part.png --out out --ref-p1 100 100 --ref-p2 500 100 --ref-mm 200
```

Outputs: `geometry.json`, `geometry.svg`, `geometry.dxf`.

## What it intentionally does not do yet

- infer bends or 3D sheet-metal topology from a single photograph;
- claim exact dimensions without calibration;
- create native `.SLDPRT` directly;
- replace a human DXF/CAD release review.

The JSON geometry model is the interoperability boundary for future SolidWorks/FreeCAD automation.
