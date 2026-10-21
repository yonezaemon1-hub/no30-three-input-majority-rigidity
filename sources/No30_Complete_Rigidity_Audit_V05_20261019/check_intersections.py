"""Independent set-based consistency audit for all stated intersection formulas.
This checker does not depend on verify_v05.py. Finite tests only.
"""
def shift(u,a,n):
    return {(i-a) % n for i in u}

def pieces(u,a,b,n):
    u0=u
    u1=shift(u,a,n)
    u2=shift(u,b,n)
    return len(u0 & u1), len(u0 & u2), len(u1 & u2), len(u0 & u1 & u2)

def verify():
    tests=0
    # General Case I counts and disjointness.
    for m in range(12,180):
        n=2*m+1
        for d in range(2,(m-1)//3+1):
            r=m-d; a=m-d-4; b=d+3
            u=set(range(0,d+3)) | set(range(d+7,m+3))
            for p in range(2*d+1,(m+d+1)//2+1):
                q=m+d+1-p
                if not(p<=q<=r): continue
                c1,c2,c3,t=pieces(u,p,p+q,n)
                f=lambda s:max(0,a-s)+min(b,s-4)
                assert (c1,c2,c3,t)==(f(p),f(r),f(q),0),(m,d,p,(c1,c2,c3,t))
                assert c1+c2+c3>=m
                tests+=1
    # d=0, d=1 exact tables
    for m in range(12,231):
        n=2*m+1
        for d in (0,1):
            r=m-d
            for p in range(max(1,2*d+1),(m+d+1)//2+1):
                q=m+d+1-p
                if not(p<=q<=r): continue
                if d==0:
                    if p in (1,(m+1)//2):continue
                    l=max(4,p-1)
                else:
                    if p==3 or (m%2==0 and p==(m+2)//2):continue
                    l=max(5,p-2)
                u=set(range(l-1))|set(range(l+3,m+3))
                actual=pieces(u,p,p+q,n)
                if d==0:
                    expected=({2:(m-5,5,4,2),3:(m-7,5,3,0),4:(m-8,5,3,0)}.get(p,(m-p-3,5,p-2,0)))
                else:
                    expected=(m-9,5,4,0) if p<=6 else (m-p-2,5,p-3,0)
                assert actual==expected,(m,d,p,actual,expected)
                tests+=1
    # E-family, universal correction for the d=1 even-m balanced boundary
    for k in range(6,231):
        m=2*k;n=4*k+1;u=set(range(0,k-1))|set(range(k+1,2*k+1))
        assert pieces(u,k+1,2*k+2,n)==(k-1,2,k-1,0),k
        tests+=1
    # Recheck the V0.4 special obstruction intersection counts
    for m in range(12,231):
        n=2*m+1
        u=set(range(0,2))|set(range(5,8))|set(range(14,m+7))
        h=min(2,max(0,m-13))
        assert pieces(u,3,m+2,n)==(m-10,5+h,5+h,h),('A',m)
        if m%2==0:
            k=m//2
            u=set(range(0,2))|set(range(4,k+2))|set(range(2*k+5,3*k+3))
            assert pieces(u,k,2*k+1,n)==(4,2*k-5,3,1),('B-even',m)
        else:
            k=(m-1)//2
            u=set(range(0,2))|set(range(4,k+3))|set(range(k+5,2*k+3))
            assert pieces(u,k+1,2*k+2,n)==(k,3,k,1),('B-odd',m)
        tests+=1
    print(f'PASS: {tests} exact set-intersection identities checked')
    small=[]
    for d in range(2,6):
        for m in range(max(12,3*d+1),2*d+11):
            a=m-d-4;b=d+3
            f=lambda s:max(0,a-s)+min(b,s-4)
            margin=min(f(p)+f(m+d+1-p)+f(m-d)-m for p in range(2*d+1,(m+d+1)//2+1))
            small.append((d,m,margin))
    print('PASS: finite boundary table rows',len(small),'minimal margins by d', {d:min(v for dd,m,v in small if dd==d) for d in range(2,6)})
if __name__=='__main__':verify()
