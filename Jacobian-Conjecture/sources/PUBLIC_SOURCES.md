# Public source map — Jacobian counterexample aftermath

**Checkpoint:** 2026-08-11

This file tracks public work relevant to distinguishing independently useful BLIND-session mathematics from results already in the literature. Literature matching and mathematical correctness are separate questions.

## Core public references

### Aaron Lou — counterexample derivation

Public derivation of the announced counterexample mechanism using a linear factor times a quadratic factor, with resultant normalization and explicit polynomialization.

- `https://aaronlou.com/jacobian_counterexample_derivation.pdf`

Relevance: likely contains the substance behind BLIND 4's later normalized-gradient formulation.

### Tanush Shaska — graded/invariant structure

- arXiv: `2607.20210`
- `https://arxiv.org/abs/2607.20210`
- untouched source bundle acquired 2026-08-11
- SHA-256: `abf541b7e211d5ef0b14145ddb303f0cc34cb959fa7bec17f9efac1f6e3eadc9`

Acquired bundle contents:

- `00README.json`
- `sh-131-latest.tex`
- `sh-131-macro.tex`

No separately listed ancillary PDF, script, notebook, or certificate is present in the acquired bundle.

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
- original source endpoint: `https://arxiv.org/e-print/2608.02863`
- untouched source bundle acquired 2026-08-11
- SHA-256: `3f31ed51b3589cc41ba51aa140632fcaff74da92fa85442492d96069583994ce`

Acquired bundle contents:

- `00README.json`
- `main.tex`
- `sh-132-macro.tex`
- `sh-132-ref.tex`
- `sh-132.tex`

Relevance: general lift conditions, graded constructions, monodromy/moduli, boundary semigroups, minimal-model program.

#### Missing cited companion

The source text cites a companion preprint named:

`balanced_minimal_models_companion.pdf`

approximately titled *Differential obstructions and minimal models for balanced graded Keller maps*.

The acquired arXiv bundle does **not** contain it. Bounded checks found:

- no ancillary-download entry on the arXiv format page;
- HTTP 404 from the canonical ancillary candidate URL;
- no retained local copy on the acquisition courier machine.

**Status: NOT PUBLICLY LOCATED as of 2026-08-11.**

This is an explicit literature-coverage limitation. It blocks complete priority comparison for claims potentially overlapping differential obstructions/minimal models, especially the chart-relative degree-17 result. It does not justify inferring absence of overlap.

### Independent Lean verification record — Zenodo 10.5281/zenodo.21514514

- DOI: `10.5281/zenodo.21514514`
- title: *An Independent Lean 4 Verification of the Alpöge–Fable Counterexample*
- creator: Pablo Nogueira Grossi / G6 LLC
- exact API metadata acquired 2026-08-11
- metadata JSON SHA-256: `99887565b0261c816f4e80d1d21fe1516b1aecd917aa9f9aaf2cd49bd552afbf`

The record contains exactly one attached file:

- `Screenshot 2026-07-16 at 4.18.13 PM.png`
- 33,833 bytes
- Zenodo checksum: `md5:5507ed840f46bff0672db5cb45a117e0`
- local SHA-256: `2e8f70ba575f05d9f6d525751c354538758c9e2834080380566b644e71e7faa2`

The record description contains the Lean formalization and identifies the external code repository `https://www.github.com/TOTOGT/jacobian/`; the Zenodo deposit itself contains no separate Lean source archive.

Relevance: independent formal verification of the determinant and collision computation and a useful attribution/verification ledger, not a source for the boundary-ring/minimality claims.

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

### Provisional / literature-coverage caveat

- chart-relative degree-17 canonical-potential minimality and uniqueness of the hidden-degree-5 direction.

The missing Kistner–Shaska companion prevents a fully closed priority statement on the last item unless an authentic copy later becomes available or equivalent public content can be ruled in/out by another source.

## Research rule

Do not infer novelty from absent search hits or absent ancillary files. Mathematical equivalence under different coordinates, non-indexed notes, very recent revisions, and unavailable cited material must be distinguished from a genuine negative literature result.
