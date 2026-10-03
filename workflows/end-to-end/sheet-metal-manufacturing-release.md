# Sheet Metal Manufacturing Release

## Chain

SolidWorks model → Sheet Metal validation → Flat Pattern → Technical Drawing → DXF release → Laser/CAM process mapping → Bending → Welding/Fasteners → Assembly → Cost → Documentation

## Gates
1. **Design gate:** material, thickness, bends, reliefs, interfaces, and manufacturability are defined.
2. **Drawing gate:** dimensions, tolerances, notes, revision, material/thickness, weld/fastener information are consistent.
3. **DXF gate:** scale, units, geometry integrity, cut/mark separation, and filename/revision are checked.
4. **Production gate:** machine/tool/CAM-specific constraints are confirmed by the receiving process.
5. **Commercial gate:** quantity and process route match the cost/quotation basis.
6. **Release gate:** all artifacts carry consistent identity and revision.

## Failure modes
- Treating a visible DXF entity as automatically cut or marked.
- Using material properties from a different alloy/temper without disclosure.
- Mixing drawing and model revisions.
- Giving a machine-specific SolidWorks instruction without version evidence.
- Presenting estimated dimensions/costs as exact.
