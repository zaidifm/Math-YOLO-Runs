# Minimal-direction surjectivity: independent high-degree proof and BLIND 1 comparison

**Date:** 2026-08-11  
**Status:** current-run synthesis. This supplements `MINIMAL_DIRECTION_SURJECTIVITY_2026-08-11.md`.

## Independent Newton/Vandermonde proof for m >= 9

For the minimal scalar family, every `w != 0` recovery polynomial has normalized form

\[
P(t)=H(t)+\kappa t^2(1+t)+pt+q,
\qquad H=t^d(1+t)^e,
\]

with `d+e=m` and `kappa != 0`.

Because `P-H` has degree at most three, the coefficients of `t^{m-1},...,t^4` in `P` and `H` agree. Newton identities therefore give equality of the first `m-4` root power sums.

The root multiset of `H` consists of `0` with multiplicity `d` and `-1` with multiplicity `e`. If the distinct nonzero roots of a hypothetical squareful `P` are `r_i` with multiplicities `n_i>=2`, then

\[
\sum_i n_i r_i^j=e(-1)^j,
\qquad1\le j\le m-4.
\]

Move the `-1` term to the left and combine it with any actual root `r_i=-1`. This gives a signed measure on distinct nonzero support points whose first `m-4` positive moments vanish.

A squareful degree-m polynomial has at most `floor(m/2)` distinct roots. After adding the comparison point `-1`, the signed support has size at most

\[
\lfloor m/2\rfloor+1.
\]

For `m>=9`,

\[
\lfloor m/2\rfloor+1\le m-4.
\]

Taking as many moment equations as support points gives a Vandermonde matrix `(r_i^j)`. Its determinant is a nonzero Vandermonde factor times the product of the nonzero support points. Hence every signed weight is zero.

Therefore the only nonzero root of `P` is `-1` with multiplicity exactly `e`; degree then forces zero to have multiplicity `d`. Thus `P=H`, contradicting `kappa != 0`.

This independently rederives the `m>=9` simple-root theorem without the logarithmic-derivative pole-count argument in the main note.

## Relation to the historical BLIND 1 surjective family

The retained BLIND 1 report had already produced a different monomial family `S_m` satisfying

\[
\det JS_m=1,\qquad\deg_{gen}S_m=m,
\]

and proved it surjective for every `m>=6`.

Its degree profile is

\[
\boxed{(5m,5m-1,4).}
\]

The BLIND 1 `m=5` member is explicitly nonsurjective, and the historical report states that this only proves sharpness for that monomial sequence and **does not rule out a different generic-degree-five surjective deformation**.

The 2026-08-11 boundary-ideal classification selects different, degree-minimal canonical directions. Their scalar families have degree profile

\[
\boxed{
(D_m,D_m-1,4),\qquad
D_m=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}}
\]

For every `m>=6`, `D_m<5m`. The current theorem therefore gives degree-efficient surjective representatives of every generic degree `m>=6` inside the fixed chart.

More importantly, `QUINTIC_LAMBDA_SURJECTIVITY_2026-08-11.md` resolves the BLIND 1 degree-five question positively: on the minimal degree-17 quintic line, every nonzero scalar is surjective except the two roots of

\[
27\lambda^2+99\lambda+5=0.
\]

So the current advance relative to the retained project archive is not merely existence of arbitrary-degree surjective Keller maps. It is:

1. the boundary-ideal/minimality mechanism selecting much lower-degree representatives;
2. surjectivity of every nonzero minimal scalar family for `m>=6`;
3. and the first surjective generic-degree-five family in the retained project corpus.

This is an internal project-provenance comparison, not an external literature-priority claim.