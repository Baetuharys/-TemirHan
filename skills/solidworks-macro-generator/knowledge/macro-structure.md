# Macro structure

1. Header: purpose, version assumption, 'NOT EXECUTED' or 'tested on <file> in <version>'.
2. Get SldWorks via `Application.SldWorks`; get the active document; check type with `GetType`.
3. Validate inputs (names from the user, not defaults).
4. Store original state.
5. Do the work inside a single error-protected block.
6. Restore state; report results; list parts that failed.

Core members used in the templates (all documented in the SolidWorks API Help; confirm for your version): `SldWorks.ActiveDoc`, `ModelDoc2.GetType`, `ModelDoc2.GetActiveConfiguration`, `ModelDoc2.ShowConfiguration2`, `PartDoc.GetPartBox`, `ModelDoc2.Extension.CustomPropertyManager`, `CustomPropertyManager.Get6 / Add3`, `AssemblyDoc.GetComponents`, `Component2.GetModelDoc2`.

Assembly traversal sketch: get components (top level or all), for each get its model document, skip suppressed/lightweight components unless resolved, apply the step, log failures, continue.
Bounding box from `GetPartBox` is an axis-aligned box of the part's geometry in the current configuration; sheet-metal cut-list bounding-box properties may differ in orientation; state which one is used.
