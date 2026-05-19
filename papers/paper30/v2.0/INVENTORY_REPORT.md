# Inventory Report

## Included

- Active Paper 30 v2.0 recomputation script.
- Frozen active recomputation JSON and Markdown report.
- Frozen Paper 29 v2.0 upstream JSON inputs used for the CC/BAO carried scorecard.
- Frozen Paper 30 legacy-context JSON files needed by the active recomputation script for before/after comparison fields.
- K-style audit and R4/FIRAS impact report.
- Validation script and validation output.

## Excluded

Private exploratory scripts under `results/paper30/paper30_funrun_*` are not included as live executable support because several still use retired Schur-branch constants (`H0=68.91`, `Omega_k=-0.006`). Their frozen JSON outputs are retained only where the active recomputation report needs comparison context.

Historical figure PNGs are excluded. The v2.0 bundle is for numerical reproducibility, not manuscript figure regeneration.

## Gaps Flagged

- Manuscript CMB-temperature wording should be narrowed to FIRAS-normalized propagation language.
- Several appendix `STATUS: DERIVED` entries should be canonicalized if they remain load-bearing.
- The active public validator covers headline recomputation values. It does not rerun every historical exploratory fun-run, by design.
