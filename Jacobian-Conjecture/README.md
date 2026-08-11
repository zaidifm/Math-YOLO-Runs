# Jacobian Conjecture

## Current focus

The classical Jacobian Conjecture was refuted in dimension three in July 2026. This directory audits and extends private BLIND-session work performed immediately after the announced counterexample, with emphasis on structures that are not yet clearly matched by the public literature.

The current blackboard frontier reorganizes the earlier reciprocal-chart observations around an exact source matrix

\[
G=\begin{pmatrix}x&1+2xy\\-1+3xy+x^2z&y+6xy^2+xz+2x^2yz\end{pmatrix}\in SL_2,
\]

whose determinant identity is

\[
xK-(1+2xy)L=1.
\]

The earlier boundary generators are torus-invariant matrix products. Consequently the boundary/intersection algebra

\[
R=k[W,b,c]/(cW-b(b-1))
\]

is naturally the affine torus quotient of `SL_2`; after `q=2b-1` it is the discriminant-one quadric `q^2-4cW=1`. The old `b=1+aW` shift is the determinant-one exchange relation on the quotient big cell.

This structure now connects:

1. the BLIND 2 intersection theorem `k[a,W] ∩ k[x,y,z]=R`;
2. a scheme-theoretic boundary pullback `(W,b)k[x,y,z]=(x)`;
3. a full `sl_2` action extending the previously isolated hidden LND;
4. a second-Veronese / `A_1` associated-graded degeneration explaining the parity law in the degree filtration;
5. a complete **fixed-chart** canonical-potential classification modulo target translations by the boundary ideal `I_D=(W,b)`;
6. an all-hidden-degree sharp deformation spectrum whose degree-five case is the old degree-17 direction `a^2(1+aW)^3`;
7. the BLIND 4 two-jet criterion as a one-variable slice of the same boundary-ideal condition.

None of this is a global minimality theorem for all Keller maps.

## Start here

- [`STATUS.md`](STATUS.md) — current mathematical frontier, exact checks, and unresolved obligations.
- [`PROVENANCE.md`](PROVENANCE.md) — what came from which BLIND session versus the later 2026-08-11 synthesis.
- [`docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`](docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md) — current blackboard derivation and fixed-chart classification.
- [`scripts/jacobian_blackboard_quadric_verify.py`](scripts/jacobian_blackboard_quadric_verify.py) — exact symbolic checks for the `SL_2`, quadric, `sl_2`, leading-degree, and minimal-direction identities.
- [`verification/Jacobian_Canonical_Kernel_Exact_Validation_2026-08-11.txt`](verification/Jacobian_Canonical_Kernel_Exact_Validation_2026-08-11.txt) — exact coefficient-matrix nullities versus the classification for every bound `D=3,...,20`.
- [`docs/Jacobian_Blind_Math_Forensics_2026-08-11.md`](docs/Jacobian_Blind_Math_Forensics_2026-08-11.md) — earlier reconstruction that led into the blackboard pass.
- [`sources/PUBLIC_SOURCES.md`](sources/PUBLIC_SOURCES.md) — public literature map and current overlap assessment.
- [`sources/ACQUISITION_MANIFEST_2026-08-11.md`](sources/ACQUISITION_MANIFEST_2026-08-11.md) — exact source-bundle identities, inventories, hashes, and missing-companion status.
- [`incoming/PUBLICATION_QUEUE.md`](incoming/PUBLICATION_QUEUE.md) — first-party historical evidence publication staging.

## Evidence boundary

The underlying private archive contains the raw BLIND 2 and verification conversations, plus BLIND 1–5 findings packages and retrospective histories. Most BLIND supplementary histories are not exact raw platform transcripts. The owner has confirmed that this is the complete available BLIND provenance corpus; additional raw BLIND 1/3/4/5 conversations are not an open retrieval task. Raw private exports are intentionally **not** mirrored into this public repository.

The `SL_2/T`, quadric, full canonical classification, sharp spectrum, and Hilbert-series synthesis are **2026-08-11 current-run results** and must not be retroactively attributed to the historical BLIND sessions.

## Public-source state

The original arXiv source bundles for `2607.20210` and `2608.02863`, plus the exact Zenodo record `10.5281/zenodo.21514514`, were acquired and hash-pinned on 2026-08-11. The Kistner–Shaska paper cites `balanced_minimal_models_companion.pdf`, but that file is absent from the deposited arXiv source bundle and was **NOT PUBLICLY LOCATED** in bounded acquisition checks.

That unavailable companion is a literature-coverage limitation, not an unfinished courier task and not evidence that the companion lacks overlapping mathematics.

## Epistemic status

The determinant identity, matrix factorization, quadric equation, `sl_2` commutators, leading forms, and finite coefficient-matrix comparisons are **COMPUTED** exactly.

The strengthened intersection argument, complete fixed-chart canonical-potential classification, all-`m` sharp spectrum, and Hilbert-series formula are **DERIVED** and have survived internal adversarial checking, but still require independent specialist/formal verification.

No novelty or priority claim is made. Mathematical structure has become much clearer; priority has not magically become easier merely because the algebra stopped being coy.
