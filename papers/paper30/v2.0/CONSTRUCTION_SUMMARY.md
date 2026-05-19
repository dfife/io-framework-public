# Construction Summary

## Scripts

- `scripts/01_full_twenty_test_recompute.py`
  - Inputs: active Paper 29 projection constants, official Pantheon+SH0ES data fetched at runtime, public DESI DR2 BAO files, public TDCOSMO per-lens posterior files, frozen Paper 29 v2.0 upstream JSON outputs, and frozen Paper 30 legacy-context JSON files for comparison columns only.
  - Outputs: `results/full_twenty_test_recompute_results.json`, `reports/full_twenty_test_recompute_report.md`.
  - Verifies: Paper 30 headline confrontation values for CC, DESI BAO, CC+DESI, Pantheon+, TDCOSMO, GW sirens, AP, FRB, kSZ, clusters, Ly-alpha, angular-diameter minimum, redshift drift, S8/Weyl response, and active constants.
  - External dependencies: `numpy`, `pandas`, `scipy`, `requests`, `camb`, and network access for public observational files if not already cached.

- `scripts/02_validate_expected_outputs.py`
  - Inputs: `scripts/01_full_twenty_test_recompute.py` and frozen expected values embedded in the validator.
  - Outputs: `results/validation_results.json`.
  - Verifies: 18 frozen checks, including canonical label checks for the active baryon slots. Use `--recompute` to regenerate the active output before validation.
  - External dependencies: same Python environment as the recomputation script.

## Manuscript Values Checked

- `H0 = 67.57585653582628 km/s/Mpc`
- `Omega_m = 0.34868395067621694`
- `Omega_k = -0.04579112576013168`
- `Omega_Lambda = 0.69701575761593`
- `CC chi2 = 14.701523963980787`
- `DESI BAO chi2 = 27.735229301342457`
- `CC + DESI chi2 = 42.43675326532325`
- `Planck fixed-reference CC + DESI chi2 = 46.40432046950788`
- `Pantheon+ IO chi2 = 1757.4798174084137`
- `Pantheon+ Planck chi2 = 1759.6947847107324`
- `TDCOSMO IO chi2 = 31.597640376134585`
- `TDCOSMO Planck chi2 = 34.46226106589568`
- `AP IO chi2 = 7.88341490487783`
- `AP Planck chi2 = 6.702669976136264`
- `x = 1.5189873277742727`
- `K_gauge = 0.05487281774291466`
- `eta_BAO = 0.036124605346983495`
- `Sigma_IO = x^(-1/2) = 0.8113774333810703`

## R4 Boundary

No active Paper 30 calculation uses `R4 = 1`. The script records `R4_FIRAS = 1.0031014644` as a dependency boundary and uses the FIRAS-fixed observer thermal datum where thermal inputs are needed.
