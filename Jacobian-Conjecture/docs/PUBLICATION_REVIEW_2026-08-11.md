# Jacobian archive publication review — 2026-08-11

## Scope

Reviewed the retained evidence copies of:

- `Jacobian_Full_Research_Archive_2026-07-23.zip`
- `Jacobian_Conjecture_yolo_run.zip`

The review criterion supplied by the owner is intentionally permissive about research-related identity/provenance metadata. Public name/email, conversation IDs, UUIDs, unusual prompts, and experiment-specific model/tool records are not considered sensitive by themselves. The exclusion targets are unrelated private-life material, credentials/secrets, highly sensitive identifiers such as SSNs, and backend-only hidden reasoning that does not belong in a public research record.

## Archive structure

### July 23 full research archive

- 188 ZIP members.
- Consolidates BLIND 1–5 reports/packages, the two BLIND 3 variants, scripts, verification logs, checksums, and a comprehensive synthesis.
- Does **not** contain raw platform `conversation.json` graphs.
- Contains retrospective conversation-history reports for most blinds.

### YOLO export archive

- 61 top-level ZIP members, including nested packages.
- Contains complete raw backend exports for BLIND 2 and the later verification conversation:
  - `conversation.json`
  - `conversation.md`
  - export receipts/checksums
  - generated files and attachments.
- Also contains copies of the July full research archive and BLIND findings packages.

## Privacy scan

A recursive text scan was performed across extracted material. Targeted searches included known unrelated personal names/topics and generic privacy/security terms. The review found:

- no unrelated family/relationship discussions;
- no unrelated health discussions;
- no unrelated political/work/project discussions;
- no personal financial discussions;
- no Social Security numbers;
- no API keys, passwords, bearer tokens, private keys, or authentication cookies in the approved publication material.

The only recurring owner email in the July research archive is `ali@zaidi.fm`, used as deliberate attribution. Public-source email addresses also occur inside raw web-search output in the backend export; these are not private owner data.

Targeted known-person searches found no unrelated references to Husain/Hussein, Sophie, Alyssa, Qasim, Remus/Remy, or Avani in the reviewed mathematical corpus.

## Attachments

Two user-uploaded image attachments occur in the BLIND 2 raw export. They were visually inspected. They concern the Jacobian announcement/context and contain no unrelated private-life content. They are not necessary to establish the boundary-ring mathematics and are optional for public release.

Generated boundary-ring diagrams are mathematical artifacts and are approved for publication.

## Why `conversation.json` is excluded

The raw backend JSON includes substantially more than the visible conversation:

- backend node/message identifiers;
- workspace/account metadata;
- model/tool metadata and raw search payloads;
- internal reasoning-related fields not present in the visible transcript.

No credential leak was identified, and ordinary IDs are not the concern. The reason for exclusion is that the backend-only hidden-reasoning material is neither necessary nor appropriate as a public mathematical artifact. Public provenance should use the visible `conversation.md` transcripts plus stable hashes of the retained raw evidence masters.

## Publication classification

### GREEN — publish

- full July 23 research archive as originally packaged;
- reports, scripts, logs, certificates, checksums;
- visible BLIND 2 transcript;
- visible verification transcript;
- generated mathematical diagrams;
- current provenance/status/forensics documents.

### YELLOW — publish only with context

- retrospective BLIND 1/3/4/5 conversation histories, because they are reconstructions rather than exact platform transcripts;
- early research claims later narrowed, corrected, or superseded. These should remain historically preserved but be read against the current `STATUS.md` and provenance review.

### RED — do not directly mirror

- raw backend `conversation.json` payloads;
- any future artifact containing credentials/secrets or genuinely unrelated private-life material.

## Conclusion

No reason was found to suppress the Jacobian mathematical archive for embarrassment or unrelated personal privacy. The principal curation requirement is epistemic rather than reputational: distinguish historical model claims from currently verified results, and distinguish retrospective histories from raw visible transcripts.