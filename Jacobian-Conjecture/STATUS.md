# STATUS — Jacobian Conjecture Research

**Checkpoint:** 2026-08-11

## Current frontier

The 2026-08-11 blackboard pass reorganized the earlier boundary-ring, LND, jet, and degree-17 observations around one exact source object.

Set

\[
v=1+2xy,\qquad
L=-1+3xy+x^2z,\qquad
K=y+6xy^2+xz+2x^2yz.
\]

Then

\[
\boxed{xK-vL=1},
\]

so

\[
\boxed{G=\begin{pmatrix}x&v\\L&K\end{pmatrix}\in SL_2.}
\]

The determinant identity and the exact elementary factorization of `G` are **COMPUTED**.

### Boundary ring = torus quotient

Under row rescaling by the diagonal torus, the invariant matrix products are

\[
W=xL,\qquad b=xK,\qquad b-1=vL,\qquad c=vK.
\]

Hence

\[
\boxed{R\cong k[W,b,c]/(cW-b(b-1))}
\]

is the affine torus quotient of the displayed `SL_2` model. On `x!=0`, torus normalization gives

\[
\begin{pmatrix}1&a\\W&b\end{pmatrix},
\qquad a=v/x,
\]

so determinant one forces the old shifted relation

\[
\boxed{b=1+aW}.
\]

The hidden `(a,W)` plane is the quotient big cell. The shift is structural, not accidental.

### Discriminant-one quadric and full `sl_2`

With `q=2b-1`,

\[
\boxed{q^2-4cW=1}.
\]

The earlier hidden derivative is one root operator in the exact `sl_2` triple

\[
e(W)=0,\ e(q)=2W,\ e(c)=q,
\]

\[
f(W)=q,\ f(q)=2c,\ f(c)=0,
\]

with `h=[e,f]` and

\[
[e,f]=h,\qquad [h,e]=2e,\qquad [h,f]=-2f.
\]

These identities and commutators are **COMPUTED** exactly.

### Strengthened intersection theorem

The archived BLIND 2 theorem is

\[
\boxed{k[a,W]\cap k[x,y,z]=R.}
\]

The new determinant identity gives the exact ideal pullback

\[
(W,b)k[x,y,z]=(xL,xK)=x(L,K)=(x),
\]

because `xK-vL=1` implies `(L,K)=(1)`.

Thus the missing boundary divisor pulls back scheme-theoretically to `x=0` with multiplicity one. Combined with the quotient big cell and normality of the smooth quadric, this gives a direct divisorial proof of the intersection equality.

**Status:** supporting identities **COMPUTED**; general divisorial proof **DERIVED**, internally stress-tested, not yet independently specialist/formally reviewed.

### Associated graded = second Veronese / `A_1` cone

The source total degrees are

\[
\deg W=4,\qquad \deg b=5,\qquad \deg c=6,
\]

with top forms

\[
x^3z,\qquad 2x^3yz,\qquad 4x^3y^2z.
\]

Therefore

\[
\boxed{\operatorname{gr}R\cong
k[\bar W,\bar b,\bar c]/(\bar c\bar W-\bar b^2)
\cong k[s^2,st,t^2].}
\]

Use `deg(s)=2`, `deg(t)=3`; hidden `a`-degree is the exponent of `t`. The old ring-filtration law

\[
\boxed{\delta_R(m)=
\begin{cases}3m,&m\text{ even},\\3m+2,&m\text{ odd}
\end{cases}}
\]

is exactly the parity condition of the second Veronese. A compatible weighted Rees form is

\[
Q^2-4CW=T^{10},
\]

which degenerates the smooth discriminant-one quadric to the `A_1` cone.

### Complete fixed-chart canonical-potential classification

For the base potential

\[
h_0=a^2+Wa^3=a^2(1+aW),
\]

write `h=h0+g`. Polynomial outputs require

\[
g_a\in R,\qquad ag_a-g\in R.
\]

A complete diagonal analysis in `a^iW^j`, using the boundary valuation, gives

\[
\boxed{h=h_0+\alpha a+\beta+r,
\qquad r\in I_D=(W,b)\subset R.}
\]

The `\alpha a` and `\beta` terms are target translations. Modulo translations, the polynomializable deformation space is exactly the ideal of the missing boundary line.

This **DERIVED** statement strictly generalizes the BLIND 4 slice. The old two-jet condition

\[
H(t)=1+t+(1+t)^3R(t)
\]

is the `d=2` boundary-divisibility case.

### Sharp degree spectra and degree 17

For hidden degree `m`, the boundary ideal becomes `(s^2,st)` in the associated graded model. Minimizing the degree of the **pulled-back potential representative** gives

\[
\boxed{\mu_{\mathrm{pot}}(m)=
\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even},
\end{cases}\qquad m\ge1.}
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
\boxed{g_5=bc^2=a^2(1+aW)^3,\qquad \mu_{\mathrm{pot}}(5)=17.}
\]

The coefficient pattern `(1,3,3,1)` is the binomial expansion of the unique minimal boundary-ideal weight vector.

The potential degree and induced output-change degree agree for every `m>=2`. There is one low-degree cancellation exception:

\[
g_1=b,\qquad \deg(g_1\text{ after pullback})=5,
\]

but

\[
g_{1,a}=W,\qquad ag_{1,a}-g_1=-1,
\]

so its output change has degree 4. Thus if `\nu(m)` is the sharp output-change degree,

\[
\boxed{\nu(1)=4,\qquad \nu(m)=\mu_{\mathrm{pot}}(m)\quad(m\ge2).}
\]

This correction does not affect the degree-17 theorem or any threshold used for hidden degree at least two.

A second refinement is

\[
\delta_R(4)=12\quad\text{but}\quad \mu_{\mathrm{pot}}(4)=16,
\]

because `c^2` is ring-minimal but not an admissible canonical-potential deformation; the minimal admissible direction is `b^2c`.

### Closed bounded kernel

Modulo the two translation gauges, the predicted output-degree basis is

- `W^j`, `j>=1`: degree `4j`;
- `bW^j`, `j>=0`: degree `4j+4`;
- `b^sW^j`, `s>=2,j>=0`: degree `5s+4j`;
- `b^sc^r`, `s>=1,r>=1`: degree `5s+6r`.

Hence

\[
\boxed{H(q)=2+\frac{2q^4}{1-q^4}
+\frac{q^{10}}{(1-q^4)(1-q^5)}
+\frac{q^{11}}{(1-q^5)(1-q^6)}.}
\]

An exact SymPy reconstruction of the original coefficient-constraint matrices matched the predicted cumulative nullity for **all 18 bounds `D=3,...,20`**. At `D=16` the nullity is 15; at `D=17` it is 16, with exactly one new direction, `bc^2`.

## Durable artifacts

- `docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`
- `scripts/jacobian_blackboard_quadric_verify.py`
- `verification/jacobian_blackboard_quadric_verify_2026-08-11.txt`
- `verification/Jacobian_Canonical_Kernel_Exact_Validation_2026-08-11.txt`

The verifier checks the determinant/exchange identity, matrix factorization, quotient big cell, discriminant-one equation, `sl_2` commutators, leading forms, and minimal representatives through hidden degree 12.

## Public-source state

The source-level public corpus is acquired and hash-pinned. The cited Kistner–Shaska `balanced_minimal_models_companion.pdf` is absent from the deposited arXiv bundle and was **NOT PUBLICLY LOCATED** by bounded acquisition checks. This is a literature-coverage caveat, not evidence of non-overlap.

## Epistemic / priority state

No novelty or priority claim is made for the `SL_2/T`, quadric, classification, spectrum, or Hilbert-series synthesis.

Exact symbolic identities and finite matrix comparisons are **COMPUTED**. The general intersection/classification/spectrum arguments are **DERIVED** and require an independent second route plus specialist/formal review.

## Remaining blocking obligations

1. Independently rederive or formally check the general intersection/classification argument, preferably by a route orthogonal to SymPy.
2. Obtain external algebraic-geometry review of the quotient/divisor argument.
3. Compare the acquired public source texts theorem-by-theorem against this strengthened formulation, carrying the unavailable companion as an explicit limitation.
4. Only then decide whether a publication-quality note and any novelty language are supportable.

Additional raw BLIND provenance is **not** an open obligation.
