# Deterministic Engineering Calculators

These modules handle arithmetic that should not be delegated to free-form language generation. They intentionally accept **inputs** instead of embedding shop-specific “magic numbers”.

Included: bend geometry, sheet mass, cost/margin arithmetic, 1-D tolerance stacks and first-pass enclosure airflow. Results should be wrapped with evidence labels by the calling skill/agent.

Do **not** turn this directory into a hidden standards table. If a calculation needs a coefficient, density, strength, K-factor, gasket compression or machine capability, supply it from project data or `sources/` and record its provenance.

## Added design-support calculators
- `gasket.py`: calculates geometric compression from supplied free/compressed thickness. It does **not** invent an acceptable compression window or IP claim.
- `stiffness.py`: simple beam idealizations for sanity checks. It deliberately refuses to masquerade as a sheet/plate/shell analysis.
- CLI now also supports `tolerance`, `gasket`, and `beam` subcommands.
