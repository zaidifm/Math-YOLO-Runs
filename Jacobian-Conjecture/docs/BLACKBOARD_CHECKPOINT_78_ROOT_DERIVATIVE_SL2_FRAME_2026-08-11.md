# Blackboard checkpoint 78 — `SL_2` is the normalized spectral root-derivative frame

**Date:** 2026-08-11  
**Status:** identities COMPUTED exactly; interpretation DERIVED. No external priority claim.

In the infinity root chart of the primitive cubic, let

\[
\Psi(t)=W+t-Ut^2+2St^3,
\qquad
D=\Psi_t=1-2Ut+6St^2.
\]

The normalized infinity strict transform gives

\[
c=U-2St,
\qquad b=tc.
\]

Define

\[
\boxed{
G_{spectral}=
\begin{pmatrix}
 t/D & 1/D\\
 D(tc-1) & Dc
\end{pmatrix}.}
\]

Its determinant is identically one:

\[
\det G_{spectral}=tc-(tc-1)=1.
\]

On the polynomial source, exact substitution gives

\[
t=x/v,
\qquad D=1/v,
\qquad c=vK,
\qquad b=xK,
\]
with `v=1+2xy`. Hence

\[
t/D=x,
\quad 1/D=v,
\quad D(tc-1)=L,
\quad Dc=K,
\]
so

\[
\boxed{
G_{spectral}=
\begin{pmatrix}x&v\\L&K\end{pmatrix}.}
\]

Thus the hidden determinant-one source matrix is not an independently guessed group structure. It is exactly the normalized frame attached to:

1. a simple projective recovery root `t`;
2. its derivative `D`;
3. the normalized boundary coordinate `c`.

The identity `xK-vL=1` is therefore tautological from the spectral frame. The earlier BLIND4 normalized-gradient calculation is another coordinate expression of this same root/derivative geometry.

Exact certificate: `scripts/jacobian_spectral_root_derivative_sl2_frame_verify.py`, SHA-256 `72c06e9f745afecd1b28f40182ec94eca3fbfbf56d6a0d2bcfded79f28b5d81d`.
