# Smoke tests — solidworks-dxf-release-check

A test passes only if the expected behaviour is present and nothing is invented.

1. DXF with bend lines on the cut layer → Error: lines would be cut; asks to separate layers.
2. Exported size differs from the model's flat bounding box → Error: scale or unit problem.
3. User claims a sketch without a Cut feature will be marked → refuses to assume; says CAM-dependent.
