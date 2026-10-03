# Worked example — adding an SFT record

**Goal.** Add a weight-calculation example.

1. Compute: 1 m × 2 m × 3 mm, ρ = 7850 kg/m³ → 0.006 m³ × 7850 = **47.1 kg** (reproducible).
2. Write the record in `training/datasets/sft/` with `evidence: calculated` and provenance `knowledge/15`.
3. Add an eval case in `training/eval/cases.jsonl` expecting 47.1 ±0.1 and a density statement.
4. Run `python training/scripts/validate_dataset.py` and `python scripts/validate_all.py`.
5. Report counts per category.
