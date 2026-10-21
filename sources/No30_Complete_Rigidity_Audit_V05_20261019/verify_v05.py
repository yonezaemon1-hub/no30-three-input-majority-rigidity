"""No.30 V0.5 standalone sanity checks. Exact finite tests; not a general proof.
Windows 10 + Python 3.12, no third-party libraries.
"""
from collections import Counter
from time import perf_counter


def rot(x,s,n,mask):
    s%=n
    return ((x>>s)|(x<<(n-s)))&mask if s else x

def ones(x,m,n):
    return x.bit_count()

def counterexample(m,p,q,r):
    """Explicit theorem-case witness; x has m+1 ones and <=3 one runs."""
    d=m-r
    if d>=2:
        l=d+4;g=3
        return 'two_run_general', ((1<<l)-1)|(((1<<(m+1-l))-1)<<(l+g)),l,g
    if d==1:
        if p==3:
            # (3,m-1,m-1), V0.4-A
            # x = 1^3 0^2 1^4 0^5 1^(m-6) 0^(m-7)
            x=((1<<3)-1) | (((1<<4)-1)<<5) | (((1<<(m-6))-1)<<14)
            return 'three_run_A',x,None,None
        if m%2==0 and p==(m+2)//2:
            k=m//2
            # E: 1^k 0 1^(k+1) 0^(2k-1)
            x=((1<<k)-1)|(((1<<(k+1))-1)<<(k+1))
            return 'two_run_E',x,k,1
        l=max(5,p-2);g=3
        return 'two_run_d1',((1<<l)-1)|(((1<<(m+1-l))-1)<<(l+g)),l,g
    if d==0:
        if p==1:return 'central',None,None,None
        if p==(m+1)//2:
            k=m//2
            if m%2==0:
                # 1^3 0 1^(k-1) 0^(k+2) 1^(k-1) 0^(k-3)
                x=((1<<3)-1)|(((1<<(k-1))-1)<<4)|(((1<<(k-1))-1)<<(2*k+5))
            else:
                # 1^3 0 1^k 0 1^(k-1) 0^(2k-1)
                x=((1<<3)-1)|(((1<<k)-1)<<4)|(((1<<(k-1))-1)<<(k+5))
            return 'three_run_B',x,None,None
        l=max(4,p-1);g=3
        return 'two_run_d0',((1<<l)-1)|(((1<<(m+1-l))-1)<<(l+g)),l,g
    raise AssertionError((m,p,q,r))

def analytic_value(m,p,q,r):
    d=m-r
    a=m-d-4;b=d+3
    f=lambda s:max(0,a-s)+min(b,s-4)
    return f(p)+f(q)+f(r)

def verify(max_m=230):
    tic=perf_counter();types=Counter();counts=0;low=10**8
    for m in range(12,max_m+1):
        n=2*m+1;mask=(1<<n)-1
        for d in range((m-1)//3+1):
            r=m-d
            for p in range(max(1,2*d+1),(m+d+1)//2+1):
                q=m+d+1-p
                if not(p<=q<=r):continue
                tag,x,l,g=counterexample(m,p,q,r)
                if tag=='central':
                    assert (p,q,r)==(1,m,m)
                    continue
                assert x.bit_count()==m+1,(m,p,q,r,tag,'weight')
                assert x.bit_length()<=n
                w=x & rot(x,1,n,mask)
                wa=rot(w,p,n,mask);wb=rot(w,p+q,n,mask)
                z=(w&wa)|(w&wb)|(wa&wb)
                actual=z.bit_count()
                assert actual>=m,(m,p,q,r,tag,'not counterexample',actual)
                if d>=2:
                    predicted=analytic_value(m,p,q,r)
                    assert actual==predicted,(m,p,q,r,predicted,actual)
                    assert not (w&wa&wb)
                    low=min(low,actual-m)
                types[tag]+=1; counts+=1
        if m%50==0: print('verified m =',m,flush=True)
    print('PASS max_m',max_m,'noncentral classes',counts,'case counts',dict(types),'min d>=2 margin',low,'seconds',round(perf_counter()-tic,3),flush=True)
if __name__=='__main__':
    import sys
    verify(int(sys.argv[1]) if len(sys.argv)>1 else 230)
