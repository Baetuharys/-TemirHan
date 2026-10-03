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
