# Tau resonance and the incidence-machine derivation

**Date:** 2026-08-11  
**Status:** current-run DERIVED + COMPUTED checkpoint. Exact identities have symbolic certificates; general classification statements remain subject to independent specialist/formal review. No external novelty claim.

## 1. The hidden coordinates are group coordinates

For the normalized source chart, introduce `tau != 0` and set

\[
X=1/x,\qquad a=X+\tau y,
\]
\[
W=-x+(\tau+1)x^2y+x^3z.
\]

Define

\[
v_\tau=1+\tau xy,
\]
\[
L_\tau=-1+(\tau+1)xy+x^2z,
\]
\[
K_\tau=y+\tau(\tau+1)xy^2+xz+\tau x^2yz.
\]

Then

\[
\boxed{xK_\tau-v_\tau L_\tau=1}
\]

and

\[
G_\tau=\begin{pmatrix}x&v_\tau\\L_\tau&K_\tau\end{pmatrix}\in SL_2.
\]

With `b=xK_tau`,

\[
\boxed{
G_\tau=\operatorname{diag}(1/X,X)
\begin{pmatrix}1&a\\W&1+aW\end{pmatrix}.}
\]

Thus `X` is the torus coordinate and `(a,W)` are quotient big-cell coordinates; `b=1+aW` is the determinant-one exchange relation.

## 2. Raw SL2 chart plus affine modification

Let

\[
J_\tau=\begin{pmatrix}1&x\\\tau y&1+\tau xy\end{pmatrix},
\qquad
p_\tau=(\tau+1)y+xz.
\]

Then

\[
\boxed{G_\tau=n_-(p_\tau)J_\tau^{-1}w.}
\]

If `p` is first treated as an independent variable, the hidden coordinates are

\[
X=1/x,\quad a=X+\tau y,\quad W=-x+x^2p
\]

and

\[
\det\frac{\partial(X,a,W)}{\partial(x,y,p)}=-\tau.
\]

The elementary affine modification

\[
p=(\tau+1)y+xz
\]

has Jacobian `x`. Hence

\[
\boxed{
\det\frac{\partial(X,a,W)}{\partial(x,y,z)}=-\tau x.}
\]

This explains the `x^3z` term: it is introduced by the volume-correcting affine modification.

## 3. Incidence / Legendre map

For any potential `h(a,W)`, define

\[
U=X+h_a,
\qquad
S=\frac{aU-h}{\tau}.
\]

Then

\[
\boxed{
\det\frac{\partial(S,U,W)}{\partial(X,a,W)}=-X/\tau.}
\]

Since `Xx=1`, the three determinant factors are

\[
\boxed{x\cdot(-\tau)\cdot(-X/\tau)=1.}
\]

Equivalently,

\[
\boxed{
dx\wedge dy\wedge dz
=dS\wedge dU\wedge dW
=-\frac{X}{\tau}dX\wedge da\wedge dW.}
\]

The Keller property is equality of the source and target volume forms on the common hidden chart, rather than an unexplained coefficient cancellation.

For fixed `W=w`, the recovery equation is

\[
h(a,w)-Ua+\tau S=0.
\]

It is the intersection equation between the graph `y=h(a,w)` and the affine line `y=Ua-\tau S`. Moreover

\[
(h-Ua+\tau S)'=h_a-U=-X.
\]

Thus simple roots are transverse graph/line intersections and `X=0` is tangency. For `w!=0`, missed targets are exactly line perturbations for which the recovery polynomial has no simple root.

## 4. Absolute polynomiality for the tau chart

Let

\[
R=k[a,W]\cap k[x,y,z]
=k[W,b,c]/(cW-b(b-1)),
\quad b=1+aW,\quad c=ab.
\]

The intersection proof remains valid for every `tau != 0` because

\[
(W,b)k[x,y,z]=(xL_\tau,xK_\tau)=(x).
\]

Since `X=a-tau*y`, output regularity is equivalent to

\[
\boxed{a+h_a\in R}
\]

and

\[
\boxed{a(a+h_a)-h-\tau ac\in R.}
\]

A particular solution is

\[
\boxed{
h_\tau=a^2b+\frac{2-\tau}{2}c^2.}
\]

Differences of two solutions satisfy the homogeneous fixed-chart conditions, hence the complete admissible coset is

\[
\boxed{
h=h_\tau+\alpha a+\beta+r,
\qquad r\in I_D=(W,b)\subset R.}
\]

## 5. Tau=2 is the unique low-degree resonance

At `tau=2`, the boundary-nonconstant `c^2` correction vanishes and

\[
h_2=a^2b.
\]

This has recovery degree three and yields output profile `(7,6,4)`.

For every nonzero `tau != 2`, the `c^2` class cannot be canceled by an element of `I_D`; the minimal recovery degree is four. Exact leading-form computation gives profile `(12,11,4)`, with top terms proportional to `tau^3(tau-2)`.

Therefore `tau=2` is the unique nonzero root-subgroup parameter at which the absolute polynomiality coset drops from degree four to degree three.

## 6. Exact reconstruction of the announced counterexample

Let `(P,Q,R0)` denote the announced Alpöge/Fable counterexample. At `tau=2`, the canonical map `(S,U,W)` satisfies the exact diagonal equivalence

\[
S(x,y,z)=P(\sqrt2x,\sqrt2y,z),
\]
\[
U(x,y,z)=\frac1{\sqrt2}Q(\sqrt2x,\sqrt2y,z),
\]
\[
W(x,y,z)=-\frac1{2\sqrt2}R_0(\sqrt2x,\sqrt2y,z).
\]

Thus the group/incidence construction forward-derives the announced degree `(7,6,4)` map up to elementary diagonal equivalence.

## 7. Restricted dimension-two obstruction

Within this reciprocal-incidence template, a two-dimensional analogue would have no additional quotient parameter `W`. A one-variable potential `h(a)` would need both

\[
a+h'(a)
\]

and

\[
a(a+h'(a))-h(a)
\]

to be regular across the pole of `a`. No polynomial `h` can satisfy both: degrees `>=3` fail the first condition, degrees `<=1` leave the pole, and the unique quadratic cancellation in the first condition leaves an unavoidable `a^2/2` pole in the second.

The three-dimensional construction escapes this obstruction because the exchange partner `W` creates `b=1+aW`, allowing `h_0=a^2b` to solve both pole conditions.

This is a no-go theorem for this mechanism, not a proof of the two-dimensional Jacobian Conjecture.

## 8. Degree 17 as a surjectivity threshold

Inside the normalized rank-one machine, recovery degree at most four is necessarily nonsurjective because every cubic or quartic graph admits a totally tangent affine line. The boundary filtration admits no hidden-degree-five direction below output degree 17. At degree 17 the unique quintic direction `bc^2=a^2(1+aW)^3` appears, and generic scalars are surjective.

Therefore, within this machine,

\[
\boxed{17\text{ is the first output degree at which surjectivity can occur.}}
\]

This links the previously separate degree-filtration threshold and the dual/squareful-locus phase transition.