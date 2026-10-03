# ChatGPT Adapter — v3.0

## Recommended use
Use `training/system-prompts/chatgpt-custom-gpt-instructions.md` as the behavioral instruction and upload files from `dist/chatgpt-knowledge/` as the compact thematic knowledge pack.

For a single conversation, load only the relevant `skills/<slug>/SKILL.md` plus its named knowledge/project profile files. For code/agent workflows, use the repository directly and call `scripts/mai.py` / deterministic tools.

## Important
- Product instruction/file limits can change; this repo intentionally avoids hardcoded platform limits.
- Shop-specific values belong in `project-profiles/` and should be attached with the job.
- Keep customer/confidential data out of training seeds.
- A model answer is not proof of SolidWorks execution, certification, FEA validation or physical testing.

## Rebuild
```bash
python scripts/export_chatgpt.py
```
