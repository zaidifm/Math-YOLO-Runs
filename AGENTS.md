# AGENTS.md

## Purpose

Use this repository as a durable, replayable workspace for mathematical research runs. Optimize for correctness, provenance, falsifiability, and restartability rather than rhetorical completeness.

## Claim status

Tag substantive claims internally as one of:

- **SUPPLIED** — supplied by the owner, another model, a paper, or another external source.
- **DERIVED** — reasoned in the current run but not independently checked.
- **COMPUTED** — supported by an exact or rigorous computation with an artifact.
- **VERIFIED** — independently rederived or checked by a second route/tool/source.
- **CONJECTURED** — plausible but unproved.
- **BROKEN** — falsified; preserve the counterexample and reason for failure.

Never collapse DERIVED into VERIFIED merely because the derivation looks plausible.

## Verification discipline

1. Preserve exact scripts and raw verifier output for computational claims.
2. Prefer independent methods for important results: e.g. symbolic algebra plus CAS, or proof plus formalization.
3. State the scope of minimality, uniqueness, and universality claims precisely.
4. Treat literature matching and mathematical correctness as separate questions.
5. Preserve failed routes when they explain why a representation or hypothesis is inadequate.

## Public-repository boundary

This repository is public. Do not commit:

- raw private ChatGPT conversation exports;
- credentials, cookies, browser state, tokens, or secrets;
- private evidence unrelated to a publishable mathematical claim;
- third-party PDFs/source bundles unless redistribution is clearly appropriate.

Use manifests and hashes to reference private or externally hosted evidence. Publication-safe extracts may be committed only when they contain no unrelated private material.

## Project structure

Each research project should keep, as applicable:

- `README.md` — orientation and current question;
- `STATUS.md` — current frontier, verified results, open obligations;
- `PROVENANCE.md` — who/what supplied or derived each major result;
- `docs/` — mathematical notes and audits;
- `scripts/` — executable verification/reconstruction;
- `verification/` — verifier instructions and results;
- `sources/` — source map, citations, hashes, acquisition status;
- `incoming/` — explicit contract for artifacts that still need acquisition/review.

Do not overwrite historical evidence merely to make the narrative cleaner. Add corrections and superseding notes instead.
