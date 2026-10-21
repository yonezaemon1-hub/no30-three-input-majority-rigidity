"""Independent bit-mask verifier for No.30 offset rigidity.

Python 3.12+ standard library only; no paid API and no external packages.
Usage: python verify_offset.py
"""
import json
from datetime import datetime, timezone
from pathlib import Path


def a_rule(x, n):
    m = (n - 1) // 2
    pop = x.bit_count()
    out = 0
    for i in range(n):
        omit = ((x >> ((i - 2) % n)) & 1) + ((x >> ((i - 1) % n)) & 1)
        if pop - omit >= m:
            out |= 1 << i
    return out


def b_rule(x, n, d):
    out = 0
    for i in range(n):
        if (((x >> i) & 1) + ((x >> ((i + 1) % n)) & 1)
                + ((x >> ((i + d) % n)) & 1)) >= 2:
            out |= 1 << i
    return out


def apply(x, n, d):
    return a_rule(b_rule(a_rule(x, n), n, d), n)


def main():
    exhaustive_results = []
    for n in range(5, 16, 2):
        m = (n - 1) // 2
        all_ones = (1 << n) - 1
        successes = []
        first_counterexamples = {}
        for d in range(2, n):
            first_failure = None
            for x in range(1 << n):
                expected = all_ones if x.bit_count() >= m+1 else 0
                if apply(x, n, d) != expected:
                    first_failure = x
                    break
            if first_failure is None:
                successes.append(d)
            else:
                first_counterexamples[str(d)] = first_failure
        assert successes == [m+1], (n, successes)
        exhaustive_results.append({"n": n, "input_states": 1 << n,
                                   "offsets_tested": n-2, "passing_offsets": successes,
                                   "first_counterexample_by_failing_offset": first_counterexamples})
        print(f"EXHAUSTIVE n={n}: passing offsets {successes} / {n-2} tested")

    witness_results = []
    for n in range(5, 102, 2):
        m=(n-1)//2
        all_ones=(1<<n)-1
        x=(1<<(m+1))-1  # m+1 consecutive ones
        passing=[]
        for d in range(2,n):
            got=apply(x,n,d)
            if got == all_ones:
                passing.append(d)
            # Independently check the predicted intermediate weight, based on the witness.
            w=all_ones ^ a_rule(x,n)
            z=b_rule(w,n,d)
            assert z.bit_count() == (m-1 if d==m+1 else m), (n,d,z.bit_count())
        assert passing == [m+1], (n, passing)
        witness_results.append({"n":n,"witness":x,"passing_offsets":passing})
        if n<=19 or n%20==1:
            print(f"WITNESS n={n}: only d={m+1} survives")

    report={"status":"PASS", "scope":"n=5..15 exhaustive all inputs/all offsets; n=5..101 consecutive-one witness all offsets",
            "exhaustive":exhaustive_results, "witness":witness_results}
    path=Path(__file__).resolve().parent / "verification_results.json"
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n", encoding="utf-8")
    print("RESULT=PASS")

if __name__=="__main__":
    main()
