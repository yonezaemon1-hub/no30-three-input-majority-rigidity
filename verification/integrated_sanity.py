"""No.30 integrated audit-sanity script. Python 3 standard library only.
This is an independent finite cross-check, not a proof of the infinite theorem.
"""
import hashlib, json, random, sys
from collections import Counter
from pathlib import Path

BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'sources/No30_Complete_Rigidity_Audit_V05_20261019'))
from verify_v05 import counterexample

def raw_round_a(bits):
    n=len(bits); m=(n-1)//2
    return [int(sum(bits[(i+j)%n] for j in range(n-2))>=m) for i in range(n)]

def raw_round_b(bits,a,b):
    n=len(bits)
    return [int(bits[i]+bits[(i+a)%n]+bits[(i+b)%n]>=2) for i in range(n)]

def int_to_bits(x,n): return [(x>>j)&1 for j in range(n)]

def run_three(x,a,b,n):
    bits=int_to_bits(x,n)
    return raw_round_a(raw_round_b(raw_round_a(bits),a,b))

def hash_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()

rng=random.Random(3002026)
central_total=0
for n in (5,7,9,11,13):
    m=(n-1)//2
    for x in range(1<<n):
        expected=int(x.bit_count()>=m+1)
        assert all(y==expected for y in run_three(x,1,m+1,n)),(n,x)
        central_total+=1

sample_total=0; sample_by_n={}
for n in (25,27,31,45,61,101,201):
    m=(n-1)//2; classes=[]
    for r in range(1,m+1):
        for p in range(1,r+1):
            q=n-r-p
            if p<=q<=r and (p,q,r)!=(1,m,m):
                classes.append((p,q,r))
    take=min(len(classes),200)
    selected=rng.sample(classes,take)
    for p,q,r in selected:
        tag,x,_,_=counterexample(m,p,q,r)
        assert tag!='central' and x.bit_count()==m+1
        result=run_three(x,p,p+q,n)
        assert not all(result),(n,p,q,r,tag)
        sample_total+=1
    sample_by_n[str(n)]=take

report={
 'status':'PASS',
 'scope':'Independent literal-window finite cross-check; not infinite-proof certification',
 'central_full_states_n_5_to_13':central_total,
 'noncentral_literal_three_round_witnesses':sample_total,
 'noncentral_sample_sizes':sample_by_n,
 'seed':3002026,
}
(BASE/'integrated_sanity_report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
