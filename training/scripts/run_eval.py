#!/usr/bin/env python3
"""Score model responses against training/eval/cases.jsonl (offline, no network).

Usage:
  python training/scripts/run_eval.py --list
  python training/scripts/run_eval.py --template responses.jsonl      # write a file to fill with model answers
  python training/scripts/run_eval.py --responses responses.jsonl     # score ({"id":..., "response":...} per line)
"""
import argparse, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "training/eval/cases.jsonl"
NUM = re.compile(r"\d+(?:[.,]\d+)?")

def numbers(text):
    out = []
    for m in NUM.finditer(text):
        s = m.group(0)
        # thousands separators are not expected in this library's answers; treat comma as decimal
        out.append(float(s.replace(",", ".")))
    return out

def score(case, resp):
    fails = []
    for grp in case.get("must_include_any", []):
        if not any(re.search(a, resp, re.I) for a in grp):
            fails.append(f"missing any of {grp}")
    for rx in case.get("must_not_match", []):
        if re.search(rx, resp, re.I | re.M):
            fails.append(f"forbidden pattern {rx!r}")
    for exp in case.get("expect_numbers", []):
        if not any(abs(n - exp["value"]) <= exp["tol"] for n in numbers(resp)):
            fails.append(f"expected number {exp['value']} ±{exp['tol']} not found")
    return fails

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--template")
    ap.add_argument("--responses")
    ap.add_argument("--category")
    ap.add_argument("--min-pass", type=float, default=0.0, help="exit 1 if pass rate below this (0-1)")
    a = ap.parse_args()
    cases = [json.loads(l) for l in CASES.read_text(encoding="utf-8").splitlines() if l.strip()]
    if a.category:
        cases = [c for c in cases if c["category"] == a.category]
    if a.list:
        for c in cases: print(f"{c['id']:8} {c['category']:15} {c['prompt'][:90]}")
        return
    if a.template:
        with open(a.template, "w", encoding="utf-8") as f:
            for c in cases: f.write(json.dumps({"id": c["id"], "prompt": c["prompt"], "response": ""}, ensure_ascii=False) + "\n")
        print(f"Wrote {len(cases)} rows to {a.template}"); return
    if not a.responses:
        ap.error("use --list, --template or --responses")
    resp = {}
    for l in Path(a.responses).read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l); resp[r["id"]] = r.get("response", "")
    passed = failed = skipped = 0
    by_cat = {}
    for c in cases:
        if c["id"] not in resp or not resp[c["id"]].strip():
            skipped += 1; continue
        f = score(c, resp[c["id"]])
        by_cat.setdefault(c["category"], [0, 0])
        by_cat[c["category"]][1] += 1
        if f:
            failed += 1; print(f"FAIL {c['id']} [{c['category']}]: " + "; ".join(f))
        else:
            passed += 1; by_cat[c["category"]][0] += 1
    total = passed + failed
    rate = passed / total if total else 0
    print(f"\nPassed {passed}/{total} (skipped {skipped}) = {rate:.0%}")
    for k, (p, t) in sorted(by_cat.items()): print(f"  {k:15} {p}/{t}")
    print("Note: automatic checks catch gross errors only; review rubrics manually for the rest.")
    if rate < a.min_pass: sys.exit(1)

if __name__ == "__main__":
    main()
