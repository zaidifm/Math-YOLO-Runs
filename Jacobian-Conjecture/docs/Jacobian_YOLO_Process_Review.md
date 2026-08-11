# Jacobian Conjecture YOLO Run — Process Review

**Facilitator:** Ali  
**Source material reviewed:** exported raw BLIND 2 conversation; exported verification conversation; BLIND 1–5 findings packages and retrospective histories; exact scripts and audit artifacts.

## Executive finding

The strongest lesson is not “a caveman prompt contains secret mathematics.” It is that simple prompts can alter a frontier model's **search policy** enough to matter when the mathematical object is highly verifiable and the surrounding workflow supplies diversity, controlled information leakage, and exact checking.

The experiment behaved like a primitive evolutionary/agentic research system built out of ordinary chat sessions:

**parallel variation + isolation + anti-closure pressure + self-critique + selective memo transfer + exact verification.**

## Independence was graded, not binary

- **BLIND 1:** received an information-rich structural hint: dimension three, degree/monomial profiles, reciprocal-chart architecture, repeated `1+xy`, Jacobian-factor cancellation, and cubic inversion. It reconstructed coefficients/equivalent formulas. This is strong coefficient-blind reconstruction, not answer-free discovery.
- **BLIND 2:** initially searched independently and failed in an overrestricted normalization. It was later given the exact hidden coordinates and map. Its distinctive value came afterward: shifted-boundary geometry, a degree-17 quintic construction, computational minimality work, and the boundary-ring theorem.
- **BLIND 3 (web-reviewed package):** strongest reconstruction experiment. It received only the birational architecture, not coordinates or coefficients, and found its own reciprocal chart and explicit constant-Jacobian noninjective polynomial map, later shown equivalent in mechanism to the announced counterexample.
- **BLIND 4:** initially failed twice, became skeptical, and overgeneralized narrow no-go results. After the explicit map forced a reset, it produced some of the most interesting structural interpretations: an invariant binary-cubic factorization, normalized-gradient view, finite-jet polynomialization conditions, and a corrected boundary-surjectivity picture.
- **BLIND 5:** was a reverse-engineering experiment, not independent discovery. It was supplied the explicit counterexample and asked to derive mechanism and consequences.

There are two different packages labeled BLIND 3 in the archive; the web-reviewed package is the genuinely independent reconstruction. The other largely consolidates the BLIND 2 boundary-ring trajectory. This distinction matters for provenance.

## The BLIND 2 prompt sequence is unusually informative

The raw conversation shows the following causal sequence.

1. An initial independent attempt was given a strong architectural hint but entered the wrong normalized family and produced a valid obstruction only inside that family.
2. The exact hidden coordinates/map were later supplied, so BLIND 2 should not be credited with independently discovering the base counterexample.
3. After constructing surjective deformations, the session prematurely treated a degree-30 threshold in one family as if it reflected the larger mechanism.
4. Ali asked for the model's “fundamental blind spot and weakness ... epistemically and strategically and tactically.” The model identified poor provenance bookkeeping, elegance-as-evidence, over-acceptance of framing, and insufficient destructive testing.
5. Ali then instructed it to “dig in” and not return until it had genuinely broken something. The ensuing long research burst found the shifted boundary variable

   `1 + aW = xK`,

   which changed the relevant local parameter at infinity from `aW` to `1+aW` and yielded the degree-17 direction.
6. Only **after that** did a sibling memo explicitly ask for the abstraction `k[a,W] ∩ k[x,y,z]`. BLIND 2 then formulated and proved the boundary-ring theorem. Thus the “find God” prompt is a salient precursor to the shifted-boundary breakthrough, while the full ring theorem also depended on a later mathematically precise sibling memo.

This is a much stronger causal account than “the user said keep going and a theorem appeared.”

## What the simple prompts appear to do

The useful intervention is not semantic content but policy control.

- **Anti-closure:** coherent explanations stop being acceptable termination conditions.
- **Compute allocation:** the model spends a much longer interval exploring before yielding.
- **Basin escape:** the model is invited to treat its current representation as suspect, not sacred.
- **Meta-modeling:** asking for blind spots forces the trajectory to identify its own failure mode before the next search.
- **Prior override:** telling a lagging instance that sibling instances succeeded supplies evidence that the task is feasible without revealing the answer.
- **Failure preservation:** the lagging trajectory remains alive rather than being discarded, which can later produce a distinct conceptual representation.

The strongest example is BLIND 4. Its early failure was real, but the failure placed it in a different conceptual basin. Once reset, that basin produced useful invariant/geometric ideas not emphasized by the early successful runs.

## Why this can also go badly

The same “do not stop” pressure can reward grandiosity. The BLIND 2 history records early instances where computations were narrated as though completed without durable certificates. The Riemann thread inherited in the current conversation shows the same danger: progressively larger numerical claims were proposed, stress-tested, and sometimes demoted later.

Therefore persistence is productive only when coupled to a verification gate and a provenance ledger.

## Experimental limitations

Most BLIND supplementary histories are retrospective reconstructions, not raw platform transcripts. They preserve chronology and findings but do not give a perfect record of every timestamp, branch, hidden reasoning trace, or exact prompt insertion point. The newly exported BLIND 2 and verification conversations are much stronger evidence for causal analysis.

The experiments also do not isolate prompt wording from inference budget, model stochasticity, contextual information, and tool use. A statement such as “the phrase find God caused theorem X” would be too strong. A defensible statement is that the phrase immediately preceded, and functionally changed the stopping rule for, a long exploration that produced the shifted-boundary precursor.

## Transferable protocol

For future open-problem work, preserve several trajectories; withhold the full known answer where possible; use feasibility-only information sparingly; force explicit self-audits after stalls; use dumb persistence prompts as search-policy perturbations; transmit distilled mathematical memos only after independent exploration has had time to diverge; and require exact artifacts before upgrading a claim.
