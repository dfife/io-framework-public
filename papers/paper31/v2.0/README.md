# Paper 31 v2.0 Reproducibility Bundle

This bundle supports Paper 31 v2.0, *Gravitational Slip from Schwarzschild
Interior Geometry*. It archives the active reproducibility subset for the CMB
Weyl-kernel branch, practical PlanckLite/CLASS confrontation, baryon-slot audit,
spectral-weight checks, Ly-alpha BAO inheritance, E_G/lensing pipeline, and the
pre-Zenodo manuscript-claim reconciliation audit.

Quick validation:

```bash
cd papers/paper31/v2.0
python3 scripts/08_validate_expected_outputs.py
```

Expected output:

```text
Paper 31 v2.0 validation passed: 62/62 checks
```

The full CLASS/PlanckLite scripts are included for provenance and extended
reruns. They require the external environment described in
`environment/external_dependencies.md`.

Claim boundary: the included PlanckLite/CLASS outputs are frozen
computational-audit artifacts. The validator checks that the public archive
matches the frozen v2.0 state; it does not convert conditional or reconstruction
claims into theorem-grade results.

Precision note: the reconciliation audit uses the canonical active-branch value
`x = 1.5189873277742727` (`1.51899` in manuscript display). Some older
PlanckLite provenance reports retain rounded historical display text, but the
manuscript-level values are validated through
`results/paper31_v2_0_manuscript_reconciliation_results.json`.

Boundary note: the chronometer + DESI `chi2 = 42.48` cross-paper value is
archived for traceability from public Paper 29 data, but that source labels it
as legacy Schur-context material. This bundle therefore exposes the value
without upgrading it to an active-branch reproducer.
