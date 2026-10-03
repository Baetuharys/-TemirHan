---
id: mai-knowledge-welding-fasteners-finishing
title: Welding, Fasteners and Finishing for Sheet Metal
category: joining-finishing
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [welding procedure specification, fastener manufacturer datasheet, coating supplier specification]
maturity: implemented
source_ids: [ISO-2553-2019]
---

# Welding, Fasteners and Finishing for Sheet Metal (Kaynak, Bağlantı Elemanları, Yüzey İşlemi)

## 1. Joining options
| Method | Good for | Watch out for |
|---|---|---|
| TIG (ISO 4063 process 141) | Thin sheet, stainless, aluminium, visible seams | Slow, skill-dependent |
| MIG/MAG (131 / 135) | Mild steel, production welding | Spatter, distortion on thin sheet |
| Resistance spot (21) | Overlapping sheets, high volume | Needs access from both sides; surface marks |
| Projection welding (23) | Weld nuts/studs | Tooling |
| Laser welding | Low distortion, thin sheet | Fit-up tolerance, equipment |
| Self-clinching fasteners (PEM-type nuts, studs, standoffs) | Threads in thin sheet, no welding | Sheet hardness and minimum thickness limits; hole size; edge distance |
| Welded studs (capacitor discharge) | Studs on thin sheet | Mark on the back side |
| Blind rivets | Fast, no heat | Visual, strength limits |
| Clinching (press joining) | No consumables | Tool access |
| Screws/bolts and nuts | Serviceable joints | Torque, loosening, gasket compression |

## 2. Welding design points
1. **Distortion** grows with heat input and joint length on thin sheet; use short stitch welds + tacks, balanced welding sequence, fixtures, and avoid long continuous seams unless sealing is required.
2. **Sealing seams** (IP enclosures) must be continuous and leak-checked; grind flat if the gasket crosses it.
3. **Galvanised steel**: the zinc coating is burnt away near welds; fumes require extraction; touch-up coating needed.
4. **Stainless**: heat tint reduces corrosion resistance; remove by pickling/passivation after welding; protect from carbon-steel contamination (separate tools).
5. **Aluminium**: oxide layer, high thermal conductivity, filler choice (e.g. 5xxx wire for 5754) — specify per welding procedure.
6. Weld symbols on drawings follow ISO 2553 (reference line, arrow line, elementary symbol, dimensions, "all around" and "field weld" signs). Without a symbol the drawing does not define the weld.
7. Weld quality levels: ISO 5817 (steel/nickel), ISO 10042 (aluminium). Acceptance criteria belong in the specification.

## 3. Self-clinching fasteners (PEM-type)
- The fastener is pressed into a punched/laser-cut hole in a **softer** sheet; the sheet flows into a groove and locks it.
- Check the manufacturer's datasheet for: **minimum sheet thickness**, **hole diameter and tolerance**, **minimum distance hole-centre to edge**, **maximum sheet hardness**, **installation force**, **push-out and torque-out values**.
- The hole for the fastener differs from the clearance hole for a screw; note it on the drawing and in the DXF.
- Do not paint or powder-coat the thread unless masked/ tapped after finishing; define it.
- Install **before** finishing only if the finish is compatible (galvanic/ hardness/ masking).

## 4. Finishing
| Finish | Typical thickness (check supplier) | Notes |
|---|---|---|
| Powder coat (elektrostatik toz boya) | ≈ 60–120 µm per coat, 60–80 µm common | Cures at high temperature; thickness adds to dimensions (both faces + edges); mask threads, earth points, gasket faces if required; specify RAL colour, gloss, texture, standard |
| Wet paint | 40–120 µm by system | Primer + topcoat; solvent rules |
| Electro-galvanising (elektro galvaniz) | ≈ 5–25 µm + passivation | Thin; for indoor or mild environments |
| Hot-dip galvanising (EN ISO 1461) | ≈ 45–100+ µm | For fabricated parts; thin sheet can distort; vent/drain holes needed |
| Pre-galvanised sheet (DX51D+Z) | Z-coating mass, e.g. Z100–Z275 | Cut edges and welds unprotected |
| Stainless passivation / pickling | — | Restores passive layer after welding; specify method and standard |
| Anodising (aluminium) | ≈ 5–25 µm (type II); hard anodising thicker | Colour variation between batches; dimensional growth |
| Brushed / polished (stainless, aluminium) | Grain direction | Specify grit and direction; protective film |
| Passive: oiling, protective film | — | Shipping protection |

Specify: finish type, thickness range, colour/standard, **areas to mask**, **hanging mark locations**, and acceptance criteria (adhesion, appearance).

## 5. Interaction with enclosure design
A coating on a gasket face changes flatness and compression; a coated earth-bonding point loses electrical continuity unless masked; powder coat bridges small gaps and hides weld porosity until it breaks at the edge. See `05-enclosures-ip-ik.md`.

## 6. Review checklist
Joint accessibility for the welder/tool · distortion plan · seam type (continuous/ stitch) matches function · weld symbols present · fastener datasheet values respected · finish compatible with material and with hardware · masking defined · hanging marks defined · inspection method.
