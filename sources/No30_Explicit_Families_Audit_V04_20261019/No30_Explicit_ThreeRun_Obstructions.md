# No.30 V0.4 — Explicit uniform three-run counterexamples for both residual gap families

Author: Ryutaro Yonezu (AI-assisted mathematical investigation)
Date: 2026-10-19
Status: PROOF DRAFT / awaiting independent audit. Full classification for arbitrary odd n >= 25 is STILL OPEN. Novelty INCONCLUSIVE. Publication HOLD.

## Setup

Let n=2m+1, m>=12. Work on the cyclic binary words of length n. For input x of weight m+1, let w_i=x_i x_{i+1}; then A(x) is the complement of a cyclic translate of w. With three taps T={0,a,b}, let z=B_{a,b}(w). By the established V0.3 lemma, if |z|>=m then the complete A-B-A circuit fails on x: it cannot output the constant 1 word although x has a strict 1 majority.

For U={i:w_i=1}, let U-a denote the n-cyclic translate {i-a mod n:i in U}. Then

  |B_{a,b}(w)| = |U ∩ (U-a)| + |U ∩ (U-b)| + |(U-a) ∩ (U-b)| - 2|U ∩ (U-a) ∩ (U-b)|.

This is exact pointwise inclusion-exclusion for the majority of three bits.

## Theorem V0.4-A: (3,m-1,m-1) universally fails

For every integer m>=12, choose the tap offsets a=3, b=m+2. These gaps are (3,m-1,m-1). Construct the binary word

  x = 1^3 0^2 1^4 0^5 1^(m-6) 0^(m-7).

It has length 2m+1, weight m+1 and exactly three 1-runs. Its pair-product word w has support (integer intervals inclusive, starting at 0)

  U = [0,1] ∪ [5,7] ∪ [14,m+6].

By directly intersecting U with its shifts by -3 and -(m+2), and putting h=min(2,max(0,m-13)), the three pairwise intersection cardinalities are

  |U ∩ (U-3)|            = m-10,
  |U ∩ (U-(m+2))|        = 5+h,
  |(U-3) ∩ (U-(m+2))|    = 5+h,
  |U ∩ (U-3) ∩ (U-(m+2))|= h.

Therefore |z|=(m-10)+(5+h)+(5+h)-2h=m. Every such tap triple fails. These expressions include the border cases m=12,13,14, and stabilize when m>=15.

Remark: the previous audit's run-length expression (3,4,m-5) sums to m+2, inconsistent with a margin-one majority input of weight m+1. The corrected final run length is m-6, as above.

## Theorem V0.4-B: (ceil(m/2),floor(m/2)+1,m) universally fails

**CAUTION:** The tap offsets MUST be a=ceil(m/2), b=m+1. A previous exploratory test used the incorrect even/odd offsets and was discarded. The following is for the correct, gap-qualified residual class.

**Even m=2k, k>=6**: Let T={0,k,2k+1}, with sorted cyclic gaps (k,k+1,2k). Take

  x = 1^3 0^1 1^(k-1) 0^(k+2) 1^(k-1) 0^(k-3).

It has n=4k+1 sites and 2k+1 ones. Its w support is

  U=[0,1] ∪ [4,k+1] ∪ [2k+5,3k+2].

The pairwise intersection cardinalities for shifts -k and -(2k+1) are, in order,

  (4,2k-5,3),

and the triple-intersection cardinality is 1. Thus |z|=4+(2k-5)+3-2=2k=m.

**Odd m=2k+1, k>=6**: Let T={0,k+1,2k+2}, with sorted gaps (k+1,k+1,2k+1). Take

  x = 1^3 0^1 1^k 0^1 1^(k-1) 0^(2k-1).

It has n=4k+3 sites and 2k+2 ones. Its w support is

  U=[0,1] ∪ [4,k+2] ∪ [k+5,2k+2].

The pairwise intersection cardinalities for shifts -(k+1) and -(2k+2) are, in order,

  (k,3,k),

and the triple-intersection cardinality is 1. Thus |z|=k+3+k-2=2k+1=m.

Both constructions give three-run counterexamples for every integer m>=12, with precisely the gaps that survive 1-/2-run searches.

## Proof mechanics / audit checklist

For every displayed support U, intersections are between at most three *ordinary* intervals and their modulo-n translations. The listed cardinalities result by splitting a translated interval whenever it crosses 0, applying max(0,min(right endpoints)-max(left endpoints)+1) to all interval pairs, and subtracting duplicates in triple intersections. The formulas are valid for m>=12; there is no limiting or asymptotic assumption. Please independently check the intersection counts, particularly wraparound and the small boundary cases m=12..15.

One may verify the proof using `verify_explicit_families.py`, which independently computes A, B, A by literal cyclic windows and independently recomputes set intersection cardinalities. It does *not* prove the formulas for untested m; the interval counting above is the mathematical step.

## What remains open

These theorems dispose of *two residual families* singled out by a finite 2-run search. It is not yet proved that every other noncentral triple admits a 1- or 2-run counterexample for *all* odd n>=25. Numerical checks of that last statement for n<=101 are not a proof. Consequently the universal uniqueness theorem for (1,m,m) remains a **CONJECTURE**. Prior-art novelty and importance remain INCONCLUSIVE; no priority claimed.
