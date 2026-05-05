# Paper 26 v1.2 Reproducibility Bundle

This bundle supports Paper 26 v1.2 of the Interior Observer framework:
*The Primordial Scalar Amplitude from the Hawking Boundary State and
IO-Native Replacements for LambdaCDM-Borrowed Inputs*.

The bundle reproduces the live scripted artifacts behind the paper:

- the conditional Hawking-boundary scalar amplitude `A_s`;
- the conditional tensor branch range;
- the CMB baryon-class diagnostic ledger;
- the effective optical damping parameter `tau_eff = K_gauge/2`;
- the high-l TT reionization-shape diagnostic;
- the kappa-style structural audit summary.

It does not rerun CLASS or Planck likelihoods. The public validation path uses
frozen audited CLASS rows and standard-library arithmetic.

## Quickstart

From the repository root:

```bash
python3 papers/paper26/v1.2/scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=18 pass_count=18 fail_count=0
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
```

Each script writes a frozen JSON file in `results/`. The validator reruns all
six scripts and checks generated JSON outputs against active bundle values.

## Claim Discipline

Paper 26 v1.2 is a conditional support package, not an unconditional closure
paper.

- `A_s = 2.0072459972737347e-9` is `DERIVED/CONDITIONAL on C1 + C2c`.
- `omega_b,vis = omega_b,eff = 0.02910` is `DERIVED/CONDITIONAL on AV1`.
- `tau_eff,IO = K_gauge/2 = 0.02743640887145733` is
  `DERIVED/CONDITIONAL on C3`.
- Reionization-shape insensitivity is verified for high-l TT only; low-l EE is
  not closed.

The kappa audit found no hidden continuous fitted parameter, but it flags
manuscript hygiene: Paper 26 v1.1 contains inherited wording around
`delta Gamma` versus `gamma delta K` that should be clarified in v1.2.

## Dependencies

The public validation path uses Python standard library only. CLASS and Planck
likelihood assets are not redistributed.

## Citation

Associated manuscript:

Fife, D. *Interior Observer Paper 26 v1.2*. Zenodo.

Associated release:

`paper26-v1.2`
