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
