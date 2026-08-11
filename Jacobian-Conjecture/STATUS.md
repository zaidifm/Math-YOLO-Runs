# STATUS — Jacobian Conjecture Research

**Checkpoint:** 2026-08-11

## Verified/computed frontier

### Boundary coordinates

Using the reciprocal chart

\[
X=x^{-1},\qquad a=2y+X=\frac{1+2xy}{x},\qquad W=-x+3x^2y+x^3z,
\]

define

\[
b=1+aW,\qquad c=ab.
\]

Exact symbolic algebra gives

\[
b=xK,\qquad c=(1+2xy)K,
\]

for

\[
K=y+6xy^2+xz+2x^2yz,
\]

and therefore

\[
\boxed{cW=b(b-1)}.
\]

### Candidate intersection theorem

The archived BLIND 2 theorem is

\[
\boxed{k[a,W]\cap k[x,y,z]
= k[W,b,c]/(cW-b(b-1)).}
\]

The current reconstruction identifies the right-hand side as a smooth Danielewski surface. A valuation/normality proof has been reconstructed and no defect has been found. Bounded exact intersection tests also pass. This remains **provisionally VERIFIED internally**, pending independent specialist/CAS/formal review.

### Degree filtration

For normal-form monomials,

\[
\deg(b^sW^j)=5s+4j,\qquad \deg_D(b^sW^j)=s,
\]

\[
\deg(b^sc^r)=5s+6r,\qquad \deg_D(b^sc^r)=s+2r.
\]

The predicted minimum source degree at hidden degree \(m\) is

\[
\boxed{\delta(m)=\begin{cases}3m,&m\text{ even},\\3m+2,&m\text{ odd}.
\end{cases}}
\]

so \(\delta(5)=17\).

### Canonical-potential degree-17 result

Inside the fixed reciprocal chart and canonical-potential deformation class,

\[
D\le16\implies \deg_a g\le4,
\]

while at degree 17 a unique hidden-degree-5 direction appears:

\[
\boxed{g_*=a^2(1+aW)^3=a^2b^3.}
\]

An independent exact rational-linear-algebra search reproduces rank 0 at degree 16 and rank 1 at degree 17 with coefficient pattern \((1,3,3,1)\).

This is **not** a global minimality result for all Keller maps.

### BLIND 4 two-jet criterion

For

\[
h=a^2H(t),\qquad t=aW,
\]

polynomialization in the stated family is equivalent to

\[
H(-1)=0,\quad H'(-1)=1,\quad H''(-1)=0,
\]

or

\[
\boxed{H(t)=1+t+(1+t)^3R(t).}
\]

The current synthesis shows this is a one-variable slice of the boundary ring because

\[
a^2(1+aW)^3R(aW)=bc^2R(b-1).
\]

### Locally nilpotent derivation

The hidden derivative extends to

\[
D(W)=0,\qquad D(b)=W,\qquad D(c)=2b-1,
\]

and preserves \(cW-b(b-1)\). The current audit identifies this as a locally nilpotent derivation, making the hidden \(a\)-degree an intrinsic filtration on the Danielewski surface.

### Normalized gradient

The BLIND 4 binary-cubic factorization and normalized-gradient identity pass exact symbolic checks. Current assessment: mathematically correct but probably not novel in substance, because it is a differential restatement of the public resultant normalization.

## Public-source acquisition state

The source-level public corpus required for the next comparison is now acquired and hash-pinned:

- Kistner–Shaska arXiv `2608.02863` original source bundle, SHA-256 `3f31ed51b3589cc41ba51aa140632fcaff74da92fa85442492d96069583994ce`;
- Shaska arXiv `2607.20210` original source bundle, SHA-256 `abf541b7e211d5ef0b14145ddb303f0cc34cb959fa7bec17f9efac1f6e3eadc9`;
- Zenodo record `10.5281/zenodo.21514514` metadata plus its sole attached file.

The Kistner–Shaska source bundle contains only five TeX/metadata files and does **not** contain the cited `balanced_minimal_models_companion.pdf`. The arXiv format page exposes no ancillary-download entry, the canonical ancillary candidate returned HTTP 404, and no retained local copy was found by the acquisition courier. Current status: **NOT PUBLICLY LOCATED**.

This is now a fixed literature-coverage caveat, not an uncompleted courier task.

## Public-overlap assessment

Already substantially public:

- generic cubic recovery / degree-three fiber;
- \(S_3\) monodromy;
- nonproperness and sheets escaping to infinity;
- tangent-sweep construction;
- counterexamples in all dimensions \(>2\);
- arbitrarily large generic fiber degree;
- graded quotient/lift frameworks and branch-curve semigroups.

Not yet matched by an indexed public statement found in the current audit:

- the exact intersection ring above;
- its exact source-degree/hidden-degree filtration;
- the cross-BLIND explanation of the two-jet criterion via the intersection ring.

Chart-relative degree-17 minimality remains subject to a priority caveat because the cited Kistner–Shaska companion is presently unavailable for inspection. Absence of that artifact is not evidence that it lacks an overlapping theorem.

## Remaining blocking obligations

1. Complete the theorem-by-theorem comparison against the acquired `2607.20210` and `2608.02863` source texts and the public verification trail.
2. Run an independent non-SymPy CAS audit (Sage/Singular/Macaulay2 preferred).
3. Obtain external algebraic-geometry review of the normality/divisorial-valuation proof.
4. Only after 1–3 decide whether a publication-quality note is justified and what novelty language, if any, is supportable.

Additional raw BLIND provenance is **not** an open obligation. The owner has confirmed that the surviving archive is the complete available corpus.

## Do not overclaim

Until those obligations are closed, phrases such as “new theorem,” “first proof,” or “unpublished discovery” should be treated as provisional research hypotheses, not public conclusions.
