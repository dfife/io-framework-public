# Paper 26 v2.0 Reproducibility Bundle

This bundle supports Paper 26 v2.0 of the Interior Observer framework:
*The Primordial Scalar Amplitude from the Hawking Boundary State and
IO-Native Replacements for LambdaCDM-Borrowed Inputs*.

The bundle reproduces the live scripted artifacts behind the paper:

- the Hawking-boundary scalar amplitude `A_s`;
- the conditional tensor branch range;
- the cosmic microwave background baryon-class diagnostic ledger;
- the effective optical damping parameter `tau_eff = K_gauge/2`;
- the high-multipole temperature-temperature reionization-shape diagnostic;
- the C2c forward Hawking-state arithmetic check;
- the kappa-style structural audit summary.

It does not rerun CLASS or Planck likelihoods. The public validation path uses
frozen audited diagnostic rows and Python standard-library arithmetic.

## Quickstart

From the repository root:

```bash
python3 papers/paper26/v2.0/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=22 pass_count=22 fail_count=0
```

## Detailed Reproduction

The numbered scripts can also be run one at a time from this bundle root:

```bash
python3 scripts/01_scalar_amplitude_chain.py
python3 scripts/02_tensor_conditionals.py
python3 scripts/03_cmb_baryon_class_diagnostic.py
python3 scripts/04_tau_eff_and_damping.py
python3 scripts/05_reionization_shape_tt_check.py
python3 scripts/06_kappa_audit_summary.py
python3 scripts/c2c_analysis/01_c2c_as_forward_check.py
```

Each script writes a frozen JSON file in `results/`. The validator reruns all
scripts and checks generated JSON outputs against active Paper 26 v2.0 values.

## Claim Discipline

Paper 26 v2.0 is a conditional support package, not an unconditional full-CMB
closure paper.

- `A_s = 2.0072459972737347e-9` is `DERIVED/CONDITIONAL_VERIFIED` on C1 and
  C2c.
- `omega_b,vis = omega_b,eff = 0.02910` is
  `DERIVED/CONDITIONAL_VERIFIED` on AV1.
- `tau_eff,IO = K_gauge/2 = 0.02743640887145733` is
  `DERIVED/CONDITIONAL_VERIFIED` on Theorem 26.C3 in the reduced centered
  Gaussian source-covariance class.
- Reionization-shape insensitivity is verified for high-multipole
  temperature-temperature spectra only; low-multipole electric-polarization
  closure is not claimed.

The kappa audit found no hidden continuous fitted parameter in the public
scripted outputs. It flags manuscript hygiene issues for v2.0 review: inherited
`T_obs = T_IO x^K_gauge` wording must be replaced by the Paper 17 v1.5
FIRAS-fixed readout law, and inherited bridge-variable wording around
`delta Gamma` versus `gamma delta K` should be aligned with the active body
theorem.

The observed CMB temperature is not counted as an independent Interior Observer
prediction. Paper 26 inherits `R4_FIRAS = 1.0031014644` from Paper 17 v1.5 as
the unique FIRAS-fixed observer-side thermal readout normalization.

## Dependencies

The public validation path uses Python standard library only. CLASS, Planck
likelihood assets, and observational data files are not redistributed.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 26 v2.0*. Zenodo.

Associated release:

`paper26-v2.0`
