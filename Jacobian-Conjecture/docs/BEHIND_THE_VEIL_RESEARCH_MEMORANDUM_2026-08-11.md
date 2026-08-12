# Research Memorandum: Behind the Veil

**Date:** 2026-08-11  
**Project:** Jacobian Conjecture YOLO Run  
**Status:** Research-program memorandum. This document records questions, hypotheses, and transferable heuristics suggested by the 2026-08-11 blackboard work. It does **not** claim that the broader conjectures discussed below have been solved or substantially advanced by the Jacobian calculations.

## 1. Why this memorandum exists

The 2026-08-11 Jacobian blackboard pass changed the character of the project. What had looked like a collection of unrelated phenomena—reciprocal coordinates, the shifted factor `1+aW`, a boundary/intersection ring, locally nilpotent derivations, parity in a degree filtration, the degree-17 direction, a two-jet criterion, and surjectivity behavior—collapsed onto a single source geometry built from an explicit determinant-one matrix.

The central exact identity is

\[
xK-vL=1,
\]

with

\[
v=1+2xy,\qquad
L=-1+3xy+x^2z,\qquad
K=y+6xy^2+xz+2x^2yz.
\]

Thus

\[
G=\begin{pmatrix}x&v\\L&K\end{pmatrix}\in SL_2.
\]

The previously isolated boundary generators are torus-invariant matrix products,

\[
W=xL,\qquad b=xK,\qquad b-1=vL,\qquad c=vK,
\]

so the boundary algebra

\[
R=k[W,b,c]/(cW-b(b-1))
\]

is naturally an affine torus quotient of this `SL_2` model. On the quotient big cell, determinant one forces

\[
b=1+aW.
\]

This re-representation reduced several apparently independent “miracles” to consequences of one object. That experience motivates the questions below.

## 2. The central methodological hypothesis

A useful working hypothesis is:

> **When a difficult problem accumulates many technically different partial results that repeatedly display the same exceptional cases, numerical patterns, cancellations, symmetries, or barriers, those phenomena may be coordinate shadows of a more natural object that has not yet been named.**

The breakthrough may therefore be less about proving the next estimate and more about finding the representation in which several existing estimates, identities, and exceptions become manifestations of one structure.

A practical test for a proposed representation is compression:

> **A good representation reduces the number of independent miracles.**

In the current Jacobian work, the `SL_2/T` picture is interesting precisely because it simultaneously explains the shifted factor, the boundary ring, the missing divisor, the hidden Lie action, the parity defect, the canonical deformation spectrum, the degree-17 vector, and the relation to the BLIND 4 frame calculations.

This is a heuristic, not a theorem about mathematical discovery.

## 3. What may be the actual mechanism of the dimension-three Jacobian failure

The strongest conceptual question now is:

> **Is the known dimension-three counterexample merely a polynomial construction that happens to admit an `SL_2` description, or is the `SL_2/T` boundary geometry the actual reason the counterexample exists?**

The latter possibility would imply that the explicit polynomial formulas are downstream coordinates on a simpler geometric construction.

A possible conceptual derivation would run in the reverse direction from the historical discovery:

1. begin with `SL_2` or an equivalent rank-one group model;
2. take the torus quotient and its big-cell coordinates;
3. identify the missing boundary divisor;
4. study the boundary ideal and its filtration;
5. choose canonical potentials/sections satisfying the boundary condition;
6. pull the resulting construction back through the affine source chart;
7. obtain polynomial Keller maps and their recovery equations.

If this program succeeds cleanly, the disproof becomes less a miraculous coefficient identity and more an instance of a geometric machine.

## 4. The remaining two-dimensional Jacobian Conjecture

The dimension-two problem should be reconsidered from the opposite direction.

Rather than asking only why the known three-dimensional construction cannot be imitated with fewer variables, ask:

> **What boundary configurations are possible for an étale polynomial map `A^2 -> A^2`, and do two dimensions forbid the kind of divisor contraction / quotient geometry that exists in the three-dimensional example?**

The dimension coincidence is suggestive: `SL_2` itself is three-dimensional, while its torus quotient is two-dimensional. In the current construction, an affine threefold maps into an `SL_2` model, a source divisor is contracted, and a two-dimensional quotient surface controls polynomialization.

This raises a concrete research program:

- classify candidate boundary completions of polynomial étale maps in dimension two;
- identify whether an analogue of the `SL_2/T` big-cell-plus-missing-divisor mechanism can exist;
- determine whether dimension two admits an obstruction theorem phrased in boundary geometry rather than coefficient degree;
- test whether the truth of JC2 is equivalent, or at least closely related, to the impossibility of a specific nonproper boundary configuration.

No such theorem has been established here. The point is that the three-dimensional mechanism suggests a more geometric target for a proof of the two-dimensional case.

## 5. Local conditions versus global boundary failure

The counterexample reinforces a general lesson:

> **A strong local condition may fail to imply global rigidity because the decisive phenomenon lives at infinity.**

For Keller maps, the affine Jacobian condition is locally impeccable: there is no ordinary affine ramification. Yet global injectivity/properness can fail because sheets interact with the boundary of a compactification.

This suggests treating nonproperness as primary structure rather than technical residue. For the current minimal families, a generic target has many affine preimages, special targets can lose sheets to infinity, and surjectivity can coexist with nonproperness.

Questions:

- Is there a canonical compactification in which the disappearing sheets become intersections with an explicit boundary divisor?
- Can the weighted Rees degeneration
  \[
  Q^2-4CW=T^{10}
  \]
  be incorporated into such a compactification?
- Can the recovery polynomial and its multiple-root strata be read directly as boundary-intersection data?
- Is there a geometric invariant measuring when nonproperness produces omitted targets versus merely changing fiber cardinality?

## 6. The surjectivity phase transition as geometry

The minimal scalar directions now display the phase diagram

\[
\begin{array}{c|c}
\text{generic/recovery degree }m&\text{surjectivity for nonzero scalar}\\
\hline
3&\text{never}\\
4&\text{never}\\
5&\text{all but two algebraic scalars}\\
\ge6&\text{always}.
\end{array}
\]

The current proofs use explicit squareful-polynomial classifications in low degree and rigidity arguments in high degree. A more conceptual question is:

> **Is this entire transition an intersection-theoretic statement about a low-dimensional affine slice meeting the squareful/discriminant strata in the space of degree-`m` polynomials?**

Possible picture:

- for `m=3,4`, the recovery slice is forced to meet the all-multiple-root locus;
- for `m=5`, it meets that locus in exactly two nonzero scalar parameters;
- for `m>=6`, the relevant slice misses it;
- the disappearance may follow from codimension/transversality rather than case-by-case coefficient algebra.

A uniform geometric proof would convert the current phase diagram from an observed theorem into an inevitability.

## 7. Global versus fixed-chart minimality

Inside the fixed canonical reciprocal chart, the boundary ideal and second-Veronese filtration give a sharp minimal output degree

\[
D_m=\begin{cases}
3m+2,&m\text{ odd},\\
3m+4,&m\text{ even}.
\end{cases}
\]

The major open question is whether this is only a property of the chosen chart or evidence of a broader extremal law.

Questions:

- Among **all** three-variable Keller maps of generic fiber degree `m`, is there a universal lower bound of order `3m` on polynomial degree?
- If so, are the minimal canonical directions globally extremal or asymptotically extremal?
- Is there a birationally invariant filtration that replaces the chart-dependent hidden `a`-degree?
- Can boundary valuations or compactification data produce lower bounds independently of the canonical-potential ansatz?

A positive answer would turn the current family from a convenient construction into an extremal classification phenomenon.

## 8. Monodromy and Galois structure of the hierarchy

Each minimal map reduces generic fibers to one degree-`m` recovery polynomial. This invites a systematic monodromy study.

Questions:

- Is the generic Galois/monodromy group `S_m` for the minimal degree-`m` family?
- Are there exceptional scalar parameters where the group drops?
- Can the `SL_2/T` geometry predict those drops?
- How does the branch behavior at infinity encode the generic monodromy even though the affine map is étale?

If generic monodromy is full symmetric, the family would give an explicit sequence of surjective, nonproper, étale polynomial maps with arbitrarily complicated generic monodromy.

## 9. Higher-rank generalization

If the construction is fundamentally

\[
\text{affine chart} \to \text{reductive group} \to \text{torus/spherical quotient}
\]

plus a boundary-ideal polynomialization condition, then `SL_2` may be the rank-one case of something larger.

Questions:

- What happens for `SL_n/T`, flag varieties, or other spherical varieties?
- Do cluster-style exchange relations generate polynomial Keller maps in higher dimensions?
- Can boundary semigroups and invariant rings systematically produce new nonproper étale maps?
- Are there higher-rank analogues of the second-Veronese degeneration controlling degree spectra?
- Can one classify a family of Keller counterexamples through representation-theoretic data rather than explicit coefficient searches?

This could turn one counterexample into a construction theory.

## 10. Dixmier and Poisson perspectives

The known Jacobian/Dixmier/Poisson relationships are usually discussed algebraically. The present work suggests asking whether the geometric failure has a parallel manifestation.

Questions:

- Does the `SL_2/T` boundary mechanism lift naturally to the corresponding Weyl- or Poisson-algebra constructions?
- Is non-surjectivity/nonproperness visible as a boundary phenomenon in a geometric model of those endomorphisms?
- Can the hidden `sl_2` action be interpreted directly on the associated Poisson or differential-operator side?
- Does a compactification or filtration clarify which consequences are dimension-preserving and which depend on stable equivalence?

These are research prompts only. No new Dixmier/Poisson theorem is claimed in this memorandum.

## 11. Riemann Hypothesis: the transferable lesson, not a claimed solution

Nothing in the Jacobian `SL_2/T` calculation solves RH. The useful transfer is methodological.

RH presents many persistent phenomena that are deeply linked but represented through different languages:

- primes and zeros via explicit formulas;
- the functional equation and critical-line symmetry;
- positivity criteria;
- spectral analogies;
- random-matrix statistics;
- Euler products;
- zero-density and critical-line proportion results.

The Jacobian experience strengthens one question:

> **What object would make several of these facts tautological at once?**

A genuine missing paradigm for RH would likely explain, rather than merely coexist with, multiple existing structures. It might make the critical line forced by unitarity, positivity, representation theory, or a spectral symmetry while simultaneously giving a natural home to the Euler product/prime side.

The heuristic is to seek a representation that compresses the number of independent miracles, not simply the next numerical improvement inside an existing representation.

## 12. P versus NP and proof-complexity barriers

P versus NP has accumulated barrier results—relativization, natural proofs, algebrization—and many partially connected lower-bound frameworks.

The analogous question is:

> **Are those barriers evidence that current representations systematically quotient out the invariant that distinguishes efficient computation from hard computation?**

A missing paradigm would ideally explain several barriers simultaneously rather than simply evade one of them with a more intricate lower-bound argument.

Possible research heuristic:

- compare what information is preserved or destroyed across circuit, communication, proof-complexity, pseudorandomness, and algebraic representations;
- search for an invariant whose disappearance explains known barriers;
- prefer frameworks that make barrier theorems structural consequences rather than external annoyances.

Again, this is methodological speculation, not a complexity-theory result.

## 13. Navier–Stokes and critical phenomena

For Navier–Stokes, the analogous possibility is that critical scaling, vortex stretching, dissipation, and concentration are not best treated as independent analytic obstacles.

Questions suggested by the representation heuristic:

- Is there a geometric or monotone structure whose coordinate manifestations are the existing critical estimates?
- Can potential singular concentration be represented as a boundary/compactification phenomenon in an appropriate state space?
- Are exceptional exponents or scale-critical norms evidence of a hidden symmetry or quotient rather than arbitrary analytic thresholds?

No candidate object is identified here. This is an example of how the Jacobian lesson might guide search strategy without pretending to supply an answer.

## 14. BSD, Hodge, motives, and “already structural” conjectures

Arithmetic geometry already embodies much of this philosophy: conjectural equalities often connect invariants believed to arise from one deeper cohomological or motivic object.

The Jacobian episode is a concrete reminder of why that style of thinking is powerful. Once the right object is visible, identities that previously required separate calculations can become representation-theoretic necessities.

The transferable question is not necessarily “find another `SL_2`,” but:

> **Which apparently independent invariants are already telling us that a common object exists?**

## 15. AI-assisted mathematics: re-representation as a search primitive

The productive sequence in this project was not brute-force generation alone. It was repeated re-representation:

1. a shifted factor `1+aW`;
2. an intersection ring;
3. a Danielewski surface;
4. a locally nilpotent derivation;
5. an explicit `SL_2` matrix;
6. a torus quotient;
7. a discriminant-one quadric;
8. a second-Veronese degeneration;
9. a boundary-ideal classification;
10. a minimal deformation hierarchy and surjectivity phase transition.

Each representation compressed more previously independent facts than the preceding one.

This suggests a useful AI-mathematics search protocol:

- explicitly ask for alternate coordinate systems, quotient descriptions, invariant rings, group actions, compactifications, and degenerations;
- score new representations by explanatory compression, not novelty of notation;
- repeatedly ask which facts remain independent under the new representation;
- attack the weakest hinge of a beautiful theory rather than continuing to decorate it;
- preserve failed representations because they delimit what information was missing;
- separate discovery provenance, mathematical correctness, and literature priority.

A model can be useful not only by proving lemmas but by proposing and stress-testing representations until several facts collapse into one mechanism.

## 16. A possible meta-principle

The strongest philosophical hypothesis generated by this episode is:

> **Some long-standing problems may be difficult less because the final proof is intrinsically enormous than because the objects are being represented or named in a way that hides the theorem's natural mechanism.**

This should not be romanticized. Many problems remain genuinely technically deep after the correct objects are known. But the Jacobian reconstruction gives a concrete example of how enormous apparent complexity can reside in a coordinate choice.

One can spend years studying coefficients of a polynomial map when the real object is a matrix.

One can catalog exceptional degrees when the real object is a quotient and a boundary ideal.

One can discover the vector `(1,3,3,1)` by linear algebra and regard it as exceptional, when it is simply the expansion of `(1+t)^3` forced by the geometry.

The research goal is therefore to find **the representation in which the theorem knows why it is true**.

## 17. Concrete next research questions

The most consequential next questions, in rough priority order, are:

1. **Reverse derivation:** derive the original dimension-three counterexample conceptually starting from `SL_2/T` and the boundary ideal, without reverse-engineering the known formula.
2. **Dimension two:** formulate and test a boundary-geometry obstruction that could explain why the same mechanism cannot exist for `A^2 -> A^2`.
3. **Coordinate-free classification:** reformulate canonical polynomializability as a sheaf/ideal statement on the quotient rather than the current chart calculation.
4. **Global extremality:** determine whether the `~3m` minimal-degree law survives beyond the fixed canonical chart.
5. **Compactification:** construct a uniform boundary model for the minimal families and explain escaping sheets geometrically.
6. **Phase transition:** replace low-degree squareful eliminations with one intersection/codimension theorem explaining the `3,4 | 5 | 6+` transition.
7. **Monodromy:** compute generic Galois groups and exceptional scalar loci for the degree-`m` recovery polynomials.
8. **Higher rank:** test whether analogous quotient/boundary constructions arise from `SL_n`, flag varieties, spherical varieties, or cluster charts.
9. **Orthogonal verification:** formalize the intersection/classification/surjectivity results using a proof assistant or CAS route independent of SymPy.
10. **Literature/priority:** compare the strengthened structure against all available recent work while preserving the unresolved Kistner–Shaska companion caveat.

## 18. Epistemic boundary

This memorandum intentionally mixes three levels and labels them here:

### Established inside the current project by exact computation / derivation

- the explicit `SL_2` matrix identity and factorization;
- the torus-invariant boundary products and discriminant-one quadric;
- the exact boundary ideal pullback identity;
- the second-Veronese associated-graded description;
- the fixed-chart canonical-potential classification and minimal directions as current-run derived theorems;
- exact low-degree surjectivity/non-surjectivity certificates and the current all-degree phase diagram, with the general high-degree theorem supported by two internal derivations.

These remain subject to the epistemic statuses recorded in `STATUS.md`; general theorems still warrant independent specialist/formal review.

### Inferences motivated by that structure

- `SL_2/T` may be the native mechanism behind the counterexample rather than a retrospective description;
- the dimension-three/dimension-two distinction may have a boundary-geometric explanation;
- the surjectivity transition may admit an intersection-theoretic explanation;
- the minimal degree spectrum may hint at a broader extremal principle.

### Speculative cross-problem heuristics

- other hard conjectures may hide a unifying object behind repeated exceptional patterns;
- progress may come from finding representations that compress many partial phenomena simultaneously;
- this heuristic may be useful for RH, P versus NP, Navier–Stokes, arithmetic geometry, and other problems, but **no substantive result on those problems follows from the Jacobian work itself**.

That separation should be preserved in future use of this memorandum.
