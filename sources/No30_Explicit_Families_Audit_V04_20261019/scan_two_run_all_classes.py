"""Exhaustive 1-/2-run majority-margin obstruction search, no dependencies.

Scans n=25..101 odd; this gives FINITE evidence only, not a universal theorem.
"""

def scan(n):
    m=(n-1)//2;mask=(1<<n)-1
    classes={(p,q,n-p-q) for p in range(1,m+1) for q in range(p,m+1) if q <= n-p-q <= m}
    survivors=set(classes)
    R=lambda w,a: ((w>>a)|(w<<(n-a)))&mask
    L=lambda k: (1<<k)-1
    for l in range(1,m+1):
        if len(survivors)<=3:
            break
        for g in range(1,m):
            if len(survivors)<=3:break
            x=L(l)|(L(m+1-l)<<(l+g))
            w=x&R(x,1)
            for p,q,r in tuple(survivors):
                y=R(w,p);z=R(w,p+q)
                if ((w&y)|(w&z)|(y&z)).bit_count()>=m:
                    survivors.remove((p,q,r))
    required={(1,m,m),(3,m-1,m-1),((m+1)//2,m//2+1,m)}
    assert survivors==required,(n,sorted(survivors),sorted(required))
    return len(classes), len(survivors)

if __name__=='__main__':
    counts=[]
    for n in range(25,102,2):
        total,survivors=scan(n)
        counts.append((n,total,survivors))
        print(f'n={n} classes={total} survivors={survivors}',flush=True)
    print(f'PASS: {len(counts)} odd sizes n=25..101: exactly three classes survive 1-/2-run witnesses; these include the central class and the two explicit 3-run families.')
