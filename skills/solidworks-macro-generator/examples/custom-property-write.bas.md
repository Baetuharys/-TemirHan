# Custom property read/write (VBA template)

```vb
Option Explicit
' Template: write a custom property to the active part. NOT EXECUTED here; test on a copy.
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim cpm As SldWorks.CustomPropertyManager
    Dim val As String, resolved As String
    Dim wasResolved As Boolean, link As Boolean
    Dim ret As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then MsgBox "No document open.": Exit Sub

    Set cpm = swModel.Extension.CustomPropertyManager("")    ' "" = file-level properties
    ' read (verify the Get overload available in your version)
    ret = cpm.Get6("<PROPERTY NAME>", False, val, resolved, wasResolved, link)
    ' write: type 30 = text; last argument decides overwrite
    ret = cpm.Add3("<PROPERTY NAME>", 30, "<VALUE>", 1)
End Sub
```
