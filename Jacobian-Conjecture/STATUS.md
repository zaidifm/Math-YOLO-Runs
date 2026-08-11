# STATUS — Jacobian Conjecture Research

**Checkpoint:** 2026-08-11

## Current mathematical frontier

The 2026-08-11 blackboard pass reorganized the previously separate boundary-ring, LND, jet, and degree-17 observations around a single exact structure: an `SL_2` matrix in the original source variables.

Set

\[
v=1+2xy,\qquad
L=-1+3xy+x^2z,\qquad
K=y+6xy^2+xz+2x^2yz.
\]

Then exact symbolic algebra gives

\[
\boxed{xK-vL=1},
\]

so

\[
G=\begin{pmatrix}x&v\\L&K\end{pmatrix}\in SL_2.
\]

The matrix has the exact factorization

\[
G=
\begin{pmatrix}1&0\\3y+xz&1\end{pmatrix}
\begin{pmatrix}x&1\\-1&0\end{pmatrix}
\begin{pmatrix}1&2y\\0&1\end{pmatrix}.
\]

These statements are **COMPUTED** exactly.

### Boundary ring as a torus quotient

Let the diagonal torus act by row rescaling

\[
t\cdot(x,v,L,K)=(tx,tv,t^{-1}L,t^{-1}K).
\]

The invariant matrix products are

\[
W=xL,\qquad b=xK,\qquad b-1=vL,\qquad c=vK,
\]

and therefore

\[
\boxed{R\cong k[W,b,c]/(cW-b(b-1)).}
\]

Geometrically this is the affine torus quotient of `SL_2` (left quotient in the displayed convention; equivalent to `SL_2/T` after inversion).

On `x\ne0`, torus-normalizing the first matrix entry gives

\[
\operatorname{diag}(1/x,x)G=
\begin{pmatrix}1&a\\W&b\end{pmatrix},
\qquad a=v/x,
\]

and determinant one forces

\[
\boxed{b=1+aW}.
\]

Thus the old shifted variable is the determinant-one exchange relation on the big quotient cell, rather than an unexplained pole-cancellation trick.

### Discriminant-one quadric and `sl_2`

Put

\[
q=2b-1.
\]

Then

\[
\boxed{q^2-4cW=1}.
\]

Equivalently,

\[
(xU+vV)(LU+KV)=WU^2+qUV+cV^2,
\]

whose discriminant is `(xK-vL)^2=1`.

The old hidden derivative is one root operator in a full `sl_2` action:

\[
e(W)=0,\quad e(q)=2W,\quad e(c)=q,
\]

\[
f(W)=q,\quad f(q)=2c,\quad f(c)=0,
\]

and with `h=[e,f]`,

\[
h(W)=2W,\quad h(q)=0,\quad h(c)=-2c.
\]

Exact symbolic checks verify

\[
[e,f]=h,\qquad [h,e]=2e,\qquad [h,f]=-2f.
\]

### Strengthened intersection theorem

The archived BLIND 2 theorem is

\[
\boxed{k[a,W]\cap k[x,y,z]=R.}
\]

The new `SL_2` identity tightens its proof. If `D` is the missing boundary line with ideal

\[
I_D=(W,b),
\]

then in `k[x,y,z]`

\[
(W,b)=(xL,xK)=x(L,K).
\]

Since `xK-vL=1`, `(L,K)=(1)`, hence scheme-theoretically

\[
\boxed{(W,b)k[x,y,z]=(x).}
\]

So the boundary divisor pulls back exactly to `x=0` with multiplicity one. Together with the big-cell description and normality of the smooth quadric, this gives a direct divisorial proof of the intersection equality.

**Status:** the supporting identities are **COMPUTED**; the general algebraic-geometric argument is **DERIVED** and has survived internal adversarial checking, but is not yet independently specialist/formally reviewed.

### Associated graded and the parity law

The actual total degrees are

\[
\deg W=4,\qquad \deg b=5,\qquad \deg c=6,
\]

with top homogeneous forms

\[
\operatorname{in}(W)=x^3z,\quad
\operatorname{in}(b)=2x^3yz,\quad
\operatorname{in}(c)=4x^3y^2z.
\]

Therefore

\[
\boxed{\operatorname{gr}R\cong
k[\bar W,\bar b,\bar c]/(\bar c\bar W-\bar b^2).}
\]

Equivalently,

\[
\operatorname{gr}R\cong k[s^2,st,t^2]=k[s,t]^{\{\pm1\}},
\]

with source weights `deg(s)=2`, `deg(t)=3`. Hidden `a`-degree is the exponent of `t`.

The earlier source-degree law

\[
\boxed{\delta_R(m)=
\begin{cases}
3m,&m\text{ even},\\
3m+2,&m\text{ odd}
\end{cases}}
\]

is consequently the parity constraint of the second Veronese: `s^r t^m` is invariant only when `r+m` is even. The mysterious `+2` for odd `m` is the cost of the smallest permitted `s` exponent.

A weighted Rees presentation is

\[
Q^2-4CW=T^{10},
\]

so the total-degree filtration degenerates the smooth discriminant-one quadric to the `A_1` quadric cone.

### Full fixed-chart canonical-potential classification

For the canonical construction with base potential

\[
h_0=a^2+Wa^3=a^2(1+aW),
\]

write `h=h0+g`. Polynomial outputs require both

\[
g_a\in R,\qquad ag_a-g\in R.
\]

A diagonal decomposition in monomials `a^iW^j` and the boundary valuation give the complete fixed-chart classification

\[
\boxed{
h=h_0+\alpha a+\beta+r,
\qquad r\in I_D=(W,b)\subset R.
}
\]

The `\alpha a` and `\beta` terms only translate target coordinates. Thus, modulo translations, the entire polynomializable canonical-potential deformation space is exactly the ideal of the missing boundary line.

This is **DERIVED**, not yet externally reviewed. It strictly generalizes the BLIND 4 slice. Intersecting with `h=a^2H(aW)` recovers

\[
H(t)=1+t+(1+t)^3R(t)
\]

as the `d=2` boundary-divisibility condition.

### Sharp deformation spectrum

In the associated graded model the boundary ideal becomes `(s^2,st)`. The classification predicts the sharp output-degree threshold at hidden degree `m>=1`:

\[
\boxed{\mu(m)=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}}
\]

Unique minimal representatives are

\[
g_{2r+1}=bc^r=a^r(1+aW)^{r+1},
\]

\[
g_{2r}=b^2c^{r-1}=a^{r-1}(1+aW)^{r+1}.
\]

In particular,

\[
\boxed{g_5=bc^2=a^2(1+aW)^3,\qquad \mu(5)=17.}
\]

The old `(1,3,3,1)` vector is therefore the binomial expansion of the unique minimal boundary-ideal weight vector. Degree 17 is no longer an isolated linear-algebra surprise.

A further correction/refinement is

\[
\delta_R(4)=12\quad\text{but}\quad \mu(4)=16,
\]

because the ring-minimal element `c^2` does not satisfy the canonical-potential boundary condition; the minimal admissible deformation is `b^2c`.

### Exact bounded-kernel validation

Modulo two translation gauges, the predicted canonical kernel has basis families

- `W^j`, `j>=1`, output degree `4j`;
- `bW^j`, `j>=0`, output degree `4j+4`;
- `b^sW^j`, `s>=2,j>=0`, output degree `5s+4j`;
- `b^sc^r`, `s>=1,r>=1`, output degree `5s+6r`.

Its Hilbert series is

\[
\boxed{
H(q)=2+\frac{2q^4}{1-q^4}
+\frac{q^{10}}{(1-q^4)(1-q^5)}
+\frac{q^{11}}{(1-q^5)(1-q^6)}.
}
\]

An exact SymPy reconstruction of the original coefficient-constraint matrices was run independently for every bound `D=3,...,20`. The predicted cumulative dimension matched exact nullity at all 18 bounds. At `D=16` the nullity is 15; at `D=17` it is 16, with exactly one new direction, `bc^2`.

## Verification artifacts

- `docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`
- `scripts/jacobian_blackboard_quadric_verify.py`
- `verification/jacobian_blackboard_quadric_verify_2026-08-11.txt`
- `verification/Jacobian_Canonical_Kernel_Exact_Validation_2026-08-11.txt`

The exact script checks the determinant/exchange identity, matrix factorization, quotient big cell, discriminant-one relation, `sl_2` commutators, leading forms, and minimal directions through hidden degree 12.

## Public-source acquisition state

The source-level public corpus is acquired and hash-pinned:

- Kistner–Shaska arXiv `2608.02863`, SHA-256 `3f31ed51b3589cc41ba51aa140632fcaff74da92fa85442492d96069583994ce`;
- Shaska arXiv `2607.20210`, SHA-256 `abf541b7e211d5ef0b14145ddb303f0cc34cb959fa7bec17f9efac1f6e3eadc9`;
- Zenodo record `10.5281/zenodo.21514514` metadata plus its sole attached file.

The Kistner–Shaska source does not contain the cited `balanced_minimal_models_companion.pdf`; bounded acquisition checks could not publicly locate it. This remains a fixed literature-coverage caveat, not an unfinished courier task.

## Priority / novelty status

No priority claim is made for the new `SL_2/T`, quadric, classification, spectrum, or Hilbert-series synthesis.

The unavailable Kistner–Shaska companion prevents completely closing overlap questions around differential obstructions/minimal models. Absence of that file is not evidence of absence of overlap.

## Remaining blocking obligations

1. Independently rederive or formally check the general intersection/classification argument, preferably with a non-SymPy CAS/formal route where applicable.
2. Obtain external algebraic-geometry review of the quotient/divisor argument and the canonical-potential classification.
3. Compare the acquired public source texts theorem-by-theorem against this strengthened formulation; carry the unavailable companion as an explicit limitation.
4. Only then decide whether a publication-quality note is justified and what novelty language, if any, is supportable.

Additional raw BLIND provenance is **not** an open obligation. The owner has confirmed the surviving archive is complete.

## Do not overclaim

The new structure is much stronger than the previous collection of coincidences, but the repository status discipline still applies: exact symbolic identities are not the same thing as independent theorem verification, and mathematical correctness is not the same thing as priority.
