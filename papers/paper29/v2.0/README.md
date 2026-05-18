# Paper 29 v2.0 Reproducibility Bundle

Paper 29 v2.0 is a numerical-prediction bundle for the galaxy/quasar BAO
readout kernel, the sound-speed baryon selector, DESI DR2 plus cosmic
chronometer confrontation, Cosmic Dawn diagnostics, and CMB inventory values.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper29/v2.0
python3 -m pip install -r environment/requirements.txt
python3 scripts/07_validate_expected_outputs.py
```

Expected final line:

```text
Paper 29 v2.0 validation summary: total checks=15, pass count=15, fail count=0
```

## What This Bundle Reproduces

- BAO kernel constants: `K_gauge = 0.05487281774291466`, `eta = 0.036124605346983495`, `f_perp = 1.036785027400527`, `f_parallel = 1.0182264126413767`.
- Sound-speed baryon selector: `omega_b h^2 = 0.020995719061702847`, `r_d = 144.01351425392883 Mpc`.
- DESI DR2 plus cosmic chronometer confrontation: `CC chi2 = 14.701523963980787`, `BAO chi2 = 27.735229301342457`, `combined chi2 = 42.43675326532325`.
- Reionization representative: `z_50,IO = 10.185954753995242`, `tau_IO = 0.07373089905293533`.
- Reduced 21cm benchmark: `z_dec = 123.67217038722819`, `y_21 = -5.926231688179344`, `T_21 = -190.78729466061188 mK`.
- CMB inventory: `N_eff = 3.044`, `Omega_k,IO = -0.04579112576013168`.
- Euclid DR1 3x2pt matter density: `Omega_m,IO = 0.34868395067621694`.
- Euclid spectroscopic redshift-space-distortion table:
  `f sigma_8 = 0.514324146657992` at `z=0.9`,
  `0.4695277101511699` at `z=1.2`,
  `0.42668428712778506` at `z=1.5`,
  and `0.3883581962136031` at `z=1.8`.
- CPL dark-energy equation of state: `(w0, wa) = (-1, 0)`.

## Claim Boundary

The CMB temperature is not treated as an independent IO prediction. It is the
FIRAS-fixed observer-side thermal datum inherited from Paper 17 v1.5 through
`R4_FIRAS = 1.0031014644`.

The reionization and 21cm calculations are scoped representatives: they import
standard exterior atomic and radiative-transfer physics under Premise 2 and
substitute the IO closed `K=+1` observer/local background where stated.

The `f sigma_8` script uses the active projected Paper 10 legacy branch and the
Paper 32 theorem-supported `sigma_8(0) = 0.9274824965120383`. This is a
conditional-verified active-branch calculation, not a universal proof that all
historical IO branches share the same late-time growth background.

DESI DR2 BAO mean and covariance files are not redistributed. Script
`03_desi_chronometer_confrontation.py` fetches them from the Cobaya `bao_data`
repository and checks SHA256 before use.

## Citation

If using this bundle, cite the associated Paper 29 v2.0 Zenodo record and the
GitHub release tag `paper29-v2.0` once published.
