# Incoming acquisition contract

This directory documents artifacts needed to close the current correctness/novelty audit. Do not commit credentials, cookies, browser profiles, or unrelated private exports.

## Provenance corpus is closed

The owner has confirmed that the Jacobian archives already supplied contain **all BLIND-session conversational history that still exists or is available to provide**. Do not ask Codex/Luna or any acquisition agent to search for additional raw BLIND 1/3/4/5 conversations or the sibling message that suggested `k[a,W] ∩ k[x,y,z]`. Treat the existing raw BLIND 2 conversation, raw verification conversation, BLIND 1–5 findings packages, retrospective histories, scripts, and audit artifacts as the complete available provenance corpus.

This is an evidence limitation to record, not an acquisition task.

## P0 — Kistner–Shaska ancillary package

Acquire the original arXiv source/ancillary bundle for:

- arXiv: `2608.02863`
- `https://arxiv.org/e-print/2608.02863`
- alternate: `https://arxiv.org/src/2608.02863`

Preserve the original bundle bytes and SHA-256 outside the public repo if redistribution status is unclear.

Highest-priority file named by the paper:

`balanced_minimal_models_companion.pdf`

Approximate title:

*Differential obstructions and minimal models for balanced graded Keller maps*.

Also inventory every ancillary script/certificate/log in the submission.

### Required comparison questions

1. Does the companion state or imply an intersection theorem equivalent to
   `k[a,W] ∩ k[x,y,z] = k[W,b,c]/(cW-b(b-1))`?
2. Does it contain a filtration equivalent to
   `delta(m)=3m` for even `m` and `3m+2` for odd `m`?
3. Does it prove a minimal-degree result that subsumes the chart-relative degree-17 canonical-potential theorem?
4. Does it contain the same unique hidden-degree-5 direction `a^2(1+aW)^3`, perhaps in different graded coordinates?
5. Does it state a jet condition equivalent to `H(t)=1+t+(1+t)^3R(t)`?

Record exact theorem/lemma/page references rather than only semantic similarity.

## P1 — independent CAS audit

Deferred until the repository acquisition/provenance layer is settled.

Preferred independent tools: SageMath/Singular, standalone Singular, or Macaulay2. This audit should be orthogonal to the existing SymPy checks and should distinguish finite computational evidence from proofs of infinite intersection statements.
