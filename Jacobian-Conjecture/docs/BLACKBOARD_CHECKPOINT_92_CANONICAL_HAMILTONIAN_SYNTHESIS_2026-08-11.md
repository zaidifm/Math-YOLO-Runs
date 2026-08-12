# Blackboard checkpoint 92 — canonical class, projector orbit, and Hamiltonian synthesis

**Date:** 2026-08-11  
**Status:** matrix/Poisson/form identities COMPUTED; geometric synthesis DERIVED. No external novelty claim.

Several independently discovered structures have collapsed onto one object.

## Rank-one spectral projector

The boundary coordinates form

\[
P=\begin{pmatrix}b&c\\-W&1-b\end{pmatrix},
\]

and `cW=b(b-1)` is exactly `P^2=P`, `tr P=1`. With the spectral root-derivative frame `G`,

\[
P=G^{-1}E_{11}G.
\]

Hence the boundary surface is the rank-one projector variety, equivalently the semisimple `SL_2/T` coadjoint orbit. Setting `H=2P-I` gives `H^2=I`; the associated graded removes the constant Casimir level and yields `H^2=0`, the `sl_2` nilpotent cone / second Veronese `A_1` surface.

## Darboux/Hamiltonian form

The Kirillov–Kostant brackets may be written

\[
\{W,q\}=2W,\quad\{W,c\}=q,\quad\{q,c\}=2c.
\]

On the big cell `q=1+2aW`, `c=a+a^2W`, this is simply

\[
\boxed{\{W,a\}=1.}
\]

Thus `(W,a)` are Darboux coordinates. The previously isolated derivations `e,f,h` are the Hamiltonian fields of `W,-c,-q`.

The missing color `D=(W,b)` is a Lagrangian curve. The fixed-chart deformation theorem

\[
\text{polynomializable deformations modulo translations}=I_D
\]

therefore says: **allowed regular deformations are precisely Hamiltonians vanishing on the Lagrangian color, hence Hamiltonian flows tangent to that boundary.**

## Generating-function identity

For arbitrary potential `h(a,W)`,

\[
U=X+h_a,\qquad \tau S=aU-h
\]

implies the exact one-form identity

\[
\boxed{\tau dS-a\,dU=X\,da-h_W\,dW.}
\]

Consequently

\[
\boxed{\tau\,dS\wedge dU\wedge dW=-X\,dX\wedge da\wedge dW,}
\]

so the hidden Jacobian is `-X/tau` independently of `h`. The source affine modification supplies the reciprocal character `x=X^{-1}`. Constant Jacobian is therefore the product of a generating-function volume identity and reciprocal boundary-character cancellation.

## Canonical/ramification class of the spectral cover

A degree-`m` spectral hypersurface in `P^1 x Y` has, by adjunction,

\[
K_{Z_m}=O(m-2).
\]

Because the affine target has trivial canonical bundle, this is also the finite-cover ramification/different class. It is the same `m-2` appearing in the root-derivative transition and the Picard group `Z/(m-2)` of the universal simple-root incidence.

Higher nonlinear Keller slices force an excess infinity ramification component of multiplicity `m-3`. Spectral normalization removes exactly that excess:

\[
(m-2)-(m-3)=1.
\]

Thus every higher family reduces its residual root-derivative/canonical class to the primitive cubic `O(1)` class. This explains why all degrees inherit the same normalized `SL_2/T` projector frame.

## Dimensional implication

The hidden model is one torus coordinate times a nontrivial symplectic orbit. Such an orbit has positive even dimension; the smallest is two, realized by `sl_2`. Hence the smallest dimension of this coadjoint-orbit/generating-function cancellation mechanism is `1+2=3`. This is a mechanism-level obstruction to a two-dimensional analogue, not a proof of JC2.

Certificates retained in the Library include the projector conjugation, Poisson/Darboux, generating one-form, derivative elementary-transform, and canonical-class arithmetic checks.
