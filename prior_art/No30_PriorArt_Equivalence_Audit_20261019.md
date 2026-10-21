# No.30 — Prior-Art Equivalence Audit (2026-10-19)

## Scope

Audit of the claimed classification (reported independently proof-audited in V0.5): for odd n=2m+1 >=25, let A be the synchronous, rotation-equivariant majority update whose local gate sees all but two consecutive positions, and B_{a,b}(x)_i = Maj(x_i,x_{i+a},x_{i+b}) on the n-cycle. The claimed criterion is

    A(B_{a,b}(A(x))) = Maj_n(x) * 1^n for all x
    iff the unordered circular gaps among {0,a,b} equal (1,m,m).

The V0.5 proof itself was not independently re-run in this literature audit; the user supplied Claude's reported independent mathematical audit (PASS). The novelty assessment is distinct from correctness.

## Primary literature investigated

1. **Amano, Kazuyuki; Yoshida, Masafumi (2018).** *Depth Two (n-2)-Majority Circuits for n-Majority.* IEICE Transactions on Fundamentals E101-A(9), 1543–1545. DOI: 10.1587/transfun.E101.A.1543. Official bibliographic record and abstract confirmed: https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.E101.A.1543/_p . Distinct-input status and construction discussed in the related MFCS 2018 article. **Full IEICE paper was not available during this audit (journal restricted access); no claim of line-by-line examination.**

2. **Amano, Kazuyuki (MFCS 2018).** *Depth Two Majority Circuits for Majority and List Expanders.* DOI: 10.4230/LIPIcs.MFCS.2018.81. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol117-mfcs2018/LIPIcs.MFCS.2018.81/LIPIcs.MFCS.2018.81.pdf . Theorem 1 and its proof describe for n=4k+3 a depth-two majority circuit using bottom gates on all except disjoint adjacent pairs, plus two odd/even subsets; the top majority combines 2k+3 bottom gates. No classification over triple offsets (p,q,r). The introduction specifically distinguishes the Amano–Yoshida construction as employing repeated inputs in some bottom gates, whereas Amano's MFCS construction uses distinct inputs.

3. **Kulikov, Alexander S.; Podolskii, Vladimir V.** *Computing Majority by Constant Depth Majority Circuits with Low Fan-in Gates.* ECCC TR16-158 / STACS 2017. Full text: https://eccc.weizmann.ac.il/report/2016/158/download . Section 5.1.1 gives small-n two-layer examples (some gates repeat variables) and Lemma 11; Section 5.1.2 Theorem 12 gives a depth-three O(n^(2/3)) fan-in circuit based on block decomposition. No uniform cyclic A→B→A triple-offset rigidity result identified.

4. **Engels, Christian; Garg, Mohit; Makino, Kazuhisa; Rao, Anup (2017).** *On Expressing Majority as a Majority of Majorities.* ECCC TR17-174. Full text: https://eccc.weizmann.ac.il/report/2017/174/download . Proves a lower bound of Omega(n^(4/5)) on fan-in for specified depth-two majority circuits; does not furnish the No.30 offset classification. Distinguish depth-two lower bounds from the present depth-three, high-fan-in outer gates.

5. **Lecomte, Victor; Ramakrishnan, Prasanna; Tan, Li-Yang (2022).** *The composition complexity of majority.* Full text: https://arxiv.org/pdf/2205.02374 . Analyzes local subfunction composition complexity, a different optimization problem; no direct equivalence established.

6. **Moran, Gadi (1994).** *The r-majority vote action on 0–1 sequences.* Discrete Mathematics 132, 145–174. DOI: 10.1016/0012-365X(94)90236-4. Index/abstract: https://www.sciencedirect.com/science/article/pii/0012365X94902364 . This citation **does exist** (earlier status 'unverified' should be corrected). Studies cyclic consecutive-neighborhood majority operators using run-length representations, fixed and periodic configurations. Full article unavailable during this audit, so an implicit technical corollary cannot be fully excluded.

7. **Perrot, Kévin; Rolland, Marius (2026).** *Majority Boolean networks classifying density: structural characterization and complexity.* Full text: https://arxiv.org/pdf/2602.13511 . Theorem 4.9 characterizes convergence of a single, time-homogeneous majority Boolean network by forbidden structures (leader subsets, self-sufficient subsets, self-sufficient m-cycles). Not the same class as three heterogeneous synchronous updates.

8. **Balbi, Pedro Paulo; Perrot, Kévin; Rolland, Marius; Ruivo, Eurico (2026).** *Non-trivial automata networks do exist that solve the global majority problem with the local majority rule.* Full text: https://arxiv.org/pdf/2603.19472 . Sections 3.2–3.3 construct n−2-in-degree majority networks with nonuniform neighborhoods across selected vertices, iterating a single update rule to convergence (some families in at most four steps). This is closer than a general CA survey because the same n−2 ingredient occurs, but neither a cyclically equivariant three-phase construction nor an all-triple offset rigidity classification was found.

## Claim-level finding

- **Established prior art:** Exact majority by compositions of majority gates, including depth two and depth three; n−2-input majority gates; majority dynamics on cycles and general graphs; density classification by majority networks.
- **Distinct in the inspected full texts:** The fixed, rotation-equivariant, synchronous A→B_{a,b}→A architecture; a necessary-and-sufficient classification of all unordered circular gaps for B's three inputs, sharp at n=25.
- **Do not claim:** optimal-depth majority computation, superiority in gate complexity, minimal total fan-in, defeating finite-radius CA impossibility theorems, or absolute novelty proved from absence of a match.
- **Residual uncertainty:** IEICE 2018 full text restricted; Moran 1994 full text not inspected; exhaustiveness over potentially equivalent results in filtering/morphology/circulant threshold networks is not established. As usual, lack of an exact text match does not rule out an elementary corollary.

## Decision

- Mathematical correctness: **PASS as reported in the user's supplied Claude independent V0.5 audit; not re-audited here**.
- Bibliographic correction: Amano & Yoshida 2018 **verified**; Moran 1994 **verified**.
- Direct equivalent theorem in inspected full texts: **not found**.
- Novelty: **INCONCLUSIVE (positive differentiation found, but cannot certify absence of prior equivalent work)**.
- Publication gate: **HOLD maintained per current project audit policy**.

## Suggested paper claim boundary

'We classify exactly the three-input cyclic intermediate majority neighborhoods that make a prescribed A→B→A synchronous density classifier correct for every initial state on any odd cycle of length at least 25. This is a structural rigidity result for a constrained uniform three-stage majority network, not an improvement to unrestricted majority circuit depth or fan-in.'

## Outstanding checks

- Obtain/access full Amano–Yoshida IEICE 2018 and Moran 1994 if legally available, and inspect proofs rather than just abstract/citations.
- Equivalence search in stack filters, rank-order filters, Boolean function composition and circulant threshold networks, including coordinate renaming/rotation/reflection and complementation.
- Reconcile the No.30 final paper's notation A, B, gap order, and thresholds against the proof bundle before making publication-ready claims.
