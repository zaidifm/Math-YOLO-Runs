# SL2 boundary classification — 2026-08-11 blackboard checkpoint

**Status:** DERIVED + COMPUTED in the 2026-08-11 audit; not externally reviewed and not priority-cleared.  
**Scope:** fixed reciprocal chart / canonical-potential construction only. No global minimality claim for all Keller maps.

## 1. Hidden SL2 matrix

Write

\[
v=1+2xy,\qquad
L=-1+3xy+x^2z,\qquad
K=y+6xy^2+xz+2x^2yz.
\]

The shifted-boundary identity `1+aW=xK` hides the stronger exact relation

\[
\boxed{xK-vL=1}.
\]

Therefore

\[
G(x,y,z)=
\begin{pmatrix}x&v\\L&K\end{pmatrix}\in SL_2.
\]

It has the exact elementary factorization

\[
G=
\begin{pmatrix}1&0\\3y+xz&1\end{pmatrix}
\begin{pmatrix}x&1\\-1&0\end{pmatrix}
\begin{pmatrix}1&2y\\0&1\end{pmatrix}.
\]

At `x=0`, `G=[[0,1],[-1,y]]`, so the `z` direction is contracted.

Let the torus act by row rescaling

\[
t\cdot(x,v,L,K)=(tx,tv,t^{-1}L,t^{-1}K).
\]

The invariant matrix products are

\[
W=xL,\qquad b=xK,\qquad b-1=vL,\qquad c=vK.
\]

Hence the torus-invariant ring is

\[
\boxed{R\cong k[W,b,c]/(cW-b(b-1)).}
\]

This is the BLIND 2 boundary ring. Geometrically it is the affine left quotient `T\\backslash SL_2`, equivalently `SL_2/T` after inversion.

On `x!=0`, use the torus to normalize `x=1`:

\[
\operatorname{diag}(1/x,x)G=
\begin{pmatrix}1&a\\W&b\end{pmatrix},
\qquad a=v/x,
\]

and determinant one forces

\[
\boxed{b=1+aW}.
\]

Thus the hidden `(a,W)` plane is the big-cell quotient chart. The `+1` shift is a determinant-one matrix coefficient, not an accidental pole cancellation.

## 2. Discriminant-one quadric and full sl2 action

Set

\[
q=2b-1.
\]

Then

\[
\boxed{q^2-4cW=1}.
\]

Indeed

\[
(xU+vV)(LU+KV)=WU^2+qUV+cV^2,
\]

whose binary-quadratic discriminant is `(xK-vL)^2=1`.

The missing boundary line is

\[
D=(W,b)=(W,q+1).
\]

The hidden derivative `e=partial/partial a` acts by

\[
e(W)=0,\qquad e(q)=2W,\qquad e(c)=q.
\]

Define

\[
f(W)=q,\qquad f(q)=2c,\qquad f(c)=0,
\]

and `h=[e,f]`. Then

\[
h(W)=2W,\qquad h(q)=0,\qquad h(c)=-2c,
\]

with exact commutators

\[
[e,f]=h,\qquad[h,e]=2e,\qquad[h,f]=-2f.
\]

So the LND isolated earlier is one root operator in a full `sl_2` action on the boundary quadric.

## 3. Strengthened intersection proof

The original valuation argument becomes sharper because

\[
(W,b)k[x,y,z]=(xL,xK)=x(L,K).
\]

The Bezout identity `xK-vL=1` implies `(L,K)=(1)`, hence scheme-theoretically

\[
\boxed{(W,b)k[x,y,z]=(x).}
\]

Thus the boundary divisor pulls back to `x=0` with multiplicity exactly one.

The open complement `Spec(R)\\D` is `A^2_{a,W}`: use `a=(b-1)/W` on `W!=0` and `a=c/b` on `b!=0`. At the generic point of `D`, `b` is a uniformizer and its pullback `xK` has `x`-order one because `K mod x=y` is generically nonzero. Since `R` is smooth/normal, any `f in k[a,W]` whose pullback is polynomial has no pole at any height-one prime. Therefore

\[
\boxed{k[a,W]\cap k[x,y,z]=R.}
\]

This closes the main technical gap in the earlier proof: the divisor pullback is exact as an ideal, not merely generically identified.

## 4. Degree filtration is an A1 / second-Veronese degeneration

The actual total degrees are

\[
\deg W=4,\qquad\deg b=5,\qquad\deg c=6.
\]

Their top forms are

\[
\operatorname{in}(W)=x^3z,\quad
\operatorname{in}(b)=2x^3yz,\quad
\operatorname{in}(c)=4x^3y^2z.
\]

Consequently

\[
\boxed{\operatorname{gr}R\cong
k[\bar W,\bar b,\bar c]/(\bar c\bar W-\bar b^2).}
\]

The weighted Rees family may be written, after `q=2b-1`, as

\[
\boxed{Q^2-4CW=T^{10}}.
\]

The generic fiber is the smooth discriminant-one quadric; the special fiber is the `A_1` quadric cone. Equivalently,

\[
\operatorname{gr}R\cong k[s^2,st,t^2]=k[s,t]^{\{\pm1\}},
\]

with source weights `deg(s)=2`, `deg(t)=3`.

Under `W=s^2`, `b=st`, `c=t^2`, hidden `a`-degree is the exponent of `t`. Thus the old law

\[
\delta_R(m)=
\begin{cases}3m,&m\text{ even},\\3m+2,&m\text{ odd}\end{cases}
\]

is simply the parity constraint of the second Veronese: a sign-invariant monomial `s^r t^m` requires `r+m` even. The `+2` for odd `m` is forced by the smallest allowed `r=1`.

## 5. Complete fixed-chart canonical-potential classification

Let

\[
h_0=a^2+Wa^3=a^2(1+aW)
\]

be the base potential, and write `h=h0+g`. The output changes are

\[
\Delta U=g_a,\qquad 2\Delta S=ag_a-g.
\]

Put `s=aW=b-1`. Decompose `g` uniquely by diagonal `d=i-j` of monomials `a^iW^j`:

\[
g=\sum_{r\ge0}W^rP_{-r}(s)+\sum_{d\ge1}a^dP_d(s).
\]

The intersection theorem gives, for `d>=1`,

\[
a^dP_d(s)\in R\iff b^d\mid P_d(s).
\]

For `g_d=a^dP(s)`,

\[
\partial_a g_d=a^{d-1}(dP+sP'),
\]

\[
(a\partial_a-1)g_d=a^d((d-1)P+sP').
\]

Solving the two divisibility conditions yields:

- nonpositive diagonals: arbitrary;
- `d=1`: `P'(-1)=0`, equivalently `P=alpha+b^2Q`;
- `d>=2`: `b^{d+1}|P`.

These conditions collapse to one geometric statement:

\[
\boxed{g=\alpha a+r,\qquad r\in k+I_D,\qquad I_D=(W,b)\subset R.}
\]

Therefore the full fixed-chart potential classification is

\[
\boxed{
h=h_0+\alpha a+\beta+r,
\qquad r\in I_D=(W,b).
}
\]

The `alpha a` and `beta` terms only translate target coordinates. Modulo target translations, the entire polynomializable deformation space is exactly the ideal of the missing boundary line.

This strictly generalizes the BLIND 4 slice `h=a^2H(aW)`. Its two-jet condition

\[
H(t)=1+t+(1+t)^3R(t)
\]

is precisely the `d=2` case, where the general theorem demands divisibility by `b^3`.

## 6. Sharp deformation spectrum and degree 17

In the second-Veronese degeneration, the boundary ideal becomes

\[
I_D=(s^2,st).
\]

For hidden degree `m`, minimize the source weight of an invariant monomial `s^r t^m` inside this ideal. The result is

\[
\boxed{\mu(m)=
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

For hidden degree five,

\[
\boxed{g_5=bc^2=a^2(1+aW)^3,\qquad \mu(5)=17.}
\]

Thus the `(1,3,3,1)` coefficient pattern is the binomial expansion of the unique minimal boundary-ideal weight vector. The degree-17 phenomenon is a consequence of the torus quotient + Veronese parity + boundary-ideal condition.

A new refinement is that the ring bound `delta_R(4)=12` is not sharp for canonical potentials: `c^2` fails the boundary condition. The actual deformation threshold at hidden degree four is `mu(4)=16`, represented by `b^2c`.

## 7. Closed form for every bounded canonical kernel

Modulo the two translation gauges, an explicit basis is

- `W^j`, `j>=1`, output degree `4j`;
- `bW^j`, `j>=0`, output degree `4j+4`;
- `b^sW^j`, `s>=2,j>=0`, output degree `5s+4j`;
- `b^sc^r`, `s>=1,r>=1`, output degree `5s+6r`.

Hence the exact Hilbert series by output degree is

\[
\boxed{
H(q)=2+\frac{2q^4}{1-q^4}
+\frac{q^{10}}{(1-q^4)(1-q^5)}
+\frac{q^{11}}{(1-q^5)(1-q^6)}.
}
\]

An exact SymPy reconstruction of the original coefficient-constraint matrices was checked for every degree bound `D=3,...,20`. The predicted cumulative dimension matched the exact nullity at all 18 bounds. In particular the nullities are `15` at `D=16` and `16` at `D=17`; the sole new direction at 17 is `bc^2`.

## 8. Epistemic boundary

The identities, matrix factorization, `sl_2` commutators, top-degree forms, minimal representatives through hidden degree 12, and bounded matrix comparisons are COMPUTED exactly. The general intersection/potential/Hilbert arguments above are DERIVED and have been adversarially checked in this run, but still require independent specialist/formal review before promotion to VERIFIED.

No novelty or priority claim is made. The unavailable Kistner-Shaska companion remains an explicit literature-coverage caveat.
