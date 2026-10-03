# DXF for laser cutting — checks that do not depend on one CAM system

DXF is a data exchange format; the **CAM software and machine post-processor decide what is cut, marked or ignored.** What follows are common causes of bad files, not guarantees.

- Units and scale: 1:1, the unit the CAM expects (mm). Wrong units are the most common error.
- One closed contour per cut shape; outer contour plus inner contours (holes). Open or touching-but-not-joined ends fail nesting.
- No duplicate overlapping entities (they cut twice) and no zero-length or tiny stray segments.
- Prefer lines, arcs and circles; splines and ellipses may be converted or rejected by CAM.
- Layers: separate CUT, MARK/ENGRAVE, BEND-LINE, ANNOTATION. Which layer names/colours the CAM maps to which process is a CAM setting; get it from the shop. Do not assume.
- Bend lines and dimension text must not sit on the cut layer.
- Thickness, material, quantity, revision and part number belong in the file name or an accompanying note; do not rely on text inside the DXF.
- Kerf and lead-in/lead-out are normally applied by CAM, not drawn in the DXF, unless the shop says otherwise.
- Always preview the DXF in the CAM (or a viewer) before release: count the contours, check scale with one known dimension.
