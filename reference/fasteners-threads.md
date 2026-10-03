# Metric fasteners — quick reference (verify against the actual standard/product)

Designation `M4 x 15`: **M4** = metric thread, nominal (major) diameter 4 mm; **15** = length in mm.
For screws the length reference is standard-dependent (e.g. under-head length for most head styles;
for countersunk heads the overall length). Pitch is coarse unless stated (`M4 x 0.5` would be fine pitch).
Head diameter, head height and wrench size are NOT contained in the designation; they come from the product standard (ISO 4762, ISO 7380, ISO 4017/4014, ISO 7045, ...).

| Thread | Coarse pitch, mm | Tap drill, mm | Clearance hole ISO 273: fine / medium / coarse, mm |
|---|---|---|---|
| M3 | 0.5 | 2.5 | 3.2 / 3.4 / 3.6 |
| M4 | 0.7 | 3.3 | 4.3 / 4.5 / 4.8 |
| M5 | 0.8 | 4.2 | 5.3 / 5.5 / 5.8 |
| M6 | 1.0 | 5.0 | 6.4 / 6.6 / 7.0 |
| M8 | 1.25 | 6.8 | 8.4 / 9.0 / 10.0 |
| M10 | 1.5 | 8.5 | 10.5 / 11.0 / 12.0 |
| M12 | 1.75 | 10.2 | 13.0 / 13.5 / 14.5 |

## Sheet-metal specifics
- Self-clinching studs/nuts/standoffs (PEM-type): required hole size, minimum sheet thickness and edge distance come from the **manufacturer's datasheet** for the exact part number and sheet material. Never infer them.
- Threading directly in thin sheet gives few threads; consider extruded (flow-drilled) holes, clinch nuts or rivet nuts, and say that the choice is a design decision.
- Welded studs (stud welding) mark the opposite face; a drawing must say which face is visible/cosmetic.
- In a laser DXF, a stud/PEM location is either a through hole (cut) or a mark; the file and the CAM mapping must say which.
