# Paper 5 v2.0 Reproducibility Bundle

This public support bundle reproduces the local calculations and diagnostics
used by Interior Observer Paper 5 v2.0:

- Kerr-spin temperature degradation relative to Schwarzschild.
- Vaidya null-dust incompatibility with an isotropic thermal radiation bath.
- Mixed-fluid closed Friedmann expansion-rate ratios on the active branch.
- Dependency pointers for the first peak, acoustic scale, and BBN rate-dressing
  interpretation inherited from Papers 12, 20, 22, and 24.

Quick validation:

```bash
python scripts/05_validate_expected_outputs.py
```

Expected summary:

```text
SUMMARY total_checks=17 pass_count=17 fail_count=0
```

The bundle is deterministic and uses only the Python standard library.
