# Paper 24 v2.3 Script Guide

Classification: `verified / public-reproducibility-support`

This folder contains the executable support scripts for the Paper 24 v2.3
reproducibility bundle. Each script includes a top-level docstring recording
purpose, inputs, outputs, external dependencies, claim boundary, and run
command.

## Run Order

Fast validation without PRyMordial:

```bash
python3 scripts/04_validate_expected_outputs.py
```

Optional non-PRyMordial recomputation:

```bash
python3 scripts/01_compute_qtrans_carrier.py
python3 scripts/04_validate_expected_outputs.py
```

Full rerun with PRyMordial:

```bash
export PRYM_ROOT=/path/to/PRyMordial
python3 scripts/03_run_final_bbn_scorecard.py
python3 scripts/02_recompute_excited_state_import.py
python3 scripts/04_validate_expected_outputs.py
```

## Script Inventory

### `01_compute_qtrans_carrier.py`

Purpose: recompute the final-state quadrupole carrier audit and the
`Q_trans ~= 0.040 b` target translation.

Dependencies: Python standard library only.

Writes:

```text
results/qtrans_carrier_results.json
```

Claim boundary: verifies arithmetic and JSON reproduction of the carrier audit;
the final-state measured-`Q(7Li)` carrier rule remains conditional.

### `02_recompute_excited_state_import.py`

Purpose: recompute the Henderson excited-state import, the detailed-balance
spin-multiplicity correction, and imported-response scorecard cases.

Dependencies: imports `03_run_final_bbn_scorecard.py`, so full execution
requires PRyMordial via `PRYM_ROOT`.

Writes:

```text
results/excited_state_import_recomputation_results.json
reports/excited_state_import_recomputation_memo.md
```

Claim boundary: verifies the Henderson arithmetic and source-convention checks;
the mapping from imported `B(E2)` to the Paper 24 branch-dressing scale remains
conditional.

### `03_run_final_bbn_scorecard.py`

Purpose: recompute the excited-branch kernel, angular no-go diagnostics, and
PRyMordial BBN scorecard used by Paper 24 v2.3.

Dependencies: external PRyMordial checkout, `mpmath`, and `sympy`.

Requires:

```bash
export PRYM_ROOT=/path/to/PRyMordial
```

Writes:

```text
results/final_excited_branch_results.json
results/final_excited_branch_report.txt
```

Claim boundary: verifies kernel arithmetic, angular coefficients, and local
PRyMordial reruns; the branch-dressing model is conditional.

### `04_validate_expected_outputs.py`

Purpose: validate the frozen public JSON outputs against pinned headline values.

Dependencies: Python standard library only.

Writes: no files; prints a JSON pass/fail summary.

Claim boundary: verifies integrity of the public bundle outputs. It does not
rerun PRyMordial.

## Public-Review Notes

- PRyMordial is intentionally not vendored in this repository.
- Private class-search automation and exploratory GSM/AZURE2 routes are not
  part of this support bundle.
- Reconstructed AZURE2/R-matrix scaffolds are not used as theorem evidence in
  this bundle.
- Frozen outputs are included so reviewers can audit the numerical chain before
  installing PRyMordial.
