# Paper 17 v1.5 Reproducibility Bundle

This bundle supports Paper 17 v1.5 of the Interior Observer framework:
*The Modular Projection Theorem: Operator-Level Closure of the Gauge Thermal
Transfer Principle via Shared Hilbert Space Construction and Fiberwise KMS
Inheritance*.

Paper 17 v1.5 is the correction point for the R4 / FIRAS readout-normalization
boundary. The observed CMB temperature is not counted as an independent IO
prediction in this version. FIRAS supplies the empirical observer-side thermal
datum; inside the IO readout family `T_obs(R4) = T_IO x^(R4 K_gauge)`, Theorem
17.2 fixes a unique `R4_FIRAS = 1.0031014644105183 +/- 0.009596597151571828`.

## Quickstart

From the repository root:

```bash
python3 papers/paper17/v1.5/scripts/09_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=24 pass_count=24 fail_count=0
```

## Detailed Reproduction

The numbered scripts can also be run one at a time from this bundle root:

```bash
cd papers/paper17/v1.5
python3 scripts/01_gauge_payload_determinant.py
python3 scripts/02_firas_fixed_r4.py
python3 scripts/03_readout_uniqueness_check.py
python3 scripts/04_modular_projection_surrogate.py
python3 scripts/05_foundation_closure_toy_model.py
python3 scripts/06_framework_constructible_uniqueness_summary.py
python3 scripts/07_r4_no_go_registry.py
python3 scripts/08_kappa_audit_summary.py
python3 scripts/09_validate_expected_outputs.py
```

Each script writes a JSON file in `results/`. The validator reruns the active
scripts and checks the generated outputs against the v1.5 manuscript values.

## Claim Discipline

- `K_gauge = ln(1 + gamma_BI^2)` is `DERIVED/THEOREM` as the modular-flow gauge
  payload within the reduced thermal-plus-gauge sector and the explicit G1-G6
  premise package.
- `a = dim(S2)/2 = 1` is the gauge-side Gaussian determinant exponent internal
  to the Paper 10 / Paper 17 construction of `K_gauge`; it is not R4.
- `R4` is not derived from the modular-projection stack. It is a visible
  optical readout-normalization slot fixed uniquely by FIRAS in Theorem 17.2.
- The FIRAS-fixed observer-side thermal readout is `Conditional_Verified` on
  Premise 2 plus the FIRAS empirical thermal datum.
- The historical `R4 = 1` unit readout and the old independent CMB-temperature
  prediction are retired as active claims.

The kappa audit found no hidden continuous fitted parameter remaining in Paper
17 v1.5. The load-bearing continuous field, R4, is explicitly visible, fixed
once by FIRAS, and frozen against downstream retuning.

## Dependencies

The public validation path uses Python standard library only. No external
datasets are redistributed. FIRAS is cited as an empirical input.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 17 v1.5*. Zenodo.
https://zenodo.org/records/19045892/latest

Associated release:

`paper17-v1.5`
