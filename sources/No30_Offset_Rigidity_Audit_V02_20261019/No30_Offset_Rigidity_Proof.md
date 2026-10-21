# No.30 — Offset rigidity of a three-round cyclic majority scheme (supplement)

Author: Ryutaro Yonezu  
Date: 2026-10-19  
Status: mathematical proof **candidate**; computationally checked by a separate verifier; external independent review of this *new* proposition PENDING. Scholarly novelty INCONCLUSIVE; publication HOLD.

## Definitions

Let n=2m+1 >= 5. All indices are taken modulo n and all bits are in {0,1}. Let Maj denote strict majority on an odd number of bits.

- `A_i(x) = Maj(x_i,...,x_{i+n-3})`, a cyclic window of n-2 consecutive bits. The excluded inputs are x_{i-2},x_{i-1}.
- For 2 <= d <= n-1, `B_{d,i}(x)=Maj(x_i,x_{i+1},x_{i+d})`.
- The output is a complete classification if `A(B_d(A(x))) = Maj(x)*1^n` for every binary input x.

## Proposition (offset rigidity)

For any odd n=2m+1>=5 and 2<=d<=n-1,

    A o B_d o A is a complete majority classifier  <=>  d=m+1.

In other words, the middle gate's offset is unique *within the one-parameter family B_d*, with A fixed as above. This is **not** a universal three-layer or two-layer lower bound over other update rules.

### Sufficiency

For d=m+1, this is the general theorem proven in `No30_Theorem_and_Proof_DRAFT.md` of the original V01 package. That theorem was separately audited by Claude according to the user's supplied report (no independent re-execution of Claude's code is claimed here).

### Necessity: a single explicit witness family

Take x* with ones precisely at positions 0,1,...,m (thus Maj(x*)=1). The first application of A gives `A(x*)=1-w`, where `w_i=x*_{i-2} x*_{i-1}`. Here w consists of m consecutive ones at positions 2,...,m+1. By translation-equivariance, rotate w to ones at positions 0,...,m-1.

Let z=B_d(w). There are m-1 adjacent `11` pairs (w_i,w_{i+1}), and two change-boundary pairs, located at i=m-1 (`10`) and i=n-1 (`01`). On a `11` pair, the 3-input majority is 1; on a `00` pair it is 0; at change boundaries, it equals the third input. Consequently

    |z| = m-1 + w_{m-1+d (mod n)} + w_{d-1}.

For the cyclic interval w=1 on [0,m-1], the last two terms are:

- 2 <= d <= m: (0,1)
- d = m+1: (0,0)
- m+2 <= d <= 2m: (1,0)

Thus `|z|=m` for every d!=m+1, and `|z|=m-1` for d=m+1.

If a binary word z has exactly m ones on a cycle of length 2m+1, then it has m+1 zeros. Two of those zeros must be adjacent (an odd cycle of length 2m+1 has maximum independent set size m). Choose i so that excluded inputs z_{i-2},z_{i-1} are both zero. The retained n-2 inputs then contain all m ones, so `A_i(z)=1`.

Since A and B_d commute with bit complementation,

    A(B_d(A(x*))) = A(1-B_d(w)) = 1 - A(z).

For every d!=m+1 we have |z|=m, whence A(z) has at least one 1, so the final output has at least one 0 even though Maj(x*)=1. Therefore every non-central d fails. QED.

## Strength and limitations

The new conclusion is a uniqueness result **only for the specified one-parameter family of middle rules** and the **specified fixed outer rule**. It does not overcome prior depth-two majority-circuit constructions, establish a fan-in/communication optimum, or imply a bounded-radius constant-time cellular-automaton algorithm. The main practical restriction remains the n-2 fan-in of A at every cell.

## Primary literature located for priority audit (not an assertion of novelty)

1. Amano and Yoshida (2018), "Depth Two (n-2)-Majority Circuits for n-Majority", DOI 10.1587/transfun.E101.A.1543 — explicit depth-two near-global-fan-in majority circuits for odd n>=7; unrestricted circuit model, not established as equivalent to our uniform cyclic scheme.
2. Kombarov (2018), "A circuit of depth two with limited input branching for voting function", DOI 10.3103/S0027132218050054 — another depth-two result with n-2 majority gates.
3. Kulikov and Podolskii (2017), "Computing Majority by Constant Depth Majority Circuits with Low Fan-in Gates", DOI 10.4230/LIPIcs.STACS.2017.49 — majority-gate circuit complexity.
4. Amano (2018), "Depth Two Majority Circuits for Majority and List Expanders", DOI 10.4230/LIPIcs.MFCS.2018.81 — strengthened bounds, circuit families and expanders.
5. Engels, Garg, Makino and Rao (2020), "On Expressing Majority as a Majority of Majorities", DOI 10.1137/18M1223599 — two-layer majority-of-majorities lower bounds.
6. Fukś (1997), "Solution of the density classification problem with two cellular automata rules", DOI 10.1103/PhysRevE.55.R2081 — local density classification by sequential CA updates, requiring size-dependent number of rounds.

Full equivalence/non-equivalence to all known uniform cyclic schemes is NOT established. PDF of the Amano-Yoshida paper may be access-restricted. **Overall novelty remains INCONCLUSIVE and publication HOLD**.

## Audit gates

- Independent reviewer should verify the necessity witness algebra line by line.
- Look for existing equivalently formulated one-parameter rigidity results under rotation, complement, or circuit transformations.
- If pursuing publication, explicitly disclose that the generalized theorem is only about the family (A, B_d, A), not general near-global majority circuits.
