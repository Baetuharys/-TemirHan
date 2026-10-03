# DXF release checklist

| # | Check | Pass criterion |
|---|---|---|
| 1 | File identity | part number + revision + material + thickness in file name or note |
| 2 | Units / scale | mm, 1:1, one dimension verified |
| 3 | Outer contour | one closed polyline/loop |
| 4 | Holes | each closed, no overlap with other holes |
| 5 | Duplicates | none; overlapped lines removed |
| 6 | Stray geometry | no dimension text, centre marks, sketch construction on cut layer |
| 7 | Entities | lines/arcs/circles; splines flagged |
| 8 | Layers | CUT, MARK, BEND, NOTE (or shop's scheme) |
| 9 | Marking | studs/PEM/part number on MARK, not CUT |
| 10 | Preview | CAM/viewer preview done, contour count matches, signed |
