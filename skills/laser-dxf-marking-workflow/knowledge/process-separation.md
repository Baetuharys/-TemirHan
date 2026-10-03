# Cut versus mark separation

## Principle
A DXF is geometry data. A receiving CAM/laser workflow decides how geometry is processed. The mere presence of a line in a DXF does not establish that it will be marked rather than cut.

## Required process map
Every production geometry item should be classified as one of:
- CUT
- MARK
- REFERENCE
- CONSTRUCTION/OTHER

The mapping mechanism must be agreed with the receiving CAM: layers, colors, entity types, separate files, or another documented convention.

## SolidWorks-specific caution
A sketch entity without a cut feature may still be exported as geometry. Therefore "I did not make a Cut-Extrude" is not a sufficient proof that the laser will ignore it.

## Release checks
Check scale, units, duplicate entities, closed/open contours, layer/process mapping, and the final CAM interpretation.
