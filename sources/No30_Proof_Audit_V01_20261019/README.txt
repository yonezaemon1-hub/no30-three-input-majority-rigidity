No.30 THREE-ROUND EXACT MAJORITY — AUDIT PACK v0.1
2026-10-19

Status: mathematical proof draft; finite computational audit PASS;
novelty INCONCLUSIVE; NOT peer reviewed; publication HOLD.

Contents:
- No30_Theorem_and_Proof_DRAFT.md: definitions, lemma, all-n proof candidate, prior art boundaries
- audit_no30.py: independent standard-library exhaustive checker, defaults n=5..17
- audit_report.json: completed finite audit evidence
- SHA256SUMS.txt: SHA-256 for each file above (excluding the checksum manifest itself)

Windows 10 / Python 3.12:
  py -3 audit_no30.py

Every n is odd. A uses n-2 votes per site; B uses 3 votes, one long-range.
Three update rounds are NOT three bounded-radius local communication rounds.
No new runtime/kernel/factory and no API are required.
