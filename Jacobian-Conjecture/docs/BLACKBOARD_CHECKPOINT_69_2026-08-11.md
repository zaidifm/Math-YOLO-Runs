# Blackboard checkpoint 69 — Zariski-Main finite-cover reformulation

**Date:** 2026-08-11  
**Status:** current-run DERIVED synthesis; no external novelty claim.

The durable continuation journal has advanced beyond the earlier `SL_2/T` classification to a finite-cover formulation of the Keller phenomenon.

For a generically finite étale polynomial map

\[
F:X=\mathbb A^n\to Y=\mathbb A^n,
\]

Zariski's Main Theorem factors the quasi-finite map as

\[
X\hookrightarrow\overline X\xrightarrow{\ \bar F\ }Y,
\]

with `X -> Xbar` an open immersion and `Xbar -> Y` finite. Because `F` is étale on `X`, all ramification/different of the finite extension lies in the boundary

\[
B=\overline X\setminus X.
\]

For the primitive cubic Jacobian construction, the finite completion can be represented by the spectral/root cover of the recovery polynomial, while the polynomial Keller source is its simple-root/unramified open locus.

The local/global failure can therefore be stated as follows:

> a nontrivial finite branched cover of affine space can have an unramified open model that is itself affine space of the same dimension, with the full ramification divisor expelled to the boundary.

Since `K_Y` is trivial, the finite-cover formula

\[
K_{\overline X}=\bar F^*K_Y+R=R
\]

identifies the ramification/different divisor with the canonical divisor of the finite completion. The Keller open deletes that divisor and carries the pulled-back target volume form without zeros.

This reframes the remaining two-dimensional Jacobian problem as a boundary/canonical-model obstruction question: classify finite normal surface covers of `A^2` whose full different is supported on a boundary and ask whether the étale complement can itself be `A^2`.

The next blackboard attack is to determine whether the rank-one `SL_2/T` completion is forced by the affine-space/open-model requirements, or whether other colored/spherical boundary data can support the same Jacobian-divisor cancellation mechanism.
