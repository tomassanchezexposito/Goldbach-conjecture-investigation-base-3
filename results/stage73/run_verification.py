#!/usr/bin/env python3
"""Reproduce only the declared Stage 73 regressions; keep prior stages immutable."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time
import os
import tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'results/stage73'
jobs=[
 ('stage70_recheck',['python3','-B','results/stage70/verify_stage70.py']),
 ('stage71_recheck',['python3','-B','results/stage71/verify_stage71.py']),
 ('stage72_recheck',['python3','-B','results/stage72/verify_stage72.py']),
 ('exact_results',['python3','-B','results/stage73/verify_stage73.py']),
 ('sage_results',['sage','-python','results/stage73/verify_stage73_sage.py'])]
runs=[]
for name,cmd in jobs:
    start=time.perf_counter()
    with tempfile.TemporaryFile(mode='w+t') as stdout, tempfile.TemporaryFile(mode='w+t') as stderr:
        process=subprocess.Popen(cmd,cwd=ROOT,text=True,stdout=stdout,stderr=stderr)
        _,status,usage=os.wait4(process.pid,0)
        process.returncode=os.waitstatus_to_exitcode(status)
        stdout.seek(0); stderr.seek(0)
        result=subprocess.CompletedProcess(cmd,process.returncode,stdout.read(),stderr.read())
    elapsed=time.perf_counter()-start
    if result.returncode:
        sys.stderr.write(result.stderr)
        raise SystemExit(result.returncode)
    obj=json.loads(result.stdout)
    assert obj['status']=='PASS',name
    target=OUT/(name+'.json')
    target.write_text(result.stdout)
    metrics={'peak_rss_kib':usage.ru_maxrss,'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime}
    runs.append({'name':name,'command':' '.join(cmd),'status':'PASS','elapsed_wall_seconds':elapsed,
                 'wait4_resources':metrics,'stderr':result.stderr,'output':str(target.relative_to(ROOT)),
                 'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    print(name,metrics,flush=True)
(OUT/'verification_runs.json').write_text(json.dumps({'runs':runs,'python_version':sys.version,
    'scope':'Declared finite identities, inherited regressions, and three certified interval examples only.'},indent=2)+'\n')
