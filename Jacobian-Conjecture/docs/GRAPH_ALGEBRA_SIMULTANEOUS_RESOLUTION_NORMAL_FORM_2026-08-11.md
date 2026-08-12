# Graph algebra, simultaneous resolution, and the rank-one normal form

**Date:** 2026-08-11  
**Status:** continuous-blackboard checkpoint. Exact displayed algebra has executable certificates; general normal-form statements are DERIVED under the stated rank-one assumptions. No external novelty claim.

## 1. The hidden chart is the Grothendieck simultaneous resolution

The boundary quadric is the regular semisimple adjoint orbit
\[
M=\begin{pmatrix}q&2c\\-2W&-q\end{pmatrix},
\qquad M^2=I.
\]
The weighted Rees family is
\[
Q^2-4CW=T^{10}.
\]
Set `A=T a`. Then
\[
\boxed{Q=T^5+2AW,\qquad C=T^5A+A^2W.}
\]
For
\[
\mathcal M=\begin{pmatrix}Q&2C\\-2W&-Q\end{pmatrix}
\]
one has
\[
\mathcal M^2=T^{10}I,
\qquad
\mathcal M\binom{A}{-1}=-T^5\binom{A}{-1}.
\]
Thus the hidden coordinate `A` is literally a chosen eigenline coordinate in the rank-one Grothendieck simultaneous resolution. At `T!=0` this is the regular semisimple orbit with an ordered eigenline; at `T=0` it is the Springer chart `T*P1 -> N` of the nilpotent cone.

## 2. The potential boundary data is the intrinsic two-jet module

For the missing color
\[
I_D=(W,b),
\]
the relations `aW=b-1`, `ab=c` imply
\[
\boxed{I_D^{-1}=R+Ra=O(D).}
\]
Hence the canonical potential class lives in
\[
\boxed{I_D^{-1}/I_D=O(D)/O(-D).}
\]
Locally this is `b^{-1}O/bO`: exactly the polar coefficient plus finite boundary trace.

The absolute base class is
\[
\boxed{h_\tau=c^2/b+\mu c^2,\qquad \mu=(2-\tau)/2.}
\]
Thus the historical two-jet condition is the one-variable expression of an intrinsic two-layer Laurent class along the color. `tau=2` is precisely zero quadratic highest-weight boundary trace.

## 3. The minimal rational incidence map on SL2

At the resonant value,
\[
h_0=c^2/b=a^2(1+aW).
\]
For
\[
G=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in SL_2
\]
the rational incidence coordinates are
\[
\boxed{U=\frac{1+2B+3B^2C}{A},}
\]
\[
\boxed{S=\frac{B(1+B+2B^2C)}{2A^2},}
\]
\[
\boxed{W=AC.}
\]
Relative to Haar volume their rational Jacobian is the `-2rho` semi-invariant `1/(2A^2)`.

## 4. The polynomial coefficients are forced by two base-locus resolutions

The distinguished base line is
\[
A=0,\quad B=1,\quad C=-1.
\]
On the first affine resolution chart write
\[
B=1+Au,
\qquad
C=-1+Av.
\]
Then `U` is regular, while the remaining pole of `S` has leading coefficient
\[
(-3u+2v)/(2A).
\]
Therefore the second center is forced:
\[
2v-3u=0.
\]
Normalize
\[
u=2y,
\qquad
v=3y+Az.
\]
Then
\[
\boxed{B=1+2Ay,}
\]
\[
\boxed{C=-1+3Ay+A^2z,}
\]
and determinant one forces
\[
\boxed{D=y+6Ay^2+Az+2A^2yz.}
\]
These are the hidden matrix entries of the announced map. The coefficients `2`, `3`, and the `A^2z` term are resolution data, not searched coefficients.

## 5. The source is intrinsically the affine graph algebra

Let
\[
B_0=k[SL_2],
\qquad
\mathcal A=B_0[U,S]\subset\operatorname{Frac}(B_0).
\]
Then
\[
\boxed{y=(3BD-U)/2\in\mathcal A.}
\]
Set
\[
R_3=C+1-3Ay=A^2z,
\]
\[
R_1=D-y-6Ay^2=ABz.
\]
Hence
\[
Az=R_1-2yR_3.
\]
Also
\[
R_2=S-4y^2B(3Ay+2)=B^3z.
\]
Because
\[
B^2-A(4y+4Ay^2)=1,
\]
one gets
\[
Bz=R_2-(4y+4Ay^2)R_1.
\]
Finally `B-2Ay=1`, so
\[
z=Bz-2y(Az).
\]
Thus
\[
\boxed{\mathcal A=k[A,y,z]\cong k^{[3]}.}
\]
The source `A3` is the affine graph closure of the rational incidence map, not merely a convenient blowup chart.

## 6. Every canonical deformation uses the same graph algebra

For an admissible deformation `h=h0+g`,
\[
g_a\in R,
\qquad
ag_a-g\in R.
\]
Therefore the deformed rational coordinates differ from `(U0,S0)` by regular functions on `SL2/T` and hence on `SL2`. Consequently
\[
\boxed{k[SL_2][U_h,S_h]=k[SL_2][U_0,S_0]\cong k^{[3]}.}
\]
The degree-17 map and all higher canonical maps are different projections of the same affine graph space; the source resolution is fixed.

## 7. The collapsed-color branch is impossible

If the source exceptional divisor collapses to a point of the color instead of dominating it, then `b` has order two and the induced valuation is
\[
v(a)=-1,\quad v(W)=v(c)=1,\quad v(b)=2.
\]
The unique weighted-leading potential capable of canceling `X` is `a^2b`, but after cancellation
\[
U|_{x=0}=-\tau y+P(z+\tau^2y^2).
\]
No polynomial `P` can make this vanish for all `y,z`; then `aU-h` retains a pole. Thus polynomial regularity forces the exceptional divisor to dominate the color, reducing the source modification to the normalized nondegenerate `tau` family.

## 8. The Legendre formula is forced by the determinant PDE

Once
\[
U=X+h_a
\]
is fixed, imposing hidden Jacobian `-X/tau` gives
\[
S_Xh_{aa}-S_a=-X/\tau.
\]
Along the characteristics preserving `U`, integration yields the complete solution
\[
\boxed{S=(aU-h)/\tau+\Phi(U,W).}
\]
The arbitrary `Phi` is a target shear. Thus the incidence/Legendre formula is unique up to target automorphism.

## 9. Rank-one normal-form consequence

Under the following structural assumptions:

1. reciprocal torus coordinate with one irreducible source boundary divisor;
2. a two-dimensional hidden quotient with simple pole/zero exchange;
3. color-centered triangular affine modification;
4. root-Hamiltonian first target `U=X+h_a`;
5. polynomial coordinate extension across the color;

successive rigidity arguments force:

- the `SL2/T` completion;
- nondegenerate color domination;
- the normalized `tau` source family;
- the Legendre second target;
- the potential coset `h_tau + alpha*a + beta + I_D`;
- the quadratic boundary trace `H''(-1)=2-tau`;
- minimum-degree resonance `tau=2`;
- the minimal potential `h0=c^2/b`;
- and, up to low-degree target shears/scalings, the announced degree `(7,6,4)` map.

The remaining question is whether every primitive dimension-three Keller counterexample must admit, or can be birationally organized by, a normal form of this rank-one graph-cancellation type.

## 10. General affine graph-cancellation lemma

For a smooth affine `Y` with volume `omega_Y` and rational map `Psi=(F_i)`, let
\[
A=O(Y)[F_1,...,F_n].
\]
If `A` is polynomial, its affine modification resolves the `F_i`, and the rational Jacobian factor of `Psi` is the reciprocal of the modification's relative canonical factor, then the graph projection `Spec(A)->A^n` is Keller. If the function-field degree is greater than one, it is a counterexample.

The rank-one construction solves the three hard pieces by cubic incidence, polynomial graph algebra, and `2rho` discrepancy cancellation.