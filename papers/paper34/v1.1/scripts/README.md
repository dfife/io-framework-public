# Paper 34 v1.1 Script Guide

Classification: `verified / public-reproducibility-support`

This folder contains the executable support scripts for the Paper 34 v1.1
reproducibility bundle. Each script includes a top-level docstring recording
purpose, inputs, outputs, dependencies, claim boundary, and run command.

## Run Order

From `papers/paper34/v1.1/`:

```bash
python3 scripts/01_compute_hext_grid.py
python3 scripts/02_compare_to_published_measurements.py
python3 scripts/03_run_anti_fit_check.py
python3 scripts/04_validate_expected_outputs.py
```

Expected validation output:

```json
{
  "checks": 11,
  "state": "passed"
}
```

## Script Inventory

### `01_compute_hext_grid.py`

Purpose: compute the full `(alpha,n)` grid for
`H_ext(alpha,n) = H0_active * f_Gamma^(1-alpha) * x^((n/2)*K_gauge)`.

Dependencies: Python standard library only.

Writes:

```text
results/hext_grid_results.json
```

### `02_compare_to_published_measurements.py`

Purpose: compute the six-method scorecard against imported published H0
measurement values.

Dependencies: Python standard library only.

Writes:

```text
results/published_measurements_comparison_results.json
```

### `03_run_anti_fit_check.py`

Purpose: reproduce the anti-fit backstop table. The key diagnostic is that GW
sirens remain structurally assigned to `(1,0)` even though `(3/2,1)` is
numerically closer on the admissible grid.

Dependencies: Python standard library only.

Writes:

```text
results/anti_fit_check_results.json
```

### `04_validate_expected_outputs.py`

Purpose: validate the frozen public JSON outputs against pinned headline
values.

Dependencies: Python standard library only.

Writes: no files; prints a JSON pass/fail summary.

## Claim Boundary

The scripts verify arithmetic, grid generation, scorecard pulls, and anti-fit
diagnostics. They do not prove the Paper 34 extension premises. The extension
premises and kappa-style hidden-parameter audit are included in `reports/`.
