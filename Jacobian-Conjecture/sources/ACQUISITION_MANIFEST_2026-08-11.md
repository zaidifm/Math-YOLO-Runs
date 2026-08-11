# Public-source acquisition manifest — 2026-08-11

This manifest records the exact public-source artifacts acquired for the Jacobian correctness/priority audit. The third-party source bundles themselves are retained outside this public repository; this file preserves identities, contents, and acquisition status in accordance with the repository's public-source boundary.

Acquisition was performed by a Codex Luna courier operating from the owner's MacBook. The courier was instructed to preserve downloaded bytes and perform no mathematical analysis.

## P0 — Kistner–Shaska, arXiv:2608.02863

Original source endpoint: `https://arxiv.org/e-print/2608.02863`

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `arxiv-2608.02863-source-original` | 63,134 | `3f31ed51b3589cc41ba51aa140632fcaff74da92fa85442492d96069583994ce` |
| `FILELIST.txt` | 372 | `04062cf000b647d303d8c72b5ed93dafa8379cb5664b9fa5370525f71d78063b` |
| source `SHA256SUMS.txt` receipt | 163 | `77875c0ebaea77deeb7f7d1ef4f87ce968f5a9f0bd628770676a171c006a4b6b` |
| `COMPANION_STATUS.txt` | 398 | `920899e9667d0106305f3def2236b83d5dffa60ec0d6f666e08f9981aae605c6` |

Mechanical bundle contents:

- `00README.json`
- `main.tex`
- `sh-132-macro.tex`
- `sh-132-ref.tex`
- `sh-132.tex`

### Companion status

The paper cites `balanced_minimal_models_companion.pdf`, approximately titled *Differential obstructions and minimal models for balanced graded Keller maps*.

Bounded checks found:

- file absent from the acquired source bundle;
- no ancillary-download entry exposed on the arXiv format page;
- canonical ancillary candidate returned HTTP 404;
- no retained local copy found on the courier machine.

**Status: NOT PUBLICLY LOCATED.**

This is a literature-coverage limitation, not evidence that the companion contains no overlapping result.

## P1-A — Zenodo DOI 10.5281/zenodo.21514514

Record title: *An Independent Lean 4 Verification of the Alpöge–Fable Counterexample*.

The API metadata reports exactly one attached file.

| Artifact | Bytes | SHA-256 | Upstream checksum |
|---|---:|---|---|
| `ZENODO_METADATA.json` | 18,592 | `99887565b0261c816f4e80d1d21fe1516b1aecd917aa9f9aaf2cd49bd552afbf` | n/a |
| `Screenshot 2026-07-16 at 4.18.13 PM.png` | 33,833 | `2e8f70ba575f05d9f6d525751c354538758c9e2834080380566b644e71e7faa2` | `md5:5507ed840f46bff0672db5cb45a117e0` |
| `FILELIST.txt` | 159 | `f9ea346c039fb6f47b95c9f06ff0d483b2e923bdbbd95deb8d0e098bc96ffa24` | n/a |
| local `SHA256SUMS.txt` | 367 | `9f3a99d55a72d6e0a4349558f91f07c9be593d85f5ce9ce260224ae63adc9979` | n/a |

The record description contains the Lean source text and points to the external repository `https://www.github.com/TOTOGT/jacobian/`; no separate Lean archive is attached to the Zenodo deposit.

## P1-B — Shaska, arXiv:2607.20210

Original source endpoint: `https://arxiv.org/e-print/2607.20210`

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `arxiv-2607.20210-source-original` | 45,266 | `abf541b7e211d5ef0b14145ddb303f0cc34cb959fa7bec17f9efac1f6e3eadc9` |
| `FILELIST.txt` | 242 | `3b22842d7bc7ded95510b0a9fb61c34d64189f59590eb5762398cbcd46ecff53` |
| source `SHA256SUMS.txt` receipt | 183 | `ea4088c0fd65e2db3a96a235b46c1d64d16121022339545deb1b0fcf21af1159` |

Mechanical bundle contents:

- `00README.json`
- `sh-131-latest.tex`
- `sh-131-macro.tex`

No separately listed ancillary PDF, script, notebook, or certificate is present.

## Integrity note

The source-bundle SHA-256 values above were independently recomputed in the ChatGPT runtime after receipt and matched the courier-provided values for both arXiv bundles and the Zenodo attachment/metadata.

No original source bundle was recompiled, recompressed, or substituted during intake.