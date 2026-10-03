# Default workflow — SolidWorks Sheet Metal Workflow

1. Ask version and language once (`knowledge/04`).
2. Choose the start: Base Flange/Tab (native) or Convert to Sheet Metal (imported solid).
3. Set the `Sheet-Metal` parameters: thickness, default radius, bend method, auto-relief.
4. Add features in manufacturing-aware order (flanges → corners → hems → cuts → forming tools → hardware holes) (`knowledge/03`).
5. Flatten; diagnose errors using the error table in `knowledge/03`.
6. Set custom properties; create drawing (bent + flat views) and export DXF.
7. Give each step with the English command name and the Turkish label **only if level V/C**; otherwise `[doğrulanmadı]` plus how to find the command.

## Gate before output
- Method (K-factor/table) matches the shop.
- Normal Cut used for cuts across bends where needed.
- DXF export options include/exclude bend lines deliberately.
- No invented menu path.
