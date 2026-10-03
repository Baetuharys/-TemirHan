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
