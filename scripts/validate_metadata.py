#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
REQ=['id','title','type','status','version','summary','tags','depends_on','last_reviewed']
TYPES={'master','module','blueprint'}; STATUS={'draft','active','stable','deprecated','archived'}
files=list((ROOT/'prompts').rglob('*.md'))
errs=[]
for f in files:
 s=f.read_text(encoding='utf-8')
 if not s.startswith('---\n'): errs.append(f'{f}: missing frontmatter'); continue
 parts=s.split('---',2); fm=parts[1]
 vals={}
 for line in fm.splitlines():
  if ':' in line and not line.startswith('  '):
   k,v=line.split(':',1); vals[k.strip()]=v.strip()
 if 'tags' in fm and 'tags:' in fm and not vals.get('tags'):
  vals['tags']='[block]'
 for k in REQ:
  if k not in vals or vals[k] in ('','TODO'): errs.append(f'{f}: missing/empty {k}')
 if vals.get('type') not in TYPES: errs.append(f'{f}: invalid type')
 if vals.get('status') not in STATUS: errs.append(f'{f}: invalid status')
 if vals.get('id') and not re.fullmatch(r'mai-(master|module|blueprint)-[a-z0-9]+(?:-[a-z0-9]+)*',vals['id']): errs.append(f'{f}: invalid id {vals["id"]}')
if errs:
 print('\n'.join(errs)); sys.exit(1)
print(f'OK: {len(files)} prompt files validated')
