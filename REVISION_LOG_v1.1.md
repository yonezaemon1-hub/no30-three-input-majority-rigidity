# Historical v1.1 revision log

Note added for v1.2: The references to publisher verification in this historical log concern bibliographic metadata, titles, and DOI landing pages. They do **not** assert full-text equivalence examination.

# No.30 version 1.1 revision log — 20 October 2026

The integrated v1.0 manuscript received an independent AI audit reporting PROOF PASS and BIBLIOGRAPHY PASS with minor changes, NOVELTY INCONCLUSIVE. This v1.1 release corrects the issues without changing Theorems 1–2 or their claim boundaries.

1. Added a closed finite-free correlation formula for arbitrary two-run input supports U = [0,l-2] union [l+3,m+2] and shifts 1<=s<=m (Appendix A).
2. Derived every row of the Case II and Case III correlation tables for all admissible m,p using that algebraic identity; explicitly enumerated possible triple overlaps to justify t=0 and the exceptional t=2.
3. Tightened the proof of A(z)=0 iff |z|<=m-1 at weight m+1 by choosing an omitted zero.
4. Removed the logically impossible w=0 branch in Theorem 1's proof; instead proved w has weight >=1.
5. Clarified Amano–Yoshida: every odd n>=7. Checked against IEICE publisher data.
6. Verified Moran 1994 and Fukś 1997 titles/DOIs via their journal publishers; clarified that DCAI 2019 conference proceedings are cited as Springer 2020 with pages 163–170.
7. Changed preprint headers and date label; removed source-only __pycache__/cpython-313 bytecode; checked Windows/Python 3.12-compatible verification scripts require the standard library.
8. Changed the status to report completed external AI review of integrated v1.0, while identifying v1.1 as awaiting a final differential review. Novelty INCONCLUSIVE and no priority claim are maintained. No GitHub or Zenodo publication was performed.

## Additional direct verification (not a substitute for the general proof)

The v1.1 symbolic-overlap checker independently enumerated 2,747 parameter pairs in Case II, 2,846 in Case III, and 45,144 generic autocorrelation tests for m=12..110. All agreed with direct set intersections, including the full triple overlaps. See `verification/check_symbolic_overlap_v11.py` and result log. The symbolic equations and their derivation, not these finite tests, underwrite the unbounded statements.

## External bibliographic record

- https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.E101.A.1543/_p
- https://www.sciencedirect.com/science/article/pii/0012365X94902364
- https://journals.aps.org/pre/abstract/10.1103/PhysRevE.55.R2081
- https://link.springer.com/book/10.1007/978-3-030-23887-2
