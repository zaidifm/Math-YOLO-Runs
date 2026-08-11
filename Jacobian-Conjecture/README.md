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
- [`PROVENANCE.md`](PROVENANCE.md) — what came from which BLIND session, later synthesis, and public-source acquisition provenance.
- [`docs/Jacobian_Blind_Math_Forensics_2026-08-11.md`](docs/Jacobian_Blind_Math_Forensics_2026-08-11.md) — current technical reconstruction.
- [`scripts/jacobian_blind_bridge_verify.py`](scripts/jacobian_blind_bridge_verify.py) — independent exact SymPy checks for the cross-BLIND identities.
- [`sources/PUBLIC_SOURCES.md`](sources/PUBLIC_SOURCES.md) — public literature map and current overlap assessment.
- [`sources/ACQUISITION_MANIFEST_2026-08-11.md`](sources/ACQUISITION_MANIFEST_2026-08-11.md) — exact source-bundle identities, file inventories, hashes, and the missing-companion status.
- [`incoming/ACQUISITION.md`](incoming/ACQUISITION.md) — closed P0/P1 acquisition ledger and any genuinely outstanding courier needs.
- [`incoming/PUBLICATION_QUEUE.md`](incoming/PUBLICATION_QUEUE.md) — approved first-party artifacts awaiting public historical mirroring.

## Evidence boundary

The underlying private archive contains the raw BLIND 2 and verification conversations, plus BLIND 1–5 findings packages and retrospective histories. Most BLIND supplementary histories are not exact raw platform transcripts. The owner has confirmed that this is the complete available BLIND provenance corpus; additional raw BLIND 1/3/4/5 conversations are not an open retrieval task. Raw private exports are intentionally **not** mirrored into this public repository.

## Public-source state

The original arXiv source bundles for `2607.20210` and `2608.02863`, plus the exact Zenodo record `10.5281/zenodo.21514514`, were acquired and hash-pinned on 2026-08-11. The Kistner–Shaska paper cites `balanced_minimal_models_companion.pdf`, but that file is absent from the deposited arXiv source bundle and was **NOT PUBLICLY LOCATED** in bounded acquisition checks.

That unavailable companion is a literature-coverage limitation, not an unfinished courier task and not evidence that the companion lacks overlapping mathematics.

## Epistemic status

The strongest current candidate for genuinely unmatched mathematics is the exact boundary/intersection algebra and its induced degree filtration. Exact symbolic checks pass and no defect has yet been found in the valuation/normality proof, but theorem-by-theorem public-source comparison, external specialist review, and an independent non-SymPy CAS/formal audit remain outstanding.

Novelty is provisional. In particular, the chart-relative degree-17 claim cannot receive a fully closed priority assessment while the cited Kistner–Shaska companion remains unavailable for inspection.
