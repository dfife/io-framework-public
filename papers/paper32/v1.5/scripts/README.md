# Paper 32 v1.5 Scripts

Classification: `verified / public-reproducibility-support`

Run order:

```bash
python3 scripts/01_compute_framework_constants.py
python3 scripts/02_recollapse_acceleration.py
python3 scripts/03_x_crit_identity.py
python3 scripts/04_recollapse_cycle_timescales.py
python3 scripts/05_kb7_source_block_validation.py
python3 scripts/06_n_s_derivation_chain.py
python3 scripts/07_a_s_derivation_chain.py
python3 scripts/08_universal_gmp_classification.py
python3 scripts/09_validate_expected_outputs.py
```

## Script Inventory

- `01_compute_framework_constants.py`
  - Recomputes `Q`, `K_gauge`, `f_Gamma`, `Delta`, `R_U`, `T_obs`,
    `tau_eff`, `n_s`, and `x_crit`.
- `02_recollapse_acceleration.py`
  - Recomputes `Rddot = -c^2 r_s/(2R^2)` and `Rddot(r_s)`.
- `03_x_crit_identity.py`
  - Recomputes `x_crit = Q^(-1/4)` and sample visibility statuses.
- `04_recollapse_cycle_timescales.py`
  - Recomputes `110.993 Gyr` recollapse and `221.987 Gyr` conditional cycle.
- `05_kb7_source_block_validation.py`
  - Records the scoped KB.7 validation gates and checks `Z(e^x)=Q`.
- `06_n_s_derivation_chain.py`
  - Recomputes `n_s = 1 - K_gauge/x`.
- `07_a_s_derivation_chain.py`
  - Recomputes `A_s = 2.0072459972737347e-9`.
- `08_universal_gmp_classification.py`
  - Reproduces the three-region universal-GMP characterization ledger.
- `09_validate_expected_outputs.py`
  - Validates the frozen JSON outputs shipped in the bundle.

All scripts use only the Python standard library.

