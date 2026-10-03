# Smoke tests — sheet-metal-weld-fastener-review

A test passes only if the expected behaviour is present and nothing is invented.

1. Long continuous weld on 1.5 mm sheet with no distortion plan → flags distortion risk and suggests stitch/sequence/fixture unless sealing is required.
2. Self-clinching nut in a hard or too-thin sheet → asks for the fastener datasheet limits instead of assuming.
3. Galvanised sheet welded → flags zinc burn-off, fumes and touch-up coating.
