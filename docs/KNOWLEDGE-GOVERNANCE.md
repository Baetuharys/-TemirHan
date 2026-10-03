# Knowledge and Source Governance

## Add facts in the right place
- Stable engineering explanation → `knowledge/`.
- Quick lookup card → `reference/`.
- Current/authoritative source metadata → `sources/registry.json`.
- Shop-specific value → `project-profiles/`.
- User/customer value → project context only; never training seed data.
- Deterministic equation → `tools/` plus tests.
- Behavior/workflow → `skills/` plus eval.

## Source lifecycle
A source record may be `current`, `watch`, `draft` or equivalent metadata. Draft/replacement activity must not silently rewrite a customer's governing edition. For release-critical work, verify the contract/regulatory edition and the source's current status.

## Standards copyright
Store identifiers, edition/status metadata, engineering summaries and your own notes. Do not copy protected standards into this public-style repository unless licensing explicitly permits it.

## Change rule
Every meaningful behavior change should add or update an eval case. Every deterministic calculation change should have a test. Every source-sensitive factual change should update provenance metadata.
