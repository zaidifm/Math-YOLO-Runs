# Jacobian Conjecture

## Current focus

The classical Jacobian Conjecture was refuted in dimension three in July 2026. This directory audits and extends the retained BLIND-session work around the counterexample, with strict separation between historical provenance, current-run mathematics, exact computation, and literature priority.

The 2026-08-11 blackboard frontier is organized by the exact source identity

\[
xK-(1+2xy)L=1,
\]

which gives an `SL_2` matrix

\[
G=\begin{pmatrix}x&1+2xy\\L&K\end{pmatrix}.
\]

The BLIND 2 boundary generators are its torus-invariant matrix products, so

\[
R=k[W,b,c]/(cW-b(b-1))
\]

is the affine torus quotient of this `SL_2` model. After `q=2b-1`, it is the discriminant-one quadric

\[
q^2-4cW=1.
\]

This structure now unifies the intersection ring, the hidden LND and full `sl_2` action, the degree filtration, the BLIND 4 jet criterion, the degree-17 direction, and the BLIND 4 binary-cubic frame.

The fixed-chart canonical-potential deformations are classified, modulo target translations, by the missing-boundary ideal

\[
I_D=(W,b)\subset R.
\]

The unique minimal direction at each hidden recovery degree `m` has output-degree threshold

\[
D_m=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}
\]

The current blackboard work also gives the complete nonzero-scalar surjectivity phase diagram for these minimal directions:

\[
\begin{array}{c|c}
m&\lambda\ne0\\
\hline
3&\text{never surjective}\\
4&\text{never surjective}\\
5&\text{surjective except at two algebraic coefficients}\\
\ge6&\text{always surjective.}
\end{array}
\]

At degree five the exceptional equation is

\[
27\lambda^2+99\lambda+5=0.
\]

For every `m>=6` and every nonzero scalar, the minimal-direction map is a surjective, noninjective determinant-one polynomial map of generic fiber degree `m` and degree profile `(D_m,D_m-1,4)`.

None of this is a global minimality/classification theorem for all Keller maps.

## Start here

- [`STATUS.md`](STATUS.md) — current frontier and epistemic status.
- [`PROVENANCE.md`](PROVENANCE.md) — historical BLIND provenance and earlier 2026-08-11 synthesis.
- [`docs/BLACKBOARD_PROVENANCE_ADDENDUM_2026-08-11.md`](docs/BLACKBOARD_PROVENANCE_ADDENDUM_2026-08-11.md) — provenance boundary for the late blackboard results.
- [`docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`](docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md) — `SL_2/T`, intersection, associated graded, canonical classification, and degree spectrum.
- [`docs/SL2_FRAME_BRIDGE_2026-08-11.md`](docs/SL2_FRAME_BRIDGE_2026-08-11.md) — exact bridge to the BLIND 4 binary-cubic root frame.
- [`docs/QUINTIC_LAMBDA_SURJECTIVITY_2026-08-11.md`](docs/QUINTIC_LAMBDA_SURJECTIVITY_2026-08-11.md) — complete scalar degree-five surjectivity classification.
- [`docs/MINIMAL_DIRECTION_SURJECTIVITY_2026-08-11.md`](docs/MINIMAL_DIRECTION_SURJECTIVITY_2026-08-11.md) — surjectivity theorem for all `m>=6`.
- [`docs/MINIMAL_DIRECTION_SURJECTIVITY_SECOND_PROOF_2026-08-11.md`](docs/MINIMAL_DIRECTION_SURJECTIVITY_SECOND_PROOF_2026-08-11.md) — Newton/Vandermonde second proof and comparison with the BLIND 1 family.
- [`docs/MINIMAL_SCALAR_SURJECTIVITY_PHASE_2026-08-11.md`](docs/MINIMAL_SCALAR_SURJECTIVITY_PHASE_2026-08-11.md) — complete `m=3,4,5,>=6` phase diagram.
- [`verification/`](verification/) and [`scripts/`](scripts/) — exact certificates and executable checks.
- [`sources/PUBLIC_SOURCES.md`](sources/PUBLIC_SOURCES.md) — public literature map and current overlap caveats.

## Evidence boundary

The retained corpus is the complete available BLIND provenance corpus. Additional raw BLIND 1/3/4/5 conversations are not an open acquisition task. Raw private exports are intentionally not mirrored wholesale into this public repository.

The `SL_2/T`, full fixed-chart classification, frame bridge, scalar quintic classification, degree-efficient all-`m` surjectivity theorem, and scalar phase diagram are **2026-08-11 current-run syntheses** and must not be back-attributed to the historical BLIND sessions.

BLIND 1 had already produced a different surjective family for every generic degree `m>=6`, with degree profile `(5m,5m-1,4)`. The current result sharpens the retained project record by selecting fixed-chart minimal directions, lowering those degrees to `(D_m,D_m-1,4)`, and resolving BLIND 1's explicitly open generic-degree-five surjectivity question affirmatively.

## Public-source state

The relevant original arXiv source bundles and Zenodo record are hash-pinned in the project Library/source manifests. The Kistner-Shaska paper cites `balanced_minimal_models_companion.pdf`, but that file is absent from the deposited arXiv source bundle and was **NOT PUBLICLY LOCATED** in bounded acquisition checks.

That unavailable companion remains a literature-coverage limitation, not evidence of non-overlap.

## Epistemic status

Exact determinant identities, matrix factorizations, low-degree squareful classifications, elimination certificates, witness targets, and bounded coefficient-matrix checks are **COMPUTED**.

The general quotient/intersection/classification and all-degree surjectivity arguments are **DERIVED**, with several independent internal routes, but still require external algebraic-geometry/formal review.

No external novelty or priority claim is made. The mathematics has become much less mysterious; paperwork about who got there first remains stubbornly immune to elegance.
