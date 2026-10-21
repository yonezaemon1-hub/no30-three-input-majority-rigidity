"""No30 V04: independent, standard-library-only end-to-end verification."""

def series(parts):
    return [int(bit) for bit, length in parts for _ in range(length)]


def build(m, family):
    if family == 'A':
        x=series([(1,3),(0,2),(1,4),(0,5),(1,m-6),(0,m-7)])
        return x,3,m+2,(m-10, 5+min(2,max(0,m-13)), 5+min(2,max(0,m-13)), min(2,max(0,m-13)))
    k=m//2
    if m%2==0:
        x=series([(1,3),(0,1),(1,k-1),(0,k+2),(1,k-1),(0,k-3)])
        return x,k,2*k+1,(4,2*k-5,3,1)
    x=series([(1,3),(0,1),(1,k),(0,1),(1,k-1),(0,2*k-1)])
    return x,k+1,2*k+2,(k,3,k,1)

def A(x):
    n=len(x); m=(n-1)//2
    return [int(sum(x[(i+j)%n] for j in range(n-2))>=m) for i in range(n)]


def B(x,a,b):
    n=len(x)
    return [int(x[i]+x[(i+a)%n]+x[(i+b)%n]>=2) for i in range(n)]


def one_runs(x):
    return sum(x[i]==1 and x[(i-1)%len(x)]==0 for i in range(len(x)))


def check(m,family):
    x,a,b,expected=build(m,family)
    n=2*m+1
    assert len(x)==n and sum(x)==m+1 and one_runs(x)==3
    w=[x[i]&x[(i+1)%n] for i in range(n)]
    U={i for i,b in enumerate(w) if b}
    Va={(i-a)%n for i in U}
    Vb={(i-b)%n for i in U}
    counts=(len(U & Va),len(U & Vb),len(Va & Vb),len(U & Va & Vb))
    assert counts==expected,(m,family,counts,expected)
    z=B(w,a,b)
    assert sum(z)==m and sum(z)==sum(counts[:3])-2*counts[3]
    out=A(B(A(x),a,b))
    assert out!=[1]*n, (m,family,'failed to produce counterexample')
    return sum(out)

if __name__=='__main__':
    tested=0
    for m in range(12,201):
        for fam in ('A','B'):
            check(m,fam);tested+=1
    # Larger spot checks stress wraparound with the same literal A/B implementations.
    for m in (201,250,501):
        for fam in ('A','B'):
            check(m,fam); tested+=1
    print(f'PASS: {tested} explicit majority-margin counterexamples, m=12..200 plus m=201,250,501; 2 families; all intersection counts matched; direct A-B-A failed every time.')
