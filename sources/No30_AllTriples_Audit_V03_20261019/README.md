# No.30 all-triplet exploration, audit supplement V0.3

This is a **new add-on**, not a modification of No.30 V0.1 or V0.2.

## Key results
- General gap obstruction theorem, self-contained draft proof: if a cyclic triple works, all three gaps must be at most (n-1)/2.
- Within triples containing adjacent cells, the original `(1,m,m)` geometry is necessary and sufficient, assuming V0.1 sufficiency (Claude PASS per user's report).
- For all odd n=25 to 61, each of the 17,442 noncentral tap pairs has an explicit failing majority-margin input. Pure Python independently checked the complete three-round circuit on every supplied certificate.
- Full uniqueness for **all** odd n>=25 is **not proved**. Research novelty remains **INCONCLUSIVE**, publication **HOLD**.

## Windows 10 verification

From this unzipped folder, using Python 3.12 with no extra packages:

```powershell
python .\verify_counterexamples.py
```

Expected first line:

`PASS: 17,442 distinct full-three-round counterexamples, 19 sizes, max one-run count 4`

For regenerating counterexamples (optional, requires an installed C++17 compiler):

```sh
g++ -O3 -std=c++17 find_witnesses.cpp -o find_witnesses
./find_witnesses counterexamples_25_to_61.csv
```

Python verifier checks the resulting CSV without using C++ logic.

## Claim limits

The all-n statement about arbitrary 3-tap triples is a **conjecture**. Independent proof audit is pending. No scholarly priority is claimed. See `No30_Gap_Obstruction_Proof.md`.
