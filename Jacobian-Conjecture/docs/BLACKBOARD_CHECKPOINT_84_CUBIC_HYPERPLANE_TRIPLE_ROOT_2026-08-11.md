# Blackboard checkpoint 84 — every linear cubic normalization meets the triple-root cone

**Date:** 2026-08-11  
**Status:** spanning and factorization identities COMPUTED; geometric consequence DERIVED. No external priority claim.

Let `V=Sym^3(C^2)^*` be binary cubic coefficient space and let

\[
H_L=\{F\in V:L(F)=1\}
\]

for a nonzero linear functional `L`.

Triple-root cubics form the affine cone over the cubic Veronese curve:

\[
\mathcal V_3=\{\lambda\ell^3\}.
\]

Cubes span all of `V`: the four cubics `(A-rB)^3` at `r=0,1,2,3` have coefficient determinant `108`. Hence no nonzero `L` vanishes on every cube. Choose `ell` with `L(ell^3)!=0`; rescaling gives

\[
\frac{\ell^3}{L(\ell^3)}\in H_L\cap\mathcal V_3.
\]

Therefore every affine linear three-parameter normalization of binary cubics contains a triple-root form. Since a triple-root cubic has no simple projective root, projection from its chosen-simple-root incidence variety necessarily omits a locus. Nonsurjectivity is thus forced for every linear cubic normalization, not peculiar to the primitive coefficient choice.

For the primitive family

\[
\Phi=WA^3+A^2B-UAB^2+2SB^3,
\]

write a normalized triple root as `lambda(A-rB)^3`. The fixed `A^2B` coefficient gives `lambda=-1/(3r)`, hence

\[
W=-\frac1{3r},\qquad U=r,\qquad S=\frac{r^2}{6}.
\]

Eliminating `r` yields exactly

\[
\boxed{3WU+1=0,\qquad 6S-U^2=0.}
\]

Conversely these equations factor the cubic as

\[
\Phi=W\left(A+\frac{B}{3W}\right)^3.
\]

Thus the omitted curve of the primitive degree-three Keller map is precisely the intersection of its normalization hyperplane with the Veronese cone of cubes.

Exact certificate: `scripts/jacobian_cubic_hyperplane_triple_root_verify.py`, SHA-256 `0fe296e600b9b02e99c4d8d1122c4f4bfdc404d32cac0999352458110ac08dde`.
