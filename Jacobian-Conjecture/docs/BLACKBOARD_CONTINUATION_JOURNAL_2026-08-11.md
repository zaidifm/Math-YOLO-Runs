# Jacobian BlackBoard Continuation Journal

**Started:** 2026-08-11 17:35 PDT / 2026-08-12 00:35 UTC  
**Mode:** continuous blackboard run; checkpoints record intermediate representations and attacks rather than waiting for a final narrative.  
**Epistemic rule:** exact symbolic identities = COMPUTED; general arguments = DERIVED until an independent route/formal review exists; no external novelty claim.

## Checkpoint 1 — the hidden coordinates are literally torus + quotient coordinates on SL2

The exact matrix from the previous run is

\[
G=\begin{pmatrix}x&v\\L&K\end{pmatrix},\qquad xK-vL=1,
\]
with
\[
v=1+2xy,\quad L=-1+3xy+x^2z,\quad K=y+6xy^2+xz+2x^2yz.
\]

The reciprocal coordinates satisfy
\[
X=1/x,\qquad a=v/x,\qquad W=xL,\qquad b=xK=1+aW.
\]
Hence exactly
\[
\boxed{G=\operatorname{diag}(1/X,X)\begin{pmatrix}1&a\\W&1+aW\end{pmatrix}.}
\]
Thus `X` is not merely a reciprocal source coordinate. It is the torus coordinate along `SL2 -> T\\SL2`, while `(a,W)` are big-cell quotient coordinates. The former "hidden variables" are therefore ordinary group coordinates in disguise.

This makes the source-side Jacobian cancellation conceptually less mysterious: the source birational chart separates the torus coordinate from the quotient chart.

## Checkpoint 2 — the canonical map is an incidence / Legendre map of polynomial graphs

For a potential `h(a,W)`, the canonical hidden-coordinate map is
\[
U=X+h_a,\qquad 2S=aU-h,\qquad W=W.
\]
For fixed `W=w`, define the affine plane curve
\[
C_w:\ y=h(a,w).
\]
A target `(S,U,w)` defines the line
\[
\ell_{S,U}: y=Ua-2S.
\]
The recovery equation
\[
h(a,w)-Ua+2S=0
\]
is exactly the intersection equation `C_w ∩ ell_{S,U}`.
Moreover
\[
\frac{d}{da}(h-Ua+2S)=h_a-U=-X.
\]
Therefore:

- affine source points with `x != 0` correspond to **transverse** line/curve intersections (`X != 0`);
- `X=0` is exactly tangency;
- a target is omitted from the `x!=0` chart iff **every** intersection of its line with `C_w` is tangent, equivalently the recovery polynomial has no simple root.

This reframes the squareful-polynomial calculations from the previous run as projective/dual geometry: the exceptional target locus is the locus of *totally tangent lines* to the graph family.

The Jacobian of `(X,a)->(S,U)` is `-X/2`, so the incidence projection ramifies exactly on the tangent-line locus. The reciprocal source chart contributes the inverse factor needed for constant Jacobian after pullback.

This suggests that the phase transition `m=3,4 | 5 | >=6` is the intersection behavior of a low-dimensional affine slice of line space with the totally-tangent/squareful stratum, not an accidental coefficient phenomenon.

## Checkpoint 3 — a one-parameter SL2 source-chart family explains the coefficients 2 and 3

Introduce a nonzero parameter `tau` and define
\[
X=1/x,\qquad a=X+\tau y,
\]
\[
W=-x+(\tau+1)x^2y+x^3z.
\]
Then an exact symbolic calculation gives
\[
\boxed{\det\frac{\partial(X,a,W)}{\partial(x,y,z)}=-\tau x.}
\]

Set
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
\boxed{xK_\tau-v_\tau L_\tau=1,}
\]
so
\[
G_\tau=\begin{pmatrix}x&v_\tau\\L_\tau&K_\tau\end{pmatrix}\in SL_2.
\]
Moreover
\[
a=v_\tau/x,\quad W=xL_\tau,\quad b=xK_\tau=1+aW.
\]
Thus *the same quotient ring and boundary geometry occur for every `tau != 0`.*

Let
\[
J_\tau=\begin{pmatrix}1&x\\ \tau y&1+\tau xy\end{pmatrix}.
\]
Writing
\[
p_\tau=(\tau+1)y+xz,
\]
one gets the exact factorization
\[
\boxed{G_\tau=n_-(p_\tau)J_\tau^{-1}w.}
\]
The original construction is the special value `tau=2`; the apparently arbitrary coefficients `2` in `1+2xy` and `3` in `-1+3xy+x^2z` are simply `tau` and `tau+1`.

This also subsumes the previous bridge to the BLIND4 frame: BLIND4 used `J_1^{-1}`, while the announced boundary chart used `G_2`. They lie in a continuous elementary `SL2` family rather than merely being neighboring ad hoc matrices.

## Checkpoint 4 — determinant-one incidence maps exist for every tau

For the `tau` source chart, replace the target normalization by
\[
U=X+h_a,\qquad S=\frac{aU-h}{\tau},\qquad W=W.
\]
Then
\[
\det\frac{\partial(S,U,W)}{\partial(X,a,W)}=-X/\tau.
\]
Combining with the source-chart Jacobian `-tau*x` and `Xx=1` gives
\[
\boxed{\det JF_{\tau,h}=1}
\]
identically, independent of `h`.

So the determinant cancellation is not tied to the numerical constant `2`; it is a structural duality between the torus coordinate in the `SL2` chart and the incidence/Legendre projection.

### Immediate questions opened by this checkpoint

1. Are the `tau != 0` polynomial Keller families polynomially conjugate, birationally conjugate, or genuinely inequivalent?
2. Does the complete boundary-ideal polynomialization classification remain literally unchanged for every `tau`? (Expected yes because the quotient coordinates `(a,W)` and ring `R` are unchanged; needs exact pullback degree/regularity audit.)
3. Is there a natural moduli interpretation of `tau`, or is it a choice of root-subgroup slope / gauge?
4. Can the original counterexample be *derived* by starting from the word `n_- J_tau^{-1} w` plus a minimal boundary-ideal potential, rather than discovered by coefficient search?
