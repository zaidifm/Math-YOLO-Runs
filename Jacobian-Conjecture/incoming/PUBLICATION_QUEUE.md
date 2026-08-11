# Approved publication queue

Authority: owner publication criteria clarified 2026-08-11; archive review completed the same day.

The publication-safe derivatives listed below have now also been staged durably in the ChatGPT Library under:

`/YOLO Math Runs/Jacobian Conjecture YOLO Run/Public Release Candidates/2026-07-23/`

The canonical approved historical archive is retained under:

`/YOLO Math Runs/Jacobian Conjecture YOLO Run/Historical Public Release/2026-07-23/`

They remain **not yet published to GitHub** until a raw-git/Codex or other exact-byte push is completed and read back. Staging in the Library does not change publication status.

These files are approved for a raw-git/Codex push into `Jacobian-Conjecture/historical/2026-07-23/`.

| Destination filename | SHA-256 | Size | Source |
|---|---|---:|---|
| `Jacobian_Full_Research_Archive_2026-07-23.zip` | `19eb2d7b5f4eaaf460428709caff68c4dff3803bb27b3ae7287c1b2cb67a60b6` | 572,198 | retained Jacobian Library evidence |
| `BLIND2_VISIBLE_TRANSCRIPT.md` | `1a0eabf86c0e50e9ddb1067ac02f62f770c5e4254f3f1b5b8ae73297de353843` | 54,601 | `conversation.md` from BLIND 2 export |
| `VERIFICATION_VISIBLE_TRANSCRIPT.md` | `6a5df451970ae781827683ab87093909e5296103375a63267ffb98d93320b072` | 168,177 | `conversation.md` from verification export |
| `boundary_ring_coordinate_diagram.png` | `b11b5272578c822d09b2fa33dcb2db62223bbd7f34f9767efb32ff7915966149` | 168,291 | BLIND 2 generated artifact |
| `boundary_ring_degree_semigroup.png` | `665bdb2640a63ea16870136347bcdf2566873ae138f1a5e5ac25d845b522b11b` | 132,281 | BLIND 2 generated artifact |

## Do not publish directly

- `Jacobian_Conjecture_yolo_run.zip` as a whole.
- Either raw backend `conversation.json`.
- Any future artifact containing unrelated private-life material, passwords, API keys, authentication cookies/tokens, private keys, SSNs, or other secrets.

## Explicitly allowed

- `S. Ali Zaidi` and `ali@zaidi.fm` attribution.
- Experiment-specific prompts, including informal/absurd YOLO prompts.
- Ordinary conversation UUIDs/IDs and model/tool metadata when they occur in visible research material.
- Public-source citations and public third-party contact metadata naturally included in research sources.

## Verification after push

1. Compute SHA-256 for every pushed artifact and match this table exactly.
2. Read back the committed files from GitHub.
3. Do not regenerate, rewrap, normalize line endings, or recompress the historical ZIP.
4. Update this file by moving successfully published rows into a `Published` section with the commit SHA.
