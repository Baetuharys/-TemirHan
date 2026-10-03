---
id: mai-knowledge-bending-flat-pattern
title: Bending and Flat Pattern (Büküm ve Açınım)
category: sheet-metal
evidence: formula
last_reviewed: 2026-10-02
verify_before_release: [K-factor source, bend table, press brake tooling]
maturity: implemented
source_ids: []
---

# Bending and Flat Pattern (Büküm ve Açınım)

## 1. Symbols
| Symbol | Meaning |
|---|---|
| T | material thickness (mm) |
| R | **inside** bend radius (mm) |
| θ | bend angle = the angle the flange is turned through. A flat sheet is 0°; a right-angle bend is 90° |
| K | K-factor = distance of the neutral axis from the inside surface ÷ T |
| BA | bend allowance (bükme payı) |
| BD | bend deduction (bükme düşümü) |
| OSSB | outside setback |

Always state whether θ is the *turned* angle (90° for an L) or the *included* angle (also 90° for an L, but 45° turned vs 135° included for a shallow bend). For anything other than 90° this is the most common source of error.

## 2. Formulas
```text
BA   = θ[rad] × (R + K·T)            θ[rad] = θ[°] × π / 180
OSSB = (R + T) × tan(θ / 2)
BD   = 2 × OSSB − BA
```
- If flanges are dimensioned **outside to outside**:   `Flat length = Σ(outside flange lengths) − Σ(BD)`
- If dimensioned **to the bend tangent lines (inside/flat segments)**:   `Flat length = Σ(flat segments) + Σ(BA)`

## 3. K-factor is not a constant
K depends on material, thickness, radius, bending method (air bend, bottoming, coining), tooling and grain direction. Common textbook starting values for **air bending, mild steel** (use only when no shop data exists, and label the result as an estimate):

| R / T | Starting K (estimate) |
|---|---|
| < 1 | ≈ 0.33 |
| 1 – 3 | ≈ 0.38 – 0.42 |
| > 3 | ≈ 0.45 – 0.50 |

Stainless and hard aluminium alloys behave differently (more springback, different neutral-axis shift). The correct K is obtained from: (1) the fabricator's bend table, (2) a **test bend** (measure the flat length before and after), or (3) the supplier's published data.

## 4. Worked example A — single 90° bend
T = 2 mm, R = 2 mm, θ = 90°, K = 0.40, outside legs 50 mm and 30 mm.
- BA = (π/2) × (2 + 0.4×2) = **4.398 mm**
- OSSB = (2 + 2) × tan 45° = **4.000 mm**
- BD = 2×4.000 − 4.398 = **3.602 mm**
- Flat length = 50 + 30 − 3.602 = **76.398 mm**
Check by the second method: flat segments are 50 − 4 = 46 and 30 − 4 = 26 mm, so 46 + 26 + 4.398 = 76.398 mm ✓.

## 5. Worked example B — U-channel
T = 1.5 mm, R = 1.5 mm, K = 0.38, outside dimensions 20 / 60 / 20 mm, two 90° bends.
- BA = (π/2) × (1.5 + 0.38×1.5) = 3.252 mm; OSSB = 3.0 mm; BD = 6.0 − 3.252 = **2.748 mm** per bend.
- Flat length = 100 − 2×2.748 = **94.503 mm**.

## 6. Press brake basics (V-die air bending)
| Thickness T | Typical V-die opening (rule of thumb) |
|---|---|
| < 3 mm | ≈ 6 × T |
| 3 – 10 mm | ≈ 8 × T |
| 10 – 12 mm | ≈ 10 × T |
| > 12 mm | ≈ 12 × T |

- Minimum flange length (air bending) is about **0.7 × V** (V = 8 × 3 = 24 mm gives ≈ 17 mm for a 3 mm sheet). This is why 3 mm sheet with a 10 mm flange is a tooling problem.
- In air bending the inside radius is determined by the die opening (≈ 0.16 × V for mild steel), not by the punch tip. Specifying a radius that does not match any available V-die forces bottoming/coining or special tools.
- Bend force grows with T² / V and with material strength; stainless needs noticeably more than mild steel for the same geometry.
- Springback: expect a few degrees on stainless and high-strength steel; the machine compensates by over-bending, but part-to-part spread remains.
- Bend sequence: the last bends must not collide with the machine, the punch or the already formed flanges. Deep boxes need a gooseneck or special punches; U-shaped sections with narrow openings may be impossible to form in one piece.

## 7. Features near bends
Hole, slot or notch too close to a bend line → distorts. Use the distances in `01-sheet-metal-fundamentals.md` as a starting point; the safer alternative is to move the feature, add relief, or punch/laser it after bending (secondary operation, higher cost).

## 8. Reliefs and corners
- **Bend relief** (büküm boşaltması): small notch at the end of a bend to prevent tearing.
- **Corner relief** (köşe boşaltması): needed where two bends meet; closed corners need a gap (typically ≥ T) or weld/overlap definition.
- **Rip / yırtma**: a deliberate slit at a box corner so the flat blank can unfold.

## 9. Hems (kıvırma)
Open hem, closed hem (flattened), teardrop hem. Closed hems usually need a two-stage process (pre-bend at ~30° then flatten). The flat-length rule differs from a normal bend; use the shop's value or test.

## 10. Flat pattern checklist
1. Material, thickness, grade confirmed.
2. K-factor or bend table source identified and recorded **in the drawing note**.
3. All bends have direction (up/down), angle, radius.
4. Flat pattern bounding box compared with the expected sheet size.
5. Feature-to-bend distances checked.
6. Bend lines are on a separate layer in DXF (not cut).
7. A test part has been bent and measured before releasing a large series.

## 11. What the AI must not do
- Quote a K-factor as if it were a material constant.
- Give a bend radius as "standard" without naming the die and the shop.
- Present a calculated flat length as validated without a source for K.
