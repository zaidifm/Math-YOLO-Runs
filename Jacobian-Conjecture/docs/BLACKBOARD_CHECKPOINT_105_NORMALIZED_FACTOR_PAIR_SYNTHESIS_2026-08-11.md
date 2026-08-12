# Blackboard checkpoint 105 — normalized factor-pair synthesis

**Date:** 2026-08-11  
**Status:** polynomial identities/isomorphisms COMPUTED; global class-group and quotient interpretations DERIVED. No external priority claim.

The primitive cubic counterexample can now be reconstructed from normalized factorization alone.

## Linear factor times quadratic cofactor

Write the selected root factor and quadratic cofactor as

\[
\ell=xA-vB,
\qquad
Q=LA^2+KAB+MB^2.
\]

Then the primitive cubic is exactly

\[
\boxed{\Phi=\ell Q.}
\]

Coefficient convolution gives

\[
\boxed{W=xL,\quad 1=xK-vL,\quad -U=xM-vK,\quad 2S=-vM.}
\]

Thus the hidden determinant identity `xK-vL=1` is simply the fixed `A^2B` coefficient of the normalized cubic product.

At the chosen root `r=(v,x)`,

\[
\boxed{Q(r)=-1,}
\]
so `grad Phi(r)=(-x,v)`. The two defining normalizations are therefore: one coefficient of the product is one, and the cofactor evaluates to minus one at the selected root.

## The normalized factor-pair variety is `A^3`

Let

\[
V=\{xK-vL=1,\ Lv^2+Kvx+Mx^2=-1\}\subset A^5.
\]

The original source parametrization lands in `V`. Conversely define

\[
y=vK+\frac{xM}{2},
\qquad
p=K-2yL,
\]

then

\[
v=1+2xy,
\quad
L=-1+xp,
\quad
K=vp-2y.
\]

The second normalization forces `p-3y` to be divisible by `x`; the quotient is polynomial:

\[
z=-\frac M2-4py(1+xy)+4y^2,
\qquad
p=3y+xz.
\]

Thus

\[
\boxed{V\cong A^3}
\]

with a completely polynomial inverse. In particular

\[
W=xL=-x+3x^2y+x^3z.
\]

The explicit reciprocal chart is an iterated boundary-divisibility ladder forced by the two normalized factorization equations.

## Coordinate-free counterexample

Let `H ~= A^3` be the hyperplane of binary cubics whose `A^2B` coefficient is one, and let `X` be the incidence variety of a cubic in `H` together with a chosen simple projective root. The normalized factor-pair equations identify `X ~= A^3`.

The forgetful projection

\[
X\to H
\]

is etale because a simple root deforms uniquely, generically three-to-one because a generic cubic has three simple roots, and not surjective because the normalization hyperplane contains triple-root cubics. Since source and target are affine three-space, etaleness automatically makes the polynomial Jacobian determinant a nonzero constant.

Thus the Jacobian counterexample can be constructed without an explicit determinant computation: it is the forgetful map from normalized simple cubic factorizations to normalized cubic coefficients.

## Why derivative normalization works only for cubics

For a degree-`m` factorization `Phi=ell Q`, factor scaling acts by

\[
(ell,Q)\mapsto(s ell,s^{-1}Q),
\]

while the cofactor evaluation at the root transforms by

\[
Q(r_ell)\mapsto s^{m-2}Q(r_ell).
\]

Hence:

- `m=2`: derivative normalization is scaling-invariant and becomes an extra equation/unit obstruction;
- `m=3`: weight one, so `Q(r)=-1` fixes the `G_m` gauge uniquely;
- `m>3`: normalization leaves a residual `mu_{m-2}` ambiguity, matching the cyclic Picard/root-derivative obstruction.

Degree three is uniquely the degree where normalized simple factorization becomes an ordinary affine factor-pair variety without losing dimension or introducing a finite root-extraction ambiguity.

## Global normalization constraint

For any nontrivial Keller map, the finite Zariski-Main normalization has a nonzero ramification divisor entirely outside the affine-space source. No nonzero effective boundary divisor can have torsion class: if a positive multiple were principal, its defining regular function would restrict to a nowhere-zero regular function on `A^n`, hence a constant, contradiction. Therefore the finite normalization is necessarily nonfactorial and its ramification/canonical class has infinite order.

This global class-group constraint is the representation-free counterpart of the nonprincipal spectral derivative/canonical line visible in the cubic construction.

Exact certificates retained in the Library:

- `jacobian_cubic_factor_cofactor_verify.py`, SHA-256 `3d55cc8ce9c3383f45552df6221f46de444eb278ab26ff42c5cd0b18519a86b3`;
- `jacobian_normalized_factor_pair_A3_verify.py`, SHA-256 `90fe1d17c46b9de6c2bc260baa003cb509f19a7effd27fe95a533f300ebc9d9a`;
- `jacobian_factor_pair_triangular_ladder_verify.py`, SHA-256 `cc1e874528e754340c5aae78996aa32d0b8ffe8802f6b6a0cda46bdde2dafc3d`.
