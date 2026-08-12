# Blackboard checkpoint 98 — the root-derivative scaling exponent `m-2`

**Date:** 2026-08-11  
**Status:** scaling identities COMPUTED; geometric synthesis DERIVED. No external priority claim.

Let `Phi(A,B)` be a homogeneous binary form of degree `m` and let `r=(A,B)` be a simple projective root. Euler's identity gives

\[
A\Phi_A+B\Phi_B=m\Phi=0
\]

at `r`, so in two dimensions

\[
\boxed{\nabla\Phi(r)=\lambda J r,\qquad J(A,B)=(-B,A),\quad\lambda\ne0.}
\]

Rescale the projective representative `r -> s r`. Homogeneity gives

\[
\nabla\Phi(sr)=s^{m-1}\nabla\Phi(r)
=(s^{m-2}\lambda)J(sr).
\]

Thus the root-derivative scalar transforms by

\[
\boxed{\lambda\mapsto s^{m-2}\lambda.}
\]

This one exponent explains three phenomena that arose independently earlier in the run.

## Degree two: exponent zero

For `m=2`, projective root scaling cannot change `lambda`. The nonzero derivative scalar is therefore a genuine invariant/unit on the chosen-simple-root cover. This is the root-frame version of the degree-two obstruction: a nontrivial quadratic simple-root cover carries an unavoidable nonconstant unit and cannot be affine space.

## Degree three: exponent one

For `m=3`, there is a unique algebraic normalization `s=lambda^{-1}` such that

\[
\nabla\Phi(sr)=J(sr).
\]

Every simple cubic root therefore has a canonical normalized representative, without root extraction and without residual finite ambiguity. This is precisely the normalization behind the determinant-one root/derivative frame of Checkpoint 78.

Degree three is not merely the first generic degree not excluded by branching. It is the unique degree for which projective root scaling trivializes the derivative character linearly.

## Higher degree: cyclic root extraction

For `m>3`, normalization requires

\[
s^{m-2}=\lambda^{-1},
\]

leaving a residual `mu_{m-2}` ambiguity. The same cyclic order has already appeared as

\[
\operatorname{Pic}(X_m)=\mathbb Z/(m-2),
\]

as the derivative transition

\[
E=-t^{m-2}D,
\]

and as the spectral canonical/ramification class

\[
K_{Z_m}=O(m-2).
\]

They are the same projective root-derivative character in different languages.

## Why higher nonlinear Keller slices return to the cubic frame

The canonical higher families force excess derivative vanishing at infinity of order `m-3`. Removing that forced factor changes the effective exponent from

\[
(m-2)-(m-3)=1.
\]

Equivalently the normalized transition becomes `Etilde=-tD`, and the root/derivative normalization becomes linear again, exactly as in the cubic case.

Hence one calculation gives the trichotomy

\[
\boxed{
\begin{array}{ccl}
m=2&:&\text{derivative character cannot be normalized}\Rightarrow\text{unit obstruction},\\
m=3&:&\text{weight one}\Rightarrow\text{canonical }SL_2\text{ root frame},\\
m>3&:&\text{weight }m-2\Rightarrow\mu_{m-2}\text{ torsor / Picard twisting},\\
&&\text{higher Keller slices subtract }m-3\text{ at infinity and return to weight one.}
\end{array}}
\]

This unifies the generic-degree-two obstruction, cubic canonicity, universal higher-degree Picard torsion, spectral canonical class, and the common cubic normalization skeleton of the entire higher minimal hierarchy.

Exact certificate: `scripts/jacobian_root_derivative_scaling_trichotomy_verify.py`, SHA-256 `88edfffb8f8b0e2b3034222b22143cf183c3578473e86dbadd6cdb080de429bc`.
