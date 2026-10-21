# No.30 V0.5 — audit handoff

**Status:** The proof of universal all-three-tap classification for all odd n>=25 is a **complete proof candidate**; it is NOT independently audited. The already reported Claude audits of V0.1, V0.3 and V0.4 are external evidence, but they do not certify V0.5. Novelty: INCONCLUSIVE. Publication: HOLD. No additional runtime, package, cloud service or paid API is necessary.

## Central claim

For n=2m+1>=25, with synchronous A equal to the (n-2)-input majority on the consecutive sites i,...,i+n-3, and B_{a,b} equal to the 3-input majority on sites i,i+a,i+b, we claim:

    A o B_{a,b} o A computes global majority for every input
    iff the cyclic gaps of {0,a,b} are (1,m,m) up to permutation.

The NEW work in V0.5 removes the open general 2-run obstruction conjecture by explicit, uniform witnesses. The proof treats all sorted gap types, with detailed interval formulas and a table of only 19 small boundary parameter rows.

## Main deliverable

- `No30_Full_Triple_Classification_Proof.md` — complete proposed mathematical argument, with case split and exact overlap identities.
- `verify_v05.py` — independently computes the actual Boolean middle majority, with explicit counterexamples for every noncentral gap class with m=12..230.
- `verify_v05_output.txt` — actual output from `python verify_v05.py 230`.
- `check_intersections.py` — separate pure-set checker of all stated pair/triple intersection formulas, including the inherited V0.4 A/B families.
- `check_intersections_output.txt` — actual output from `python check_intersections.py`.
- `SHA256SUMS.txt` — content hashes of the five files above, excluding this readme and the manifest.

## Reproduce on Windows 10 / PowerShell / Python 3.12

    Expand-Archive .\No30_Complete_Rigidity_Audit_V05_20261019.zip -DestinationPath .\No30_V05 -Force
    cd .\No30_V05
    python .\verify_v05.py 230
    python .\check_intersections.py
    Get-FileHash -Algorithm SHA256 .\No30_Full_Triple_Classification_Proof.md

The numerical experiments test finitely many inputs and do not prove the claim by themselves. The mathematical proof is the separate case analysis in the `.md` file. A new independent proof audit should verify the V0.5 interval formula in Case I, the 19-row table, the two boundary-overlap tables, and the use of the already-audited V0.4 A/B three-run witnesses.

## No.30 release gate

General proof: PROPOSED / INDEPENDENT AUDIT PENDING.
Numerical checks: PASS in specified finite domain.
Novelty: INCONCLUSIVE, literature audit pending.
Publication: HOLD.
