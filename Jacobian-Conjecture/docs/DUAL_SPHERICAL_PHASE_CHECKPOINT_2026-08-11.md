# Dual/spherical phase checkpoint

**Date:** 2026-08-11  
**Status:** current-run DERIVED + COMPUTED checkpoint; no external novelty claim.

## Two boundaries and the discriminant

In the hidden coordinate `X=1/x`, two different boundary phenomena separate cleanly:

- `x=0` is `X=infinity`; it is the polynomialization boundary controlled by the color `D=(W,b)` and the intersection ring;
- `x=infinity` is `X=0`; it is the nonproperness boundary where recovery roots become tangent and sheets escape.

For fixed `W=w`, the potential graph is `y=h(a,w)` and a target `(S,U,w)` represents the affine line `y=Ua-tau*S`. The recovery polynomial is

\[
h(a,w)-Ua+\tau S.
\]

Its derivative is `h_a-U=-X`. Hence simple roots are transverse intersections and multiple roots are points on the `X=0` infinity divisor.

The nonproperness hypersurface is therefore the graph-dual/discriminant resultant

\[
\operatorname{Res}_a(h-Ua+\tau S,h_a-U)=0.
\]

The image complement is the deeper locus where **all** intersections are tangent, equivalently the recovery polynomial has no simple root.

## Binary forms and coincident-root loci

For the minimal hidden-degree-`m` direction,

\[
g_m=a^d(1+aW)^e,
\qquad d+e=m,
\]

and after `t=aW` its high recovery form is

\[
H_{d,e}(t)=t^d(1+t)^e.
\]

Homogenization gives `T^d(S+T)^e` in `Sym^m(k^2)`. Thus the surjectivity problem is an intersection problem in classical binary-form representation theory: varying the target line changes only the final two coefficients, and missed targets occur when that two-plane meets the coincident-root locus with every multiplicity at least two.

The codimension of the maximal all-multiple locus is `ceil(m/2)`, explaining the transition from forced low-degree intersections to eventual avoidance.

## SL2/T weight monoid and the color ideal

The boundary quadric

\[
q^2-4cW=1
\]

is `SL2/T`. Its associated graded is

\[
k[s^2,st,t^2],
\]

and representation-theoretically the coordinate ring is multiplicity-free with even highest weights,

\[
k[SL2/T]\simeq\bigoplus_{n\ge0}V_{2n}.
\]

The missing boundary line is `D=(W,b)`, which degenerates to the color `s=0` with ideal `(s^2,st)`. Modulo target gauges, polynomializing canonical potentials are precisely the color ideal. The sharp degree spectrum is therefore optimization over the `SL2/T` weight monoid subject to one color valuation.

This gives a spherical interpretation of the old parity defect and the degree-17 vector.

## Tau is the second boundary jet

For the diagonal slice

\[
h=a^2H(aW),
\]

the absolute regularity conditions in the normalized `tau` source chart are exactly

\[
\boxed{H(-1)=0,\quad H'(-1)=1,\quad H''(-1)=2-\tau.}
\]

Equivalently,

\[
H(t)=1+t+\frac{2-\tau}{2}(1+t)^2+(1+t)^3R(t).
\]

Thus the root-subgroup parameter is the missing second boundary jet. The original `tau=2` chart is precisely the zero-second-jet resonance, recovering the BLIND4 condition.

## Two-parameter surjectivity staircase

Write

\[
h_{\tau,m,\lambda}=h_\tau+\lambda g_m,
\qquad
h_\tau=a^2b+\mu c^2,
\quad \mu=(2-\tau)/2.
\]

Exact low-degree elimination plus the high-degree pole-count argument give the following nonsurjective locus in the structural parameter plane `(tau,lambda)`:

- `m=5`: one algebraic exceptional curve `E5(mu,lambda)=0`; at `tau=2`, three branches coalesce at `lambda=0` and the two surviving nonzero points satisfy `27 lambda^2+99 lambda+5=0`;
- `m=6`: the curve `lambda=-(tau-2)^2/16` plus two isolated cube-pattern points satisfying `19 tau^2+104 tau+121=0`, `lambda=9(tau+1)/4`;
- `m=7`: three isolated parameter pairs;
- `m=8`: exactly `(tau,lambda)=(-11,96)`;
- `m>=9`: no exceptional nonzero parameter pairs.

Thus the nonsurjective set falls from curve to points to empty exactly as coincident-root codimension outruns the available structural parameters.

## Restricted dimension-two obstruction

Within this reciprocal-incidence mechanism, dimension two leaves no extra quotient coordinate analogous to `W`. A one-variable potential `h(a)` would need both `a+h'` and `a(a+h')-h` regular across a simple pole of `a`. No polynomial can satisfy both. The three-dimensional exchange partner `W`, through `b=1+aW`, is exactly what removes that obstruction.

This explains the dimension threshold for this mechanism only; it is not a proof of JC2.
