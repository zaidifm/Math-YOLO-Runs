# Coadjoint orbit, Springer degeneration, and the `-2rho` Jacobian mechanism

**Date:** 2026-08-11  
**Status:** current-run DERIVED + COMPUTED checkpoint. Exact identities have executable verification; broader geometric conclusions await independent review. No external novelty claim.

## Semisimple orbit

For
\[
G=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in SL_2,
\qquad H=\operatorname{diag}(1,-1),
\]
set
\[
W=AC,\quad b=AD=1+BC,\quad c=BD,\quad q=2b-1.
\]
Then
\[
\boxed{G^{-1}HG=\begin{pmatrix}q&2c\\-2W&-q\end{pmatrix}.}
\]
Therefore the boundary equation
\[
q^2-4cW=1
\]
is exactly the regular semisimple adjoint orbit of `H`, with stabilizer `T`.

The color `D=(W,b)` is the upper-triangular Borel line inside this orbit.

## Adjoint-quotient degeneration

The weighted Rees family is
\[
\boxed{Q^2-4CW=T^{10}.}
\]
With
\[
\mathcal M=\begin{pmatrix}Q&2C\\-2W&-Q\end{pmatrix},
\]
this is
\[
\mathcal M^2=T^{10}I.
\]
Hence it is the base change of the quadratic adjoint quotient/Casimir
\[
\chi:\mathfrak{sl}_2\to\mathbb A^1,
\qquad \chi=Q^2-4CW,
\]
along `T -> T^10`. The generic fiber is semisimple; the special fiber is the nilpotent cone `M^2=0`.

The source-degree weights `(W,Q,C)=(4,5,6)` are scalar weight five plus the PGL2 Borel cocharacter weights `(-1,0,+1)`.

## Springer chart

On the semisimple big cell,
\[
q=1+2aW,\qquad c=a+a^2W.
\]
The associated-graded map is
\[
\boxed{(a,W)\mapsto (W,\bar b=aW,\bar c=a^2W),}
\]
which is the standard affine chart of the Springer/minimal resolution
\[
T^*\mathbf P^1\to\mathcal N.
\]
Thus the hidden `A^2_{a,W}` is simultaneously a Darboux chart on the semisimple orbit and a cotangent chart resolving the nilpotent cone.

With Poisson convention `{W,a}=1`,
\[
\{W,q\}=2W,\quad \{W,c\}=q,\quad \{q,c\}=2c,
\]
and the earlier `sl2` derivations are Hamiltonian:
\[
e=\{W,-\},\qquad f=\{-c,-\},\qquad h=\{-q,-\}.
\]
The hidden form `dW wedge da` is therefore the Kirillov--Kostant form on the orbit and the canonical cotangent form on the Springer chart.

## `-2rho` volume cancellation

The invariant volume form on the `A!=0` cell of `SL2` is
\[
\omega_G=\frac{dA\wedge dB\wedge dC}{A}
=-\frac{dX}{X}\wedge da\wedge dW.
\]
The source affine modification and target incidence map satisfy
\[
\Phi_\tau^*\omega_G=\tau x^2\,dx\wedge dy\wedge dz,
\]
\[
\Psi_h^*(dS\wedge dU\wedge dW)=\frac{X^2}{\tau}\omega_G.
\]
Since `X=1/x`, their composition preserves the standard affine volume exactly.

Under the left torus `diag(s,s^{-1})`, `X -> X/s`, so `X^2` has character `s^{-2}=e^{-2rho}`. Relative to Haar volume, the rational incidence map carries Jacobian divisor `-2{A=0}` and the two-step affine modification carries the opposite discrepancy `+2E`.

The determinant-one condition is therefore a cancellation of opposite canonical/Jacobian divisors carrying the rank-one `2rho` character.

## Consequence for the dimension threshold of this mechanism

This construction needs a two-dimensional symplectic coadjoint orbit plus one torus/reciprocal coordinate. The smallest nontrivial orbit is two-dimensional, and in rank one
\[
2+1=3=\dim SL_2.
\]
There is no one-dimensional symplectic orbit supplying a dimension-two version of this mechanism. This explains the dimension-three threshold for the present construction, not the full two-dimensional Jacobian Conjecture.

## Generalization target

The rank-one picture suggests a precise higher-rank research program: spherical/coadjoint spaces, colors, torus coordinates, affine modifications realizing `+2rho`, rational incidence maps realizing `-2rho`, meromorphic potentials selected by color regularity, and coincident-root/discriminant geometry controlling nonproperness.