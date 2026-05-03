# Paper 32 v1.5 Reproducibility Bundle

Classification: `verified / public-reproducibility-support`

This bundle contains the curated scripts, frozen outputs, and support reports
needed to audit the load-bearing numerical and structural claims in Paper 32
v1.5.

It is intentionally not a mirror of the private research lab. Exploratory
route searches, scratch state, manuscript drafts, and large private artifacts
are excluded.

## Paper Version

Paper:

```text
Paper 32 v1.5
The Cosmological Constant Drops Out: A Closed-Universe Cosmology with Zero
Fitted Parameters
```

Public paper record:

```text
https://zenodo.org/records/19558163/latest
```

Framework convention reference for new papers:

```text
https://dfife.github.io/data/conventions_v2.md
```

## What This Bundle Reproduces

The scripts reproduce the public arithmetic and structural ledgers for:

- the framework constants table from `gamma_BI`, `x`, `M_U`, and the Rosetta identity;
- the local recollapse acceleration and Lambda-dropout mechanism;
- the observer-boundary identity `x_crit = Q^(-1/4)`;
- the `111 Gyr` recollapse and `222 Gyr` conditional cycle timescales;
- the scoped Theorem 32.KB.7 source-block validation;
- the scalar-index formula `n_s = 1 - K_gauge/x`;
- the scalar-amplitude formula `A_s = 2.0072459972737347e-9`;
- the three-part universal-GMP characterization;
- the Paper 32 framework-closure kappa audit.

## Quick Validation

From this directory:

```bash
python3 scripts/09_validate_expected_outputs.py
```

Expected output:

```json
{
  "checks": 12,
  "state": "passed"
}
```

## Full Rerun

The scripts use only the Python standard library. From this directory:

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

The rerun rewrites the JSON files in `results/`.

## Headline Values

```text
gamma_BI = 0.2375
x = 1.519
Q = 1.05640625
K_gauge = 0.05487281774291466
Delta = 5.624216852624105
r_s = 6.685e26 m
Rddot(r_s) = -6.722177851434687e-11 m/s^2
x_crit = 0.9863754613328337
Delta tau_recollapse = 110.9932628887098 Gyr
Delta tau_cycle = 221.9865257774196 Gyr
n_s = 0.963875696021781
A_s = 2.0072459972737347e-9
```

## Claim Boundary

- `verified`: arithmetic reproduction of the constants, recollapse, cycle,
  scalar-index, scalar-amplitude, and validation JSONs.
- `derived/scoped`: KB.7 source-block validation, scalar-source results, and
  realized typed-bridge GMP classification at their stated scopes.
- `conditional`: the full 222 Gyr cycle and hard-restart morphology, which
  require explicit bounce/restart selector packages.
- `not included`: private route-search logs, manuscript drafts, and exploratory
  theorem-discovery automation.
- `not claimed`: universal P4 for arbitrary observables, universal GMP on the
  full local algebra, or derivation of Premise 2.

## Reports

The `reports/` directory includes the framework-closure kappa audit and the
support reports cited by that audit. These reports are included so readers can
audit the scope boundaries behind the numerical values.

