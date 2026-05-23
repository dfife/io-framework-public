# Version

Bundle version:

```text
paper34-v2.0-repro
```

Supported paper version:

```text
Paper 34 v2.0
```

Creation date:

```text
May 2026
```

Policy:

- This folder is immutable once published except for correction commits that
  are explicitly documented.
- Paper 34 v1.1 and v1.2 remain available at `papers/paper34/v1.1/` and `papers/paper34/v1.2/`.
- A future Paper 34 v2.1 support package must be created as
  `papers/paper34/v2.1/`.
- Do not overwrite v1.1 outputs with v2.0 results, and do not overwrite v2.0
  outputs with later versions.

v2.0 update:

- Records the Paper 17 v1.5 FIRAS-fixed `R4_FIRAS` value for provenance.
- Verifies Paper 34's `H_ext(alpha,n)` scorecard has no active R4 dependency.
- Clarifies that the Planck CMB row is a compound CMB-inference / baseline
  projected-background row, not an independent CMB-temperature prediction and
  not a single primitive alpha-rung.
- Adds the v2.0 Planck classification and §10 scoped-closure theorem memos.
- Updates the baseline-branch boundary: Paper 10 / Paper 29 projected observer
  branch is the sole active Paper 34 branch; Schur 68.91 is retired diagnostic
  history after the hidden-parameter branch audit.
- Leaves all six Paper 34 H0 predictions and residuals numerically unchanged.
