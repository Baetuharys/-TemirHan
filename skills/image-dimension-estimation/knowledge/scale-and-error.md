# Scale and error

scale (mm/px) = known length (mm) / pixel length (px).
Tilt: a feature turned by angle a from the image plane appears shorter by cos(a): 10 deg -> 1.5%, 15 deg -> 3.4%.
Pixel reading: if each end is read within +/-2 px, length uncertainty is about +/-2 px x scale x sqrt(2) when the two ends are independent, or +/-4 px x scale as a worst case.
Depth: features nearer to the camera than the reference look larger; the error grows with the depth difference relative to the camera distance.
Lens distortion is larger toward the image edges; keep the reference near the feature.
