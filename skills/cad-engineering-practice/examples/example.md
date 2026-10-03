# Worked example — sending a sheet-metal part to a laser shop

**Request.** "Tedarikçi CAD dosyasını istedi, ne göndereyim?"

**Answer pattern.**
1. Ask: tedarikçinin CAD sistemi/sürümü? Ürün ağacı (BOM) gerekli mi?
2. Recommend the **release package** (same revision on all): drawing PDF · flat-pattern DXF · STEP · BOM/quote notes.
3. DXF checks: mm, scale 1:1, bend lines on their own layer, no stray sketches (`skills/solidworks-dxf-release-check`).
4. Naming: `PARTNO_REV.ext`, no Turkish characters or spaces.
5. Risks left: material/thickness conflicts between model and drawing; finish note; K-factor note on the flat pattern.

**Not allowed.** Sending the native file as the only deliverable, or a PDF without a DXF for a laser job.
