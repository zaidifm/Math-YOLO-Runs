# PROVENANCE — Jacobian Conjecture BLIND Work

## Evidence classes

The private source archive reviewed for this project contains:

- an exported raw BLIND 2 conversation;
- an exported raw verification conversation;
- BLIND 1–5 findings packages;
- retrospective supplementary histories for most BLIND sessions;
- exact scripts and audit artifacts.

Most supplementary BLIND histories are **not** raw platform transcripts. They preserve chronology and mathematical findings but do not preserve a perfect record of every timestamp, branch, hidden reasoning trace, or prompt insertion point.

The owner has confirmed that this is the **complete available BLIND conversational/provenance corpus**. Additional raw BLIND 1/3/4/5 conversations or sibling-source transcripts are not available and should not be requested from future Codex/Luna acquisition agents. Missing raw provenance is therefore a fixed evidence limitation, not an open retrieval task.

Raw private conversation exports are intentionally not committed to this public repository.

## BLIND-session provenance

### BLIND 1

Received an information-rich structural hint: dimension three, degree/monomial profiles, reciprocal-chart architecture, repeated `1+xy`, Jacobian-factor cancellation, and cubic inversion. Reconstructed coefficients/equivalent formulas.

**Status:** strong coefficient-blind reconstruction, not answer-free discovery.

### BLIND 2

Initially searched independently and failed in an overrestricted normalization. It was later supplied the exact hidden coordinates/map, so it should not be credited with independently discovering the base counterexample.

Its distinctive post-map work includes:

- shifted-boundary geometry;
- the identity `1 + aW = xK`;
- a degree-17 quintic/canonical-potential direction;
- computational minimality work;
- the boundary/intersection-ring theorem.

Causal sequence preserved by the raw conversation:

1. an early overrestricted normalization produced only a local obstruction;
2. the exact map/hidden coordinates were later supplied;
3. an early degree-30 threshold in one family was overgeneralized;
4. the owner asked for an explicit epistemic/strategic/tactical blind-spot audit;
5. a subsequent long exploration found `1 + aW = xK`, changing the natural boundary parameter from `aW` to `1+aW` and producing the degree-17 direction;
6. **afterward**, a sibling memo explicitly suggested the abstraction `k[a,W] ∩ k[x,y,z]`; BLIND 2 then formulated and proved the boundary-ring theorem.

Accordingly, the full intersection theorem is not provenance-clean as a wholly isolated BLIND 2 discovery: the crucial shifted coordinate arose in BLIND 2, while the explicit intersection-ring abstraction was later supplied by a sibling.

### BLIND 3

Two different packages were historically labeled BLIND 3.

The web-reviewed package is the strongest reconstruction experiment: it received only the birational architecture, not the coordinates or coefficients, and produced its own reciprocal chart and explicit constant-Jacobian noninjective polynomial map later shown equivalent in mechanism to the announced counterexample.

The other BLIND 3 package largely consolidates the BLIND 2 boundary-ring trajectory.

### BLIND 4

Initially failed twice, became skeptical, and overgeneralized narrow no-go results. After the explicit map forced a reset it developed:

- invariant binary-cubic factorization;
- normalized-gradient formulation;
- finite/two-jet polynomialization conditions;
- corrected boundary-surjectivity interpretation.

Current reconstruction shows the two-jet theorem is a one-variable slice of BLIND 2's boundary ring, while the normalized-gradient identity is probably a differential reformulation of the public resultant normalization.

A raw BLIND 4 platform transcript is not available; the supplied findings package and retrospective history are the authoritative surviving evidence for that run.

### BLIND 5

Reverse-engineering experiment. It was supplied the explicit counterexample and asked to derive mechanism and consequences. It should not be treated as an independent discovery run.

## Earlier 2026-08-11 synthesis

The initial ChatGPT audit added or made explicit several connections that were not cleanly stated in the archived blind reports:

1. recognition of `cW=b(b-1)` as a Danielewski surface;
2. interpretation of the hidden affine plane as the complement of one boundary component;
3. the bridge showing BLIND 4's jet condition is directly a boundary-ring condition;
4. extension of `∂/∂a` to the locally nilpotent derivation
   `D(W)=0`, `D(b)=W`, `D(c)=2b-1`;
5. interpretation of hidden `a`-degree as the induced LND filtration;
6. associated-graded leading relation `cW=b^2` and the `+1` shift as the smoothing/splitting of the double-root boundary cone.

These observations must not be back-attributed to the original BLIND sessions absent evidence already contained in the surviving corpus.

## 2026-08-11 blackboard synthesis — SL2 quotient and canonical classification

A later blackboard pass in the same ChatGPT thread, explicitly undertaken after the owner asked to stop relying on literature search and attack the structure algebraically, produced a stronger reorganization. These results are **current-run synthesis**, not BLIND-session results.

### Exact identities and computed structure

The audit introduced

- `v=1+2xy`;
- `L=-1+3xy+x^2z`;
- the existing `K=y+6xy^2+xz+2x^2yz`;

and observed/checked the exact Bezout identity

`xK-vL=1`.

This yields the source matrix

`G=[[x,v],[L,K]] in SL_2`,

with an exact elementary matrix factorization. The earlier boundary generators are its torus-invariant matrix products:

- `W=xL`;
- `b=xK`;
- `b-1=vL`;
- `c=vK`.

Consequently the BLIND 2 boundary surface is reinterpreted as the affine torus quotient of `SL_2`, and on the big cell the relation `b=1+aW` is exactly the determinant-one exchange relation after torus normalization.

After setting `q=2b-1`, the boundary equation becomes `q^2-4cW=1`, a discriminant-one affine quadric. The previously isolated hidden LND extends to a full `sl_2` triple. These identities and commutators are **COMPUTED** exactly by the new verifier.

### Strengthened intersection proof

The new identity also gives

`(W,b)k[x,y,z]=(xL,xK)=x(L,K)=(x)`

because `xK-vL=1` forces `(L,K)=(1)`.

This identifies the missing boundary divisor's pullback scheme-theoretically, with multiplicity one, and sharpens the earlier valuation/normality argument for

`k[a,W] ∩ k[x,y,z]=R`.

The general divisorial argument is **DERIVED** in this run and is not yet externally/formally reviewed.

### Associated graded and degree filtration

The same pass computed the top forms of `(W,b,c)` and identified

`gr R = k[Wbar,bbar,cbar]/(cbar Wbar-bbar^2)`

with the second-Veronese/sign-invariant ring `k[s^2,st,t^2]`. With source weights `deg(s)=2`, `deg(t)=3`, hidden `a`-degree becomes the exponent of `t`. This makes the old parity formula

`delta_R(m)=3m` for even `m`, `3m+2` for odd `m`

a direct consequence of the sign-invariance parity constraint.

### Complete fixed-chart canonical-potential classification

A diagonal decomposition of `g in k[a,W]`, combined with the boundary valuation, yielded the current-run theorem candidate:

`h = h0 + alpha*a + beta + r`, with `r in I_D=(W,b) subset R`,

for the fixed reciprocal-chart canonical-potential construction. The `alpha*a` and `beta` terms are target translations, so modulo translations the polynomializable deformation space is the boundary ideal itself.

This statement is **DERIVED**, not yet independently verified. It strictly generalizes the BLIND 4 one-variable/two-jet slice; that criterion becomes the `d=2` boundary-divisibility case.

### Sharp spectrum and bounded validation

The classification gives the all-hidden-degree candidate spectrum

- `mu(m)=3m+2` for odd `m`;
- `mu(m)=3m+4` for even `m`;

with unique minimal representatives `bc^r` for odd degree and `b^2c^{r-1}` for even degree. In particular the old degree-17 direction is `bc^2=a^2(1+aW)^3`.

An independent exact reconstruction of the original coefficient-constraint matrices matched the classification's predicted cumulative nullity for every degree bound `D=3,...,20` (18/18 bounds). This finite agreement is **COMPUTED** evidence for, not a substitute for, the general classification proof.

Artifacts:

- `docs/SL2_BOUNDARY_CLASSIFICATION_2026-08-11.md`;
- `scripts/jacobian_blackboard_quadric_verify.py`;
- `verification/jacobian_blackboard_quadric_verify_2026-08-11.txt`;
- `verification/Jacobian_Canonical_Kernel_Exact_Validation_2026-08-11.txt`.

None of these current-run observations should be back-attributed to BLIND 2 or BLIND 4 merely because they unify structures first seen there.

## 2026-08-11 public-source acquisition provenance

A Codex Luna courier operating from the owner's Mac acquired the following without performing mathematical analysis:

- untouched arXiv `2608.02863` source bundle, SHA-256 `3f31ed51b3589cc41ba51aa140632fcaff74da92fa85442492d96069583994ce`;
- exact Zenodo API metadata and the sole attached file for DOI `10.5281/zenodo.21514514`;
- untouched arXiv `2607.20210` source bundle, SHA-256 `abf541b7e211d5ef0b14145ddb303f0cc34cb959fa7bec17f9efac1f6e3eadc9`.

The Kistner–Shaska arXiv bundle does not contain the cited `balanced_minimal_models_companion.pdf`. Bounded checks found no arXiv ancillary-download entry, the canonical ancillary candidate returned HTTP 404, and no retained local copy was found. Its status is therefore **NOT PUBLICLY LOCATED** as of this checkpoint.

This negative result must be represented correctly: it prevents complete comparison against the cited companion, but it is not evidence that the companion contains no overlapping result.

## Priority caveats

Novelty and priority are separate from correctness. Before any public priority claim:

- independently check the current-run `SL_2/T`, intersection, classification, spectrum, and Hilbert-series arguments;
- compare the acquired `2607.20210` and `2608.02863` source texts theorem-by-theorem against the strengthened formulation;
- carry the unavailable Kistner–Shaska companion as an explicit literature-coverage limitation unless an authentic copy later becomes available;
- compare other genuinely relevant recent/non-indexed notes where evidence warrants it;
- obtain independent specialist review.

Do not condition priority assessment on recovering additional raw BLIND histories; the owner has confirmed no further such material is available.
