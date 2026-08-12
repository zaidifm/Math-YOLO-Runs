# Blackboard checkpoint 86 — classification of all linear cubic incidence normalizations

**Date:** 2026-08-11  
**Status:** representative algebra COMPUTED; orbit classification and additive-invariant argument DERIVED. No external priority claim.

A nonzero linear normalization `L(F)=1` on binary cubic coefficient space determines a dual binary cubic

\[
P_L(u,v)=L((uA+vB)^3).
\]

Up to `GL_2` and scalar there are three nonzero multiplicity types, represented by

\[
(3):\ c_0=1,\qquad
(2+1):\ c_1=1,\qquad
(1+1+1):\ c_1-c_2=1.
\]

For a fixed chosen projective root, the coefficient fiber is `A^2`; simplicity removes an affine line unless the derivative becomes a nonzero constant on that fiber. The generic simple fiber is therefore `A^1 x G_m`, of class `L(L-1)`.

The three incidence varieties have Grothendieck/Hodge classes

\[
\boxed{[X_{(3)}]=\mathbb L^3-\mathbb L^2,}
\]

\[
\boxed{[X_{(2+1)}]=\mathbb L^3,}
\]

\[
\boxed{[X_{(1+1+1)}]=\mathbb L^3-\mathbb L.}
\]

The reason is geometric:

- type `(3)` forbids one root point entirely and has only generic fibers;
- type `(1+1+1)` has every root point but no cap fiber;
- type `(2+1)` has one distinguished root where the derivative is automatically a nonzero constant and the whole fiber is `A^2`, capping the generic `A^1 x G_m` fibers.

Checkpoint 79 explicitly proves the `(2+1)` representative is `A^3`. The other two types have different Hodge–Deligne polynomials from affine three-space. Hence

\[
\boxed{X_L\cong A^3\iff P_L\text{ has multiplicity type }(2+1).}
\]

The `(2+1)` locus is a single `GL_2` orbit. The induced action on root space and cubic coefficient space transports the incidence projections, so after identifying the sources with affine three-space, all **linear cubic incidence Keller maps** lie in one left-right polynomial equivalence class: the primitive degree-three map.

Combined with the hyperplane–Veronese result of Checkpoint 84:

1. there is exactly one affine-space source orbit in the entire linear cubic incidence architecture;
2. every linear cubic normalization necessarily contains triple-root forms;
3. therefore the unique affine-space incidence map is necessarily nonsurjective.

This uniqueness statement no longer assumes the reciprocal coordinates, the exchange relation, the hidden `SL_2` frame, or the canonical potential ansatz. It assumes only: binary cubics, one affine linear normalization, and chosen simple root incidence.

Certificates:

- `jacobian_cubic_normalization_orbit_classification_verify.py`, SHA-256 `fbf370d6f578cc8781d04a66ff2cbca2fa39c8777f9103afbe5e21a1e2c804a8`;
- `jacobian_cubic_normalization_motivic_classes_verify.py`, SHA-256 `48d3a86745b7aa65d63c1b220d657726060248524ab03cf7596925bf7e5593e5`.
