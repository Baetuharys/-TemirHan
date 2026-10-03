---
id: mai-knowledge-solidworks-sheet-metal
title: SolidWorks Sheet Metal Workflow
category: solidworks
evidence: software-behavior
last_reviewed: 2026-10-02
verify_before_release: [SolidWorks version, installed language, add-in/licence level, shop bend table]
maturity: implemented
source_ids: [SW-HELP-DXF]
---

# SolidWorks Sheet Metal Workflow

**Version warning.** Command names, dialog layout and defaults change between SolidWorks releases and between language packs. This file uses the **English command names**. In a Turkish interface, look the command up with the command search box or the right-click menu, and use the label the user actually sees (see `04-solidworks-turkish-ui-and-terminology.md`). Never invent a menu path.

## 1. Two ways to start a sheet-metal part
1. **Native sheet-metal modelling** — begin with *Base Flange/Tab* from a sketch (open or closed profile). The part gets a `Sheet-Metal` feature (holds default bend radius, thickness, K-factor/bend method, auto-relief) and a `Flat-Pattern` feature that is suppressed until you flatten.
2. **Convert a solid** — *Convert to Sheet Metal* (shell the solid first, choose the fixed face and bend edges, then add rips). Useful for imported geometry; needs clean, uniform wall thickness.

## 2. Core features (English names)
| Feature | Use |
|---|---|
| Base Flange/Tab | First wall; open sketch → bends are added automatically with the default radius |
| Edge Flange | Add a flange along an edge (angle, length convention, position, relief) |
| Miter Flange | Flanges along a sketched path with mitred corners |
| Hem | Open/closed/teardrop/rolled edge |
| Jog | Offset step in a flat wall |
| Sketched Bend | Bend along a sketched line in a flat region |
| Lofted-Bend | Transition between two profiles (cones, hoppers) |
| Closed Corner | Close the gap between two flanges at a corner |
| Break-Corner / Corner-Trim | Chamfer or round sheet corners |
| Forming Tool | Louvers, ribs, extrusions from the tool library |
| Vent | Grille/vent patterns |
| Rip | Open a sharp edge in a shell |
| Insert Bends | Convert a solid to sheet-metal bends |
| Unfold / Fold | Temporarily flatten selected bends to cut across them |
| Flatten (Flat-Pattern) | Toggle the full flat pattern |
| Normal Cut (option in Extruded Cut) | Cut perpendicular to the sheet through formed surfaces; needed for cuts across bends in a way that flattens correctly |

## 3. Bend parameters — the settings that control flat-length
In the `Sheet-Metal` feature (and each flange) choose how the flat length is computed:
- **K-Factor** — enter the ratio.
- **Bend Allowance** — enter the length directly.
- **Bend Deduction** — enter the deduction directly.
- **Bend Table** — lookup file (Excel or text) by material, thickness, radius, angle.
- **Gauge table** — table of allowed thickness/radius combinations per material; applies thickness and radius automatically.

Key rule: **the CAD method must match the shop's process.** If the shop uses its own bend table, the same table has to be loaded in the SolidWorks file or the flat DXF will be wrong. Record the method in the drawing note (e.g. "Flat pattern generated with K = 0.40, ref. shop bend table rev. B").

## 4. Auto-relief and corners
Relief type options: **Rectangular, Obround, Tear**. Choose by process: tear relief is cheapest but leaves a sharp edge; rectangular and obround are cut by laser/punch. Relief ratio and corner treatment are part of the model, not an afterthought.

## 5. Typical modelling sequence for an enclosure
1. Define thickness, material, default radius, bend method (Sheet-Metal feature).
2. Base Flange/Tab (back panel) → Edge Flanges (sides) → Closed Corner / corner relief.
3. Hems and return flanges for stiffness and sealing faces.
4. Cuts: use Extruded Cut with *Normal Cut* for features crossing bends; add forming tools (louvers) from the library.
5. Add holes for hardware; confirm clearance holes vs PEM/clinch holes (different diameters).
6. Flatten; inspect for overlaps, self-intersection, relief and bend lines.
7. Check the bounding box against the sheet format.
8. Set custom properties (material, thickness, finish, weight, revision).
9. Create the drawing (flat pattern view + bent view) and the DXF.

## 6. Flat pattern and DXF export
- Right-click the `Flat-Pattern` feature (or use the export command) to export DXF/DWG. Export options include which entities (geometry, bend lines, forming tool markers, sketches) and the bend-line layer/linetype.
- **Cut geometry and bend lines must be separable** (different layer/colour) so the laser does not cut the bend lines. See `skills/solidworks-dxf-release-check`.
- Always open the DXF in a viewer or the CAM system before release; check units (mm), scale 1:1, no stray sketch geometry, no hidden duplicate lines.
- If the part contains forming tools, decide whether the DXF should include only the cut outline (usual for laser) or marking geometry.

## 7. Common errors and what to check
| Symptom | Likely cause | Check |
|---|---|---|
| Flat-Pattern is red/fails to flatten | Overlap, missing relief, closed corner without gap, thickness inconsistency | Highlight the failing face in the error message; add relief; verify one fixed face |
| Bend lines missing in DXF | Export option off | Export options → bend lines |
| Flat length differs from shop result | Wrong K-factor / bend table | Compare with a test bend; align table |
| Cut across bends is distorted in flat | Cut made in folded state with perpendicular-to-face instead of Normal Cut | Use Normal Cut or unfold → cut → fold |
| Hole becomes oval in the flat | Hole is on a bend region | Move away from the bend; see distance rules |
| Imported STEP will not convert | Non-uniform thickness, fillets not matching | Rebuild as native sheet metal |

## 8. Custom properties and cut list
Useful part properties for release: material, thickness, finish, weight, revision, drawing number, part number. For sheet-metal parts the cut list can carry sheet-metal data (thickness, bounding box length/width, number of bends) — check the exact property names in the installed version because they differ between versions and languages.
