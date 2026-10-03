# Default workflow — Sheet Metal Manufacturability Check

1. Cutting: min hole/slot, web, corner radii, edge distances, nesting friendliness.
2. Forming: radius vs tooling, flange length, hole-to-bend, relief, bend sequence and collisions, springback, grain direction.
3. Joining: weld access and distortion, hardware datasheet limits, galvanised/stainless considerations.
4. Finishing: coating thickness vs fits, masking, hanging marks, drain holes.
5. Assembly/inspection: tolerance stack, datum accessibility.
6. Cost drivers: extra setups, special tools, secondary operations.
7. Classify each finding as **Error / Risk / Suggestion**, cite location, give a fix.

## Gate before output
- Rules of thumb are labelled *typical*; shop values override.
- No finding without a location.
- The first process that could reject the part is named.
