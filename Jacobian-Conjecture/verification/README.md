# Verification

## Current exact symbolic replay

Requires Python 3 and SymPy.

Run from repository root:

```bash
python Jacobian-Conjecture/scripts/jacobian_blind_bridge_verify.py
```

The current verifier checks:

- `b = xK`;
- `c = (1+2xy)K`;
- `cW = b(b-1)`;
- preservation of the boundary relation by `D(W)=0`, `D(b)=W`, `D(c)=2b-1`;
- the unified canonical deformation formulas modulo the boundary relation;
- the hidden-coordinate formulas for `d/da` and `a*d/da-g`;
- the cubic finite-jet equivalence;
- top-degree monomials/degrees of `W,b,c`.

A known-good output from the 2026-08-11 ChatGPT runtime is stored in [`sympy_bridge_output_2026-08-11.txt`](sympy_bridge_output_2026-08-11.txt).

## What this verifier does NOT prove

This small script does not by itself prove the infinite intersection theorem or global novelty. The full intersection theorem currently rests on the reconstructed normality/divisorial-valuation argument in `docs/Jacobian_Blind_Math_Forensics_2026-08-11.md` plus larger archived exact computations.

## Next independent verification

After the missing ancillary literature is acquired, run an orthogonal CAS audit using Sage/Singular or Macaulay2. Desired targets include elimination/saturation/subalgebra calculations, smoothness/normality checks, bounded intersection dimensions, and an independent reconstruction of the degree-16/17 transition.
