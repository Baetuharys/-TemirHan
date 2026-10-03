---
id: mai-knowledge-technical-drawing
title: Technical Drawing for Sheet Metal (Teknik Resim)
category: technical-drawing
evidence: standard-derived
last_reviewed: 2026-10-02
verify_before_release: [company drawing standard, customer standard, edition of ISO 128 / 129 / 5457 / 7200]
maturity: implemented
source_ids: [ISO-2768-1-1989, ISO-2553-2019, ISO-21920-1-2021]
---

# Technical Drawing for Sheet Metal (Teknik Resim)

## 1. Purpose
A drawing is a **contract**: it states what must be delivered and how it will be inspected. A model alone is not a contract unless the company works model-based (MBD) and agrees that.

## 2. Standards map (where to look)
| Question | Family |
|---|---|
| Line types, views, sections | ISO 128 series |
| Dimensioning principles | ISO 129-1 |
| Sheet sizes and layout | ISO 5457 |
| Title block | ISO 7200 |
| Scales | ISO 5455 |
| General tolerances | ISO 2768-1, ISO 2768-2 (replaced by ISO 22081 for geometrical general tolerances; check which your customer cites) |
| Geometrical tolerancing | ISO 1101; datums ISO 5459; ASME Y14.5 in US practice |
| Tolerancing principle | ISO 8015 (independence principle) |
| Surface texture | ISO 21920 series (older: ISO 1302 / ISO 4287) |
| Welding symbols | ISO 2553 |
| Welded structures general tolerance | ISO 13920 |
| Threads | ISO 6410 (representation), ISO 261/262 (metric) |
Verify the current edition before citing.

## 3. Sheet sizes and projection
A0 841×1189, A1 594×841, A2 420×594, A3 297×420, A4 210×297 (mm). Europe/Türkiye: **first-angle projection** (symbol: truncated cone, ISO). US: third angle. Always show the projection symbol.

## 4. Title block (minimum for release)
Part number · name · revision (with date and change description) · material and grade · thickness (sheet) · general tolerance note (e.g. ISO 2768-m) · surface finish/coating · scale · sheet size · units · projection symbol · drawn/checked/approved · company / confidentiality note · weight (if required) · mass tolerance if relevant. For sheet metal: "**flat pattern generated with K = … / bend table …**".

## 5. Views for a bent sheet-metal part
- Front/side/top views to define the **bent** shape.
- **Flat pattern view** (açınım) with overall flat dimensions and bend lines (direction, angle, radius).
- Detail and section views where needed.
- A 3D reference view is helpful but is not a dimension source.
- Bend table or bend notes: "BEND UP 90° R2" style, per bend, or a table with bend ID, direction, angle, inner radius.

## 6. Dimensioning rules
1. Each dimension once; no duplicates.
2. Do not make closed dimension chains (over-definition) — choose the functional chain.
3. State the convention for bent dimensions (to **outside** virtual sharp, to inside, or to mid-line). For sheet metal, "to outside virtual sharp" is common, but state it.
4. Dimension from datums that match the **inspection** and **assembly** method.
5. Holes: diameter, count, position from datums, tolerance only if functional; indicate PEM/clinch holes with part reference.
6. Radii: inside radius, thickness-based note acceptable.
7. Chamfers and countersinks: angle and diameter.
8. Do not dimension the flat pattern and the bent part from conflicting references.
9. Reference dimensions in brackets (REF).

## 7. Notes that belong on sheet-metal drawings
- Material/grade and thickness tolerance reference.
- General tolerances.
- Deburr and break sharp edges (e.g. 0.2–0.5 mm; state if different).
- Grain direction (if relevant).
- Surface finish and where it must **not** be applied (gasket, ground contact).
- Welding symbols or note: seam type, length, continuous/intermittent.
- Inspection requirements, e.g. critical dimensions marked.
- Packaging/marking if applicable (laser etching).

## 8. Revision control
Every change → new revision letter/number, date, description, who approved. A drawing issued without a revision is not controllable. The BOM, the model and the DXF carry the same revision.

## 9. Review checklist (use as skill output)
Classify each finding as **Error** (blocks manufacture/inspection), **Risk** (ambiguous), **Suggestion**.
1. Title block complete? 2. Views sufficient? 3. Flat pattern present? 4. Dimension conflicts? 5. Tolerance statement present? 6. Datum scheme coherent? 7. Bend notes correct and matching count? 8. Finish and masking? 9. Material and thickness consistent with BOM/model? 10. Revision consistent across documents? 11. Values read from an image are flagged as "read from image".

## 10. Failure patterns
No general tolerance note · flat pattern missing · K-factor not stated · inside/outside mix · dimension chain closed · GD&T frame references an undefined datum · title-block material differs from the BOM · revision not updated after a model change · DXF shows bend lines as cut lines.
