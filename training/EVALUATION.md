# Evaluation Protocol

## Goals
Detect (1) fabrication, (2) wrong numbers, (3) missing uncertainty, (4) unsafe macro code, (5) terminology errors, (6) confidentiality failures.

## Case format (`eval/cases.jsonl`)
`id, category, lang, prompt, must_include_any (list of alternative-groups), must_not_match (regex), expect_numbers ({value, tol}), rubric`.
- *must_include_any*: for each group at least one regex must match.
- *must_not_match*: none may match (case-insensitive, multiline).
- *expect_numbers*: a number within tolerance must appear (comma decimals are read as decimals).

## Scoring
Automatic pass-rate per category + manual rubric review for a sample (≥ 10 cases per release). Record: model name/version, date, prompt version, knowledge files version, pass rate, notable failures.

## Release gates
- `python scripts/validate_all.py` passes.
- Gold self-test passes at 100 %.
- A real model run on all 45 cases is recorded in `training/eval/runs/` (create the folder; one JSON/markdown file per run).
- No regression > 5 points in any category versus the previous run.

## Adding cases
Every bug found in production becomes an eval case first, then a prompt/knowledge/dataset fix.
