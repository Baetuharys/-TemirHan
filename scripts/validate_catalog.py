#!/usr/bin/env python3
from pathlib import Path
import sys,re
ROOT=Path(__file__).resolve().parents[1]
ids={}
for f in (ROOT/'prompts').rglob('*.md'):
 s=f.read_text(encoding='utf-8'); m=re.search(r'^id:\s*(\S+)',s,re.M)
 if m: ids[m.group(1)]=f
errs=[]
for f in (ROOT/'prompts').rglob('*.md'):
 s=f.read_text(encoding='utf-8')
 m=re.search(r'^depends_on:\s*\[(.*?)\]',s,re.M)
 if m and m.group(1).strip():
  for dep in [x.strip().strip("'\"") for x in m.group(1).split(',') if x.strip()]:
   if dep not in ids: errs.append(f'{f}: missing dependency {dep}')
if errs: print('\n'.join(errs)); sys.exit(1)
print(f'OK: dependency graph valid ({len(ids)} items)')
