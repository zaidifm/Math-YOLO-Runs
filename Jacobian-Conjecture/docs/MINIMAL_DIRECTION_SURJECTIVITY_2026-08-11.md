# Minimal canonical directions: surjectivity for every recovery degree m >= 6

**Date:** 2026-08-11  
**Status:** current-run blackboard theorem candidate. Low-degree algebra is COMPUTED exactly; the all-m argument is DERIVED below. Independent specialist/formal review is still required.  
**Scope:** fixed reciprocal-chart canonical-potential construction only.

## Minimal directions

Let `b=1+aW`. For odd `m=2r+1`, define

\[
g_m=bc^r=a^r b^{r+1}.
\]

For even `m=2r`, define

\[
g_m=b^2c^{r-1}=a^{r-1}b^{r+1}.
\]

Uniformly write

\[
\boxed{g_m=a^d b^e,\qquad d+e=m,}
\]

where

\[
(d,e)=
\begin{cases}
((m-1)/2,(m+1)/2),&m\text{ odd},\\
(m/2-1,m/2+1),&m\text{ even}.
\end{cases}
\]

Consider

\[
\boxed{h_{m,\lambda}=h_0+\lambda g_m,\qquad h_0=a^2(1+aW),\quad\lambda\ne0.}
\]

## Direct polynomialization and Keller determinant

With

\[
v=1+2xy,\quad L=-1+3xy+x^2z,\quad K=y+6xy^2+xz+2x^2yz,
\]

we have `a=v/x`, `b=xK`, `W=xL`.

Exact differentiation gives

\[
(g_m)_a=a^{d-1}b^{e-1}(mb-e),
\]

\[
a(g_m)_a-g_m=a^db^{e-1}((m-1)b-e).
\]

After pullback,

\[
\Delta U=\lambda v^{d-1}x^{e-d}K^{e-1}(mxK-e),
\]

\[
2\Delta S=\lambda v^d x^{e-d-1}K^{e-1}((m-1)xK-e).
\]

Because `e-d` is 1 for odd `m` and 2 for even `m`, these are polynomial.

The canonical hidden-coordinate map has

\[
\det\frac{\partial(S,U,W)}{\partial(X,a,W)}=-X/2,
\]

while the reciprocal-coordinate change has

\[
\det\frac{\partial(X,a,W)}{\partial(x,y,z)}=-2x.
\]

Since `Xx=1`,

\[
\boxed{\det JF_{m,\lambda}=1.}
\]

The degree profile for `m>=5` is

\[
\boxed{(D_m,D_m-1,4),\qquad
D_m=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}}
\]

## Boundary plane

On `x=0`, `W=0` and `U=y`. The second output has the form

\[
S=z+\Phi_{m,\lambda}(y),
\]

so the entire target plane `W=0` is covered for every `m>=5` and every `lambda`.

## Universal recovery polynomial

For target `(S,U,w)` with `w!=0`, set `t=wa`. Multiplying the recovery equation by `w^d` and dividing by `lambda` gives

\[
\boxed{
P(t)=H_{d,e}(t)+\kappa t^2(1+t)+pt+q,
\qquad H_{d,e}=t^d(1+t)^e,
}
\]

where

\[
\kappa=w^{d-2}/\lambda,
\qquad p=-Uw^{d-1}/\lambda,
\qquad q=2Sw^d/\lambda.
\]

A recovery root is affine exactly when it is simple, because for

\[
f(a)=h(a,w)-Ua+2S
\]

one has

\[
f'(a)=h_a-U=-X.
\]

Thus a target with `w!=0` is missed iff `P` has no simple root.

For every `m>=6`, `lambda!=0`, and `w!=0`, the relevant `kappa` is nonzero.

## Uniform obstruction for m >= 9

Assume `m>=9` and every root of `P` is multiple. Let `C=rad(P)`. Then

\[
\deg C\le\lfloor m/2\rfloor.
\]

Consider

\[
\Delta=P'/P-H'/H.
\]

The reduced denominator of `P'/P` divides `C`, while that of `H'/H` divides `t(t+1)`. Hence a nonzero `Delta` has reduced denominator degree at most

\[
\lfloor m/2\rfloor+2.
\]

But `P-H` has degree at most three, so

\[
P/H=1+O(t^{3-m}),
\]

and therefore

\[
\Delta=(\log(P/H))'=O(t^{2-m}).
\]

For `m>=9`,

\[
m-2>\lfloor m/2\rfloor+2.
\]

A nonzero rational function cannot decay at infinity to order exceeding the degree of its reduced denominator. Thus `Delta=0`, so `P/H` is constant. Both are monic, hence `P=H`, forcing `kappa=p=q=0`, contradiction.

Therefore every recovery polynomial has a simple root for `m>=9`.

## Low cases m=6,7,8

These sit below the strict denominator inequality and were checked exactly.

### m=6

A squareful sextic is either a square of a cubic or a cube of a quadratic.

Matching a cubic square against

\[
t^2(1+t)^4+\kappa t^2(1+t)+pt+q
\]

forces `kappa=0`.

Matching a quadratic cube forces `kappa=4/27` from the `t^3` coefficient, but the `t^2` coefficient then disagrees (`4/3` versus `31/27`).

So no squareful sextic exists for `kappa!=0`.

### m=7

Every squareful septic has form `A_2^2 B_1^3`. Matching coefficients through `t^4` reduces to

\[
\gamma(35\gamma^2-60\gamma+24)=0.
\]

The remaining `t^3,t^2` compatibility gives

\[
\gamma(21\gamma^4-135\gamma^3+448\gamma^2-528\gamma+192)=0.
\]

The quadratic and quartic factors have exact resultant

\[
24869376\ne0.
\]

The `gamma=0` branch forces `kappa=0`. Hence no squareful septic exists for `kappa!=0`.

### m=8

A squareful octic is either a square quartic or `A_1^2B_2^3`.

The square-quartic match forces `kappa=-3/128` from `t^3`, but its `t^2` coefficient is `-25/512` rather than `-3/128`.

The `A_1^2B_2^3` match uniquely gives

\[
(t+1)^2(t^2+t)^3=t^3(1+t)^5=H,
\]

hence `kappa=0`.

So no squareful octic exists for `kappa!=0`.

## Theorem

Combining the low cases with the logarithmic-derivative argument:

\[
\boxed{
\text{For every }m\ge6\text{ and every }\lambda\in\mathbb C^\times,
F_{m,\lambda}:\mathbb C^3\to\mathbb C^3
\text{ is surjective.}
}
\]

For a generic target the recovery polynomial has `m` simple roots, so

\[
\boxed{\deg_{gen}F_{m,\lambda}=m.}
\]

Thus every member is noninjective.

Together with the determinant calculation, these are surjective noninjective Keller maps of every generic fiber degree `m>=6`.

## Degree five is the only low-degree bifurcation

For `m=5`, the separate scalar-line classification shows exactly two exceptional nonzero coefficients:

\[
\lambda_\pm=\frac{-33\pm7\sqrt{21}}{18}.
\]

All other nonzero degree-five coefficients are surjective.

Thus:

\[
\boxed{
m=5:\text{ two exceptional nonzero coefficients};
\qquad
m\ge6:\text{ every nonzero coefficient is surjective}.
}
\]

The archived degree-17 `lambda=2` map is therefore the first visible member of an infinite hierarchy rather than an isolated example.

## Verification

- `scripts/jacobian_minimal_direction_surjectivity_verify.py`
- `verification/jacobian_minimal_direction_surjectivity_verify_2026-08-11.txt`

No external novelty or priority claim is made.