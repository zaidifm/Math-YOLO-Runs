# Blackboard checkpoint 70 — the `k=2` exchange alternative self-destructs

**Date:** 2026-08-11  
**Status:** exact identities COMPUTED; the boundary-residue classification argument is DERIVED and internally checked. No external priority claim.

Checkpoint 69 suggested testing colored completions beyond the `SL_2/T` exchange relation. The first natural alternative is

\[
b=1+a^2W,
\qquad c=ab,
\qquad c^2W=b^2(b-1).
\]

Use the most general linear source-boundary ansatz compatible with the required Jacobian character:

\[
X=x^{-1},\qquad a=X+r,
\]
\[
W=-x^2+x^3s,
\]
where
\[
r=\alpha y+\beta z,\qquad s=py+qz,
\qquad \Delta=\alpha q-\beta p.
\]

Exact calculation gives

\[
\boxed{\det\frac{\partial(X,a,W)}{\partial(x,y,z)}=-\Delta x.}
\]

The exchange function is divisible by `x`, so `b=xK` and `c=ab` pull back polynomially. On `x=0` the quotient remembers the single boundary coordinate

\[
\boxed{c_0=s-2r.}
\]

For the incidence map

\[
U=X+h_a,\qquad S=\frac{aU-h}{\Delta},
\]

boundary valuation forces the principal potential

\[
h\equiv\frac12a^2b
\]
up to corrections invisible to the leading cancellation. The only correction that can alter the remaining simple-pole residue at the same diagonal order is `gamma*a^2*b^2`; higher admissible corrections change the residue only by functions of `c_0`.

The unavoidable residue class is represented by

\[
\rho=3s-8r
\]
modulo boundary functions. Its transverse component is detected by

\[
\boxed{
\rho\wedge c_0
=(3s-8r)\wedge(s-2r)
=-2\,r\wedge s.
}
\]

In coordinates,

\[
\boxed{\det(\rho,c_0)=-2\Delta.}
\]

The `gamma*a^2*b^2` correction changes `rho` only by a multiple of `c_0`, leaving this wedge invariant. Thus polynomiality of `S` would require the residue to be a function of `c_0`, forcing the wedge to vanish and hence

\[
\Delta=0.
\]

But `Delta=0` is exactly degeneration of the source Jacobian.

Therefore, in this complete linear `k=2` exchange / affine-modification ansatz,

\[
\boxed{
\text{boundary regularity}\Longrightarrow\text{Jacobian degeneracy}.
}
\]

Conceptually, the quotient boundary remembers only one linear combination `c_0`, while the source Jacobian measures the area form `r wedge s`. The unavoidable incidence residue retains the transverse source-boundary direction. Hidden potentials cannot cancel that direction because it has been contracted by the quotient; forcing cancellation collapses the area form itself.

This is concrete evidence that the original exponent-one relation `b=1+aW` is rigid rather than one arbitrary choice among generalized Veronese exchanges.

Exact certificate: `scripts/jacobian_k2_exchange_obstruction_verify.py` (SHA-256 `9d5e508223e58890b89017ca59101ed64423728c96fe20cb15edb0d4c64874b9`).
