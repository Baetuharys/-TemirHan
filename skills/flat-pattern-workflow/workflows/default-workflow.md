# Default workflow — Flat Pattern Workflow

1. Confirm material, thickness, radii, and the bend method used by the **shop**, not only by CAD.
2. Flatten and check for errors (overlaps, failed bends, missing relief, closed corners).
3. Check feature-to-bend distances (see `knowledge/01`, `knowledge/02`).
4. Compute the expected flat length by hand for one or two bends as a sanity check (`knowledge/02`).
5. Verify bounding box against the sheet format and nesting.
6. Prepare bend lines on a separate layer; decide marking geometry.
7. Record method and revision in the drawing note; export DXF; open and inspect.
8. Recommend a test bend before series release.

## Gate before output
- K-factor or bend table source recorded.
- Units mm, scale 1:1.
- Bend lines are not cut lines.
- Hole/slot distortion near bends considered.
