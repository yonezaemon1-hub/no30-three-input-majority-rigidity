"""Produce one concrete <=2-run counterexample per nonexceptional, gap-admissible class."""
import csv
from pathlib import Path

OUT=Path(__file__).with_name('two_run_certificates_25_to_101.csv')

def construct(n,l,g):
    m=(n-1)//2
    return ((1<<l)-1)|(((1<<(m+1-l))-1)<<(l+g))

def R(w,k,n):
    return ((w>>k)|(w<<(n-k)))&((1<<n)-1)


def main():
    rows=[]
    for n in range(25,102,2):
        m=(n-1)//2
        classes={(p,q,n-p-q) for p in range(1,m+1) for q in range(p,m+1) if q <= n-p-q <= m}
        exceptions={(1,m,m),(3,m-1,m-1),((m+1)//2,m//2+1,m)}
        pending=classes-exceptions
        for l in range(1,m+1):
            if not pending:break
            for g in range(1,m):
                if not pending:break
                x=construct(n,l,g);w=x&R(x,1,n)
                for p,q,r in sorted(tuple(pending)):
                    u=R(w,p,n);v=R(w,p+q,n)
                    if ((w&u)|(w&v)|(u&v)).bit_count()>=m:
                        rows.append((n,p,q,r,l,g,str(x)))
                        pending.remove((p,q,r))
        assert not pending,(n,sorted(pending))
    with open(OUT,'w',newline='',encoding='utf8') as f:
        wr=csv.writer(f)
        wr.writerow(['n','p','q','r','ones_first_run','zero_gap_first','x_decimal'])
        wr.writerows(rows)
    print(f'PASS: wrote {len(rows)} concrete 1-/2-run gap-admissible obstruction certificates for n=25..101 to {OUT.name}')

if __name__=='__main__':main()
