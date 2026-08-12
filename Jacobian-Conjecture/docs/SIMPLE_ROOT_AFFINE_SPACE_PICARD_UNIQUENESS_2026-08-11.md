# Simple-root incidence, affine space, and the cubic Picard uniqueness

**Date:** 2026-08-11  
**Status:** continuous-blackboard DERIVED + COMPUTED checkpoint; no external novelty claim.

## 1. The dimension-three source is the simple-root locus of normalized cubics

Let
\[
\Phi_{S,U,W}(r,s)=Wr^3+r^2s-Urs^2+2Ss^3
\]
and let
\[
\overline Z_3=V(\Phi)\subset P^1\times A^3_{S,U,W}
\]
be the finite degree-three projective spectral cover. Let `Z_3^circ` be the relative simple-root locus.

The normalized polynomial source maps to it by
\[
(x,y,z)\mapsto\bigl(F(x,y,z),[1+2xy:x]\bigr),
\]
and exact differentiation gives
\[
\Phi(1+2xy,x)=0,
\]
\[
\boxed{(\Phi_r,\Phi_s)(1+2xy,x)=(-x,1+2xy).}
\]
Hence the marked root is simple everywhere and is already unit-gradient normalized.

Conversely, for any finite simple root `a` of
\[
f(t)=Wt^3+t^2-Ut+2S
\]
with `d=f'(a)`, the unique source point is
\[
x=-1/d,
\qquad
y=(a+d)/2,
\qquad
z=-Wd^3+\frac32ad+\frac52d^2.
\]
For the infinity root `[1:0]` (which occurs at `W=0` and is always simple because the `r^2s` coefficient is one), the source point is
\[
x=0,
\qquad y=U,
\qquad z=S-8U^2.
\]
Thus
\[
\boxed{Z_3^\circ\cong A^3.}
\]
The counterexample is simply the natural simple-root projection `Z_3^circ -> A^3`.

## 2. `SL2` is the unit-gradient framed-root model

For
\[
G=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in SL_2,
\]
set `W=AC` and interpret `[B:A]` as a root. Requiring
\[
\Phi_r(B,A)=-A,
\qquad
\Phi_s(B,A)=B
\]
uniquely forces
\[
U=(1+2B+3B^2C)/A,
\]
\[
S=B(1+B+2B^2C)/(2A^2).
\]
So the rational `SL2` map is the moduli map for a normalized cubic together with a unit-gradient framed root.

Synthetic division by the marked root gives
\[
b=1+aW,
\qquad c=ab,
\]
so
\[
\det\begin{pmatrix}1&a\\W&b\end{pmatrix}=1.
\]
The `SL2/T` boundary geometry is therefore also the first transfer matrix of synthetic division.

## 3. Why cubic degree is unique

For a degree-`m` homogeneous binary form, at a simple root
\[
\nabla\Phi(r,s)=\lambda(-s,r).
\]
Under root rescaling `(r,s)->c(r,s)`,
\[
\lambda\mapsto c^{m-2}\lambda.
\]
Thus unit-gradient normalization requires an `(m-2)`-th root of the inverse derivative. Cubics are the unique nontrivial degree for which this is rational with exponent one.

The global obstruction is sharper. The universal marked-root incidence variety of degree-`m` binary forms is
\[
\mathcal U_m\cong P^1\times P^{m-1}.
\]
Let `H1,H2` generate its Picard group. The repeated-root divisor has class
\[
R\sim(m-1)H_1+H_2,
\]
while the pullback of the coefficient-normalization hyperplane has class
\[
H\sim H_1+H_2.
\]
Therefore the normalized simple-root locus
\[
Z_m^\circ=(P^1\times P^{m-1})\setminus(R\cup H)
\]
has
\[
\boxed{
\operatorname{Pic}(Z_m^\circ)
\cong Z^2/\langle(m-1,1),(1,1)\rangle
\cong
\begin{cases}
Z,&m=2,\\
0,&m=3,\\
Z/(m-2),&m\ge4.
\end{cases}}
\]

Consequently:

- the quadratic normalized simple-root locus cannot be `A2`;
- cubic degree is the unique nontrivial degree with no Picard obstruction, and the explicit isomorphism above proves it is `A3`;
- every universal normalized degree `m>=4` simple-root locus has nontrivial torsion and cannot be `A^m`.

The torsion generator is the tautological root line; the derivative trivializes its `(m-2)`-th power. This is the global form of the unit-gradient Kummer obstruction.

## 4. Quadratic contrast

For the natural quadratic analogue the simple-root locus retains an unavoidable derivative-scale boundary class. In an affine monic chart it is `A1 x Gm`; globally in the coefficient-normalized projective formulation its Picard group is nontrivial. A quadratic root cannot absorb its derivative by homogeneous rescaling because the scaling exponent `m-2` is zero.

Thus, within the universal projective simple-root architecture, dimension three is not merely the first successful example. Cubic degree is the unique degree at which the unramified marked-root geometry can itself become affine space.

## 5. Ramification inversion / inverse different

For every canonical spectral extension,
\[
f'(a)=h_a-U=-X,
\qquad
\boxed{x=-1/f'(a).}
\]
Thus the reciprocal source coordinate is the Grothendieck residue / generator of the inverse different. The Keller affine model extends this inverse-different generator as a regular coordinate while moving the finite cover's ramification divisor to infinity.

This gives a compact structural description of the primitive disproof:
\[
\boxed{
\text{normalized cubic coefficient space}
\leftarrow \text{simple-root locus }A^3
\cong \text{unit-gradient framed-root graph closure}.}
\]
The degree-three behavior is root counting; the Jacobian-one behavior is ramification normalization plus the affine graph discrepancy cancellation.