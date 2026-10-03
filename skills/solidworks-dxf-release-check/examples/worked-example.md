# Example: stud locations

Flat pattern has eight M4 stud locations. Design intent: marks on the visible face only; no through-holes.
- Finding: the sketch circles exported as ordinary circles on layer 0 -> a CAM may cut them. Severity: Error.
- Fix: put the circles on a MARK layer (or per the shop's convention) and ask the shop how the CAM maps that layer; confirm in CAM preview.
- Release wording: "DXF ready for CAM preview; marking behaviour to be confirmed by CAM preview."
(Check `cases/laser-dxf-stud-marking/` for the acceptance criteria.)
