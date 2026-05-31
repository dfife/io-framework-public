# Paper 3 v2.0 Sharp-EOS Junction-Limit Theorem Memo

## Compact Statement

The retired discrete Vaidya-to-OS construction is not the active physical
early-time model. Its clean Israel-Darmois result survives only as the
sharp-equation-of-state limit of Paper 5's continuous mixed-fluid interior:
metric continuity follows from continuous `a`, extrinsic-curvature continuity
from continuous `adot`, and the Raychaudhuri acceleration magnitude changes by
the fixed factor `2` between pure radiation and pure dust at fixed `a` and
`rho`.

## Status

`DERIVED/CONDITIONAL_VERIFIED`.

The result is conditional on using the sharp-transition limit of the Paper 5
continuous mixed-fluid interior. It is not a claim that the old discrete
Vaidya phase is the active physical model.

## P1/P2 Dependency Chain

- P1: the observable universe is inside a Schwarzschild black hole, giving the
  closed IO interior support and horizon-contained geometry.
- P2: standard GR applies inside the horizon. This licenses the
  Israel-Darmois matching conditions and the FRW/Raychaudhuri acceleration
  equation inside the P1 container.
- Paper 5: replaces the retired discrete Vaidya radiation phase with a
  continuous mixed-fluid closed-FRW interior.
- Paper 3 v2.0: uses only the sharp-EOS limiting statement as manuscript
  support.

## Assumptions

- The scale factor `a` is continuous through the limiting transition.
- The first derivative `adot` is continuous through the limiting transition.
- The density `rho` is finite and compared at fixed `a` and `rho`.
- The equation-of-state parameter is `w=1/3` for pure radiation and `w=0` for
  pure dust.

## Derivation

Metric continuity in the homogeneous FRW support follows from continuity of
`a`. Extrinsic-curvature continuity follows from continuity of the first
derivative `adot`; it does not follow from continuity of `addot`.

The acceleration is governed by the Raychaudhuri equation:

```text
addot/a = -(4 pi G/3) rho (1 + 3w).
```

At fixed `a` and `rho`, the pure-radiation magnitude has factor
`1 + 3(1/3) = 2`, while the pure-dust magnitude has factor `1 + 3(0) = 1`.
Therefore

```text
|addot_rad| / |addot_dust| = 2.
```

## Evidence

- Reproducible script:
  `scripts/04_sharp_eos_junction_limit.py`
- Frozen result:
  `results/sharp_eos_junction_limit_results.json`
- Validator:
  `scripts/05_validate_expected_outputs.py`

The validator checks the status label, the survival verdict, the acceleration
ratio, and the guard that extrinsic curvature is tied to `adot`, not `addot`.
