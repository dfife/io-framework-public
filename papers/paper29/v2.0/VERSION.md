# Version

- Paper: 29
- Paper version: v2.0 working draft
- Bundle version: v2.0
- Bundle build date: 2026-05-18
- Intended release tag: `paper29-v2.0`

## Constants Snapshot

- `gamma_BI = 0.2375`
- `x = 1.5189873277742727`
- `K_gauge = ln(1 + gamma_BI^2) = 0.05487281774291466`
- `eta = K_gauge / x = 0.036124605346983495`
- `R4_FIRAS = 1.0031014644`
- `H0 = 67.57585653582628 km/s/Mpc`
- `Omega_m = 0.34868395067621694`
- `Omega_k = -0.04579112576013168`
- `Omega_lambda = 0.6970157307777745`
- `omega_b h^2 = 0.020995719061702847`
- `r_d = 144.01351425392883 Mpc`
- `N_eff = 3.044`
- `sigma8_theorem_active = 0.9274824965120383`

## Bundle Extension

The 2026-05-18 extension adds reproducibility coverage for Paper 29 v2.0
subsections 5.6, 5.7, and 5.8:

- Euclid DR1 3x2pt matter density, `Omega_m,IO = 0.34868395067621694`.
- Euclid RSD `f sigma_8(z)` table at `z = 0.9, 1.2, 1.5, 1.8`.
- CPL dark-energy equation of state, `(w0, wa) = (-1, 0)`.

## R4/FIRAS Boundary

No Paper 29 script uses `R4 = 1`. The bundle records `R4_FIRAS` only as an
inherited observer-side thermal normalization. The CMB temperature is not
validated as an independent prediction.
