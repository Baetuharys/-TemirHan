---
id: mai-knowledge-image-dimension-estimation
title: Estimating Dimensions from Images (Görselden Ölçü Tahmini)
category: visual-measurement
evidence: calculation
last_reviewed: 2026-10-02
verify_before_release: [physical measurement of the real part for any manufacturing use]
maturity: implemented
source_ids: []
---

# Estimating Dimensions from Images (Görselden Ölçü Tahmini)

## 1. What is possible and what is not
A photograph can give a **scale-based estimate** with an uncertainty. It cannot give a manufacturing dimension. Every number from an image must be labelled **estimate (from image)** with an error range and a confidence level. If the part will be manufactured, measure it physically (caliper, tape, CMM, 3D scan).

## 2. Methods, from best to weakest
| Method | Requirement | Typical error |
|---|---|---|
| **A. Reference object in the same plane** (ruler, A4 sheet, coin, known standard part) | Plane of the object parallel to the camera; reference in the same plane | ~1–3 % when done carefully |
| **B. Known feature of the part** (standard hole, M8 nut, DIN rail width, 19" rack unit) | The feature size is certain | 2–5 % |
| **C. Perspective correction (homography)** using four known points of a rectangle | Four coplanar points, known rectangle size | 1–3 % in the plane |
| **D. Pinhole camera model** `Z = f·H/h` | Known focal length, sensor size, distance | 5–15 %; distance error dominates |
| **E. Multiple views / photogrammetry** | Many overlapping photos + scale bar | ~0.1–1 % with a good setup |
| **F. Visual guess without reference** | none | **Not acceptable as a result**; give a range and say so |

## 3. Core formulas
Scale (method A): `mm_per_pixel = L_ref[mm] / L_ref[px]`;  `L_obj = L_obj[px] × mm_per_pixel`.
Example: an A4 sheet's long side (297 mm) measures 1485 px; the part measures 640 px → 0.2 mm/px → **128 mm**.
Error propagation (relative errors add roughly): if each pixel measurement has ±3 px: `δ ≈ L × (3/1485 + 3/640) ≈ 0.67 %` → ±0.86 mm for 128 mm — the **pixel** error is small; the real error is dominated by perspective and plane mismatch, usually several times larger. Always add a plane/perspective error term.
Pinhole (method D): `Z = f × H / h` where f is the focal length in the same unit as h (convert pixels with sensor pixel size: `pixel_size = sensor_width / image_width_px`).
Depth difference: an object closer to the camera than the reference looks larger; a feature 10 % closer appears ~10 % larger. **Reference and measured feature must be at the same distance.**

## 4. Photographing for measurement (protocol)
1. Camera perpendicular to the measured plane; part centered; avoid wide-angle lenses and phone ultra-wide mode (distortion).
2. Put the reference object **next to the part, in the same plane**; flat, unfolded.
3. Ruler/scale visible along both axes if possible.
4. Same distance for reference and part; no zoom change between shots.
5. Even light; no strong shadows on edges.
6. Take 2–3 photos; keep the original file (not a cropped screenshot).
7. Provide: material, thickness (if known), what is the function of the part.

## 5. Typical error sources
Perspective / camera not perpendicular · lens distortion at the image edges · reference not in the same plane · low resolution (few pixels per mm) · edge blur · compression artifacts · shadows interpreted as edges · reference with unknown real size (a "credit card" is 85.60 × 53.98 mm; A4 is 210 × 297 mm; coins differ between countries).

## 6. Handling sheet-metal parts
- Flat blank (plaka): good for contour estimate, hole positions, overall size.
- Bent part: only projected dimensions in the plane; bend radii and angles need a profile view.
- Thickness: from an edge-on photo with a reference or caliper; an image can tell "about 2 mm", not "1.5 vs 2".
- Hole diameters: measure against a reference at the same plane.
- Reconstructing a flat pattern from a bent photo is possible only with additional bend data; flag as concept.

## 7. Report format (what the AI must return)
| Item | Estimated value | Error range | Confidence (low/med/high) | Method / reference used |
|---|---|---|---|---|
Followed by: assumptions (plane parallel? reference size certain?), what to measure physically, and the statement "estimate from image — not for manufacturing".

## 8. Refusal conditions
No reference object and no known feature → give relative proportions only. Reference at a different distance → say so and give a wider range. Blurry/low-resolution image → list which values could not be read.
