# Compact Knowledge Bundle — 02-solidworks.md


---

## SOURCE FILE: `knowledge/03-solidworks-sheet-metal.md`

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


---

## SOURCE FILE: `knowledge/04-solidworks-turkish-ui-and-terminology.md`

---
id: mai-knowledge-solidworks-turkish-ui
title: SolidWorks Turkish Interface and Terminology
category: solidworks-turkish
evidence: unverified-ui-labels
last_reviewed: 2026-10-02
verify_before_release: [every Turkish UI label against a Turkish installation]
maturity: implemented
source_ids: []
---

# SolidWorks Turkish Interface and Terminology

## 1. The honest status
The Turkish **UI labels** in this library are **not verified** against an installed Turkish SolidWorks. A made-up button name is worse than none, so the library treats labels in three confidence levels:

| Level | Meaning | How the AI writes it |
|---|---|---|
| **V** (verified) | Copied from a screenshot or text supplied by a user with the stated SolidWorks version | Use the Turkish label as shown |
| **C** (common) | Widely used core term, high confidence, still unverified for the specific version | Use it, add "(ekranda farklı görünebilir)" if the step matters |
| **U** (unverified) | Not checked | Write the English command name; put `[doğrulanmadı]` next to any Turkish guess |

Machine-readable file: `reference/solidworks-ui-labels.csv` (EN command, TR label, level, version, source, note). Anyone can fill it from screenshots.

## 2. Three layers that must never be mixed
1. **UI path** — what to click (language and version dependent).
2. **Feature / property name** — what appears in the FeatureManager tree or in custom properties (language dependent; a property created in a Turkish session keeps its Turkish name).
3. **API name** — macro/API identifiers are **always English** (`ModelDoc2`, `FeatureManager`, `CustomPropertyManager`).

## 3. Core terms with level C (confidence: common)
| English | Turkish | Level |
|---|---|---|
| Part | Parça | C |
| Assembly | Montaj | C |
| Drawing | Teknik resim | C |
| Sketch | Eskiz | C |
| Feature / FeatureManager | Özellik / Özellik Yöneticisi | C |
| Dimension | Ölçü | C |
| Configuration | Konfigürasyon | C |
| Rebuild | Yeniden oluştur | U |
| Sheet metal | Sac levha | C (trade term); menu label U |
| Flat pattern | Açınım / Düz açınım | C (trade term); feature label U |

Everything else is U until verified. Do **not** extend this table without evidence.

## 4. How the AI should answer a SolidWorks question in Turkish
1. Ask once for the **SolidWorks version** and whether the UI is Turkish.
2. Give the English command name first when the Turkish label is U: "**Edge Flange** (Kenar Flanşı olabilir — ekranda doğrula)".
3. Tell the user how to find the command without knowing the label: type the English or Turkish word in the command search box, or right-click the feature in the tree.
4. Offer a screenshot request when the label matters: "Menünün ekran görüntüsünü gönderirsen Türkçe adı kayda geçiririm."
5. Never write a menu path as if it were certain when it is U.

Example answer (U-level command):
> Sac levha parçada kenarı bükmek için **Edge Flange** komutunu kullan. Türkçe arayüzde adı sürüme göre değişebilir; komut arama kutusuna "flanş" veya "edge" yazarak bulabilirsin. Ekranda gördüğün adı yazarsan sonraki adımlarda onu kullanırım.

## 5. Capture protocol (how to verify labels quickly)
1. Open a Turkish SolidWorks; note the version (Help → About).
2. For each command: screenshot of the toolbar tooltip *and* of the PropertyManager title.
3. Fill one row in `reference/solidworks-ui-labels.csv`: `en_command, tr_label, level=V, version, source=screenshot, note`.
4. Run `python scripts/validate_reference.py` to check the CSV.
5. Re-run the evaluation set (`training/eval`) to confirm the AI uses V rows correctly.

## 6. Turkish technical writing policy (summary)
Order of preference: exact UI label → standard term → established shop term → Öztürkçe word where it is already in real use and unambiguous → coined words only as marked suggestions. Full rules: `docs/terminology-policy.md`. Glossary: `reference/glossary-sacmetal.md`.


---

## SOURCE FILE: `knowledge/13-solidworks-macros-api.md`

---
id: mai-knowledge-solidworks-macros-api
title: SolidWorks Macros and API (Makro ve API)
category: macros
evidence: software-behavior
last_reviewed: 2026-10-02
verify_before_release: [every API member against the API Help of the user's SolidWorks version, macro run on a copy of the file]
maturity: implemented
source_ids: [SW-HELP-2026-VBA, SW-HELP-2026-FLATPATTERN-ENUM]
---

# SolidWorks Macros and API (Makro ve API)

## 1. Why macros are risky for an AI to write
The SolidWorks API is large and changes between releases (members are added as `...2`, `...3` versions, older ones are obsolete). A model that "remembers" an API call can invent a member or use the wrong argument list. The macro will either not compile, silently do nothing, or **modify the file wrongly**. The library therefore uses strict rules.

## 2. Rules for generated macros
1. Ask for: SolidWorks version, document type (Part/Assembly/Drawing), what is selected, desired result, whether the macro may modify the file.
2. Use only API members the AI can name with certainty; mark every other call `' VERIFY: check IModelDoc2 members in API Help for your version`.
3. **Read-only first.** Start with macros that read and report; add write operations (properties, save, export) only when requested.
4. Always check for `Nothing`: no active document, wrong document type, empty selection.
5. Never delete features/files in a first version; never overwrite the original; write output next to it with a new name.
6. Add `Option Explicit`, clear variable types, error handling, a message at the end that says what was done.
7. API names are English even in a Turkish interface; message texts to the user may be Turkish.
8. Tell the user to **test on a copy** and to save before running.
9. Do not claim the macro was run or tested unless the user supplied the result.
10. Avoid selecting by display names that change with language; prefer type-based traversal.

## 3. Skeleton A — report the document and its mass (read-only, VBA)
```vb
Option Explicit
Dim swApp As SldWorks.SldWorks

Sub main()
    Set swApp = Application.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "Açık belge yok."
        Exit Sub
    End If

    Dim swMass As SldWorks.MassProperty
    Set swMass = swModel.Extension.CreateMassProperty   ' VERIFY: newer versions may offer CreateMassProperty2
    If swMass Is Nothing Then
        MsgBox "Kütle özellikleri alınamadı."
        Exit Sub
    End If

    MsgBox swModel.GetTitle & vbCrLf & _
           "Kütle (kg): " & Format(swMass.Mass, "0.000") & vbCrLf & _
           "Hacim (m^3): " & Format(swMass.Volume, "0.000000")
End Sub
```
Notes: mass depends on the material assigned in the model and on the active configuration; the value is **calculated**, not weighed.

## 4. Skeleton B — write a custom property (modifies the file)
```vb
Option Explicit
Dim swApp As SldWorks.SldWorks

Sub main()
    Set swApp = Application.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then Exit Sub

    Dim swPropMgr As SldWorks.CustomPropertyManager
    Set swPropMgr = swModel.Extension.CustomPropertyManager("")   ' "" = file-level properties

    Dim rc As Long
    rc = swPropMgr.Add3("Revision", swCustomInfoType_e.swCustomInfoText, "A", _
                        swCustomPropertyAddOption_e.swCustomPropertyReplaceValue)
    ' VERIFY: interpret rc with the Add3 return enumeration in API Help
    MsgBox "Revision özelliği yazıldı. Dosyayı kaydetmeyi unutmayın."
End Sub
```
Notes: the property name is a string chosen by the user's template; property names created in a Turkish session keep their Turkish text. Configuration-specific properties use the configuration name instead of `""`.

## 5. Skeleton C — list configuration names
```vb
Dim names As Variant
names = swModel.GetConfigurationNames
Dim i As Long
For i = LBound(names) To UBound(names)
    Debug.Print names(i)
Next i
```

## 6. Typical macro tasks (and the risk of each)
| Task | Risk | Safer approach |
|---|---|---|
| Fill title-block properties | Overwriting | Only-if-new option; log old values |
| Batch export DXF of flat patterns | Wrong flat/bend-line options, configuration | Export one part first; inspect the DXF; use the export-options API of the installed version (verify) |
| Rename/renumber files | Broken references | Prefer PDM or CAD rename tools; macro only logs |
| Update drawing revision tables | Version differences | Read first, write later |
| Apply a material or finish | Wrong density → wrong mass | Use library materials; verify result |
| Batch STEP export | Large assemblies slow | Test one |

## 7. Debugging checklist
Compile error · type-library references missing (SldWorks, swconst) · `Nothing` objects · wrong document type · array bounds · version difference · 64-bit vs 32-bit declarations (`PtrSafe`) · running macros from a network path.

## 8. Security
Run only macros from trusted sources; review code before running; keep macro security enabled; never run a macro that downloads or executes external code unless you wrote it.

## 9. What the AI must say when unsure
"Bu API üyesinin adını/argümanlarını sürümünüz için doğrulayamıyorum. API Help'te `IModelDoc2` altında arayın ya da makro kaydedicisiyle bir örnek kaydedip bana gönderin; ona göre uyarlayayım."
