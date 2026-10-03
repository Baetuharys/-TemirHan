#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
en={re.search(r'^id:\s*(\S+)',f.read_text(encoding='utf-8'),re.M).group(1) for f in (ROOT/'prompts').rglob('*.md') if re.search(r'^id:\s*(\S+)',f.read_text(encoding='utf-8'),re.M)}
tr={re.search(r'^id:\s*(\S+)',f.read_text(encoding='utf-8'),re.M).group(1) for f in (ROOT/'tr').rglob('*.md') if re.search(r'^id:\s*(\S+)',f.read_text(encoding='utf-8'),re.M)}
missing=sorted(en-tr)
print('OK: Turkish mirror covers all current prompt IDs' if not missing else 'Missing Turkish IDs:\n'+'\n'.join(missing))
sys.exit(1 if missing else 0)
