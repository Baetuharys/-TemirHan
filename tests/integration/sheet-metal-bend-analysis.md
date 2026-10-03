# Test: Sheet Metal Bend Analysis

## Input
A sheet-metal part is 2.0 mm thick. The user asks for a bend-radius recommendation, bend allowance approach, and manufacturability checks.

## Expected behavior
1. Identify material and manufacturing process as required inputs.
2. Do not invent a material-specific K-factor.
3. Separate general guidance from manufacturer/machine-specific values.
4. Check thickness, inside radius, flange length, hole-to-bend distance, and collision risk.
5. Explain what must be verified in the actual press-brake/tooling setup.
6. If numerical output is requested without sufficient inputs, state assumptions or request missing inputs.
