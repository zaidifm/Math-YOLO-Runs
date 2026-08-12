# Blackboard checkpoint 80 — no nontrivial Keller map can have generic degree two

**Date:** 2026-08-11  
**Status:** global algebraic argument DERIVED; quadratic discriminant identity COMPUTED. No external novelty claim.

For a quadratic `pT^2+qT+r` with chosen root `a`, root incidence gives

\[
r=-pa^2-qa.
\]

Hence its discriminant restricts to

\[
\boxed{q^2-4pr=(2pa+q)^2.}
\]

The chosen root is simple iff `D=2pa+q` is nonzero. Therefore the discriminant is a nonconstant unit on the chosen-simple-root incidence variety. Such a variety cannot be affine space, because `O(A^n)^*=C^*`.

This quadratic observation upgrades through Zariski Main.

Assume

\[
F:A^n_C\to A^n_C
\]

is everywhere étale and has generic degree two. Factor it as an open immersion into the finite normalization

\[
A^n\hookrightarrow\overline X\xrightarrow{\pi}A^n.
\]

A nontrivial quadratic function-field extension must ramify along a divisor of `A^n`. If it were `K(A^n)(sqrt(d))` with every prime-divisor valuation of `d` even, then `div(d)=2D`; since `Pic(A^n)=0`, `d` differs from a square by a constant, and over `C` the extension would be trivial.

Let `B` be a branch divisor of the nontrivial quadratic normalization. Because the polynomial source is étale, it contains no ramification point. If `F^{-1}(B)` were nonempty, étale flatness would make it a divisor whose generic point lies over the generic branch point. But a degree-two cover over its generic branch point has only the ramified double sheet. Contradiction. Hence

\[
F^{-1}(B)=\varnothing.
\]

If `delta` defines an irreducible component of `B`, then `delta o F` is a nowhere-zero regular function on `A^n`, hence constant. Dominance makes the coordinate-ring pullback injective, forcing `delta` itself to be constant, contradiction.

Therefore

\[
\boxed{\text{no everywhere-étale polynomial self-map of affine space has nontrivial generic degree }2.}
\]

Generic degree one is birational étale and gives an open immersion; an injective polynomial endomorphism of affine space over characteristic zero is an automorphism. Consequently every noninjective Keller map satisfies

\[
\boxed{\deg_{gen}F\ge3.}
\]

The Alpöge/Fable map has generic degree three, so it attains the global minimum possible generic fiber degree.

Conceptually: in degree two, branch consumes both sheets, forcing an étale affine source to avoid the whole branch divisor and creating a forbidden unit. In degree three, two sheets may collide while a third simple sheet survives. The simple-root cubic incidence construction exploits exactly that first available possibility.

Exact quadratic certificate: `scripts/jacobian_degree_two_global_obstruction_verify.py`, SHA-256 `95725732f55d9ef3bcfc1f9cd47e2c12ea4228f323059a5bfa15c9ae5df3abe6`.
