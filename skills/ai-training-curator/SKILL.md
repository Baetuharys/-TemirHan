---
id: mai-skill-ai-training-curator
title: AI Training Curator
type: skill
status: active
version: 1.0.0
summary: Curate, validate and extend the library training assets: SFT and preference datasets, evaluation cases, RAG chunks and system prompts.
tags: [training, evaluation, rag, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: ai-training-curator
description: Curate, validate and extend the library's AI training assets: SFT/preference datasets, evaluation cases, RAG chunks and system prompts. Use for veri seti hazırlama, eval ekleme, RAG derleme, model eğitimi/ince ayar planı.
---

# AI Training Curator

## Purpose
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

## Output contract
Change summary · counts per category · validation output · open risks.

## Failure modes
- Training on confidential or unverified data.
- Adding data without eval cases.
- Teaching confident answers where the library requires abstention.

## Self-test
1. Add a customer drawing to the dataset → refuses to add confidential customer data; proposes anonymisation.
2. Fine-tune request without data → recommends prompt+RAG first, lists minimum dataset size and the evaluation plan.
3. New SFT record with an invented K-factor → rejected in review.
