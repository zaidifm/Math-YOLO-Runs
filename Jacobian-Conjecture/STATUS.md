# STATUS — Jacobian Conjecture Research

**Checkpoint:** 2026-08-11 blackboard frontier

## 1. Hidden source geometry

Set

\[
v=1+2xy,\qquad L=-1+3xy+x^2z,\qquad K=y+6xy^2+xz+2x^2yz.
\]

Exact symbolic algebra gives

\[
\boxed{xK-vL=1},
\]

hence

\[
\boxed{G=\begin{pmatrix}x&v\\L&K\end{pmatrix}\in SL_2.}
\]

With torus row scaling, the invariant matrix products are

\[
W=xL,\qquad b=xK,\qquad b-1=vL,\qquad c=vK.
\]

Therefore the BLIND 2 boundary ring is the affine torus quotient

\[
\boxed{R=k[W,b,c]/(cW-b(b-1)).}
\]

On the quotient big cell, torus normalization gives

\[
\begin{pmatrix}1&a\\W&b\end{pmatrix}
\]

and determinant one forces

\[
\boxed{b=1+aW}.
\]

With `q=2b-1`,

\[
\boxed{q^2-4cW=1},
\]

and the earlier hidden LND extends to a full exact `sl_2` triple.

**Status:** matrix identities, factorization, quotient invariants, quadric equation, and `sl_2` commutators are **COMPUTED** exactly.

## 2. Strengthened intersection theorem

The archived BLIND 2 theorem is

\[
\boxed{k[a,W]\cap k[x,y,z]=R.}
\]

The new determinant identity gives

\[
(W,b)k[x,y,z]=(xL,xK)=x(L,K)=(x),
\]

because `xK-vL=1` implies `(L,K)=(1)`.

Thus the missing boundary divisor pulls back scheme-theoretically to `x=0` with multiplicity one. Together with the quotient big cell and normality of the smooth quadric, this gives a direct divisorial proof of the intersection equality.

**Status:** exact ideal identity **COMPUTED**; general divisorial theorem **DERIVED**, internally stress-tested, awaiting independent specialist/formal review.

## 3. Associated graded and degree law

The source degrees are

\[
\deg W=4,\qquad\deg b=5,\qquad\deg c=6,
\]

and

\[
\boxed{\operatorname{gr}R\cong
k[\bar W,\bar b,\bar c]/(\bar c\bar W-\bar b^2)
\cong k[s^2,st,t^2].}
\]

Thus the total-degree degeneration is the second Veronese / `A_1` cone. With `deg(s)=2`, `deg(t)=3`, hidden `a`-degree is the exponent of `t`, and

\[
\boxed{\delta_R(m)=
\begin{cases}3m,&m\text{ even},\\3m+2,&m\text{ odd}.
\end{cases}}
\]

The old parity defect is the sign-invariance constraint.

## 4. Complete fixed-chart canonical-potential classification

For

\[
h_0=a^2(1+aW),
\]

write `h=h0+g`. Polynomial outputs require

\[
g_a\in R,\qquad ag_a-g\in R.
\]

Diagonal decomposition plus the boundary valuation gives

\[
\boxed{h=h_0+\alpha a+\beta+r,\qquad r\in I_D=(W,b)\subset R.}
\]

The `alpha*a` and `beta` terms are target translations. Modulo translations, the whole polynomializable deformation space is the ideal of the missing boundary line.

This strictly generalizes BLIND 4's two-jet slice.

The unique minimal direction at hidden degree `m` is

\[
g_{2r+1}=bc^r=a^r(1+aW)^{r+1},
\]

\[
g_{2r}=b^2c^{r-1}=a^{r-1}(1+aW)^{r+1}.
\]

For `m>=2`, its sharp output-degree threshold is

\[
\boxed{D_m=
\begin{cases}3m+2,&m\text{ odd},\\3m+4,&m\text{ even}.
\end{cases}}
\]

In particular

\[
\boxed{g_5=bc^2=a^2(1+aW)^3,\qquad D_5=17.}
\]

The old `(1,3,3,1)` vector is the binomial expansion of this unique minimal boundary-ideal vector.

An exact reconstruction of the original coefficient matrices matched the classification at every degree bound `D=3,...,20`.

## 5. BLIND 4 and boundary `SL_2` are the same source family

Define

\[
J_t=\begin{pmatrix}1&x\\ty&1+txy\end{pmatrix}\in SL_2.
\]

The BLIND 4 binary-cubic root frame is exactly `J_1^{-1}`.

If `p=3y+xz`, `n_-(p)=[[1,0],[p,1]]`, and `w=[[0,1],[-1,0]]`, then the boundary matrix satisfies

\[
\boxed{G=n_-(p)J_2^{-1}w.}
\]

Thus the normalized-gradient and boundary-quotient pictures are adjacent members of the same elementary `SL_2` source geometry, not unrelated appearances of the group.

The exact binary-cubic coefficient expansion and normalized gradient are independently checked in `scripts/jacobian_blind4_sl2_bridge_verify.py`.

## 6. Quintic scalar line: exact surjectivity classification

Consider

\[
h_{5,\lambda}=h_0+\lambda a^2(1+aW)^3.
\]

For `lambda!=0`, the resulting map has

\[
\det J=1,\qquad(\deg S,\deg U,\deg W)=(17,16,4),
\]

and generic fiber degree five.

For target `w!=0`, setting `t=wa` gives the recovery quintic

\[
P_\lambda(t)=
\lambda t^5+3\lambda t^4+(1+3\lambda)t^3+(1+\lambda)t^2-uwt+2sw^2.
\]

A target is missed iff every recovery root is multiple. Exact squareful elimination gives

\[
\boxed{27\lambda^2+99\lambda+5=0}
\]

as the complete nonzero exceptional condition.

Hence

\[
\boxed{\lambda_\pm=\frac{-33\pm7\sqrt{21}}{18}}
\]

are the only two bad nonzero coefficients. Constructive omitted targets are recorded for both.

Every other nonzero `lambda` gives a **surjective, noninjective** degree-`(17,16,4)` Keller map of generic fiber degree five.

At `lambda=0`, the recovery degree drops to three and an explicit omitted curve is recovered.

## 7. All minimal directions: surjectivity for every m >= 6

For the unique minimal direction write

\[
g_m=a^d(1+aW)^e,\qquad d+e=m,
\]

with `e-d=1` for odd `m` and `e-d=2` for even `m`.

For every `lambda!=0`, these directions polynomialize directly and the canonical Jacobian identity gives

\[
\boxed{\det JF_{m,\lambda}=1.}
\]

For target `w!=0`, every recovery polynomial normalizes to

\[
\boxed{P(t)=t^d(1+t)^e+\kappa t^2(1+t)+pt+q,\qquad\kappa\ne0.}
\]

For `m>=9`, two independent blackboard proofs exclude a squareful `P`:

1. a logarithmic-derivative pole-count argument;
2. a Newton-identity/Vandermonde moment argument.

The low cases `m=6,7,8` are closed by exact coefficient classifications.

Therefore

\[
\boxed{
\text{for every }m\ge6\text{ and every }\lambda\in\mathbb C^\times,
F_{m,\lambda}\text{ is surjective.}
}
\]

For generic targets it has `m` simple recovery roots, so

\[
\boxed{\deg_{gen}F_{m,\lambda}=m.}
\]

These are surjective, noninjective Keller maps with degree profile

\[
\boxed{(D_m,D_m-1,4)}.
\]

## 8. Complete nonzero-scalar phase diagram

Exact low-degree factorizations close the remaining cases:

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

Degree five is the bifurcation layer. The squareful recovery stratum meets its scalar line at exactly two nonzero coefficients; at degree six that intersection disappears and never returns.

## 9. Internal comparison with BLIND 1

BLIND 1 had already produced a different surjective noninjective family for every generic degree `m>=6`, with degree profile

\[
(5m,5m-1,4).
\]

Its `m=5` member was nonsurjective and the report explicitly left open whether another generic-degree-five deformation could be surjective.

The current result sharpens that surviving project record:

- minimal directions reduce the profile to `(D_m,D_m-1,4)` with `D_m<5m` for every `m>=6`;
- the boundary filtration explains why these are degree-minimal inside the fixed canonical chart;
- and the quintic scalar classification resolves the retained project's degree-five question positively.

This is an internal project-provenance comparison, not an external literature-priority claim.

## 10. Durable artifacts

Core structural notes:

- `docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`
- `docs/SL2_FRAME_BRIDGE_2026-08-11.md`
- `docs/QUINTIC_LAMBDA_SURJECTIVITY_2026-08-11.md`
- `docs/MINIMAL_DIRECTION_SURJECTIVITY_2026-08-11.md`
- `docs/MINIMAL_DIRECTION_SURJECTIVITY_SECOND_PROOF_2026-08-11.md`
- `docs/MINIMAL_SCALAR_SURJECTIVITY_PHASE_2026-08-11.md`

Exact scripts and outputs are under `scripts/` and `verification/` with matching names.

## 11. Epistemic / priority state

No external novelty or priority claim is made.

The main exact identities, low-degree factorization/elimination certificates, bounded-kernel calculations, and concrete witness formulas are **COMPUTED**.

The general quotient/intersection/classification theorems and all-degree surjectivity argument are **DERIVED**, with several independent internal routes, but still require external algebraic-geometry/formal review before promotion to publication-level VERIFIED status.

The unavailable Kistner-Shaska `balanced_minimal_models_companion.pdf` remains a literature-coverage caveat.

Additional raw BLIND provenance is **not** an open acquisition task.
