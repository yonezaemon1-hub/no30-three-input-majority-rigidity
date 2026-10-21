"""No.30 independent exhaustive verification, Python standard library only.

Usage: py -3 audit_no30.py
       py -3 audit_no30.py --max-n 15

This code is an independent reconstruction from the theorem definitions.
It does not prove the theorem for arbitrary n.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path


def a_rule(x: tuple[int, ...]) -> tuple[int, ...]:
    n = len(x)
    m = (n - 1) // 2
    s = sum(x)
    return tuple(int(s - x[(i - 2) % n] - x[(i - 1) % n] >= m)
                 for i in range(n))


def b_rule(x: tuple[int, ...]) -> tuple[int, ...]:
    n = len(x)
    h = (n + 1) // 2
    return tuple(int(x[i] + x[(i + 1) % n] + x[(i + h) % n] >= 2)
                 for i in range(n))


def count_runs(x: tuple[int, ...], bit: int) -> int:
    return sum(x[i] == bit and x[(i - 1) % len(x)] != bit
               for i in range(len(x)))


def lemma_data(w: tuple[int, ...]) -> tuple[int, int, int, int, int]:
    n = len(w)
    m = (n - 1) // 2
    h = m + 1
    s = sum(w)
    r = count_runs(w, 1)
    q = sum(w[i] != w[(i + 1) % n] and w[(i + h) % n] == 0
            for i in range(n))
    v = tuple(w[(k * m) % n] for k in range(n))
    long_zero_runs = sum(v[i] == 1 and v[(i + 1) % n] == 0
                         and v[(i + 2) % n] == 0 for i in range(n))
    b_count = sum(b_rule(w))
    return s, r, q, long_zero_runs, b_count


def run(max_n: int) -> dict:
    results = []
    for n in range(5, max_n + 1, 2):
        m = (n - 1) // 2
        lemma_checked = 0
        for x in itertools.product((0, 1), repeat=n):
            expected = (int(sum(x) > m),) * n
            got = a_rule(b_rule(a_rule(x)))
            assert got == expected, ('THEOREM_FAIL', n, x, got, expected)
            if 0 < sum(x) <= m:
                s, r, q, l2, bcount = lemma_data(x)
                assert q == 2 * l2, ('EXACT_IDENTITY_FAIL', n, x, q, l2)
                assert l2 >= 1, ('NO_LONG_ZERO_RUN', n, x)
                assert bcount == s + r - q, ('COUNT_IDENTITY_FAIL', n, x)
                assert bcount <= s + r - 2, ('LEMMA_FAIL', n, x)
                lemma_checked += 1
        results.append({'n': n, 'all_states': 1 << n,
                        'theorem_failures': 0, 'minority_lemma_states': lemma_checked,
                        'lemma_failures': 0})
        print(f"PASS n={n}, all_states={1<<n}, lemma_states={lemma_checked}")

    witness = {}
    n = 5
    for name in ('A', 'B', 'AA', 'AB', 'BA', 'BB'):
        fns = {'A': a_rule, 'B': b_rule}
        counterexample = None
        for x in itertools.product((0, 1), repeat=n):
            y = x
            for rule in name:
                y = fns[rule](y)
            if y != (int(sum(x) > (n - 1) // 2),) * n:
                counterexample = {'input': ''.join(map(str, x)),
                                  'output': ''.join(map(str, y))}
                break
        assert counterexample is not None, ('TWO_ROUND_LOWER_BOUND_FAIL', name)
        witness[name] = counterexample
    print('PASS n=5, no exact classification among rule words of length <=2')
    return {'status': 'PASS', 'max_n': max_n, 'results': results,
            'total_states_checked': sum(row['all_states'] for row in results),
            'total_minority_lemma_states': sum(row['minority_lemma_states'] for row in results),
            'n5_counterexamples': witness,
            'scope': 'exhaustive finite checks; all-n proof is separate, novelty not established'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=17)
    args = parser.parse_args()
    if args.max_n < 5 or args.max_n % 2 != 1:
        parser.error('--max-n must be odd and >=5')
    report = run(args.max_n)
    target = Path(__file__).resolve().parent / 'audit_report.json'
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('REPORT', target.name)
