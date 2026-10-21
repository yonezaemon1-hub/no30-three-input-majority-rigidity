# No.30 V0.5 — Complete rigidity of three-tap cyclic majority for all odd n >= 25

Author: Ryutaro Yonezu (AI-assisted research)
Date: 2026-10-19
Status: COMPLETE PROOF CANDIDATE / INDEPENDENT AUDIT REQUIRED. Scholarly novelty INCONCLUSIVE. Publication HOLD.

## Definitions and theorem

Let n=2m+1, m>=12, and all indices be interpreted modulo n. Define the synchronous Boolean operations

    A(x)_i = Maj_{n-2}(x_i,...,x_{i+n-3}),
    B_{a,b}(x)_i = Maj_3(x_i,x_{i+a},x_{i+b}), 0<a<b<n.

The cyclic gaps of T={0,a,b} are a, b-a, n-b. Under cyclic permutation and reversal of this triple, success is equivalent (the reflection argument is given in V0.3). Let p<=q<=r be those gaps in sorted order.

**Claim (classification for n>=25).** The identity

    A o B_{a,b} o A = Maj_n(x) * 1^n    for every binary x

holds if and only if (p,q,r)=(1,m,m).

**Scope.** The sufficiency of the (1,m,m) tap pattern is V0.1, independently audited in the earlier reported review. The proof below establishes universal NECESSITY, combining the already audited V0.3 and V0.4 counterexamples with new 2-run families. The classification remains subject to an independent audit of this V0.5 proof.

## Reduction to one counterexample per noncentral gap class

If |x|=m+1, put w_i=x_i x_{i+1}. By V0.3 (also readily checked directly), A(x) is the complement of a cyclic translate of w, and bit complementation commutes with both majority rules. Also A(z) is identically zero if and only if |z|<=m-1. Thus it suffices to find x of weight m+1 with

    |B_{p,p+q}(w)| >= m.

Let U={i : w_i=1}. Let U-s be its cyclic translation and f_U(s)=|U intersect (U-s)|. With b=p+q=n-r,

    |B_{p,b}(w)| = f_U(p) + f_U(q) + f_U(r) - 2 t,

where t=|U intersect (U-p) intersect (U-b)|. Here f_U(n-s)=f_U(s).

If r>=m+1, the universal *single-run* witness from the independently audited V0.3 Theorem 1 immediately fails. Hence assume r<=m and write d=m-r>=0. Because p+q+r=2m+1 and p<=q<=r, we have

    p+q=m+d+1,     2d+1<=p<=q<=m-d.

We treat d>=2, d=1 and d=0 separately. All witnesses below have |x|=m+1.

## Case I: d>=2: one universal two-run witness

Take

    x = 1^(d+4) 0^3 1^(m-d-3) 0^(m-3).

Since p>=2d+1, q<=r=m-d and p<=q, necessarily m>=3d+1; thus all lengths in x are positive for d>=2. Its pair-product support is exactly

    U = [0,d+2] union [d+7,m+2].

This is contained in the integer interval [0,m+2], which comprises m+3 cyclic positions. If U, U-p and U-b had a common site, some translate of the three tap positions would lie inside this interval, forcing one of their three cyclic gaps to be >=n-(m+2)=m-1. But r=m-d<=m-2. Hence t=0.

For every 2d+1<=s<=m-d, the pair autocorrelation is

    f_U(s) = [m-d-4-s]_+ + min(d+3, s-4),      (1)

where [v]_+=max(0,v). Proof: the first term counts within the long interval [d+7,m+2]; the second counts overlaps from [0,d+2] into that long interval. The short interval has no self-overlap at shifts s>=2d+1>d+2, and the possible wrapped cross-overlap is absent because s<=m-d.

Put alpha=m-d-4, beta=d+3, gamma=d+7. For s>=gamma, equation (1) simplifies to

    f_U(s)=beta+[alpha-s]_+.

### Case I-a: d>=6

Here p>=2d+1>=d+7=gamma, so p,q,r>=gamma. By (1),

    |B(w)| >= 3beta+[alpha-p]_++[alpha-q]_+
            >= 3d+9 + [2alpha-(p+q)]_+
            = 3d+9 + [m-3d-9]_+
            >= m.

The second inequality is [v]_+ + [u]_+ >= [u+v]_+. This holds for all feasible m,d,p,q in this branch.

### Case I-b: 2<=d<=5, m>=2d+11

Then alpha>=gamma, r>=gamma and q>=gamma: indeed q>=(m+d+1)/2 >= (3d+12)/2 >=d+7.

If p>=gamma, the same argument as Case I-a applies.

If p<gamma<=alpha, then equation (1) gives f_U(p)=alpha-4 and f_U(q),f_U(r)>=beta. Therefore

    |B(w)| >= alpha-4+2beta = m+d-2 >= m.

### Case I-c: remaining finite small cases

Only the following parameter pairs remain (they are finite because 2<=d<=5 and max(12,3d+1)<=m<=2d+10). For each row, evaluate the **explicit formula (1)** at s=p, q=m+d+1-p, r=m-d, over each integer

    2d+1<=p<=floor((m+d+1)/2).

The table reports min_p (f_U(p)+f_U(q)+f_U(r)-m); each displayed value is computed by substitutions in (1), rather than by searching arbitrary binary words.

| d | m | minimum margin |
|---|---|---|
|2|12|0|
|2|13|0|
|2|14|0|
|3|12|1|
|3|13|2|
|3|14|1|
|3|15|1|
|3|16|1|
|4|13|2|
|4|14|3|
|4|15|4|
|4|16|3|
|4|17|2|
|4|18|2|
|5|16|5|
|5|17|6|
|5|18|5|
|5|19|4|
|5|20|3|

Every margin is nonnegative, completing Case I for every integer m>=12.

## Case II: d=1, i.e. r=m-1

Now p+q=m+2 and 3<=p<=q. There are three subcases.

**(a) p=3.** The gap pattern is (3,m-1,m-1); the previously independently audited V0.4-A three-run witness gives |B(w)|=m for every m>=12:

    x = 1^3 0^2 1^4 0^5 1^(m-6) 0^(m-7).

**(b) m=2k even and p=q=k+1.** The gap pattern (k+1,k+1,2k-1) has a new 2-run witness

    x = 1^k 0 1^(k+1) 0^(2k-1).

Then U=[0,k-2] union [k+1,2k], with offsets a=k+1 and b=2k+2. A direct overlap count gives the three pair intersections (k-1, 2, k-1), triple intersection zero, and hence |B(w)|=2k=m. Here k>=6 follows from m>=12.

**(c) all other p>=4.** Take g=3, l=max(5,p-2), and the generic two-run input

    x = 1^l 0^3 1^(m+1-l) 0^(m-3),
    U = [0,l-2] union [l+3,m+2].

The pair-intersection table is exact:

| p | f_U(p) | f_U(q) | f_U(r) | triple intersection t |
|---|---:|---:|---:|---:|
| 4,5,6 | m-9 | 4 | 5 | 0 |
| 7 to floor((m+2)/2), excluding (b) | m-p-2 | p-3 | 5 | 0 |

For every row, the sum is exactly m. This follows by intersecting the displayed integer intervals; in particular, the three-way intersection is empty because the only geometrically possible alignment when the largest gap is m-1 would require the interior tap to land in the removed four-position gap [l-1,l+2]. Thus every noncentral gap type in Case II fails.

## Case III: d=0, i.e. r=m

Now p+q=m+1 and 1<=p<=q. There are three subcases.

**(a) p=1.** The gap type is (1,m,m). It succeeds for all odd n>=5 by V0.1.

**(b) p=ceil(m/2).** If m=2k, this is (k,k+1,2k); if m=2k+1, this is (k+1,k+1,2k+1). These are exactly the two parity subcases of the independently audited V0.4-B three-run witness, giving |B(w)|=m for every m>=12.

**(c) every other p>=2.** Choose g=3 and l=max(4,p-1), with the same two-run x and U as in Case II. Because p<ceil(m/2), the following overlap table is valid for all m>=12:

| p | f_U(p) | f_U(q) | f_U(r) | triple t | |B(w)| |
|---|---:|---:|---:|---:|---:|
|2|m-5|4|5|2|m|
|3|m-7|3|5|0|m+1|
|4|m-8|3|5|0|m|
|5 to ceil(m/2)-1|m-p-3|p-2|5|0|m|

Here r=m and q=m+1-p. These entries again follow by ordinary intersections of U with U-p and U-(m+1), including the wrapped two-site contribution when p=2. They prove failure in every remaining noncentral gap class.

## Conclusion

All sorted cyclic gap triples are covered:

* If max gap >=m+1, V0.3 supplies a counterexample.
* Otherwise r=m-d; Case I eliminates every d>=2 triple.
* Case II eliminates all r=m-1 triples by V0.4-A, the new parity-boundary two-run witness, or the explicit two-run table.
* Case III eliminates every r=m triple other than (1,m,m) by V0.4-B or the explicit two-run table.
* V0.1 establishes the sufficiency of (1,m,m).

Thus the stated if-and-only-if classification holds for all odd n=2m+1>=25, subject to independent audit of this V0.5 argument and of the cited prerequisite proofs.

## Reproducibility, caution, and novelty boundary

`verify_v05.py` constructs a concrete counterexample for every noncentral gap triple with m=12..230 (n=25..461), checks its majority-margin, and cross-checks Case I's exact interval formula against direct Boolean calculations. The script's finite checks do NOT establish this infinite theorem; the case argument above does.

V0.5 changes the prior status of the **infinite all-triples classification** from CONJECTURE to COMPLETE PROOF CANDIDATE, not to independent-audit PASS. There has been no exhaustive new literature search for this particular full rigidity theorem; scholarly novelty stays INCONCLUSIVE. Do not claim any lower bound for unrestricted majority circuits. Publication remains HOLD.
