# Paper 31 v2.0 Reproducibility Bundle

This bundle supports Paper 31 v2.0, *Gravitational Slip from Schwarzschild
Interior Geometry*. It archives the active reproducibility subset for the CMB
Weyl-kernel branch, practical PlanckLite/CLASS confrontation, baryon-slot audit,
spectral-weight checks, Ly-alpha BAO inheritance, and E_G/lensing pipeline.

Quick validation:

```bash
cd papers/paper31/v2.0
python3 scripts/08_validate_expected_outputs.py
```

Expected output:

```text
Paper 31 v2.0 validation passed: 25/25 checks
```

The full CLASS/PlanckLite scripts are included for provenance and extended
reruns. They require the external environment described in
`environment/external_dependencies.md`.

Claim boundary: the included PlanckLite/CLASS outputs are frozen
computational-audit artifacts. The validator checks that the public archive
matches the frozen v2.0 state; it does not convert conditional or reconstruction
claims into theorem-grade results.
