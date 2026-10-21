No.30 Offset Rigidity — V02 independent-audit handoff
Date: 2026-10-19
Author: Ryutaro Yonezu

Purpose:
This is an ADDENDUM to the original No30_Proof_Audit_V01_20261019.zip.
Original V01 is unchanged. This archive provides one additional
necessary-and-sufficient theorem for the family A o B_d o A, its direct proof,
and a fresh separate bitmask verifier written with Python standard library.

Contents:
- No30_Offset_Rigidity_Proof.md: math result, proof, scope, prior art
- verify_offset.py: full tests and explicit counterexample family
- verification_results.json: completed test results
- SHA256SUMS.txt: integrity hashes for the other three files and README

To reproduce on Windows 10 / Python 3.12:
  py -3.12 verify_offset.py
Expect: RESULT=PASS and a refreshed verification_results.json.
The verifier checks all 43,680 states for n=5,7,9,11,13,15,
for every admissible offset d at each n (538,848 (input,offset) test pairs).
It also checks the explicit run witness for every odd n from 5 to 101.

State of audit:
- Original general A o B_(m+1) o A theorem: independently audited
  PASS in a supplied Claude report.
- NEW 'offset rigidity' theorem: algebraic proof candidate and in-house
  verification PASS. External reviewer has NOT yet signed off.
- Scholarly novelty: INCONCLUSIVE. Publication: HOLD.
- 2018 papers already show depth-two near-global majority circuits
  in a more general model, so the scope is deliberately narrow.
