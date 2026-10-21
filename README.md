# No.30 — Rigidity of Three-Input Majority Compositions on Odd Cyclic Networks

**English preprint v1.2, 20 October 2026** — Ryutaro Yonezu / Yonezu Research Lab.

Status: **mathematical proof reviewed by an independent AI assistant; reported integrated v1.0 PASS and v1.1 differential PASS.** No human peer review. **Scholarly novelty INCONCLUSIVE; no priority claim.** Publication-ready as a transparent *unrefereed preprint*; this archive does not itself confirm public GitHub/Zenodo posting.

**Rights: All rights reserved.** (c) 2026 Ryutaro Yonezu. Source code supplied for verification; no general reuse license granted for manuscript or code.

## Main theorem

For odd n=2m+1>=25, outer layer A is the synchronous majority of n-2 consecutive cyclic sites and middle layer B the synchronous three-tap majority on {0,a,b}. The consensus A(B(A(x))) equals global majority on all binary x **if and only if** the unordered cyclic gaps of the tap set are {1,m,m}. The successful pattern works for all odd n>=5. The lower threshold 25 is sharp (additional success configurations at n=21 and 23).

This is an architecture-constrained classification, not a general-depth or fan-in optimality claim.

## Main files

- `No30_Rigidity_Preprint_v1.2.pdf` — 9-page English paper.
- `No30_Rigidity_Preprint_v1.2.tex` — editable mathematical source.
- `REVISION_LOG_v1.2.md` — editorial corrections after v1.1 review.
- `INDEPENDENT_AI_REVIEW_SUMMARY_20261020.md` — author-supplied report summary and limitations.
- `CLAIM_AND_AUDIT_MATRIX.md` — status and scope.
- `verification/*` — finite checks and recorded outputs.
- `source_archives/*`, `sources/*` — V0.1–V0.5 evidence and original archives.
- `prior_art/*` — prior-art audit and limitations.
- `SHA256SUMS.txt` — digest of every other ZIP member.

## Local verification (Windows 10, Python 3.12)

```powershell
python .\verification\check_symbolic_overlap_v11.py
python .\verification\integrated_sanity.py
python .\verification\boundary_sharpness.py
python .\sources\No30_Complete_Rigidity_Audit_V05_20261019\verify_v05.py 230
python .\sources\No30_Complete_Rigidity_Audit_V05_20261019\check_intersections.py
```

Only the standard library is required for these scripts. Build PDF from the TeX using `pdflatex` twice if a TeX distribution is available.

## Scholarly status

Bibliographic metadata and some publisher records have been checked. Full-text equivalence coverage of all prior work is incomplete. **Novelty INCONCLUSIVE.** AI-assisted proof and numerical audits are reported, but no human peer review has occurred. No claim of priority or general majority-circuit optimality is made.
