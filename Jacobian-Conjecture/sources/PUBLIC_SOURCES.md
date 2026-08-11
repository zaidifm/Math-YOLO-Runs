# Public source map — Jacobian counterexample aftermath

**Checkpoint:** 2026-08-11

This file tracks public work relevant to distinguishing independently useful BLIND-session mathematics from results already in the literature.

## Core public references

### Aaron Lou — counterexample derivation

Public derivation of the announced counterexample mechanism using a linear factor times a quadratic factor, with resultant normalization and explicit polynomialization.

- `https://aaronlou.com/jacobian_counterexample_derivation.pdf`

Relevance: likely contains the substance behind BLIND 4's later normalized-gradient formulation.

### Tanush Shaska — graded/invariant structure

- arXiv: `2607.20210`
- `https://arxiv.org/abs/2607.20210`

Relevance: invariant quotient, cubic fiber equation, generic degree three, monodromy, discriminant/nonproperness, and explicit escape of preimages to infinity.

### Christopher Long — Gaussian Moments / Jacobian consequences

- arXiv: `2607.18186`
- `https://arxiv.org/abs/2607.18186`

Relevance: consequences of the Jacobian disproof and use of classical reductions in the reverse direction.

### Gao — higher-dimensional counterexamples

- arXiv: `2608.00222`
- title: *Counterexamples to the Jacobian conjecture in dimensions greater than two*
- `https://arxiv.org/abs/2608.00222`

Relevance: tangent-sweep geometry, counterexamples in all dimensions greater than two, arbitrarily large generic fiber degree, nonproperness at infinity.

### Kyle Kistner and Tanush Shaska — graded Keller maps

- arXiv: `2608.02863`
- `https://arxiv.org/abs/2608.02863`
- source/ancillary bundle: `https://arxiv.org/e-print/2608.02863`

Relevance: general lift conditions, graded constructions, monodromy/moduli, boundary semigroups, minimal-model program.

**Critical unresolved dependency:** the arXiv submission references an ancillary companion preprint named

`balanced_minimal_models_companion.pdf`

with title approximately

*Differential obstructions and minimal models for balanced graded Keller maps*.

The current ChatGPT runtime can read the main paper but cannot directly ingest the gzip arXiv source bundle. This companion must be acquired and compared before any priority claim about the BLIND 2 degree-17/minimality result.

## Classical structural context

### Danielewski surfaces

The reconstructed BLIND 2 boundary surface

\[
cW=b(b-1)
\]

is of classical Danielewski form `XY=p(Z)`, here with `p(Z)=Z(Z-1)`.

This identification does not by itself imply that the specific Jacobian-chart intersection theorem is already in the literature. It supplies the correct existing language for smoothness, normality, locally nilpotent derivations, and boundary completions.

## Current novelty-matching status

### Clearly public in substance

- hidden/generic cubic recovery;
- generic fiber degree 3;
- `S_3` monodromy;
- discriminant and nonproperness;
- sheets escaping to infinity;
- tangent-sweep mechanism;
- higher-dimensional generalizations;
- arbitrarily large generic fiber degree;
- broad graded quotient/lift theory;
- normalized-resultant picture underlying the BLIND 4 gradient identity.

### Not matched by an indexed statement found so far

- `k[a,W] ∩ k[x,y,z] = k[W,b,c]/(cW-b(b-1))` in this reciprocal chart;
- the induced exact two-filtration law `delta(m)`;
- the explicit derivation of the BLIND 4 two-jet criterion as a slice of that intersection ring.

### Provisional / blocked on ancillary comparison

- chart-relative degree-17 canonical-potential minimality and uniqueness of the hidden-degree-5 direction.

## Research rule

Do not infer novelty from absent search hits. Mathematical equivalence under different coordinates, ancillary material, non-indexed notes, and very recent revisions must be checked separately from correctness.
