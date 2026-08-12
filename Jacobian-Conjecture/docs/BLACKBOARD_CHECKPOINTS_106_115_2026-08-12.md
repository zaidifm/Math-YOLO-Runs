# Jacobian Blackboard Checkpoints 106–115

**Date:** 2026-08-12  
**Status:** durable bridge checkpoint. The canonical full continuation journal is preserved in the project Library; this file records the theorem-level state that had not yet been mirrored to GitHub when the previous tool window ended.

## 106 — boundary class group of the finite normalization

For the Zariski-Main factorization of a Keller map

\[
X\simeq \mathbb A^n\hookrightarrow \bar X\to \mathbb A^n,
\]

write the divisorial boundary as

\[
\bar X\setminus X=D_1\cup\cdots\cup D_r.
\]

Because `O(X)^*=O(\bar X)^*=C^*` and `Cl(X)=0`, the divisor localization sequence gives

\[
\boxed{\operatorname{Cl}(\bar X)\cong\bigoplus_{i=1}^r\mathbb Z[D_i].}
\]

Thus the boundary primes form a free basis of the class group. In particular the finite normalization of a nontrivial Keller map is not factorial and its boundary/ramification class cannot be torsion.

## 107 — complete-intersection root-Jacobian character

For a transverse complete intersection of `r-1` homogeneous equations of degrees `d_i` in `P^{r-1}`, the projective-root Jacobian scalar transforms under root scaling by

\[
\boxed{\kappa=\sum_i d_i-r.}
\]

Weight one, `kappa=1`, is the analogue of the binary-cubic derivative-normalization miracle. If every equation is genuinely nonlinear, only two cases survive:

- one cubic in `P^1`;
- two quadrics in `P^2`.

No genuinely nonlinear higher-rank weight-one complete intersection exists.

## 108 — the two-conic sibling collapses

For a quadratic plane map `(P,Q)` with constant Jacobian, the homogeneous quadratic parts satisfy

\[
ae-bd=af-cd=bf-ce=0,
\]

so they are proportional. A target linear change removes one quadratic part; after an affine source normalization one component is linear and constant Jacobian forces a triangular automorphism. Hence the only higher-rank primitive weight-one sibling does not produce a counterexample.

## 111 — discriminant pullback is the cofactor discriminant

Write the normalized cubic factorization

\[
\Phi=(xA-vB)(LA^2+KAB+MB^2).
\]

The normalization gives `Res(ell,Q)=Q(r)=-1`, hence

\[
\boxed{\Delta_{\Phi}\circ F=K^2-4LM.}
\]

The source preimage of the target discriminant is exactly the collision locus of the two *unselected* roots. The selected root never enters the branch because its resultant with the cofactor is a unit. The hypersurface `K^2-4LM=0` is smooth in source `A^3`; the triple-root target locus has no source point.

## 112 — JC2 finite normalization is finite free

For a hypothetical plane Keller counterexample, the finite normalization algebra `B` over `R=C[u,v]` is Cohen–Macaulay of depth two. Auslander–Buchsbaum makes it locally free and Quillen–Suslin makes it globally free:

\[
\boxed{B\cong R^{\oplus d}.}
\]

Trace splits `B=R\oplus E`, with `E` free of rank `d-1`. Thus JC2 can be reformulated as the existence of a very constrained finite free algebra with all ramification pushed into a free boundary class lattice while its Keller open is `A^2`.

## 113 — degree-three branch curves have irreducible pullback

For generic degree three, codimension-one inertia is a transposition and leaves exactly one unramified sheet. Therefore for every irreducible branch polynomial `p(u,v)`,

\[
\boxed{p(F_1,F_2)=c\,q(x,y)}
\]

with `q` irreducible, and `V(q)` maps birationally to the branch curve `V(p)`.

## 114 — plane Keller maps concentrate the projective root-Jacobian at infinity

Let `p=deg P`, `q=deg Q`, and homogenize the fiber equations in `P^2`. At a projective common root,

\[
\nabla F_1\times\nabla F_2=\lambda(A,B,C).
\]

The constant affine Jacobian gives

\[
\boxed{\lambda=J_0 C^{p+q-3}.}
\]

Thus every plane Keller map pushes its entire projective root-Jacobian divisor to infinity. Removing the forced excess `C^{p+q-4}` leaves the same residual weight-one character `J_0 C` seen in the primitive cubic. A higher-degree JC2 counterexample would therefore need a nontrivial elementary transformation at infinity that strips this excess while resolving the source back to `A^2`.

## 115 — nontrivial Keller monodromy is nonabelian and non-Galois

Every codimension-one inertia generator of a Keller normalization must fix at least one sheet, because the affine Keller image omits no divisor. A faithful transitive abelian permutation group is regular, so every nonidentity element is fixed-point-free. Hence

\[
\boxed{G_{mon}\text{ is nonabelian for every nontrivial Keller map}.}
\]

Likewise the generic field extension can never itself be nontrivially Galois: a connected Galois cover acts regularly on its sheets, contradicting the fixed-sheet inertia condition.

This gives another structural reason generic degree three is the first possible degree: `S_3` is the smallest transitive nonabelian group and a transposition is the smallest branch cycle that can be nontrivial while leaving one sheet alive.

## Integrity note

The canonical Library continuation journal was corrected at CP115 to use the actual verifier SHA-256:

`8b94f5cf10e462c3b3c08700ba9cec191e3497a80e130b1192fbeb87398825e5`

No external novelty or priority claim is made for these current-run deductions.