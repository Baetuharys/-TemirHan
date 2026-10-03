#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import date

ROOT=Path(__file__).resolve().parents[1]
BASE={
 'master': ROOT/'prompts/masters/active',
 'module': ROOT/'prompts/modules',
 'blueprint': ROOT/'prompts/skill-blueprints',
}
CATEGORIES=['capability','constraints','domain','output','tone']

def main():
 p=argparse.ArgumentParser()
 p.add_argument('kind', choices=BASE)
 p.add_argument('slug')
 p.add_argument('--category', choices=CATEGORIES)
 a=p.parse_args()
 if a.kind=='module':
  if not a.category: p.error('--category is required for module')
  d=BASE[a.kind]/a.category
  ident=f'mai-module-{a.slug}'
 else:
  d=BASE[a.kind]
  ident=f'mai-{a.kind}-{a.slug}'
 d.mkdir(parents=True,exist_ok=True)
 f=d/f'{ident}.md'
 if f.exists(): raise SystemExit(f'Exists: {f}')
 title=a.slug.replace('-',' ').title()
 f.write_text(f'''---\nid: {ident}\ntitle: {title}\ntype: {a.kind}\nstatus: draft\nversion: 0.1.0\nsummary: TODO\ntags: []\ndepends_on: []\nlast_reviewed: {date.today()}\nportability: provider-agnostic\nadapter_support: [chatgpt, claude]\n---\n\n# {title}\n\n## Purpose\nTODO\n\n## Instructions\nTODO\n''',encoding='utf-8')
 print(f)
if __name__=='__main__': main()
