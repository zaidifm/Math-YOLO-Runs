# Blackboard checkpoint 73 — the source is the simple-root locus of a finite projective cubic cover

**Date:** 2026-08-11  
**Status:** explicit identities and chart inverses COMPUTED; global geometric identification DERIVED from those charts. No external novelty claim.

For the primitive `tau=2` potential

\[
h_0(a,W)=a^2+Wa^3,
\]

the recovery equation is

\[
Wa^3+a^2-Ua+2S=0.
\]

Homogenize the root coordinate `[A:B] in P^1`:

\[
\boxed{\Phi_{S,U,W}(A,B)=WA^3+A^2B-UAB^2+2SB^3.}
\]

The relative cubic hypersurface

\[
\overline Z=\{\Phi=0\}\subset P^1\times A^3_{S,U,W}
\]

is the finite projective spectral/root completion of the generic cubic cover.

For a source point define `v=1+2xy`. The selected projective root is globally

\[
\boxed{[A:B]=[v:x].}
\]

The pair `(v,x)` never vanishes simultaneously, and exact substitution gives

\[
\Phi_F(v,x)=0.
\]

More strongly,

\[
\boxed{\Phi_A(v,x)=-x,\qquad \Phi_B(v,x)=v.}
\]

Thus

\[
\boxed{\nabla_{A,B}\Phi(v,x)=(-x,v),}
\]

the symplectic rotation of the root vector. The selected root is therefore simple at every source point, including `x=0`.

On the finite root chart `B=1`, a simple root `a` has

\[
X=U-2a-3Wa^2\ne0,
\]

and the inverse source coordinates are

\[
x=X^{-1},\qquad y=(a-X)/2,
\qquad z=(W+x-3x^2y)/x^3.
\]

On the infinity chart `A=1`, put `t=B/A`. Then

\[
\Psi(t)=W+t-Ut^2+2St^3=0,
\qquad
D=\Psi_t=1-2Ut+6St^2.
\]

For a simple root (`D!=0`) the inverse begins

\[
\boxed{x=t/D,\qquad y=U-3St,}
\]

and `z` simplifies to a regular polynomial expression after using `Psi=0`. At the infinity root `t=0`,

\[
\boxed{x=0,\qquad y=U,\qquad z=S-8U^2.}
\]

The two local inverses agree on their overlap. Consequently

\[
\boxed{A^3_{source}\cong \overline Z^{simple},}
\]

the simple-root locus of the finite projective cubic spectral cover, and the Keller map is precisely the restriction of the finite cover projection to that open locus.

This makes the Zariski-Main picture literal: the finite completion is the projective root cover; its ramification is the multiple-root locus; and affine three-space is the complementary simple-root model. The divisor `x=0` is the simple root at projective infinity over `W=0`, not an ad hoc point outside the finite model.

Exact certificate: `scripts/jacobian_projective_spectral_simple_root_verify.py`, SHA-256 `b77b8b5561393a959be9d5a07ba73d23260da1e5509daf7ae1c690c0b7ee3be6`.
