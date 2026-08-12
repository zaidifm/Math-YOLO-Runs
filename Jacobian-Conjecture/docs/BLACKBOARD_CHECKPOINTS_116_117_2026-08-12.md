# Jacobian Blackboard Checkpoints 116–117

## 116 — degree-three branch geometry diagonalizes in the boundary lattice

For a generic-degree-three Keller normalization, codimension-one inertia is a transposition. Over each irreducible branch divisor `B_j=(p_j=0)` there is exactly one ramified boundary prime `D_j` of index two and one unramified visible prime `Q_j` of residue degree one. Thus

\[
\boxed{\operatorname{div}_{\bar X}(p_j)=2D_j+Q_j.}
\]

Using the previously derived boundary basis

\[
\operatorname{Cl}(\bar X)=\bigoplus_i\mathbb Z[D_i],
\]

we obtain

\[
\boxed{[Q_j]=-2[D_j].}
\]

If every boundary component is ramified, then

\[
K_{\bar X/Y}=\sum_j[D_j],\qquad [Q_{\rm vis}]=-2K_{\bar X/Y}.
\]

This makes degree-three branch pullback diagonal in the free boundary class lattice rather than an arbitrary relation.

## 117 — no two-dimensional affine linear cubic slice can descend the primitive mechanism to `A^2`

Let `L ~= A^2` be any affine two-plane in binary cubic coefficient space and `X_L` the incidence surface of a cubic in `L` together with a chosen simple projective root. Assume the generic cubic has three distinct roots and the incidence is connected/transitive.

For root coordinate `t=A/B`, let

\[
e(t)=(t^3,t^2,t,1),\qquad d(t)=(3t^2,2t,1,0),
\]

and let `ell_1,ell_2` be the two normalization covectors. The generic root fiber is `G_m`; it changes type precisely when

\[
D(t)=\det(\ell_1,\ell_2,e(t),d(t))=0.
\]

In Plucker coordinates of the normalization line,

\[
\boxed{D(t)=-p_{01}+2p_{02}t-(p_{03}+3p_{12})t^2+2p_{13}t^3-p_{23}t^4.}
\]

`D` cannot vanish identically for an honest projective line.

For a connected incidence, an exceptional root fiber is either a cap `A^1` or empty; if the evaluation covector itself lies in the normalization line and the affine constants are compatible, every cubic has that fixed root and the incidence is reducible.

The explicit root-fiber stratification gives

\[
[X_L]=\mathbb L^2-1+c-e(\mathbb L-1).
\]

If `X_L ~= A^2`, the Hodge–Deligne polynomial forces exactly one cap and no empty root fibers. Hence the quartic `D` must have exactly one set-theoretic root. Move it to `t=0`; then `D` is a nonzero multiple of `t^4`. Its coefficient conditions plus the Plucker relation force all Plucker coordinates to vanish except `p_{23}`. Therefore the normalization line is `P(span(e_2,e_3))`, which contains the twisted-cubic point `e(0)=e_3`.

That is precisely the excluded rank-drop case: compatible constants give a fixed root and reducible incidence; incompatible constants give an empty root fiber. Contradiction.

Therefore

\[
\boxed{\text{no connected chosen-simple-root incidence over a two-dimensional affine linear slice of binary cubics is }\mathbb A^2.}
\]

So the primitive cubic counterexample cannot descend to JC2 merely by imposing one additional affine linear condition on its cubic target family.

Exact certificate: `jacobian_cubic_two_parameter_slice_obstruction_verify.py`, SHA-256 `25910c37b5508a0c95ae969ec86d243c79c4c003db41b55587d6ddf50e054c11`.

No external novelty claim is made.