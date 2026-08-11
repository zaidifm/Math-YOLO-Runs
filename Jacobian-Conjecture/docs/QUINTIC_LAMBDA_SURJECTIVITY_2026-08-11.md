# Scalar quintic line: exact surjectivity classification

**Date:** 2026-08-11  
**Status:** current-run blackboard result. Exact formulas/elimination are COMPUTED; the theorem is DERIVED from those identities and elementary algebra. Independent specialist/formal review and literature-priority clearance remain outstanding.  
**Scope:** fixed reciprocal-chart canonical-potential family only.

## Family

With

\[
h_0=a^2(1+aW),\qquad g_5=a^2(1+aW)^3,
\]

consider

\[
\boxed{h_\lambda=h_0+\lambda g_5.}
\]

Let

\[
v=1+2xy,\quad L=-1+3xy+x^2z,\quad K=y+6xy^2+xz+2x^2yz,
\]

so `W=xL`, `a=v/x`, `1+aW=xK`.

If `(S0,U0,W)` is the base canonical map, exact differentiation gives

\[
S_\lambda=S_0+\frac\lambda2v^2K^2(1+4vL),
\]

\[
U_\lambda=U_0+2\lambda x^2vK^3+3\lambda xLv^2K^2,
\]

\[
W_\lambda=xL.
\]

Direct symbolic calculation gives

\[
\boxed{\det J(S_\lambda,U_\lambda,W_\lambda)=1.}
\]

For `lambda != 0`, the degree profile is `(17,16,4)`.

## Boundary plane

At `x=0`,

\[
W=0,\qquad U=y,\qquad S=z+\frac{16-3\lambda}{2}y^2.
\]

Therefore the entire target plane `W=0` is covered for every `lambda`.

## Recovery quintic

For a target `(s,u,w)` with `w!=0`, put `t=wa`. The recovery equation is

\[
\boxed{
P_{\lambda;s,u,w}(t)
=\lambda t^5+3\lambda t^4+(1+3\lambda)t^3+(1+\lambda)t^2
-uwt+2sw^2.
}
\]

If `f(a)=h_lambda(a,w)-ua+2s`, then

\[
f'(a)=h_a-u=-X.
\]

Thus a simple recovery root gives an affine source point; a multiple root has `X=0` and escapes to infinity. A target with `w!=0` is missed iff its quintic has no simple root.

## Squareful elimination

For `lambda != 0`, a degree-five polynomial with no simple root has multiplicity pattern `3+2` or `5`, hence can be written

\[
\lambda(t-r)^3(t-s)^2
\]

(with `r=s` allowed).

Set `k=1/lambda`. Matching the fixed coefficients gives

\[
3r+2s=-3,
\]

\[
3r^2+6rs+s^2=3+k,
\]

\[
r^3+6r^2s+3rs^2=-(1+k).
\]

Eliminating `s` gives

\[
E_2=4k+15r^2+18r+3=0,
\]

\[
E_3=4k-5r^3+18r^2+27r+4=0.
\]

Exact elimination yields

\[
\boxed{\operatorname{Res}_r(E_2,E_3)=320k(5k^2+99k+27).}
\]

Since `k!=0`, squareful recovery is possible only if

\[
5k^2+99k+27=0,
\]

or equivalently

\[
\boxed{27\lambda^2+99\lambda+5=0.}
\]

The two roots are

\[
\boxed{\lambda_\pm=\frac{-33\pm7\sqrt{21}}{18}.}
\]

A simpler blackboard elimination reaches the same condition: use `E2` to eliminate `k`; `E3` reduces to

\[
(r+1)(5r^2-8r-1)=0.
\]

The `r=-1` branch gives `k=0`; the two finite branches give the same `lambda_\pm`.

## Constructive omitted targets at the two exceptional values

Let `k` satisfy `5k^2+99k+27=0`, `lambda=1/k`. Set

\[
r=-\frac{2k+3}{21},\qquad s=\frac{k-9}{7}.
\]

For

\[
W=1,\qquad U=\frac{3-4k}{15},\qquad S=-\frac{28k+9}{250},
\]

exact reduction modulo the quadratic gives

\[
P(t)=\lambda(t-r)^3(t-s)^2.
\]

All roots are multiple, so every recovery branch has `X=0`. Since `x=0` forces `W=0`, this `W=1` target is genuinely omitted.

## Classification

If

\[
\lambda\ne0,\qquad27\lambda^2+99\lambda+5\ne0,
\]

then every recovery quintic at `w!=0` has a simple root, hence an affine preimage. The plane `w=0` is already covered. Therefore `F_lambda` is surjective.

At `lambda=0`, recovery drops to

\[
P_0=t^3+t^2-uwt+2sw^2.
\]

For

\[
U=-\frac1{3w},\qquad S=\frac1{54w^2},
\]

one gets

\[
P_0=(t+1/3)^3,
\]

so the base map is nonsurjective.

Hence across the full scalar line:

\[
\boxed{
F_\lambda\text{ is nonsurjective exactly for }
\lambda\in
\left\{0,\frac{-33-7\sqrt{21}}{18},\frac{-33+7\sqrt{21}}{18}\right\}.
}
\]

For every other nonzero `lambda`, `F_lambda` is a surjective, noninjective Keller map with determinant `1`, degree profile `(17,16,4)`, and generic fiber degree five.

The historical archive's `lambda=2` example is recovered because `27*2^2+99*2+5=311 != 0`.

## Verification

- `scripts/jacobian_quintic_lambda_surjectivity_verify.py`
- `verification/jacobian_quintic_lambda_surjectivity_verify_2026-08-11.txt`

No external novelty or priority claim is made.