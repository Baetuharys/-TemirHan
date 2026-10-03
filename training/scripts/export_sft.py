#!/usr/bin/env python3
"""Export SFT/preference data to provider formats (strips extra metadata keys).

  python training/scripts/export_sft.py openai   -> training/export/openai-sft.jsonl, openai-dpo.jsonl
  python training/scripts/export_sft.py claude   -> training/export/claude-sft.jsonl

Check the provider's CURRENT fine-tuning documentation before uploading: supported models,
formats and minimum example counts change. This script only reshapes the data.
"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "training/export"; OUT.mkdir(exist_ok=True)
sft = [json.loads(l) for p in sorted((ROOT / "training/datasets/sft").glob("*.jsonl")) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
pref = [json.loads(l) for p in sorted((ROOT / "training/datasets/preference").glob("*.jsonl")) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
sysmsg = {r["id"]: r["messages"][0]["content"] for r in sft}
target = sys.argv[1] if len(sys.argv) > 1 else ""
if target == "openai":
    with (OUT / "openai-sft.jsonl").open("w", encoding="utf-8") as f:
        for r in sft: f.write(json.dumps({"messages": r["messages"]}, ensure_ascii=False) + "\n")
    default_sys = sft[0]["messages"][0]["content"]
    with (OUT / "openai-dpo.jsonl").open("w", encoding="utf-8") as f:
        for p in pref:
            f.write(json.dumps({
                "input": {"messages": [{"role": "system", "content": default_sys}, {"role": "user", "content": p["prompt"]}]},
                "preferred_output": [{"role": "assistant", "content": p["chosen"]}],
                "non_preferred_output": [{"role": "assistant", "content": p["rejected"]}],
            }, ensure_ascii=False) + "\n")
    print(f"openai-sft.jsonl ({len(sft)}), openai-dpo.jsonl ({len(pref)}) -> training/export/")
elif target == "claude":
    with (OUT / "claude-sft.jsonl").open("w", encoding="utf-8") as f:
        for r in sft:
            m = r["messages"]
            f.write(json.dumps({"system": m[0]["content"], "messages": [{"role": "user", "content": m[1]["content"]}, {"role": "assistant", "content": m[2]["content"]}]}, ensure_ascii=False) + "\n")
    print(f"claude-sft.jsonl ({len(sft)}) -> training/export/")
else:
    print(__doc__); sys.exit(1)
