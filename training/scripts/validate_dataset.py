#!/usr/bin/env python3
"""Validate training datasets (SFT, preference, eval). Exit code 1 on any error."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
errs, warns = [], []

# Patterns that must never appear in training data (confidentiality / fabrication guard)
FORBIDDEN = [
    (re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"), "e-mail address"),
    (re.compile(r"\b(?:\+?90|0)\s?5\d{2}\s?\d{3}\s?\d{2}\s?\d{2}\b"), "phone number"),
    (re.compile(r"\bTR\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{2}\b"), "IBAN"),
    (re.compile(r"(?i)\b(confidential|gizli|müşteri adı:)\b.{0,20}\bdrawing\b"), "confidential marker"),
]

def load(path):
    rows = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append((i, json.loads(line)))
        except json.JSONDecodeError as e:
            errs.append(f"{path.name}:{i}: invalid JSON ({e})")
    return rows

def scan(path, i, text):
    for rx, what in FORBIDDEN:
        if rx.search(text):
            errs.append(f"{path.name}:{i}: possible {what} in data")

def check_sft(path):
    ids, prompts = set(), set()
    for i, r in load(path):
        for k in ("id", "category", "lang", "evidence", "provenance", "messages"):
            if k not in r:
                errs.append(f"{path.name}:{i}: missing '{k}'")
        if r.get("id") in ids:
            errs.append(f"{path.name}:{i}: duplicate id {r.get('id')}")
        ids.add(r.get("id"))
        m = r.get("messages", [])
        roles = [x.get("role") for x in m]
        if roles != ["system", "user", "assistant"]:
            errs.append(f"{path.name}:{i}: roles must be system,user,assistant (got {roles})")
        if len(m) == 3:
            u, a = m[1]["content"], m[2]["content"]
            if u in prompts:
                errs.append(f"{path.name}:{i}: duplicate user prompt")
            prompts.add(u)
            if len(a) < 120:
                warns.append(f"{path.name}:{i}: very short assistant answer")
            if re.search(r"\d", a) and not re.search(r"\[(HESAPLANAN|VERİLEN|KAYNAKLI|UYGULAMA|TAHMİN|VARSAYIM|AÇIK|CALCULATED|FACT-SUPPLIED|SOURCE-BACKED|PRACTICE|ESTIMATE|ASSUMPTION|OPEN)\]", a) \
               and r["category"] in ("bending", "weight", "cost", "image"):
                warns.append(f"{path.name}:{i}: numeric answer without an evidence label")
            for x in m:
                scan(path, i, x["content"])
    return len(ids)

def check_pref(path):
    ids = set()
    for i, r in load(path):
        for k in ("id", "category", "prompt", "chosen", "rejected", "reason"):
            if not r.get(k):
                errs.append(f"{path.name}:{i}: missing '{k}'")
        if r.get("id") in ids:
            errs.append(f"{path.name}:{i}: duplicate id")
        ids.add(r.get("id"))
        if r.get("chosen") == r.get("rejected"):
            errs.append(f"{path.name}:{i}: chosen == rejected")
        scan(path, i, (r.get("chosen") or "") + (r.get("rejected") or ""))
    return len(ids)

def check_eval(path):
    ids = set()
    for i, r in load(path):
        for k in ("id", "category", "prompt", "rubric"):
            if not r.get(k):
                errs.append(f"{path.name}:{i}: missing '{k}'")
        if r.get("id") in ids:
            errs.append(f"{path.name}:{i}: duplicate id")
        ids.add(r.get("id"))
        if not (r.get("must_include_any") or r.get("must_not_match") or r.get("expect_numbers")):
            errs.append(f"{path.name}:{i}: no automatic check defined")
        for g in r.get("must_include_any", []):
            for rx in g:
                try: re.compile(rx)
                except re.error as e: errs.append(f"{path.name}:{i}: bad regex {rx!r}: {e}")
        for rx in r.get("must_not_match", []):
            try: re.compile(rx)
            except re.error as e: errs.append(f"{path.name}:{i}: bad regex {rx!r}: {e}")
    return len(ids)

n_sft = sum(check_sft(p) for p in sorted((ROOT / "training/datasets/sft").glob("*.jsonl")))
n_pref = sum(check_pref(p) for p in sorted((ROOT / "training/datasets/preference").glob("*.jsonl")))
n_eval = sum(check_eval(p) for p in sorted((ROOT / "training/eval").glob("cases*.jsonl")))
for w in warns: print("WARN:", w)
if errs:
    print("\n".join("ERROR: " + e for e in errs)); sys.exit(1)
print(f"OK: {n_sft} SFT, {n_pref} preference pairs, {n_eval} eval cases")
