# Minimal scalar directions: complete surjectivity phase diagram

**Date:** 2026-08-11  
**Status:** current-run blackboard synthesis. Exact low-degree factorization certificates plus the companion quintic/all-degree proofs. Independent specialist/formal review remains outstanding.  
**Scope:** fixed reciprocal-chart canonical-potential scalar lines.

For each hidden degree `m>=3`, let `g_m` be the unique minimal boundary-ideal direction and consider

\[
h_{m,\lambda}=h_0+\lambda g_m,\qquad\lambda\ne0.
\]

## m=4: every nonzero scalar is nonsurjective

Here `g_4=ab^3`. For `w!=0`, put

\[
\kappa=1/(\lambda w).
\]

The normalized recovery quartic is

\[
P_4=t(1+t)^3+\kappa t^2(1+t)+pt+q.
\]

Set

\[
C=3+\kappa,\qquad A=C/2,\qquad B=C(1-\kappa)/8,
\]

and choose

\[
p=CB-1,\qquad q=B^2.
\]

Then exactly

\[
\boxed{P_4=(t^2+At+B)^2.}
\]

So every root is multiple and the corresponding target is omitted. This works for every fixed `lambda!=0` and every chosen `w!=0` after translating `p,q` back to target coordinates.

Thus every nonzero `m=4` scalar map is nonsurjective. Its degree profile is `(16,15,4)` and generic recovery degree is four.

## m=3: every nonzero scalar is nonsurjective

Here `g_3=ab^2`. The normalized recovery cubic is

\[
P_3=t(1+t)^2+\kappa t^2(1+t)+pt+q,
\qquad\kappa=1/(\lambda w).
\]

For `kappa!=-1`, put

\[
r=-(2+\kappa)/(3(1+\kappa)),
\]

\[
p=3(1+\kappa)r^2-1,
\qquad q=-(1+\kappa)r^3.
\]

Then

\[
\boxed{P_3=(1+\kappa)(t-r)^3.}
\]

For every fixed nonzero `lambda` one can choose `w!=0` with `kappa!=-1`. Hence every nonzero `m=3` scalar map is nonsurjective.

## m=5: exactly two exceptional nonzero coefficients

The exact quintic classification gives

\[
F_{5,\lambda}\text{ nonsurjective}
\iff
27\lambda^2+99\lambda+5=0
\]

for `lambda!=0`.

Thus the only bad nonzero values are

\[
\lambda_\pm=(-33\pm7\sqrt{21})/18.
\]

Every other nonzero scalar gives a surjective, noninjective degree-`(17,16,4)` Keller map of generic fiber degree five.

## m >= 6: every nonzero scalar is surjective

The minimal-direction theorem proves

\[
\boxed{m\ge6,\ \lambda\ne0\Longrightarrow F_{m,\lambda}\text{ surjective}.}
\]

Each map has determinant one, generic fiber degree `m`, and degree profile

\[
(D_m,D_m-1,4),
\qquad
D_m=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}
\]

## Phase diagram

\[
\boxed{
\begin{array}{c|c}
\text{hidden/generic degree}&\text{surjectivity for }\lambda\ne0\\
\hline
m=3&\text{never}\\
m=4&\text{never}\\
m=5&\text{except at two algebraic }\lambda\\
m\ge6&\text{always}
\end{array}}
\]

The degree-five line is the bifurcation layer. Its squareful recovery stratum meets the scalar line at exactly two nonzero coefficients. At degree six that intersection disappears and, by the high-degree rigidity argument, never returns.

## Internal project comparison

The retained BLIND 1 monomial family already gave surjective noninjective maps for every generic degree `m>=6`, but with degree profile `(5m,5m-1,4)`, and its `m=5` member was nonsurjective. The BLIND 1 report explicitly left open whether a different generic-degree-five deformation could be surjective.

The current boundary-minimal family:

- lowers the degree profile to `(D_m,D_m-1,4)`;
- is minimal inside the fixed canonical chart by the boundary-ideal filtration;
- and resolves the retained project's degree-five question affirmatively.

This is an internal provenance comparison, not an external literature-priority claim.

## Verification

- `scripts/jacobian_minimal_scalar_phase_verify.py`
- `verification/jacobian_minimal_scalar_phase_verify_2026-08-11.txt`
- `docs/QUINTIC_LAMBDA_SURJECTIVITY_2026-08-11.md`
- `docs/MINIMAL_DIRECTION_SURJECTIVITY_2026-08-11.md`
- `docs/MINIMAL_DIRECTION_SURJECTIVITY_SECOND_PROOF_2026-08-11.md`
