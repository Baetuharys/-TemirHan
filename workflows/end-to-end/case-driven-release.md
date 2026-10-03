# Case-Driven Release Workflow

## Purpose
Use the v0.9 case library as regression tests for the engineering AI system.

## Flow
1. Select a case matching the user task.
2. Load the case's known inputs only.
3. Apply the referenced skills in order.
4. Label each statement as one of:
   - supplied fact
   - calculation
   - engineering practice
   - assumption
   - estimate
   - source-dependent claim
5. Run the case acceptance criteria.
6. Record failure modes encountered.
7. Do not fill missing case inputs with invented values.
8. Produce a release/action summary.

## Regression rule
When a skill changes, rerun every case that depends on it. A passing case means the response meets the acceptance criteria; it does not mean the underlying manufacturing process is certified.
