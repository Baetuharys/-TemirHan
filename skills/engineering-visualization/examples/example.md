# Worked example — exploded view of a bracket assembly

**Request.** Exploded view of a 2-part bracket with 4 screws for a work instruction.

**Invariants (stated before prompting).** 2 plates, 4 screws, 4 holes per plate, front-isometric view, plate proportion 3:2, no extra parts.
**Prompt skeleton.** Subject → view → part list with counts → materials → style (clean technical illustration, white background) → negative constraints (no extra screws, no text).
**Verification.** Count parts and holes in the result; compare proportions; reject the image if any count differs. Label the image *illustrative, not dimensionally accurate*.
