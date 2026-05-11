# Paper 23 v2.0 Reproducibility Bundle

Paper 23 develops the Interior Observer primordial perturbation bookkeeping on
the Oppenheimer-Snyder interior: closed-S3 scalar perturbations, the
boundary-to-bulk bridge operator, the No-Doubling theorem, and the scalar
spectral-index calculation.

This v2.0 bundle also performs the May 2026 R4/FIRAS repair audit. The important
boundary is that `R4_FIRAS = 1.0031014644` is inherited from Paper 17 v1.5 as the
FIRAS-fixed observer-side thermal readout normalization, but it does not enter
Paper 23's active scalar spectral-index calculation.

## Quickstart

From the repository root:

```bash
python3 papers/paper23/v2.0/scripts/08_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=30 pass_count=30 fail_count=0
```

No external datasets are redistributed or required for the validation scripts.

## What This Bundle Reproduces

- `R4_FIRAS = 1.0031014644` dependency audit and CMB-temperature claim boundary.
- Closed-S3 scalar harmonic and Mukhanov-Sasaki wavenumber bookkeeping.
- Scalar bridge operator support, branch selection, and uniqueness/proportionality checks.
- White boundary baseline and Hopf-selection bookkeeping.
- No-Doubling theorem arithmetic and scalar spectral-index result:

```text
1 - n_s = K_gauge / x = 0.03612435625139463
n_s = 0.9638756437486053
Planck residual = +0.24389434557015036 sigma
```

- Tensor-sector support statements and scope boundary.
- Kappa-style audit summary identifying R4 damage, stale inherited Paper 22
  values, noncanonical labels, abbreviations, and IO-local terminology.

## Claim Boundary

The observed CMB temperature is not counted as an independent IO prediction in
this bundle. FIRAS fixes the observer-side readout normalization in Paper 17
v1.5. Paper 23's active scalar spectral-index value is independent of that
normalization.

The bundle follows the current claim-label convention:

- `DERIVED/THEOREM`
- `DERIVED/CONDITIONAL_VERIFIED`
- `DERIVED/NO-GO`
- `VERIFIED`
- `IMPORTED/EMPIRICAL`
- `RECONSTRUCTION`
- `RECONSTRUCTION/RESEARCH_ONLY`
- `OPEN/PREMISE_GAP`
- `SUPERSEDED`
- `Historical/SUPERSEDED`

## Script Order

1. `01_r4_firas_dependency_audit.py`
2. `02_scalar_perturbation_equations.py`
3. `03_bridge_operator_and_uniqueness.py`
4. `04_white_baseline_and_hopf_selection.py`
5. `05_no_doubling_and_spectral_index.py`
6. `06_tensor_perturbations.py`
7. `07_kappa_audit_summary.py`
8. `08_validate_expected_outputs.py`

## Citation

If you use this bundle, cite the associated Paper 23 manuscript and the immutable
GitHub release tag `paper23-v2.0`.

