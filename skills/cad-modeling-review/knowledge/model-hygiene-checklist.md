# Model hygiene checklist

- Sketches fully defined; dimensions named where they drive others.
- Features in a logical order; no feature depends on a face that may disappear.
- External references: list them; broken ones are Errors.
- Rebuild without warnings; suppressed features explained.
- Material assigned; density source recorded; mass plausible.
- Configurations named by purpose; the active one is the intended default.
- Custom properties filled for the template (number, description, material, thickness).
- Assembly: no over-defined mates; interference check on key assemblies; units set.
- Export: STEP (neutral 3D), DXF/DWG (flat 2D); file name with part number and revision.
