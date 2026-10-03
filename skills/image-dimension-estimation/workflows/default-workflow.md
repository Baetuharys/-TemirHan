# Default workflow — Image Dimension Estimation

1. Check the photo: is the reference on the same plane as the feature? is the view roughly straight-on? is anything cropped?
2. State the reference and its size. If the size is assumed, class results as Scaled estimate with the assumption named.
3. Compute scale = known mm / known px. Apply only to features on that plane.
4. For each feature give value, class, and +/- error (main source named: pixel reading, tilt, lens, reference size).
5. List what would tighten the numbers: a straight-on photo, a ruler in frame, one measured dimension from the user.
6. If the stated purpose is manufacturing, say clearly that a measurement is needed before cutting.

## Gate before output
- No dimension without a class. - No single number without a range. - Reference named. - Perspective warning given when tilt is visible.
