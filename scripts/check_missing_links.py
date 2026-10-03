#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
errs=[]
for f in (ROOT/'prompts').rglob('*.md'):
 s=f.read_text(encoding='utf-8')
 for target in re.findall(r'`(mai-(?:master|module|blueprint)-[a-z0-9-]+)`',s):
  if not any(target==re.search(r'^id:\s*(\S+)',x.read_text(encoding='utf-8'),re.M).group(1) if re.search(r'^id:\s*(\S+)',x.read_text(encoding='utf-8'),re.M) else False for x in (ROOT/'prompts').rglob('*.md')):
   errs.append(f'{f}: unresolved {target}')
if errs: print('\n'.join(errs)); sys.exit(1)
print('OK: no unresolved internal prompt IDs')
