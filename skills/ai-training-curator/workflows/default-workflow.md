# Default workflow — AI Training Curator

1. Clarify the goal: prompting/skills only, RAG, or fine-tuning. Recommend the cheapest option that meets the need (`training/README.md`).
2. Check data sensitivity (`training/DATA-GOVERNANCE.md`): no customer drawings, names, prices or personal data in datasets.
3. Write records from verified material only; every number is computed or sourced; label evidence.
4. Add or update eval cases first; every new behaviour needs at least one eval case with must_include / must_not_match checks.
5. Run `python scripts/validate_all.py` and `python training/scripts/validate_dataset.py`.
6. Report what changed, counts per category, and which eval cases cover it.
