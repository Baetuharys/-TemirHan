# Config switch and restore (VBA template)

```vb
Option Explicit
' Template: switch a part to a named configuration, read its bounding box, restore the original.
' NOT EXECUTED in this repository. Test on a COPY of the file first.
' Verify every member in the SolidWorks API Help of your version.

Dim swApp As SldWorks.SldWorks

Sub main()
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim origConfig As String
    Dim targetConfig As String
    Dim box As Variant
    Dim restored As Boolean

    On Error GoTo ErrHandler
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then MsgBox "No document open.": Exit Sub
    If swModel.GetType <> swDocPART Then MsgBox "Run this on a part.": Exit Sub

    targetConfig = "<FLAT-PATTERN CONFIGURATION NAME>"      ' SUPPLIED by the user: do not guess

    origConfig = swModel.GetActiveConfiguration().Name       ' remember original state
    If Not swModel.ShowConfiguration2(targetConfig) Then
        MsgBox "Configuration not found: " & targetConfig: Exit Sub
    End If

    Set swPart = swModel
    box = swPart.GetPartBox(True)                           ' array xmin,ymin,zmin,xmax,ymax,zmax in metres
    If IsEmpty(box) Then MsgBox "No bounding box.": GoTo Restore

    Debug.Print "Length(mm)=" & (box(3) - box(0)) * 1000 & "  Width(mm)=" & (box(4) - box(1)) * 1000

Restore:
    restored = swModel.ShowConfiguration2(origConfig)       ' always return the user's configuration
    Exit Sub

ErrHandler:
    On Error Resume Next
    If Len(origConfig) > 0 Then swModel.ShowConfiguration2 origConfig
    MsgBox "Macro stopped: " & Err.Description
End Sub
```
