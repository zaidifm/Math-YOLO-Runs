# Blackboard checkpoint 71 — power-exchange exponent rigidity

**Date:** 2026-08-11  
**Status:** valuation argument DERIVED; minimal linear models COMPUTED exactly. No external priority claim.

Consider the normalized generalized exchange

\[
b=1+a^kW,
\qquad X=x^{-1},
\qquad a=X+r(y,z)+O(x).
\]

For `b` to remain regular and vanish along the source boundary, the leading behavior of `W` must be

\[
W=-x^k+O(x^{k+1}).
\]

Therefore all derivatives of `W` tangent to `x=0` have order at least `x^{k+1}`. Since `partial_x X=-x^{-2}` while boundary derivatives of `a` have order zero,

\[
\boxed{\operatorname{ord}_{x=0}J_{source}\ge k-1.}
\]

The ordinary incidence/Legendre map contributes exactly one inverse torus character,

\[
J_{incidence}\sim X=x^{-1},
\]

so

\[
\boxed{\operatorname{ord}_{x=0}J_{total}\ge k-2.}
\]

Thus `k>2` cannot produce a nonzero constant Jacobian in this mechanism.

For the minimal linear model

\[
a=X+\alpha y+\beta z,
\qquad
W=-x^k+x^{k+1}(py+qz),
\]
with `Delta=alpha*q-beta*p`, exact calculation gives

\[
J_{source}=-\Delta x^{k-1},
\qquad
J_{total}=x^{k-2}.
\]

This identity was checked symbolically for `k=1,...,8`.

The remaining cases are then sharply separated:

- `k>2`: boundary divisibility forces the wrong Jacobian valuation;
- `k=2`: the Jacobian valuation is correct, but Checkpoint 70 proves boundary regularity forces `Delta=0`;
- `k=1`: the only surviving exponent. Divisibility already permits order-`x^2` corrections, and the transverse source-boundary direction can be placed one order later (`x^3z`) to supply exactly the missing Jacobian factor `x`.

Hence, within the normalized power-exchange + ordinary incidence mechanism,

\[
\boxed{k=1\text{ is selected simultaneously by divisor, character, and regularity constraints}.}
\]

Exact certificate: `scripts/jacobian_exchange_exponent_rigidity_verify.py`, SHA-256 `7cfbaebf65c620d881cd5b721cffa2beb026474843c6037e279ad74b112a5e06`.
