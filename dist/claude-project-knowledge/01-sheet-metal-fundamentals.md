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
