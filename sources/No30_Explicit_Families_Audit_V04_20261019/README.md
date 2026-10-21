# No.30 V0.4: explicit residual-family obstructions

Date: 2026-10-19
Author: Ryutaro Yonezu (AI-assisted research)

**Research status:** V0.3 gap obstruction and adjacent-pair classification independently audited PASS per Claude report. V0.4 newly proved two explicit counterexample families algebraically, with standard-library numerical verification. V0.4 proof awaits independent mathematical audit. No.30 full uniqueness for arbitrary n>=25: STILL A CONJECTURE. Scholarly novelty INCONCLUSIVE; publication HOLD. Prior results and files V0.1/V0.2/V0.3 unchanged.

## V0.4 deliverables

- `No30_Explicit_ThreeRun_Obstructions.md`: proof draft for two uniform counterexample families, including all exact overlaps and border cases.
- `verify_explicit_families.py`: literal A->B->A check of two families for m=12..200 and m=201,250,501; also checks each exact intersection count.
- `scan_two_run_all_classes.py`: complete run-length-1/2 scan over gap-admissible canonical classes n=25..101 odd; three types remain.
- `build_two_run_certificates.py`: regenerates explicit x-decimal witnesses for all nonexceptional admissible classes; do not modify CSV by hand.
- `two_run_certificates_25_to_101.csv`: 3830 independently checkable binary witnesses. Each row specifies n, sorted gaps p,q,r, x and run parameters.
- `verify_two_run_certificates.py`: recomputes actual A->B->A for each CSV row and proves CSV's *finite class coverage* (not infinite classification).
- `two_run_scan_results.txt`: console transcript of finite class scan.
- `verify_run.txt`: complete success transcript of V0.4 verifiers.
- `SHA256SUMS.txt`: checksums of all other package files.

## Run under Windows 10 + Python 3.12, no installation/API/cloud required

```powershell
cd "$env:USERPROFILE\Downloads\No30_V04_Explicit_Families"
python .\verify_explicit_families.py
python .\scan_two_run_all_classes.py
python .\verify_two_run_certificates.py
```

See `verify_run.txt` for expected PASS lines.

## New exact results

A. With gaps `(3,m-1,m-1)` and `a=3,b=m+2`, the 3-run word
`1^3 0^2 1^4 0^5 1^(m-6) 0^(m-7)` has `|B(w)|=m` for every integer m>=12.

B. With gaps `(ceil(m/2),floor(m/2)+1,m)` and offsets `a=ceil(m/2),b=m+1`, there are exact 3-run counterexamples for *every* integer m>=12, split according to parity. See proof.

**Important correction:** exploratory intermediate notes briefly used offsets `a=floor(m/2),b=m`; this gives a different triple and does NOT prove family B. Those intermediate claims are retracted. This package contains only the corrected offsets, formulas, and verifications.

C. For odd n=25..101, full finite classification follows combining V0.3's gap obstruction, the 3830 two-run witnesses in the CSV, these two general three-run obstructions, and V0.1 central sufficiency. A proof of the crucial global two-run exhaustion statement for *all* n is not yet available.
