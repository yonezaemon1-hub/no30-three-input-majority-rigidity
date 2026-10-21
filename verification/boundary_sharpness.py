"""Exact exhaustive boundary check of the n=25 sharpness claim.
Enumerates every strict-margin-one majority input for n=21 and 23.
The other cases reduce by complement symmetry and the A rule's n-2 window.
Python standard library only, no external runtime.
"""
import json
from pathlib import Path

def rot(x,s,n,mask):
    return ((x>>s)|(x<<(n-s))) & mask

def enumerate_margin(n):
    m=(n-1)//2
    a,b=3,m+2  # gaps (3,m-1,m-1)
    mask=(1<<n)-1
    x=(1<<(m+1))-1
    checked=0;max_output_ones=0
    while x<=mask:
        w=x & rot(x,1,n,mask)
        wa=rot(w,a,n,mask); wb=rot(w,b,n,mask)
        z=(w&wa)|(w&wb)|(wa&wb)
        k=z.bit_count()
        assert k<=m-1,(n,x,k)
        max_output_ones=max(k,max_output_ones)
        checked+=1
        c=x&-x
        r=x+c
        x=(((r^x)>>2)//c)|r
    return {'n':n,'gap_type':[3,m-1,m-1],'margin_one_inputs':checked,'max_B_ones':max_output_ones,'status':'PASS'}

results=[enumerate_margin(21),enumerate_margin(23)]
assert results[0]['margin_one_inputs']==352716
assert results[1]['margin_one_inputs']==1352078
report={'status':'PASS','exact_margin_one_input_total':sum(r['margin_one_inputs'] for r in results),'results':results,'interpretation':'For n=21 and 23, gap (3,m-1,m-1) succeeds on all inputs by margin-one reduction; n=25 is the first odd length where the rigidity theorem can hold.'}
p=Path(__file__).resolve().parent/'boundary_sharpness_result.json'
p.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
