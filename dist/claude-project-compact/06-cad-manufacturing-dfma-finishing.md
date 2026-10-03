# Compact Knowledge Bundle — 06-cad-manufacturing-dfma-finishing.md


---

## SOURCE FILE: `knowledge/09-cad-engineering-practice.md`

---
id: mai-knowledge-cad-engineering-practice
title: CAD Engineering Practice (CAD Mühendislik Pratiği)
category: cad
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [company PDM rules, customer file-exchange requirements]
maturity: implemented
source_ids: []
---

# CAD Engineering Practice (CAD Mühendislik Pratiği)

## 1. File formats and what each is for
| Format | Use | Pitfall |
|---|---|---|
| Native (SLDPRT, SLDASM, SLDDRW) | Design work | Needs the same CAD and often the same version; references break when files move |
| STEP (.stp/.step, AP203/214/242) | Neutral 3D exchange | No feature tree; check units; configurations are not preserved |
| Parasolid (.x_t/.x_b) | Exchange between Parasolid-based CAD | Version limits |
| IGES | Legacy surface exchange | Stitching problems; avoid for solids |
| DXF / DWG | 2D profiles for laser/punch, drawings exchange | Units, layers, splines, scale, bend lines |
| PDF | Released drawing | Not a data source; vector PDF preferred over scan |
| STL / 3MF | 3D printing, visualisation | Mesh only |
| 3D PDF / eDrawings | Review | Not for manufacturing data |
Rule: release **drawing PDF + DXF (flat) + STEP (3D)** with the same revision label.

## 2. Naming and numbering
Part numbers are meaningful identifiers, not descriptions. Keep the number short, unique, immutable; put description in the properties. File name = part number + revision only if the PDM does not manage revisions. Avoid spaces, Turkish characters (ç, ğ, ı, ö, ş, ü) and special characters in file names exchanged with other systems, to avoid encoding problems.

## 3. Folder and reference hygiene
- One project folder, relative references, no local-drive links.
- Use **Pack and Go** (or the CAD's equivalent) for sending a complete assembly.
- Do not rename a file outside the CAD; use the CAD's rename or PDM so references update.
- Library parts (standard hardware) come from a controlled library, not a copy per project.

## 3b. Revision and change control
Revision in the title block, the model's properties and the file/PDM label must agree. A change requires: reason, scope, affected parts/drawings, approval, date. Keep the previous revision accessible (archive), never overwrite released files silently.

## 4. Modelling practice
1. Sketches fully defined; limit sketch complexity.
2. Capture design intent with a few master sketches/parameters/global variables rather than hundreds of ad-hoc dimensions.
3. Name important features and dimensions.
4. Use configurations/design tables for variants (sizes) instead of copies.
5. Keep assemblies mate-clean: fix the first component, avoid over-mated assemblies, use sub-assemblies to reflect real build structure.
6. Use lightweight/large-assembly modes on big assemblies; avoid circular references.
7. Check interference and clearance before release.
8. Keep units consistent (mm-g-s; or per company standard). Confirm the unit on imported files.

## 5. Release package for a sheet-metal part
| Item | Check |
|---|---|
| 3D model | Material, thickness, mass |
| Drawing PDF | Revision, general tolerances, flat pattern, finish |
| DXF | Units mm, 1:1, bend lines separable, no stray geometry |
| BOM | Quantity, material, revision |
| Notes for quote | Quantity, finish, tolerances, delivery date |
| Change record | What changed since last revision |

## 6. Mass properties
Mass = volume × density; density comes from the material assigned in CAD and must match the real grade (e.g. 1.4301 ≈ 7900–8000 kg/m³, DC01 ≈ 7850 kg/m³, EN AW-5754 ≈ 2670 kg/m³). Coatings, welds, hardware and cut-outs affect the real mass. Mass in a CAD model is a *calculated* value; label it so.

## 7. Model-based definition (MBD) in short
Product and manufacturing information (PMI) attached to the 3D model can replace drawings **only** if the customer and quality system accept it. Otherwise keep the 2D drawing as the contractual document.

## 8. Handling of imported geometry
Check units and scale; check for gaps/sliver faces; heal faces; verify sheet thickness; rebuild as native sheet-metal when it will be flattened; do not trust an imported model's flatten result without a thickness check.

## 9. Data security
Customer drawings and models are confidential. Do not paste them into public tools; use approved environments (see `training/DATA-GOVERNANCE.md`).


---

## SOURCE FILE: `knowledge/14-welding-fasteners-finishing.md`

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


---

## SOURCE FILE: `knowledge/19-manufacturing-process-selection-and-dfma.md`

---
id: mai-knowledge-manufacturing-process-selection
title: Manufacturing Process Selection and DFMA
category: manufacturing
evidence: practice
last_reviewed: 2026-10-02
verify_before_release: [quantity, tolerances, material/finish, supplier capability, inspection plan]
maturity: implemented
source_ids: []
---

# Manufacturing Process Selection and DFMA

## 1. Do not optimize a part before knowing volume
Prototype, 20-piece batch and 20,000-piece production can justify different tooling and joining strategies. Always capture quantity, repeat demand and acceptable setup cost.

## 2. Process routing questions
For every feature ask:
- which operation creates it?
- does the feature survive the next operation?
- does it need a secondary setup?
- can it be inspected after forming/welding/coating?
- is there tool access and fixture access?
- does it create a special tool, manual rework or hidden setup cost?

## 3. Sheet-metal route
Typical route may include laser/turret → deburr → form → weld/insert hardware → grind/clean → finish → assemble → inspect. The actual route is supplier-specific; use it to identify risk and cost, not as a fixed universal sequence.

## 4. DFMA review
Look for:
- unnecessary unique thicknesses/material grades;
- mirrored parts that can be commonized;
- features requiring special punches/tools without volume justification;
- welds that exist only because locating features are absent;
- inaccessible nuts/screws;
- hardware inserted too early for coating;
- cosmetic surfaces exposed to grinding/handling;
- tolerances tighter than the functional need;
- drawings that mix process instructions with design requirements ambiguously.

## 5. Supplier capability profile
Maintain a project profile containing available material sizes, laser limits, tooling, preferred inside radii, bend table/K data, press-brake envelope, welding capability, finishes, insertion hardware and inspection tools. These project values override generic heuristics.


---

## SOURCE FILE: `knowledge/25-corrosion-finishing-and-material-compatibility.md`

---
id: mai-knowledge-corrosion-finishing-compatibility
title: Corrosion, Surface Finishing and Material Compatibility
category: materials-manufacturing
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [environment, base material, finish specification, supplier process, galvanic contacts, masking and grounding requirements]
maturity: implemented
source_ids: []
---

# Corrosion, Surface Finishing and Material Compatibility

## Environment first
Indoor dry, outdoor rain, coastal salt, chemical washdown, condensation and buried/contact environments create different risks. Do not choose a coating by appearance alone.

## Design-for-finish checklist
- Drain/vent closed cavities where the process requires it.
- Avoid inaccessible crevices and water traps.
- Include coating buildup in tight fits, threads and gasket stacks.
- Define masking where electrical bonding or precision fits require bare metal.
- Check edge coverage and cut-edge condition.
- Ensure weld spatter/grind condition matches finish quality.
- Separate dissimilar metals when the environment and area ratio create galvanic risk.

## Powder coating
Specify the base material, pretreatment expectations, colour/texture, appearance class if relevant, masking and critical post-coat dimensions. A nominal coating thickness should come from the approved process/supplier specification rather than AI memory.

## Stainless and aluminium
Do not treat all stainless or aluminium grades as interchangeable. Fabrication route, chloride exposure, surface contamination, welding and cleaning can dominate performance.

## Release record
Record finish system and approved supplier/process reference, not only a colour name. Confirm how repaired welds/cut edges and field modifications will be protected.
