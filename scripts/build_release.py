#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, shutil, subprocess, sys, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
OUT=ROOT.parent/f'mechanical-ai-engineering-v{VERSION}.zip'
MANIFEST=ROOT/'RELEASE-MANIFEST.json'

def run(*cmd):
    subprocess.run(cmd,cwd=ROOT,check=True)

def sha256(path: Path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def main():
    run(sys.executable,'scripts/validate_all.py')
    run(sys.executable,'training/scripts/build_rag_chunks.py')
    run(sys.executable,'rag/build_index.py')
    run(sys.executable,'scripts/export_chatgpt.py')
    run(sys.executable,'scripts/export_claude_skills.py')
    run(sys.executable,'training/scripts/run_eval.py','--responses','training/eval/gold-sample-responses.jsonl','--min-pass','1.0')
    for p in ROOT.rglob('__pycache__'): shutil.rmtree(p,ignore_errors=True)
    for p in ROOT.rglob('*.pyc'):
        p.unlink(missing_ok=True)
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p==MANIFEST: continue
        rel=p.relative_to(ROOT).as_posix()
        files.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha256(p)})
    manifest={'name':'Mechanical AI Engineering','version':VERSION,'file_count':len(files),'files':files}
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if OUT.exists(): OUT.unlink()
    with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file(): z.write(p,Path(f'mechanical-ai-engineering-v{VERSION}')/p.relative_to(ROOT))
    print(f'Built {OUT} ({OUT.stat().st_size} bytes), files={len(files)+1}')
    print(f'SHA256 {sha256(OUT)}')
if __name__=='__main__': main()
