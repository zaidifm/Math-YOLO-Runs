# Approved publication queue

Authority: owner publication criteria clarified 2026-08-11; archive review completed the same day.

## Current publication plan

The owner has chosen a **browsable non-ZIP GitHub release** rather than mirroring the approved July archive as one opaque ZIP.

The original archive remains the immutable provenance anchor in the ChatGPT Library:

- `Jacobian_Full_Research_Archive_2026-07-23.zip`
- size: 572,198 bytes
- SHA-256: `19eb2d7b5f4eaaf460428709caff68c4dff3803bb27b3ae7287c1b2cb67a60b6`

A canonical expanded Git tree has been prepared and round-trip verified in the ChatGPT runtime. It contains **124 files** and publishes:

- canonical expanded BLIND 1–5 packages;
- both historically distinct BLIND 3 packages;
- the unique independent boundary-audit script/log;
- verification logs;
- original archive inventories, checksums, duplicate report, and tree record;
- archive-level synthesis/search/verification reports;
- publication-safe visible BLIND 2 and verification transcripts;
- the two boundary-ring diagrams;
- `EXTRACTION_MAP.md`, documenting every path transformation and omitted redundant nested ZIP wrapper;
- `PUBLISHED_TREE_SHA256.txt`, pinning every published file byte-for-byte.

Nested package ZIP wrappers and redundant byte-identical workspace copies are **not** to be committed. Their original paths, sizes, and SHA-256 values are recorded in `EXTRACTION_MAP.md` and in the preserved original archive manifests.

## Courier staging artifact

The exact prepared tree is available in the ChatGPT Library at:

`/YOLO Math Runs/Jacobian Conjecture YOLO Run/Courier Staging/Jacobian_Historical_Expanded_Git_Staging_2026-08-11.tar.zst`

Transport artifact:

- size: 414,534 bytes
- SHA-256: `96283072261cf7124dc1d833c01b7806b199e7ede79d9e85d8c7190f3a660d1b`

The transport archive is **not** a publication target. It exists only to move the organized directory tree to a normal raw-git client. It was decompressed into a fresh directory after creation; all 124 file SHA-256 values matched the source tree exactly.

### Required raw-git destination

Extract the transport artifact and copy its contents into:

`Jacobian-Conjecture/historical/2026-07-23/`

The resulting repository should therefore contain paths such as:

- `historical/2026-07-23/EXTRACTION_MAP.md`
- `historical/2026-07-23/PUBLISHED_TREE_SHA256.txt`
- `historical/2026-07-23/archive/packages/blind2/...`
- `historical/2026-07-23/transcripts/BLIND2_VISIBLE_TRANSCRIPT.md`
- `historical/2026-07-23/diagrams/boundary_ring_coordinate_diagram.png`

Do not add the `.tar.zst` itself to GitHub.

## Previously approved derivative identities

| Published-tree file | SHA-256 | Size |
|---|---|---:|
| `transcripts/BLIND2_VISIBLE_TRANSCRIPT.md` | `1a0eabf86c0e50e9ddb1067ac02f62f770c5e4254f3f1b5b8ae73297de353843` | 54,601 |
| `transcripts/VERIFICATION_VISIBLE_TRANSCRIPT.md` | `6a5df451970ae781827683ab87093909e5296103375a63267ffb98d93320b072` | 168,177 |
| `diagrams/boundary_ring_coordinate_diagram.png` | `b11b5272578c822d09b2fa33dcb2db62223bbd7f34f9767efb32ff7915966149` | 168,291 |
| `diagrams/boundary_ring_degree_semigroup.png` | `665bdb2640a63ea16870136347bcdf2566873ae138f1a5e5ac25d845b522b11b` | 132,281 |

## Do not publish directly

- `Jacobian_Conjecture_yolo_run.zip` as a whole.
- Either raw backend `conversation.json`.
- The `.tar.zst` courier artifact.
- Redundant nested package ZIP wrappers from the July archive.
- Any future artifact containing unrelated private-life material, passwords, API keys, authentication cookies/tokens, private keys, SSNs, or other secrets.

## Explicitly allowed

- `S. Ali Zaidi` and `ali@zaidi.fm` attribution.
- Experiment-specific prompts, including informal/absurd YOLO prompts.
- Ordinary conversation UUIDs/IDs and model/tool metadata when they occur in visible research material.
- Public-source citations and public third-party contact metadata naturally included in research sources.

## Verification after push

1. Check out the resulting commit into a clean worktree.
2. Verify every line of `PUBLISHED_TREE_SHA256.txt` against the committed files.
3. Confirm that neither the transport `.tar.zst` nor the original July ZIP nor the private evidence master was committed.
4. Read back representative reports, scripts, transcripts, and both PNGs from GitHub.
5. Update this file with the publication commit SHA and mark the queue **COMPLETE**.
