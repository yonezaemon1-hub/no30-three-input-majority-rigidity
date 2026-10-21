"""Independently verify the complete CSV via literal A/B/A updates (no bit trick)."""
import csv
from pathlib import Path
from verify_explicit_families import A,B,one_runs

P=Path(__file__).with_name('two_run_certificates_25_to_101.csv')
seen={};count=0
with P.open(newline='',encoding='utf8') as f:
    for row in csv.DictReader(f):
        n,p,q,r,l,g=(int(row[k]) for k in ('n','p','q','r','ones_first_run','zero_gap_first'))
        m=(n-1)//2;assert n in range(25,102,2)
        assert p<=q<=r<=m and p+q+r==n
        xdec=int(row['x_decimal'])
        x=[(xdec>>i)&1 for i in range(n)]
        assert sum(x)==m+1 and one_runs(x)<=2
        assert sum(A(B(A(x),p,p+q)))<n,(n,p,q,r,l,g)
        s=seen.setdefault(n,set())
        assert (p,q,r) not in s
        s.add((p,q,r));count+=1
for n in range(25,102,2):
    m=(n-1)//2
    admissible={(p,q,n-p-q) for p in range(1,m+1) for q in range(p,m+1) if q<=n-p-q<=m}
    exceptions={(1,m,m),(3,m-1,m-1),((m+1)//2,m//2+1,m)}
    assert seen[n]==admissible-exceptions,(n,len(seen[n]),len(admissible-exceptions))
print(f'PASS: independent full A->B->A recheck of {count} 2-run certificates; complete class coverage for 39 odd lengths n=25..101.')
