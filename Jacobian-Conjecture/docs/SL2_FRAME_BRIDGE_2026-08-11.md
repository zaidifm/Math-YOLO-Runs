# Bridge between the BLIND 4 cubic frame and the boundary SL2 frame

**Date:** 2026-08-11  
**Status:** exact identities COMPUTED in the current audit; structural interpretation is current-run synthesis and must not be back-attributed to BLIND 4.

The earlier BLIND 4 normalized-gradient calculation and the later boundary-quotient calculation contain two `SL_2` matrices. They are not unrelated occurrences.

Define the elementary family

\[
\boxed{
J_t=
\begin{pmatrix}
1&x\\
ty&1+txy
\end{pmatrix}\in SL_2.
}
\]

## BLIND 4 frame = `J_1^{-1}`

Let

\[
u=1+xy.
\]

Then

\[
J_1^{-1}=
\begin{pmatrix}u&-x\\-y&1\end{pmatrix},
\]

which is exactly the BLIND 4 change of binary variables

\[
\ell=uX-xW,
\qquad
m=W-yX.
\]

The selected root vector `(x,u)` is the second column of `J_1`, so `J_1^{-1}` sends it to `(0,1)`.

## Boundary frame = lower shear of `J_2^{-1}` followed by Weyl

Put

\[
v=1+2xy,
\qquad
p=3y+xz,
\]

and

\[
n_-(p)=\begin{pmatrix}1&0\\p&1\end{pmatrix},
\qquad
w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Then the boundary matrix

\[
G=\begin{pmatrix}x&v\\L&K\end{pmatrix}
\]

satisfies the exact factorization

\[
\boxed{G=n_-(p)J_2^{-1}w.}
\]

Indeed

\[
L=xp-1,
\qquad
K=vp-2y.
\]

So the BLIND 4 root frame and the boundary frame are the `t=1` and `t=2` members of the same elementary source family, with the boundary frame adding one lower-unipotent shear and the Weyl element.

## Exact bridge to the counterexample binary cubic

The BLIND 4 quadratic-factor coefficients can be written

\[
\boxed{
\beta=3(up-2y),
\qquad
x\alpha=\beta-p.
}
\]

With `(\ell,m)=J_1^{-1}(X,W)`, exact expansion gives

\[
\boxed{
\ell(2m^2+\beta\ell m+\alpha\ell^2)
=2F_1X^3-F_2X^2W+2XW^2-F_3W^3,
}
\]

where `(F_1,F_2,F_3)` are the coordinates of the explicit Jacobian counterexample.

At the selected root `(X,W)=(x,u)`, `(\ell,m)=(0,1)`. The gradient in `(\ell,m)` coordinates is therefore `(2,0)`, and the chain rule gives

\[
\boxed{\nabla P_F(x,u)=2(u,-x).}
\]

Thus the BLIND 4 normalized-gradient identity is an immediate consequence of the `J_1^{-1}` root frame.

The third output also becomes

\[
\boxed{F_3=x(1-L).}
\]

## Verification

Exact script:

- `scripts/jacobian_blind4_sl2_bridge_verify.py`

Recorded output:

- `verification/jacobian_blind4_sl2_bridge_verify_2026-08-11.txt`

This resolves the first structural question left open by `SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`: the BLIND 4 binary-cubic `SL_2` and the boundary `SL_2/T` picture are adjacent pieces of the same source geometry.
