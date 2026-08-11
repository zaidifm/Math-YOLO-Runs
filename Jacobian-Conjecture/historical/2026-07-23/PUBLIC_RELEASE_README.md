# Jacobian historical public release — 2026-07-23

Publication review completed 2026-08-11.

## Decision

The mathematical contents of the retained Jacobian archives contain **no unrelated personal-life material** found in the review. The owner's supplied attribution `S. Ali Zaidi` / `ali@zaidi.fm` is intentionally public.

The following artifacts are **approved for public mirroring**:

- `Jacobian_Full_Research_Archive_2026-07-23.zip`, byte-for-byte unchanged from the retained evidence copy.
- The visible Markdown transcript of BLIND 2.
- The visible Markdown transcript of the later verification conversation.
- BLIND-generated mathematical code, reports, logs, certificates, and diagrams.

The following are **not part of the public release**:

- raw backend `conversation.json` exports, because they contain backend-only metadata and hidden reasoning-related fields that are not needed to reproduce or assess the mathematical experiment;
- authentication material, if any is ever encountered;
- anything unrelated to the Jacobian/YOLO mathematics experiment.

The two user-uploaded screenshots in BLIND 2 were inspected and contain no unrelated personal material, but they are not necessary for the mathematical release.

## Privacy/security review

A recursive scan of the retained archives found no discussion of unrelated family, relationship, health, political, financial, or other private-life matters. Targeted searches included known personal names/topics as well as generic credential and sensitive-identifier patterns.

No API keys, passwords, bearer tokens, authentication cookies, private keys, or Social Security numbers were found in the approved publication set.

The larger raw YOLO export does contain ChatGPT backend metadata such as conversation/message/account identifiers. Those identifiers are not treated as sensitive under the owner's publication criteria, but the raw JSON is still excluded because the backend-only reasoning and machinery add no scientific value.

## Provenance warning

Most BLIND 1/3/4/5 supplementary histories are retrospective reconstructions rather than raw platform transcripts. Raw platform provenance is strongest for BLIND 2 and the later verification conversation. See `../../PROVENANCE.md` and `../../docs/Jacobian_YOLO_Process_Review.md`.

## Approved-artifact SHA-256 values

```text
19eb2d7b5f4eaaf460428709caff68c4dff3803bb27b3ae7287c1b2cb67a60b6  Jacobian_Full_Research_Archive_2026-07-23.zip
1a0eabf86c0e50e9ddb1067ac02f62f770c5e4254f3f1b5b8ae73297de353843  BLIND2_VISIBLE_TRANSCRIPT.md
6a5df451970ae781827683ab87093909e5296103375a63267ffb98d93320b072  VERIFICATION_VISIBLE_TRANSCRIPT.md
b11b5272578c822d09b2fa33dcb2db62223bbd7f34f9767efb32ff7915966149  boundary_ring_coordinate_diagram.png
665bdb2640a63ea16870136347bcdf2566873ae138f1a5e5ac25d845b522b11b  boundary_ring_degree_semigroup.png
```

## Repository-transfer status

The GitHub connector used for this review can write repository text directly but does not accept container-local binary/attachment paths as upload inputs. The approved large/binary artifacts and exact full transcripts therefore remain **approved and hash-pinned for the next raw-git/Codex push**, rather than being reconstructed through lossy copy/paste. This file is the authority for what that push may publish.