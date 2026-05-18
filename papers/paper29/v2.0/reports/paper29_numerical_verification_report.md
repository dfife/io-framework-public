# Paper 29 v2.0 Numerical Verification Report

## Summary

- Total validation checks: 18
- PASS: 18
- FAIL: 0

## Checked Claims

- `K_gauge = 0.05487281774291466`: PASS
- `eta = K_gauge/x = 0.036124605346983495`: PASS
- `f_perp = exp(eta) = 1.036785027400527`: PASS
- `f_parallel = exp(eta/2) = 1.0182264126413767`: PASS
- `omega_b h^2 = 0.020995719061702847`: PASS
- `r_d = 144.01351425392883 Mpc`: PASS
- `CC chi2 = 14.701523963980787`: PASS
- `BAO chi2 = 27.735229301342457`: PASS
- `combined chi2 = 42.43675326532325`: PASS
- `z_50,IO = 10.185954753995242`: PASS
- `tau_IO = 0.07373089905293533`: PASS
- `z_dec = 123.67217038722819`: PASS
- `y21 = -5.926231688179344`: PASS
- `T21 = -190.78729466061188 mK`: PASS
- `N_eff = 3.044`: PASS
- `Omega_k,IO = -0.04579112576013168`: PASS
- `Omega_m,IO = 0.34868395067621694`: PASS
- `f sigma_8(z=1.2) = 0.4695277101511699`: PASS
- `(w0, wa) = (-1, 0)` via `cpl_residual_norm = 0`: PASS

## Surface Issue Flagged

The manuscript's `1:2` ratio language should refer to exponent coefficients,
not exponential multiplier excesses.
