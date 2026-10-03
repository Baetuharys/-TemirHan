# Compact Knowledge Bundle — 04-drawing-gdt-tolerances-quality.md


---

## SOURCE FILE: `knowledge/06-technical-drawing.md`

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


---

## SOURCE FILE: `knowledge/07-gdt-and-tolerancing.md`

---
id: mai-knowledge-gdt-tolerancing
title: GD&T and General Tolerances (Geometrik Toleranslandırma)
category: gdt
evidence: standard-derived
last_reviewed: 2026-10-02
verify_before_release: [ISO 1101 / ASME Y14.5 edition, ISO 2768 / ISO 22081 edition, customer standard]
maturity: implemented
source_ids: [ISO-1101-2017, ISO-5459-2024, ASME-Y14.5-2018-R2024, ISO-2768-1-1989]
---

# GD&T and General Tolerances (Geometrik Toleranslandırma)

## 1. Why GD&T
Plus/minus tolerances control a size but not its form, orientation or location relative to functional surfaces. GD&T states **function-based** requirements with datums that match how the part is assembled and inspected. Use it only where function demands it; sheet-metal parts are mostly controlled by general tolerances plus a few critical features.

## 2. Symbols (ISO 1101 geometrical characteristics)
| Type | Characteristic | Needs datum? | Typical sheet-metal use |
|---|---|---|---|
| Form | Straightness | No | Long edges, rails |
| Form | Flatness | No | Sealing face, mounting plate |
| Form | Circularity (roundness) | No | Rolled cylinders |
| Form | Cylindricity | No | Rolled/welded cylinders |
| Profile | Profile of a line | Optional | Cross-section of a formed section |
| Profile | Profile of a surface | Optional | Formed shape, cut contour |
| Orientation | Parallelism | Yes | Flange parallel to base |
| Orientation | Perpendicularity | Yes | Side wall to base |
| Orientation | Angularity | Yes | Non-90° flanges |
| Location | Position | Yes | Hole patterns, PEM holes |
| Location | Concentricity / Coaxiality | Yes | Rare in sheet metal |
| Location | Symmetry | Yes | Slots centered on a part |
| Run-out | Circular run-out | Yes | Rotating parts |
| Run-out | Total run-out | Yes | Rotating parts |
ISO 1101 lists concentricity and symmetry separately; ASME Y14.5 has not included concentricity and symmetry since the 2009 edition (position and profile are used instead). State which standard the drawing follows.

## 3. Feature control frame
`| symbol | ⌀ tolerance value + modifier | datum A | datum B | datum C |`
- A ⌀ in front of the value means a cylindrical tolerance zone (hole position).
- Modifiers: Ⓜ maximum material condition (MMC), Ⓛ least material condition (LMC), Ⓟ projected tolerance zone, Ⓕ free state (non-rigid parts, relevant for thin sheet metal). Use only if the function (assembly clearance) justifies it.
- Datum order matters: primary (3 points of contact), secondary (2), tertiary (1).

## 4. Datum strategy for sheet metal
- The datum surfaces should be **stable and reachable**: a flat mounting face, a large flange, a pattern of holes.
- Avoid datums on bent corner radii or on thin unsupported flanges.
- A thin sheet is non-rigid: state the **restraint condition** in the note (e.g. ISO 10579 non-rigid parts), or the part will measure differently on every fixture.
- Choose datums to match assembly: the face that touches the mounting surface is datum A; hole pattern for fasteners is the location reference (B, C).

## 5. Selection guide (what to control and how)
| Requirement | Control |
|---|---|
| Mounting face must be flat | Flatness (e.g. 0.3 mm) |
| Door flange must be parallel to the frame | Parallelism to datum A |
| Hole pattern fits a mating part | Position of holes, ⌀ zone, with MMC if clearance holes |
| Slot centered on edge | Symmetry (ISO) or position (ASME) |
| Contour of a formed part | Profile of a surface |
| Side wall square to base | Perpendicularity |
Do not mix many controls on one feature without need; every frame adds inspection cost.

## 6. ISO 2768-1 general tolerances (linear dimensions, mm)
| Nominal range | f (fine) | m (medium) | c (coarse) | v (very coarse) |
|---|---|---|---|---|
| 0.5 – 3 | ±0.05 | ±0.1 | ±0.2 | — |
| > 3 – 6 | ±0.05 | ±0.1 | ±0.3 | ±0.5 |
| > 6 – 30 | ±0.1 | ±0.2 | ±0.5 | ±1 |
| > 30 – 120 | ±0.15 | ±0.3 | ±0.8 | ±1.5 |
| > 120 – 400 | ±0.2 | ±0.5 | ±1.2 | ±2.5 |
| > 400 – 1000 | ±0.3 | ±0.8 | ±2 | ±4 |
| > 1000 – 2000 | ±0.5 | ±1.2 | ±3 | ±6 |
| > 2000 – 4000 | — | ±2 | ±4 | ±8 |

Angular tolerance by length of the shorter leg:
| Length (mm) | f / m | c | v |
|---|---|---|---|
| up to 10 | ±1° | ±1°30′ | ±3° |
| > 10 – 50 | ±0°30′ | ±1° | ±2° |
| > 50 – 120 | ±0°20′ | ±0°30′ | ±1° |
| > 120 – 400 | ±0°10′ | ±0°15′ | ±0°30′ |
| > 400 | ±0°5′ | ±0°10′ | ±0°20′ |

For sheet-metal bent parts, class **m** is the usual default; the achievable bend angle (±0.5°–1°) and leg length depend on process. A class **f** requirement across bends is typically unrealistic. A drawing written "ISO 2768-mK" refers to linear (m) and geometrical (K, from ISO 2768-2). ISO 22081 has since replaced ISO 2768-2 for geometrical general tolerances; verify which one the customer cites.

## 7. Fits (shaft/hole) — only a pointer
ISO 286 (IT grades and fit letters such as H7/g6) applies to machined features; sheet-metal holes are normally governed by general tolerance or an IT-class stated on the drawing (laser holes seldom reach IT8 without secondary operations).

## 8. How to avoid over-tolerancing
1. State the function. 2. Choose the loosest tolerance that works. 3. Check against the process capability (laser ±0.1–0.2, bend ±0.5°). 4. Check that the inspection method exists (CMM, gauge, optical). 5. Remove the tolerance if no function requires it.

## 9. Common GD&T mistakes
Datums not defined on the drawing · datum on a feature that moves · position tolerance relative to a free-form edge · missing datum order · ⌀ missing on a hole pattern · tolerance tighter than the manufacturing process · MMC without a clearance check · flatness tighter than the size tolerance allows.


---

## SOURCE FILE: `knowledge/17-tolerance-stack-and-fits.md`

---
id: mai-knowledge-tolerance-stack
title: Tolerance Stack, Fits and Functional Clearances
category: tolerancing
evidence: formula-and-practice
last_reviewed: 2026-10-02
verify_before_release: [drawing standard, process capability, datum scheme, measurement method]
maturity: implemented
source_ids: [ISO-1101-2017, ISO-5459-2024, ASME-Y14.5-2018-R2024, ISO-2768-1-1989]
---

# Tolerance Stack, Fits and Functional Clearances

## 1. Separate three questions
- **Nominal geometry:** what is the intended size/location?
- **Allowed variation:** what tolerance is assigned and under which standard?
- **Functional result:** what clearance/interference/misalignment may occur at assembly?

A drawing can be dimensionally “within tolerance” and still fail function if the datum scheme or stack path is wrong.

## 2. 1-D worst-case stack
For a signed chain `R = ±A ±B ...`, use the same signs for nominals and calculate worst-case bounds from each contributor’s limits. The helper in `tools/calculators/tolerance.py` is appropriate only when the stack is genuinely one-dimensional.

## 3. RSS/statistical stack
RSS is **not** a magic tighter tolerance. Use it only if the statistical assumptions are justified by process data and the tolerances have been converted to compatible statistical quantities. Otherwise use worst-case or a process-capability model agreed with quality/manufacturing.

## 4. Sheet-metal realities
- bend angle/radius variation can convert into large edge-position error over long flanges;
- formed features may require profile/position concepts rather than very tight ± dimensions;
- welding adds distortion and fixture dependence;
- coating thickness affects tight fits, grounding points and gasket interfaces;
- laser-cut accuracy does not imply bent-assembly accuracy.

## 5. Datum selection
Datums should represent the functional locating interfaces and a realistic inspection setup. Do not choose a thin free edge as a primary datum simply because it is convenient on the drawing.

## 6. General tolerances
If a drawing references a general-tolerance standard, verify the **edition and scope**. The source registry notes that ISO 2768-1:1989 remained published while a replacement edition was under publication in 2026. Do not silently assume an old company title-block note is still current.

## 7. Output expected from the AI
A useful tolerance answer includes the stack path, signs, nominal result, worst-case result, any statistical assumption, the functional requirement being protected, and a recommendation for which dimensions should be controlled directly.


---

## SOURCE FILE: `knowledge/26-metrology-inspection-and-quality-planning.md`

---
id: mai-knowledge-metrology-inspection-quality
title: Metrology, Inspection and Quality Planning
category: quality
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [critical characteristics, measurement method, gauge capability, sampling/acceptance plan, datum setup]
maturity: implemented
source_ids: [ISO-5459-2024, ISO-1101-2017]
---

# Metrology, Inspection and Quality Planning

## Design dimensions that can be verified
A dimension or GD&T control is only useful if manufacturing and inspection can establish the referenced features/datums. Avoid creating an elegant drawing that requires an unavailable measurement setup for every part.

## Characteristic classes
Separate:
- safety/regulatory or interface-critical characteristics;
- function-critical dimensions;
- process-control dimensions;
- reference/information-only dimensions.

This helps avoid inspecting every dimension with the same effort.

## Measurement planning
For each critical item state: nominal/tolerance, datum setup, tool or method, access/orientation, frequency or sampling rule, recording requirement and reaction plan. Match measurement uncertainty/capability to the tolerance being judged.

## Sheet-metal realities
Formed parts relax when unclamped; flexible panels can be distorted by the fixture. Define whether inspection is free-state, restrained or assembled when this changes the result. Measure hole patterns and interfaces from functional datums rather than accumulating chained dimensions where possible.

## First article / prototype
Use early builds to validate both the part and the measurement method. A repeated disagreement between CAD and inspection can be a datum/fixture problem, not only a fabrication problem.
