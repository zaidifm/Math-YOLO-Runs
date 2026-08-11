# Jacobian Blind-Session Mathematical Forensics — 2026-08-11

## Scope

This memo reconstructs and independently checks the three most distinctive post-counterexample structures in the archived BLIND 2 / BLIND 4 work:

1. the BLIND 2 boundary/intersection ring;
2. the BLIND 2 degree filtration and chart-relative degree-17 minimality theorem;
3. the BLIND 4 finite-jet polynomialization criterion and normalized-gradient binary-cubic formulation.

The base counterexample, generic cubic recovery, escape to infinity, broad higher-degree families, and much of the graded/monodromy picture are now public. The focus here is the residue not obviously matched by indexed public papers as of 2026-08-11.

## 1. Hidden reciprocal chart

Use

\[
X=x^{-1},\qquad a=2y+X=\frac{1+2xy}{x},\qquad
W=-x+3x^2y+x^3z.
\]

Write

\[
v=1+2xy,\quad L=-1+3xy+x^2z,\quad W=xL,
\]

and

\[
K=y+6xy^2+xz+2x^2yz.
\]

The exact shifted identity is

\[
\boxed{b:=1+aW=xK}.
\]

Define

\[
\boxed{c:=ab=vK}.
\]

Then

\[
\boxed{cW=b(b-1)}.
\]

These identities were independently rechecked symbolically.

## 2. Boundary/intersection ring theorem

The archived BLIND 2 theorem is

\[
\boxed{k[a,W]\cap k[x,y,z]=B},\qquad
B:=k[W,b,c]/(cW-b(b-1)).
\]

The theorem is best understood geometrically.

### 2.1 The surface is a Danielewski surface

The equation

\[
Wc=b(b-1)
\]

is the standard Danielewski form \(XY=p(Z)\) with \(p(b)=b(b-1)\). Since \(p\) has two simple roots, the surface is smooth (hence normal).

The projection \(W=0\) has two affine-line components:

\[
E_0:\ W=b=0,\qquad E_1:\ W=0,\ b=1.
\]

The hidden affine plane \(\mathbb A^2_{a,W}\) identifies exactly with \(\operatorname{Spec}B\setminus E_0\):

- if \(W\neq0\), \(a=(b-1)/W\);
- if \(b\neq0\), \(a=c/b\);
- on \(W=0,b=1\), one has \(a=c\).

Thus \(B\) is a one-divisor completion of the hidden reciprocal chart.

### 2.2 Why source-polynomiality is exactly regularity across the added boundary

After localizing the source at \(x\),

\[
k[x,y,z,x^{-1}]=k[x,x^{-1},a,W],
\]

because

\[
y=\frac{ax-1}{2x},\qquad
z=\frac{2W+5x-3ax^2}{2x^3}.
\]

So an element of \(k[a,W]\) can fail to be a source polynomial only along \(x=0\).

The source divisor \(x=0\) maps dominantly to \(E_0\). Indeed,

\[
W=xL,\quad L\equiv-1\pmod x,
\]

so \(W\) vanishes to first order, while

\[
c\equiv y\pmod x,
\]

so the map covers the generic point of \(E_0\). Therefore the \(x\)-adic valuation restricts to the divisorial valuation of \(E_0\) with ramification index one.

Since \(B\) is normal, a rational function on it that is regular away from \(E_0\) belongs to \(B\) exactly when its valuation at \(E_0\) is nonnegative. This gives the reverse inclusion and proves the intersection theorem.

**Assessment:** the proof is mathematically coherent. The remaining gap is not an observed algebraic flaw; it is the absence of external specialist refereeing/formalization.

## 3. A new structural observation: the hidden derivative extends as an LND

The hidden derivative \(\partial/\partial a\) at fixed \(W\) extends to a derivation \(D\) of the boundary ring:

\[
D(W)=0,\qquad D(b)=W,\qquad D(c)=2b-1.
\]

It preserves \(cW-b(b-1)=0\), and it is locally nilpotent. Consequently the BLIND 2 "hidden \(a\)-degree" is naturally the \(D\)-degree on this Danielewski surface.

The filtration has

\[
\deg_D W=0,\qquad \deg_D b=1,\qquad \deg_D c=2.
\]

Its leading relation is

\[
cW=b^2,
\]

so the associated graded ring is a toric quadratic cone. The actual boundary ring \(cW=b(b-1)\) is a smooth deformation of that cone. This makes the mysterious shift by \(+1\) conceptual: without it one sees the singular double-root cone; with it, the boundary splits into two smooth components.

## 4. Exact degree filtration

Using \(cW=b(b-1)\), a monomial basis is

\[
b^sW^j\quad(s,j\ge0),\qquad b^sc^r\quad(s\ge0,r\ge1).
\]

The highest source-degree monomials of the generators are

\[
W:\ x^3z\quad(\deg=4),
\]

\[
b:\ 2x^3yz\quad(\deg=5),
\]

\[
c:\ 4x^3y^2z\quad(\deg=6).
\]

Their exponent patterns show that distinct normal-form monomials cannot cancel at top total degree. Hence

\[
\deg(b^sW^j)=5s+4j,\qquad \deg_D(b^sW^j)=s,
\]

\[
\deg(b^sc^r)=5s+6r,\qquad \deg_D(b^sc^r)=s+2r.
\]

The minimum source total degree of a nonzero boundary-ring element of hidden degree \(m\) is therefore

\[
\boxed{\delta(m)=\begin{cases}3m,&m\text{ even},\\3m+2,&m\text{ odd}.\end{cases}}
\]

In particular \(\delta(5)=17\).

## 5. Canonical-potential degree-17 theorem

For the canonical hidden map

\[
U=X+h_a,\qquad S=\frac{aX+ah_a-h}{2},
\]

start from

\[
h_0=a^2+Wa^3=a^2(1+aW)
\]

and deform by \(g\in k[a,W]\). Then

\[
\Delta U=g_a,\qquad 2\Delta S=ag_a-g.
\]

If the new outputs are source polynomials, both expressions lie in \(B\). If \(m=\deg_a g\ge2\), then \(ag_a-g\) still has hidden degree \(m\), so an output total-degree cap \(D\) forces \(\delta(m)\le D\).

Thus

\[
D\le16\implies m\le4.
\]

At \(D=17,m=5\), the sole normal-form direction at the top is \(bc^2\), and it is realized by

\[
\boxed{g_*=a^2b^3=a^2(1+aW)^3}.
\]

Indeed

\[
(g_*)_a=bc(5b-3),
\]

\[
a(g_*)_a-g_*=c^2(4b-3),
\]

of source total degrees 16 and 17.

An independent rational-linear-algebra computation reproduces the threshold: at degree 16 the projection of the solution space to hidden degree \(\ge5\) has rank 0; at degree 17 it has rank 1, with coefficients \(1,3,3,1\), i.e. \(a^2(1+aW)^3\).

**Scope:** this is sharp only inside the fixed reciprocal chart and canonical-potential class. It is not a global minimality theorem for all Keller maps.

## 6. BLIND 4 finite-jet criterion is the same boundary algebra in one variable

BLIND 4 restricts to

\[
h=a^2H(t),\qquad t=aW.
\]

Its exact divisibility calculation says polynomialization occurs iff

\[
H(-1)=0,\qquad H'(-1)=1,\qquad H''(-1)=0,
\]

or equivalently

\[
\boxed{H(t)=1+t+(1+t)^3R(t)}.
\]

This can now be explained by the boundary ring rather than by coefficient cancellation.

Let \(b=1+t\) and define the deformation relative to \(H_0=1+t\):

\[
g=a^2(H(t)-(1+t)).
\]

The jet condition is exactly

\[
g=a^2b^3R(b-1)=bc^2R(b-1)\in B.
\]

So BLIND 4's two-jet theorem is a one-parameter slice of BLIND 2's intersection theorem.

There is also a direct local proof. Put

\[
Q(b)=H(b-1)-b.
\]

Then

\[
g=\frac{c^2Q(b)}{b^2}.
\]

Using the extended derivation \(D=\partial_a\),

\[
Dg=\frac{c\,[2Q+(b-1)Q']}{b},
\]

\[
aDg-g=\frac{c^2\,[Q+(b-1)Q']}{b^2}.
\]

At the missing boundary \(E_0\), \(b\) is a uniformizer and \(c\) is generically a unit. Regularity of both expressions is equivalent to

\[
b^3\mid Q(b),
\]

which is exactly the two-jet condition at \(t=-1\).

For arbitrary \(R\), the output corrections can be written entirely inside \(B\):

\[
\Delta U=bc\bigl((5b-3)R+b(b-1)R'\bigr),
\]

\[
2\Delta S=c^2\bigl((4b-3)R+b(b-1)R'\bigr).
\]

This explicitly unifies the two blind-session discoveries.

## 7. Normalized-gradient binary cubic

BLIND 4 associates to target \((A,B,C)\) the binary cubic

\[
P_{A,B,C}(X,W)=2AX^3-BX^2W+2XW^2-CW^3.
\]

For the base counterexample define

\[
L=uX-xW,\qquad M=W-yX,
\]

with \(u=1+xy\). The change \((X,W)\mapsto(L,M)\) is in \(SL_2\). Exact expansion gives

\[
P_F=L\left(2M^2+\beta LM+\alpha L^2\right),
\]

where

\[
\alpha=(3u-1)z+9y^2,\qquad \beta=3xuz+3y(3u-2).
\]

At the selected root vector \((x,u)\), \(L=0,M=1\), hence

\[
\boxed{\nabla P_F(x,u)=2(u,-x)}.
\]

This is exact and useful, but it is probably not a separate unpublished theorem in substance. Public cubic-factor derivations already normalize the resultant of the selected linear factor and residual quadratic. For a binary factorization \(P=LQ\), the resultant with \(L\) is (up to the standard scale convention) \(Q\) evaluated on the root vector of \(L\). Here \(Q(x,u)=2\), and

\[
\nabla(LQ)|_{L=0}=Q\nabla L,
\]

which is exactly the normalized-gradient identity. So BLIND 4 found an elegant differential/invariant restatement of the public resultant normalization.

Likewise its discriminant pullback

\[
\Delta(F)=\beta^2-8\alpha
\]

is the residual-quadratic discriminant after the normalized linear factor is removed.

## 8. What appears unmatched publicly as of 2026-08-11

### Strongest unmatched exact structure

1. The specific intersection theorem
   \[
   k[a,W]\cap k[x,y,z]=k[W,b,c]/(cW-b(b-1)).
   \]
2. The induced two-filtration degree law \(\delta(m)\).
3. The resulting chart-relative canonical-potential degree-17 sharpness / one-dimensional quintic direction.
4. The explicit identification that the BLIND 4 two-jet criterion is precisely a slice of the same intersection ring.

Targeted searches for the exact ring relation/phrases/formulas found no indexed match in the current public Jacobian literature.

### Partly public / likely subsumed

- Finite lift/pole cancellation conditions: public graded-Keller work has general lift conditions and osculating-jet interpretations.
- Boundary semigroups: public work now has semigroups at infinity of branch curves, but this is not the same object as the BLIND 2 intersection ring.
- Normalized gradient: likely equivalent to resultant normalization already public on July 20.
- Generic cubic/S3/nonproperness/escape: fully public.
- Larger generic degrees and many surjective examples: public.

### Important unresolved priority caveat

Kistner–Shaska (Aug. 3) cite an ancillary companion preprint, *Differential obstructions and minimal models for balanced graded Keller maps*, which is not separately indexed in ordinary search. Their main paper says it contains differential obstruction/minimal-degree results. Its exact contents need to be compared before any priority claim about the BLIND 2 degree obstruction is made.

## 9. Why this could have been missed without being wrong

1. **Time:** the counterexample is only weeks old and the public theory is moving daily.
2. **No transmission mechanism:** the blind work remained private. A correct theorem in a ChatGPT archive does not spontaneously enter arXiv.
3. **Representation choice:** public work rapidly moved to graded quotients, tangent-sweep geometry, monodromy, moduli, and invariant lifting. BLIND 2 instead preserved an awkward reciprocal chart and asked which hidden rational functions become source polynomials. That makes the intersection ring visible.
4. **The decisive shift is easy to discard:** \(aW\) approaches \(-1\) on the deleted divisor, so \(1+aW\), not \(aW\), vanishes there. Once this is noticed the Danielewski surface is natural; before it, the correct algebra is not obvious.
5. **YOLO pressure plausibly changed search policy:** the archive shows BLIND 2 first overrestricted the problem, later found the shifted boundary variable under persistence pressure, and only afterward received a sibling memo explicitly asking for the intersection ring. Thus the full theorem was not magically generated from a content-free phrase, but persistence helped preserve a nonstandard representation long enough for the key boundary variable to appear.
6. **Some apparent novelty is notation:** the normalized-gradient result is a good example. It looked new under one coordinate language but collapses to a public resultant normalization once translated.

## 10. Verification status from this audit

- exact boundary identities: PASS;
- independent bounded-box intersection tests through hidden exponent boxes 9 x 9: PASS;
- degree-16/17 rational linear-algebra threshold: PASS;
- base and degree-17 Jacobian/collision/quintic checks: PASS;
- BLIND 4 two-jet criterion: PASS;
- normalized-gradient and discriminant identities: PASS;
- full theorem proof: no defect found; rests on standard normality/divisorial-valuation arguments and deserves external algebraic-geometry review;
- Lean: no `lean` or `lake` binary is currently available on PATH in this runtime; exact SymPy/rational algebra was sufficient for the checks above.

## Bottom line

The most defensible candidate for genuinely unpublished mathematics in the blind sessions is **not** the degree-17 counterexample itself, nor generic degree five, nor the normalized-gradient slogan. It is the **exact boundary/intersection algebra of the reciprocal chart**, together with its degree filtration and the way that algebra explains both the degree-17 threshold and BLIND 4's finite-jet criterion.

The evidence currently favors “valid chart-specific structure that public work has not yet stated in this form,” not “hallucinated theorem.” Priority/newness remains provisional until the ancillary Kistner–Shaska companion preprint and any very recent non-indexed notes are inspected by a specialist.
