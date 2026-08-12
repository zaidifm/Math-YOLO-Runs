# Blackboard checkpoint 75 — spectral normalization forces the `SL_2/T` boundary ring

**Date:** 2026-08-11  
**Status:** normalization identities COMPUTED exactly; geometric interpretation DERIVED. No external priority claim.

Let `t=1/a` be the projective recovery-root coordinate near infinity. The primitive cubic spectral equation is

\[
\Psi(t)=W+t-Ut^2+2St^3=0.
\]

The degree-drop point is `(t,W)=(0,0)`. Normalize the distinguished infinity branch by introducing

\[
\boxed{b=\frac{t+W}{t}=1+aW}
\]
so that

\[
W=t(b-1),
\]
then, because `b` vanishes to the same first order as `t` on the source branch,

\[
\boxed{c=\frac bt=ab.}
\]

Eliminating `t` gives immediately

\[
\boxed{cW=b(b-1).}
\]

Thus the Danielewski/discriminant-one-quadric boundary surface is the affine normalization chart forced by the projective recovery cover itself. The later identification of this surface with `SL_2/T` is therefore a homogeneous interpretation of a normalization geometry that the spectral cover already demands.

For the primitive potential `h0=a^2b`,

\[
t^3(h_0-Ua+2S)=t^2(c-U+2St),
\]
so the strict transform is

\[
\boxed{c-U+2St=0,}
\]
which is smooth along `t=0` because its `c`-derivative is one.

For the unique minimal direction

\[
g_m=a^db^e,\qquad d+e=m,
\]
with `h=h0+lambda*g_m`, exact substitution gives

\[
\boxed{
t^m f
=t^{m-1}\left(c-U+2St+\lambda t^{e-d+1}c^e\right).
}
\]

For the minimal spectrum

\[
e-d+1=2\quad(m\text{ odd}),
\qquad
e-d+1=3\quad(m\text{ even}),
\]
so every strict transform remains smooth at `t=0`. This was checked exactly for `m=5,...,12`.

Consequences:

1. `1+aW` is the first normalization ratio at the projective infinity root.
2. `c=ab` is the second normalization ratio.
3. `cW=b(b-1)` is forced by eliminating the projective root parameter.
4. Higher minimal deformations inherit the same boundary surface because they enter the normalized equation only at order `t^2` or `t^3`.
5. The primitive cubic is the common first-order infinity skeleton of the entire minimal family.

The explanatory arrow can therefore be reversed:

\[
\boxed{
\text{projective recovery cover}
\to\text{normalize infinity root}
\to cW=b(b-1)
\to SL_2/T.
}
\]

Exact certificate: `scripts/jacobian_spectral_infinity_normalization_verify.py`, SHA-256 `633655d3068a847e8dc93876eb126b5662d51b612016099983d7180de1817e4f`.
