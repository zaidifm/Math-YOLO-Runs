# Jacobian Conjecture

## Current focus

The classical Jacobian Conjecture was refuted in dimension three in July 2026. This directory audits and extends private BLIND-session work performed immediately after the announced counterexample, with emphasis on structures that are not yet clearly matched by the public literature.

The main candidate structure is the reciprocal-chart boundary/intersection algebra

\[
k[a,W]\cap k[x,y,z]
\stackrel{?}{=}
k[W,b,c]/(cW-b(b-1)),
\qquad b=1+aW,\ c=ab.
\]

Current work connects this to:

1. a Danielewski-surface completion of the hidden reciprocal chart;
2. an exact hidden-degree/source-degree filtration;
3. chart-relative canonical-potential minimality with first hidden degree-5 direction at source degree 17;
4. the BLIND 4 finite/two-jet polynomialization criterion;
5. a locally nilpotent derivation extending \(\partial/\partial a\);
6. the public binary-cubic/resultant/normalized-gradient picture.

## Start here

- [`STATUS.md`](STATUS.md) — verified frontier and unresolved obligations.
- [`PROVENANCE.md`](PROVENANCE.md) — what came from which BLIND session, later synthesis, and public work.
- [`docs/Jacobian_Blind_Math_Forensics_2026-08-11.md`](docs/Jacobian_Blind_Math_Forensics_2026-08-11.md) — current technical reconstruction.
- [`scripts/jacobian_blind_bridge_verify.py`](scripts/jacobian_blind_bridge_verify.py) — independent exact SymPy checks for the cross-BLIND identities.
- [`incoming/ACQUISITION.md`](incoming/ACQUISITION.md) — artifacts still needed from a Mac/Codex acquisition run.
- [`sources/PUBLIC_SOURCES.md`](sources/PUBLIC_SOURCES.md) — public literature map and unresolved priority caveat.

## Evidence boundary

The underlying private archive contains the raw BLIND 2 and verification conversations, plus BLIND 1–5 findings packages and retrospective histories. Most BLIND supplementary histories are not exact raw platform transcripts. Raw private exports are intentionally **not** mirrored into this public repository.

## Epistemic status

The strongest current candidate for genuinely unmatched mathematics is the exact boundary/intersection algebra and its induced degree filtration. Exact symbolic checks pass and no defect has yet been found in the valuation/normality proof, but external specialist review and an independent CAS/formal audit remain outstanding. Novelty is provisional until the Kistner–Shaska ancillary companion preprint and any other non-indexed recent work are compared theorem by theorem.
