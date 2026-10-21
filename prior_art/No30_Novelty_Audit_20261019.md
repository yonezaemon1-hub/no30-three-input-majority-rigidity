# No.30 — Prior-Art / Novelty Audit (2026-10-19)

**Status:** theorem correctness: independent V0.5 audit reportedly PASS (Claude report supplied by researcher); novelty: **INCONCLUSIVE**; publication: **HOLD** pending fuller prior-equivalence audit. This document does not independently re-run the proof or establish novelty.

## Precisely scoped claim under assessment

For odd n=2m+1>=25, let A be the synchronous per-site majority over n-2 consecutive positions and B_{a,b} be synchronous 3-input majority with inputs at offsets {0,a,b} modulo n. The supplied V0.5 independent-audit report states the classification

    A o B_{a,b} o A = constant global-majority map
       iff the cyclic gaps of {0,a,b} are {1,m,m}.

For n=21 and n=23, the additional success class {3,m-1,m-1} is reported. The n>=25 threshold is sharp within that model, according to the submitted independent audit.

Only this *uniform cyclic three-stage placement classification* is under consideration for potential novelty. It is not a claim that depth-three majority gates are generally optimal, nor that perfect density classification is impossible otherwise.

## Primary literature and overlap assessment

1. **Amano & Yoshida (2018)**, *Depth Two (n-2)-Majority Circuits for n-Majority*, IEICE Transactions. DOI: https://doi.org/10.1587/transfun.E101.A.1543
   - Abstract confirms explicit depth-2 majority-of-majorities construction for odd n>=7.
   - Hence 'depth three majority computes global majority' **is not new in an unrestricted circuit model**.
   - This paper's publisher full text was access-restricted during this audit: comparison of exact gate wiring remains incomplete.

2. **Amano & Yoshida (2018)**, Japanese RIMS proceedings *多数決関数を計算する2層の多数決回路について*, 2088:1–8. Link: https://cir.nii.ac.jp/crid/1050003824810693248 ; handle 2433/251591.
   - Abstract reports three essentially different n-2-input depth-2 constructions. Main text not yet checked against V0.5.

3. **Kulikov & Podolskii (2017)**, *Computing Majority by Constant Depth Majority Circuits with Low Fan-in Gates*, STACS. DOI https://doi.org/10.4230/LIPIcs.STACS.2017.49
   - General circuit-complexity bounds and constructions; no exact equivalence to this per-site cyclic A-B-A wiring identified in the accessible paper/abstract material.

4. **Lecomte, Ramakrishnan & Tan (2022)**, *The Composition Complexity of Majority*, CCC. DOI https://doi.org/10.4230/LIPIcs.CCC.2022.19
   - Composition lower bounds when inner functions query k << n bits, distinct model because A uses n-2 inputs.

5. **Fukś (1997)**, *Solution of the density classification problem with two cellular automata rules*, Phys Rev E. DOI https://doi.org/10.1103/PhysRevE.55.R2081
   - Exact density classification from a scheduled sequence of elementary CA 184 and 232. The rules and stage-count regime differ.

6. **Moran (1994)**, *The r-majority vote action on 0–1 sequences*, Discrete Mathematics. DOI https://doi.org/10.1016/0012-365X(94)90236-4
   - Cyclic majority dynamics and run-size theory; an especially relevant structural antecedent to A as a radius-(m-1) majority operation. The full paper was not acquired. Possible indirect consequences remain unchecked.

7. **Yli-Harja, Neuvo & Astola (1991)**, *Analysis of the properties of median and weighted median filters using threshold logic and stack filter representation*, IEEE TSP. DOI https://doi.org/10.1109/78.80823
   - Cascades of median/weighted median operators expressed as stack/weighted median filters; potential equivalent language but no match to the exact offset uniqueness theorem identified. Full text not fully checked.

8. **Abilhoa & de Oliveira (2020)**, *Density Classification Based on Agents Under Majority Rule: Connectivity Influence on Performance*, DCAI / Springer. DOI https://doi.org/10.1007/978-3-030-23887-2_19
   - Compared full conference-paper text (readable online): its circulant connections are symmetric +/- jumps, and it repeatedly applies the same majority update, assessing empirical performance over sizes 7–17 and additional sampling at 55. This is not the same 3-stage A-B-A model or exact classification theorem.

9. **Perrot & Rolland (2026)**, *Majority Boolean networks classifying density: structural characterization and complexity*, arXiv:2602.13511, https://arxiv.org/pdf/2602.13511
   - Primary full PDF reviewed: characterizes forbidden patterns for a **single fixed graph** with synchronous majority iterations. No theorem explicitly equating to the cyclic heterogeneous A-B-A placement classification was identified. This does not rule out an indirect derivation.

10. **Balbi, Perrot, Rolland & Ruivo (2026)**, *Non-trivial automata networks do exist that solve the global majority problem with the local majority rule*, arXiv:2603.19472, https://arxiv.org/pdf/2603.19472
   - Partial visibility networks with fixed local majority and evolving iterates; model distinct from A-B-A with nearly global A. Full primary PDF accessible.

## Search strategies used

- `majority of majorities`, `(n-2)-majority circuits`, `constant depth majority circuits`
- `density classification cellular automata two rules`, `time varying neighborhood`
- `cyclic majority vote run length`, `circulant graph majority classification`
- `median filter cascades`, `stack filters threshold composition`
- `majority Boolean networks density classification structural characterization`
- direct and translated variants of rigidity/uniqueness of offsets in majority gates

## Verdict / claim boundary

**Direct exact prior theorem found:** NO, within inspected accessible sources.
**Established novelty:** NO — remains INCONCLUSIVE.
**Strongest potentially residual theorem:** uniqueness of the cyclic 3-input intermediate neighborhood for all odd n>=25, under fixed all-but-two-input outer majority updates and a three-round, uniform, synchronous A-B-A architecture.

Recommended abstract wording until audit closure:

> We give a complete characterization, for odd ring sizes n>=25, of the three-input cyclic neighborhoods that yield exact global majority consensus under a specified three-stage majority-update schedule. To the best of our knowledge among the sources consulted, this precise characterization has not been identified previously; priority is not asserted.

Next checks before upgrading novelty status:
1. Obtain and compare full texts of Amano–Yoshida (both 2018 versions) at gate wiring level.
2. Compare complete Moran (1994) median-run characterization and classical cascade results for an immediate corollary.
3. Use time-expanded networks to test whether Perrot–Rolland (2026) three forbidden patterns directly imply the cyclic placement rigidity. A proof of implication would substantially narrow novelty.
4. Independently repeat relevant equivalence assessment, not only text/keyword matches.

No journal peer-review or originality certification has been performed. No research files or proofs were modified by this novelty memo.
