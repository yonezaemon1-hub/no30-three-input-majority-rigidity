# No.30 — Three-Round Exact Majority Classification on Odd Rings

**Author:** Ryutaro Yonezu  
**Status (2026-10-19):** mathematical proof *draft*; independently checked computationally in this package; novelty INCONCLUSIVE; **not peer reviewed; publication HOLD**.

## Scope and terminology

Let `n = 2m+1 >= 5`, with all subscripts in `Z/nZ` and binary configuration `x=(x_i)`. Let `Maj` denote strict global majority. Define synchronous, translation-equivariant but **size-dependent and long-range** Boolean maps:

\[
A_i(x)=\operatorname{Maj}(x_i,x_{i+1},\ldots,x_{i+n-3}),
\qquad
B_i(x)=\operatorname{Maj}(x_i,x_{i+1},x_{i+m+1}).
\]

The first rule uses **n−2 inputs** per site. These are not fixed-radius cellular automaton rules as n grows. In particular, the claim concerns **three synchronous layers**, NOT constant-time local communication with bounded-degree local neighborhoods, and is not a contradiction of classic cellular-automata impossibility results.

## Theorem (to be independently audited)

For all odd `n>=5` and every `x in {0,1}^n`, 
\[
\boxed{A(B(A(x)))= \operatorname{Maj}(x)\,\mathbf{1}.}
\]

### Lemma: sparse-boundary contraction

For binary `w` with `1<=|w|<=m`, let `r` be the number of cyclic runs of 1's in **ordinary index order** `0,1,...,n−1`, let `h=m+1`, and define `B` as above. Then
\[
\boxed{|B(w)|\le |w|+r-2.}
\]

**Proof (new direct combinatorial argument):** Write `s=|w|`. Among the n adjacent pairs `(w_i,w_{i+1})`, the `11` pairs number `s-r`, and the change-boundary pairs number `2r`. At a `11` pair, `B_i(w)=1`, at `00` it is 0, and on a change boundary `B_i(w)=w_{i+h}`. Consequently
\[
|B(w)|=s+r-q,
\quad q=\#\{i:w_i\ne w_{i+1},\ w_{i+h}=0\}.
\]

Shift indices to `j=i+h`, and note `i=j-h ≡ j+m (mod n)` and `i+1 ≡ j-m (mod n)` because `n=2m+1`. Therefore
\[
q=\sum_{j:w_j=0}|w_{j+m}-w_{j-m}|.
\]

Because `gcd(m,2m+1)=1`, the reindexing `v_t=w_{tm mod n}` gives a full cyclic permutation of all sites, so
\[
q=\sum_{t:v_t=0}|v_{t+1}-v_{t-1}|.
\]

For any cyclic nonconstant binary word, this last sum is **exactly twice** the number `L_2(v)` of cyclic runs of 0 with length at least 2. A singleton zero has both neighboring bits 1 and contributes 0. A zero-run of length at least 2 has exactly two zero endpoints adjacent (on one side) to a 1, each contributing 1, while its interior contributes 0. Thus
\[
\boxed{|B(w)|=s+r-2L_2(v)}.
\]

Since `w` has at least `m+1` zeros, so does `v`. An odd cycle of length `2m+1` with `m+1` zeros cannot have all zeros isolated (maximum independent set of this cycle has size `m`). Therefore `L_2(v)>=1`. Hence `q>=2`, proving the lemma. QED.

### Proof of theorem

The maps `A` and `B` commute with bit complementation; hence it is sufficient to prove the majority-1 case.

Let `s=|x|>=m+1`. The `A` rule sees `n-2=2m-1` bits and outputs 1 iff at least `m` of them are ones.

**Case 1: `s>=m+2`.** Even after omitting two arbitrary bits, each `A_i(x)` sees at least `s-2>=m` ones; thus `A(x)=1^n`, and both subsequent stages preserve `1^n`.

**Case 2: `s=m+1`.** Let `R` be the cyclic number of 1-runs in `x`. As `x` is not constant, `R>=1`. Define `w_i=x_{i-2} x_{i-1}` using Boolean multiplication. The first stage is precisely
\[
A(x)=1^n-w.
\]
Indeed the retained ones number `m+1-x_{i-2}-x_{i-1}` falls below `m` exactly when both excluded bits are 1. Each run of 1s in `x` of length `ell` yields a run of 1s in `w` of length `ell-1` if `ell>=2`, and no 1s otherwise. Hence
\[
|w|=(m+1)-R,\qquad r(w)\le R.
\]
If `w=0`, then `A(x)=1^n` and we are done. Otherwise `1<=|w|<=m`, and the lemma implies
\[
|B(w)|\le |w|+r(w)-2\le m-1.
\]
As `B` respects bit complementation, `B(A(x))=1^n-B(w)`. If a word `z` has at most `m-1` ones, any `A_i(z)` sees at most `m-1` ones, below threshold `m`, so `A(z)=0^n`. By complement symmetry, `A(1^n-z)=1^n`. Apply with `z=B(w)` to get `A(B(A(x)))=1^n`.

This proves the strict majority-1 case; complement symmetry gives the strict majority-0 case. QED (subject to independent proof review).

## Computational audit

- `audit_no30.py` reproduces the theorem and exact lemma equality over **all** binary configurations for odd `n=5,7,...,17`.
- For the six-digit tally, full enumeration is `32+128+512+2048+8192+32768+131072=174752` states.
- The script checks that `A`, `B`, `AA`, `AB`, `BA`, and `BB` do not all classify the 5-cycle exactly. This proves a 2-stage lower bound **only within the alphabet of those two fixed rules, uniformly over all odd n**, not among arbitrary rule families.
- All evidence is auditable using the Python 3 standard library (tested in the execution environment; intended to be compatible with Python 3.12 on Windows 10).
- These finite tests are checks, NOT a substitute for an independently examined all-n proof.

## Relevant prior art and novelty boundary

1. H. Fuks (1997), *Solution of the Density Classification Problem with Two Cellular Automata Rules*, **Physical Review E** 55, R2081, DOI 10.1103/PhysRevE.55.R2081. Perfect classification with sequential ECA rules 184 and 232; number of updates grows with n.
2. H. F. Chau et al. (1998), *Classifying rational densities using two one-dimensional cellular automata*, **Physical Review E** 57, 1367, DOI 10.1103/PhysRevE.57.1367. More general density thresholds with successive cellular automata.
3. A. Kulikov and V. Podolskii (2016), *Computing Majority by Constant Depth Majority Circuits with Low Fan-in Gates*, ECCC TR16-158. Distinguishes bounded fan-in majority circuit depth from unbounded near-global fan-in constructions.

This package **does not establish publication priority or novelty**. The novelty search must continue across voting circuits/majority-of-majorities identities, variable-radius and nonuniform cellular automata, cyclic Boolean networks, and equivalent relabelings of 1D ring schemes. No claim of best possible layer count over unrestricted constructions is justified. Do not describe this as a fixed-radius three-step local density-classification algorithm.

## Next audit gates

- Independently verify each congruence and the exact identity `q=2 L_2(v)` by pencil proof and a separate implementation.
- Confirm the `n=5` two-layer counterexamples and explicitly delimit what that lower bound proves.
- Complete primary-source novelty search, including equivalent formulations and majority-circuit literature.
- Only then refine the manuscript, confirm evidence and SHA256, and make a publication decision.
