"""Standalone exact verifier, Python 3.12, no third-party libraries.
This does NOT trust the C++ bitwise-majority reduction: it evaluates all
three synchronous rounds from their definitions on every supplied witness.
"""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

def outer_A(bits: list[int]) -> list[int]:
    n=len(bits); threshold=(n-1)//2
    return [int(sum(bits[(i+j)%n] for j in range(n-2))>=threshold)
            for i in range(n)]

def middle_B(bits: list[int],a:int,b:int) -> list[int]:
    n=len(bits)
    return [int(bits[i]+bits[(i+a)%n]+bits[(i+b)%n]>=2)
            for i in range(n)]

def circular_one_runs(bits: list[int]) -> int:
    return sum(bits[i] and not bits[(i+1)%len(bits)] for i in range(len(bits)))

def verify():
    seen=set(); counts=Counter();maxruns=0
    with (HERE/'counterexamples_25_to_61.csv').open(newline='') as fh:
        reader=csv.DictReader(fh)
        for row in reader:
            n,a,b,x,cnt,runs=(int(row[key]) for key in
                           ['n','a','b','witness_decimal','defect_majority_ones','one_runs'])
            m=(n-1)//2
            assert n in range(25,62,2) and 1<=a<b<n
            assert (a,b) not in {(1,m+1),(m,m+1),(m,n-1)}
            assert (n,a,b) not in seen
            seen.add((n,a,b));counts[n]+=1
            bits=[(x>>i)&1 for i in range(n)]
            assert sum(bits)==m+1
            assert circular_one_runs(bits)==runs
            maxruns=max(maxruns,runs)
            first=outer_A(bits)
            actual_middle=middle_B(first,a,b)
            last=outer_A(actual_middle)
            assert last != [1]*n, (n,a,b,x)
            defect=[1-z for z in first]
            assert sum(middle_B(defect,a,b))==cnt
            assert cnt>=m
    assert set(counts)==set(range(25,62,2))
    for n,v in counts.items():
        assert v==(n-1)*(n-2)//2-3,(n,v)
    print(f'PASS: {len(seen):,} distinct full-three-round counterexamples, {len(counts)} sizes, max one-run count {maxruns}')
    for n in sorted(counts):print(f'  n={n:2d} rejected_noncentral={counts[n]:4d}')

if __name__=='__main__':verify()
