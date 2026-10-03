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
