# Compact Knowledge Bundle — 01-sheet-metal-materials.md


---

## SOURCE FILE: `knowledge/01-sheet-metal-fundamentals.md`

---
id: mai-knowledge-sheet-metal-fundamentals
title: Sheet Metal Fundamentals (Sac Levha Temelleri)
category: sheet-metal
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [shop capability list, material certificate, customer standard]
maturity: implemented
source_ids: []
---

# Sheet Metal Fundamentals (Sac Levha Temelleri)

**How to read this file.** Values marked *typical* are engineering-practice ranges that differ between shops, machines and tooling. They are starting points for a design review, never production limits. The authoritative value is the one in the fabricator's capability sheet.

## 1. What "sheet metal" is
Sheet metal (sac, sac levha) is flat rolled metal, normally 0.4–6 mm thick; above ~6 mm it is usually called plate (levha / kalın sac). Parts are cut flat, formed by bending, joined and finished. Almost every sheet-metal decision follows from one fact: **the part is designed 3D but manufactured from a flat blank**.

## 2. Manufacturing chain (üretim zinciri)
```text
Material → Cutting (laser / punch / plasma / waterjet) → Deburring →
Forming (press brake bending, rolling, forming tools) → Joining (welding, PEM/clinch,
rivet, screw) → Surface finish (powder coat, galvanizing, passivation, anodizing) →
Assembly → Inspection → Packing
```
A design decision always has a cost and a risk in at least one later step. Ask "what does this do to the next step?"

## 3. Common materials in Türkiye (grade names on quotes and drawings)
| Common TR name | Typical EN designation | Notes |
|---|---|---|
| DKP (soğuk haddelenmiş sac) | DC01 (EN 10130) | Clean surface, good bending, needs paint/coating against rust |
| HRP / siyah sac (sıcak haddelenmiş) | S235JR (EN 10025) or DD11 | Cheaper, scale on surface, thicker gauges |
| Galvaniz sac | DX51D+Z (EN 10346) | Zinc coating is damaged by welding and laser edges; coating mass (e.g. Z100, Z275) must be specified |
| Paslanmaz 304 | 1.4301 / AISI 304 | Austenitic, work-hardens, springback higher than mild steel |
| Paslanmaz 316L | 1.4404 / AISI 316L | Better chloride resistance (marine, chemical) |
| Alüminyum 5754 | EN AW-5754 (AlMg3) | Good formability and weldability, common for enclosures |
| Alüminyum 5052 | EN AW-5052 (AlMg2.5) | Common outside Europe; do not treat as identical to 5754 without checking |
| Alüminyum 1050 | EN AW-1050 | Very soft, low strength |

Equivalence tables are approximate. For anything certified (pressure, food, marine, rail) use the exact standard and the mill certificate (3.1 test certificate / 3.1 sertifika).

Typical stock thicknesses (mm): 0.5 · 0.6 · 0.8 · 1.0 · 1.2 · 1.5 · 2.0 · 2.5 · 3.0 · 4.0 · 5.0 · 6.0 · 8.0 · 10.0. Always confirm that the thickness is stocked in the chosen grade; a 1.25 mm sheet is not a standard grade-independent choice. Thickness tolerance (EN 10131 for cold-rolled, EN 10051 for hot-rolled, EN 485-4 for aluminium) is part of the real part-to-part variation and affects bends and fits.

## 4. Cutting processes
| Process | Strength | Typical limitation |
|---|---|---|
| Fiber laser | Fast on thin to medium sheet, narrow kerf, fine detail | Heat-affected edge; reflective metals need suitable machine; thick-plate speed drops |
| CO₂ laser | Good edge on thicker mild steel | Slower on thin sheet than fiber |
| Turret punch | Fast for many holes and forms (louvers, ribs), tools create features | Tool library limits shape; burr direction |
| Plasma | Thick plate, low cost | Wider kerf, rougher edge |
| Waterjet | No heat-affected zone, any material | Slow, taper on thick material |

Laser kerf is typically 0.1–0.3 mm depending on thickness, nozzle and material. Nested parts are separated by a web (typically ≥ 1 × thickness, shop dependent).

## 5. Design rules of thumb (typical values)
All distances in terms of material thickness **T** and inside bend radius **R**. Check against the fabricator.

| Rule | Typical starting value | Why |
|---|---|---|
| Inside bend radius | ≥ 1 × T for mild steel; larger for 5xxx/6xxx aluminium, hard tempers, stainless | Cracking on the outside of the bend |
| Minimum flange length (after bend) | ≈ 3–4 × T + R, tooling dependent | Flange must sit on the die shoulder |
| Hole centre-to-bend line | ≥ 2.5 × T + R (hole edge to bend start ≥ ~2 T) | Hole distorts into an oval if too close |
| Slot or cut-out edge to bend | ≥ 3 × T + R | Same distortion |
| Hole diameter (laser, steel) | ≥ ~1 × T | Heat and dross; stainless may need more |
| Hole diameter (punch) | ≥ ~1–1.5 × T | Punch strength |
| Hole edge to sheet edge | ≥ 1.5–2 × T | Tear-out and edge bulge |
| Bend relief width | ≥ T (often ≥ 1.0–1.5 × T) | Prevents bulging and tearing at the end of a bend |
| Bend relief depth | ≥ R + T (+ small margin) | Relief must go past the bend tangent line |
| Hem (closed) | Min. inner radius & flat-length rules are shop specific | Cracks if the material is not annealed enough |
| Grain direction | Bend across the rolling direction when possible, esp. for stainless/aluminium | Cracking along the grain |

## 6. Features commonly formed in sheet
Louvers (panjur), lances, extruded/tapped holes, embossed ribs (nervür), countersinks, offsets/jogs, hems, flanged holes, dimples. Formed features need a **tool** (standard or custom); a feature that is not in the shop's tool library becomes a custom tool or a different process, with cost and lead time.

## 7. Tolerances that are realistic
Typical achievable values (shop dependent): laser cut contour ±0.1–0.2 mm; punched features ±0.1–0.2 mm; bend angle ±0.5°–1° (air bending); bend position/leg length ±0.2–0.5 mm accumulating per bend; flatness of larger sheets is limited by the material. A "±0.05" requirement on a bent dimension is normally not realistic and needs measurement and process planning. See `knowledge/07-gdt-and-tolerancing.md` for ISO 2768.

## 8. Joining (short)
Welding (TIG, MIG/MAG, spot), self-clinching fasteners (PEM-type nuts, studs, standoffs), blind rivets, screws, clinching, adhesive. Details in `knowledge/14-welding-fasteners-finishing.md`.

## 9. Common failure patterns
1. Hole or cut-out too close to a bend → deformed feature.
2. No relief at the end of a bend → tearing and bulging.
3. Flat pattern generated with a K-factor that does not match the shop's process → parts too long/short after bending.
4. Dimensioning the bent part from the wrong side (inside vs outside) → accumulated error.
5. Using a thickness that is not stocked in the required grade.
6. Painting or powder-coating a surface that is also a gasket, grounding (earth bonding), or press-fit surface without masking.
7. Specifying a finish without specifying where the hanging marks may be.

## 10. What to ask when information is missing
Material and grade · thickness · quantity · process and machine · inside radius or tooling · K-factor or bend table source · finish · tolerance class · delivery form (DXF, STEP, drawing) · acceptance criteria.


---

## SOURCE FILE: `knowledge/02-bending-and-flat-pattern.md`

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


---

## SOURCE FILE: `knowledge/15-materials-reference.md`

---
id: mai-knowledge-materials-reference
title: Materials Reference for Sheet-Metal Work
category: materials
evidence: source-dependent
last_reviewed: 2026-10-02
verify_before_release: [mill certificate, material standard, supplier datasheet]
maturity: implemented
source_ids: []
---

# Materials Reference for Sheet-Metal Work (Malzeme Referansı)

Values here are **typical handbook values for first-pass work**. Certified work uses the standard and the mill certificate (3.1). Densities differ slightly between sources; always state the value used.

## 1. Density and plate weight per m²
Weight per m² of plate = `T[mm] × ρ[kg/m³] / 1000`. Plate weight = area × that value.

| Material | ρ (kg/m³) | 1 mm | 2 mm | 3 mm | 5 mm | 10 mm |
|---|---|---|---|---|---|---|
| Carbon steel DC01 / S235JR | 7850 | 7.85 | 15.70 | 23.55 | 39.25 | 78.50 |
| Stainless 1.4301 (304) | 7930 | 7.93 | 15.86 | 23.79 | 39.65 | 79.30 |
| Stainless 1.4404 (316L) | 7990 | 7.99 | 15.98 | 23.97 | 39.95 | 79.90 |
| Aluminium EN AW-5754 | 2670 | 2.67 | 5.34 | 8.01 | 13.35 | 26.70 |
| Aluminium EN AW-5052 | 2680 | 2.68 | 5.36 | 8.04 | 13.40 | 26.80 |
| Aluminium EN AW-1050 | 2710 | 2.71 | 5.42 | 8.13 | 13.55 | 27.10 |
| Copper (Cu-ETP) | 8960 | 8.96 | 17.92 | 26.88 | 44.80 | 89.60 |
| Brass CuZn37 | 8440 | 8.44 | 16.88 | 25.32 | 42.20 | 84.40 |
| Titanium grade 2 | 4510 | 4.51 | 9.02 | 13.53 | 22.55 | 45.10 |

Example: 1 m × 2 m × 3 mm carbon steel = 2 m² × 23.55 kg/m² = **47.1 kg**; in stainless 304 → 47.58 kg; in EN AW-5754 → 16.02 kg.
For a finished part use the CAD mass properties and mark them *calculated*; add hardware, welds and coating separately.

## 2. Grade designations and approximate equivalents
| Common name | EN | Other designations (approximate, verify) |
|---|---|---|
| DKP | DC01 (EN 10130) | St12 (old DIN), SPCC (JIS) |
| HRP / black sheet | S235JR (EN 10025-2); DD11 | St37-2 (old DIN) |
| Galvanised | DX51D+Z (EN 10346) | — |
| Stainless 304 | 1.4301 (X5CrNi18-10) | AISI 304 |
| Stainless 316L | 1.4404 (X2CrNiMo17-12-2) | AISI 316L |
| Stainless 430 | 1.4016 | AISI 430 (ferritic, magnetic) |
| Aluminium 5754 | EN AW-5754 (AlMg3) | — |
| Aluminium 5052 | EN AW-5052 (AlMg2.5) | — |
| Aluminium 1050 | EN AW-1050A | — |
Equivalent does not mean identical; chemical limits, tolerances and mechanical properties differ.

## 3. Typical mechanical and physical values (order of magnitude)
| Property | Carbon steel | Stainless 304 | Aluminium 5xxx |
|---|---|---|---|
| Young's modulus E | ≈ 200–210 GPa | ≈ 190–200 GPa | ≈ 69–70 GPa |
| Coefficient of thermal expansion | ≈ 11–12 ×10⁻⁶ /K | ≈ 16–17 ×10⁻⁶ /K | ≈ 23–24 ×10⁻⁶ /K |
| Yield strength (annealed/typical) | DC01 ≈ ≤ 280 MPa; S235 ≥ 235 MPa | ≈ 200–300 MPa (higher after cold work) | 5754-H22 ≈ 130–190 MPa |
| Tensile strength | DC01 ≈ 270–410 MPa; S235 ≈ 360–510 MPa | ≈ 500–700 MPa | 5754-H22 ≈ 220–290 MPa |
| Magnetic | yes | austenitic: normally not (weakly after forming) | no |
Treat these as ranges; temper, thickness and standard edition change them.

## 4. Forming behaviour
Mild steel: forgiving, small radii OK. Stainless: work-hardens, higher bending force and springback; larger radii. Aluminium 5xxx: good formability in soft tempers; harder tempers crack on tight radii; bend across grain.

## 5. Corrosion and environment
Mild steel needs coating. Galvanised: edges/welds exposed. Stainless 304: indoor, mild; 316L: chlorides/marine/chemical; passivation after welding. Aluminium: oxide layer; galvanic coupling with steel/stainless in wet environments needs isolation.

## 6. Weight calculation checklist
Use the **blank** area for material purchase and the **finished** mass for shipping. Confirm: grade, density used, thickness (nominal vs measured), cut-outs subtracted, coating thickness, hardware. State the formula and units: `m = V·ρ` with V in m³ and ρ in kg/m³.

## 7. What the AI must not do
Give a precise strength or equivalence without naming the standard and condition · treat 5052 and 5754 as the same · assume stainless density = steel density in a quote · invent a certificate number.
