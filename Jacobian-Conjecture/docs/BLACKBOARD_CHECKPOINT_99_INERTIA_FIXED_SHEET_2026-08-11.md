# Blackboard checkpoint 99 — every Keller branch inertia generator must fix a sheet

**Date:** 2026-08-11  
**Status:** Zariski-Main/inertia argument DERIVED; low-degree permutation types COMPUTED. No external priority claim.

Let

\[
F:X=\mathbb A^n\to Y=\mathbb A^n
\]

be an everywhere-etale polynomial map of generic degree `d>1`, and let

\[
X\hookrightarrow\overline X\xrightarrow{\pi}Y
\]

be its finite normalization/Zariski-Main factorization.

For every irreducible branch divisor `B` of `pi`, at least one prime above the geometric generic point of `B` has ramification index one. Equivalently,

\[
\boxed{\text{every codimension-one inertia generator has a fixed point on the }d\text{ sheets}.}
\]

Reason: if all sheets over a branch divisor were ramified, the etale open source could contain no point over a dense open of that divisor. But an irreducible defining equation `p` for the divisor cannot pull back to a nowhere-zero nonconstant polynomial on affine space. If `p o F` has a zero, its codimension-one zero component maps quasi-finitely and hence dominantly to the branch divisor, producing an etale/unramified generic source point above it. If it has no zero, it is a unit and hence constant, contradicting dominance.

## Degree two

The only nontrivial permutation of two sheets is a transposition with no fixed point. Thus the criterion recovers the global generic-degree-two obstruction.

## Degree three

The nontrivial cycle types are `(2,1)` and `(3)`. The fixed-sheet criterion excludes a 3-cycle. Hence every codimension-one inertia element is a transposition.

The monodromy group of a connected generic-degree-three cover is a transitive subgroup of `S_3`. Since it contains a transposition, it is necessarily

\[
\boxed{S_3.}
\]

Thus `S_3` monodromy is forced for every nontrivial generic-degree-three Keller map, not peculiar to the primitive formulas.

Over the geometric generic point of a branch divisor, a transposition fixes exactly one sheet. That is the unique unramified sheet available to the etale open source, so the universal minimum-degree local pattern is

\[
3\text{ sheets off branch}\longrightarrow1\text{ surviving affine sheet on generic branch}.
\]

The omitted codimension-two locus can occur only where the local inertia/branch configuration loses its last surviving fixed sheet.

This gives a representation-free group-theoretic filter for any Keller counterexample:

\[
\boxed{\text{no codimension-one branch cycle of its finite normalization may be fixed-point-free}.}
\]

Exact low-degree permutation certificate: `scripts/jacobian_inertia_fixed_sheet_verify.py`, SHA-256 `683134270bef652da15e0f0548e49880b04d9d4b7dd25eae89b0eff265a73ac2`.
