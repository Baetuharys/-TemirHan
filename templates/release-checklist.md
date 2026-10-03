# Release Checklist
- [ ] `python scripts/validate_all.py` passes
- [ ] `VERSION`, `CHANGELOG.md`, README status agree
- [ ] New/changed behaviour has eval cases; gold self-test 100 %
- [ ] Real model run recorded for Claude and ChatGPT (`training/eval/runs/`)
- [ ] `python training/scripts/build_rag_chunks.py` re-run
- [ ] `python scripts/export_claude_skills.py && python scripts/export_chatgpt.py` re-run
- [ ] No customer data; LICENSE present
- [ ] Open items in `catalog/topic-coverage.md` reviewed
