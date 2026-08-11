# Evidence publication manifest

Publication review completed 2026-08-11.

| Artifact | Size (bytes) | SHA-256 | Status |
|---|---:|---|---|
| `Jacobian_Full_Research_Archive_2026-07-23.zip` | 572,198 | `19eb2d7b5f4eaaf460428709caff68c4dff3803bb27b3ae7287c1b2cb67a60b6` | **APPROVED FOR PUBLIC MIRROR** |
| `Jacobian_Conjecture_yolo_run.zip` | 2,883,193 | `3f57ece815991c1a0299ed98677ce32458f07d36291311e2364bee9774926876` | **PRIVATE EVIDENCE MASTER; PUBLISH DERIVATIVES ONLY** |

## Review result

The archives were recursively inspected for unrelated personal-life content and for security-sensitive material. No unrelated discussions of family, relationships, health, politics, finances, or other private-life matters were found in the Jacobian corpus. No API keys, passwords, bearer tokens, authentication cookies, private keys, or Social Security numbers were found in the approved publication material.

`S. Ali Zaidi` and `ali@zaidi.fm` occur throughout the research reports as deliberate attribution and are approved for publication.

## Why the raw YOLO ZIP remains an evidence master

The larger ZIP contains the raw backend `conversation.json` graphs for BLIND 2 and the later verification conversation. Those payloads include backend-only metadata and hidden reasoning-related fields. They are unnecessary for public mathematical provenance and are therefore not approved for direct mirroring.

The following derivatives from that archive are approved:

- visible `conversation.md` transcript for BLIND 2;
- visible `conversation.md` transcript for the verification conversation;
- generated mathematical code, reports, logs, certificates, and diagrams.

The original raw ZIP remains hash-pinned so future provenance disputes can be checked against the retained master without publishing backend-only data.

## Known provenance limitations

- Raw platform conversation exports are available for BLIND 2 and the later verification conversation.
- Most BLIND 1/3/4/5 supplementary histories in the July research archive are retrospective reconstructions rather than complete raw platform transcripts.
- A future acquisition run may still search the owner's local historical exports for raw BLIND 1, BLIND 3 variants, BLIND 4, BLIND 5, and the exact sibling message that proposed `k[a,W] ∩ k[x,y,z]`.

## Handling rule

Publication decisions are content-based: exclude unrelated private-life material, credentials/secrets, and backend-only hidden reasoning. Ordinary research attribution, public contact information, conversation identifiers, UUIDs, and experiment-specific prompts are not redaction targets under the owner's stated policy.