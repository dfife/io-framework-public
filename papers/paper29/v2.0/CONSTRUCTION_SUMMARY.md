# Construction Summary

## Script Inventory

- `01_bao_kernel_coefficients.py`
  - Inputs: `gamma_BI`, `x`.
  - Outputs: `K_gauge`, `eta`, `exp(eta)`, `exp(eta/2)`.
  - Manuscript values verified: `K_gauge = 0.054873`, `eta = 0.036124`, `f_perp = 1.0368`, `f_parallel = 1.0182`.
  - External dependencies: none.

- `02_sound_speed_baryon_selector.py`
  - Inputs: IO observer branch constants, `omega_b h^2 = 0.020995719061702847`, CAMB.
  - Outputs: `r_d = 144.01351425392883 Mpc`, `z_drag = 1058.0903557310514`.
  - Manuscript values verified: `omega_b = 0.02100`, `r_d = 144.01 Mpc`.
  - External dependencies: CAMB as accepted drag-epoch solver.

- `03_desi_chronometer_confrontation.py`
  - Inputs: DESI DR2 GCcomb mean/covariance fetched by URL and SHA256, 35-point cosmic chronometer table.
  - Outputs: `CC chi2 = 14.701523963980787`, `BAO chi2 = 27.735229301342457`, `combined chi2 = 42.43675326532325`.
  - Manuscript values verified: `CC chi2 = 14.70`, `BAO chi2 = 27.74`, `combined chi2 = 42.44`, Planck combined `46.40`.
  - External dependencies: DESI DR2 BAO files and chronometer literature table.

- `04_reionization_prediction.py`
  - Inputs: CAMB tanh reionization representative with `tau = 0.054`, IO local and observer branch backgrounds.
  - Outputs: `z_50,IO = 10.185954753995242`, `tau_IO = 0.07373089905293533`.
  - Manuscript values verified: `z_50,IO = 10.19`, `tau_IO = 0.074`.
  - External dependencies: CAMB.

- `05_21cm_prediction.py`
  - Inputs: standard reduced 21cm formula, IO local/observer branch backgrounds, `T_CMB`.
  - Outputs: `z_dec = 123.67217038722819`, `y21 = -5.926231688179344`, `T21 = -190.78729466061188 mK`.
  - Manuscript values verified: `z_dec = 123.67`, `T_21 = -191 mK`.
  - External dependencies: standard 21cm brightness-temperature formula.

- `06_cmb_inventory.py`
  - Inputs: inherited IO constants and FIRAS-fixed `T_CMB`.
  - Outputs: `N_eff = 3.044`, `Omega_k = -0.04579112576013168`, cross-paper inherited constants.
  - Manuscript values verified: `N_eff = 3.044`, `Omega_k = -0.046`.
  - External dependencies: FIRAS temperature inherited through Paper 17.

- `07_validate_expected_outputs.py`
  - Inputs: frozen JSON outputs.
  - Outputs: PASS/FAIL validation lines and final summary.
  - Manuscript values verified: all frozen numerical claims above.

- `compute_omega_m_3x2pt.py`
  - Inputs: active Paper 10 legacy projected observer branch.
  - Outputs: `Omega_m,IO = 0.34868395067621694`.
  - Manuscript values verified: `Omega_m = 0.349`.
  - External dependencies: none.

- `compute_fsigma8_rsd.py`
  - Inputs: active closed `K=+1` IO branch, `gamma_growth = 6/11`, Paper 32 theorem-supported `sigma8(0) = 0.9274824965120383`.
  - Outputs: Euclid spectroscopic RSD table at `z = 0.9, 1.2, 1.5, 1.8`.
  - Manuscript values verified: §5.7 now has concrete bundle predictions.
  - External dependencies: standard GR growth-index approximation and Euclid RSD bin definitions.

- `compute_w0wa.py`
  - Inputs: constant `rho_Lambda`/CPL definition.
  - Outputs: `(w0, wa) = (-1, 0)` and conservative published Euclid forecast margins.
  - Manuscript values verified: §5.8 exact CPL prediction.
  - External dependencies: Euclid forecast margins from Euclid preparation VII.

## Noted Manuscript Issue

The manuscript states a `1:2` radial-to-transverse kernel coefficient ratio.
That statement is correct for the exponent coefficients `eta/2` and `eta`.
It is not exact for the exponential multiplier excesses:

```text
(exp(eta/2)-1)/(exp(eta)-1) = 0.49548454709362444
```

Suggested manuscript wording: "the exponent coefficient ratio is exactly
1:2" rather than "the multiplier excess ratio is exactly 1:2."

## New Manuscript Wording Check

Section 5.7 should not defer all numerical values to the bundle. The bundle now
produces the concrete pre-registered predictions:

| `z_eff` | `Delta z` | `f sigma_8(z)` |
| ---: | ---: | ---: |
| `0.9` | `0.2` | `0.514324146657992` |
| `1.2` | `0.2` | `0.4695277101511699` |
| `1.5` | `0.2` | `0.42668428712778506` |
| `1.8` | `0.3` | `0.3883581962136031` |

Recommended manuscript action: include this table in §5.7 and cite the bundle
as the computation source.
