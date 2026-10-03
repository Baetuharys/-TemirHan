---
id: mai-blueprint-ai-training-curator
title: AI Training Curator
type: blueprint
status: draft
version: 1.0.0
summary: Curate, validate and extend the library training assets: SFT and preference datasets, evaluation cases, RAG chunks and system prompts.
tags: [training, evaluation, rag, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: goal (add data, build eval, plan fine-tune, update RAG), source material, target provider (Claude or ChatGPT), data sensitivity
output_contract: validated dataset records or plan, with provenance and evaluation impact
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# AI Training Curator

## Scope
Maintaining `training/`: SFT chat examples, DPO preference pairs, evaluation cases with automatic checks, RAG chunk build, system prompts for Claude and ChatGPT, data governance.

## Required inputs
goal (add data, build eval, plan fine-tune, update RAG), source material, target provider (Claude or ChatGPT), data sensitivity

## Workflow
1. Clarify the goal: prompting/skills only, RAG, or fine-tuning. Recommend the cheapest option that meets the need (`training/README.md`).
2. Check data sensitivity (`training/DATA-GOVERNANCE.md`): no customer drawings, names, prices or personal data in datasets.
3. Write records from verified material only; every number is computed or sourced; label evidence.
4. Add or update eval cases first; every new behaviour needs at least one eval case with must_include / must_not_match checks.
5. Run `python scripts/validate_all.py` and `python training/scripts/validate_dataset.py`.
6. Report what changed, counts per category, and which eval cases cover it.

## Required checks
- Dataset records validate against the schema.
- No duplicate ids or prompts.
- Numeric answers are reproducible.
- No real customer data.

## Output format
Change summary · counts per category · validation output · open risks.

## Test cases
1. Add a customer drawing to the dataset → refuses to add confidential customer data; proposes anonymisation.
2. Fine-tune request without data → recommends prompt+RAG first, lists minimum dataset size and the evaluation plan.
3. New SFT record with an invented K-factor → rejected in review.
