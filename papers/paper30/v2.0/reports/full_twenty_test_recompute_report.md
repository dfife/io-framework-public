# Paper 30 Full Recomputation on the Paper 10 Legacy Branch

All branch-dependent Paper 30 tests were recomputed on the active Paper 10 legacy branch using the user-specified closed-FRW background, standard thermal radiation with `N_eff = 3.044`, and the carried Paper 29 baryon / BAO inputs where applicable.

## Active Inputs

- `H0 = 67.57585653582628`
- `Omega_m = 0.34868395067621694`
- `Omega_k = -0.04579112576013168`
- `Omega_lambda = 0.69701575761593`
- `Omega_r = 9.141746798467538e-05`
- `r_d = 144.01351425392883 Mpc`
- `omega_b,geom = 0.020995719061702847`
- `eta = 0.036124605346983495`

## Scorecard

| Test | IO current | Planck/reference | Old Schur | Change flag |
|---|---:|---:|---:|---|
| 1. Pantheon+ Type Ia SNe | `chi2=1757.480` | `chi2=1759.695` | `IO=1755.547` / `Planck=1759.737` | no category change |
| 2. TDCOSMO strong lensing | `chi2=31.598` | `chi2=34.462` | `IO=23.848` / `Planck=34.578` | no category change |
| 3. GW standard sirens | `GW170817=-0.24σ` / `GW170817 afterglow=-0.32σ` / `GWTC-3=-0.04σ` / `O4a dark+bright=-0.57σ` | `GW170817=-0.26σ` / `GW170817 afterglow=-0.36σ` / `GWTC-3=-0.06σ` / `O4a dark+bright=-0.61σ` | `H0=68.91 inside all bars` | no category change |
| 4. Alcock-Paczynski | `chi2=7.883`, `pte=0.247` | `chi2=6.703`, `pte=0.349` | `IO=9.288` / `Planck=6.710` | no category change |
| 5. Three-baryon structure | `omega_b_geom=0.02100` / `omega_b_eff=0.02899` / `omega_b_clustering=0.01704` / `omega_b_naive_bdp=0.04979` | n/a | `omega_b_geom=0.02108` / `omega_b_eff=0.02910` / `omega_b_clustering=0.01705` | category change: legacy -> recomputed |
| 6. FRB dispersion measures | `omega_b_geom=105.03` / `omega_b_eff=128.52` / `omega_b_clustering=121.64` / `omega_b_naive_bdp=547.15` | n/a | `omega_b_geom=105.68` / `omega_b_eff=124.36` / `omega_b_naive_f_b_times_Omega_m=513.51` / `omega_b_best_fit_from_frbs=103.47` | category change: omega_b_best_fit_from_frbs (fitted), closest carried slot omega_b_geom -> omega_b_geom |
| 7. kSZ pairwise momentum | `omega_b_geom=1.12x` / `omega_b_eff=1.28x` / `omega_b_clustering=1.00x` / `omega_b_naive_bdp=1.29x` | `reference=1.00x` | `flat_reference=1.00x` / `schur_acoustic_slot=1.24x` / `schur_alpha1_geometric_slot=1.09x` / `schur_clustering_slot=0.97x` / `schur_naive_bdp_fraction=2.83x` | category change: omega_b_clustering nearest; raw BDP excluded -> omega_b_clustering |
| 8. Cluster X-ray gas fractions | `omega_b_geom=0.105` / `omega_b_eff=0.146` / `omega_b_clustering=0.086` / `omega_b_naive_bdp=0.250` | n/a | `omega_b_geom=0.106` / `omega_b_eff=0.146` / `omega_b_clustering=0.086` / `omega_b_raw_bdp_times_Omega_m=0.250` | no category change |
| 9. Lyman-alpha forest UVB | `z=2.0:1.109` / `z=3.0:0.763` / `z=4.0:0.845` | benchmark UVB imported | `z=2.0:1.076` / `z=3.0:0.743` / `z=4.0:0.825` | category change: legacy -> recomputed |
| 10. Angular diameter distance minimum | `z_max=1.53240` | `z_max=1.58764` | `z_max=1.56311` | category change: legacy -> recomputed |
| 11. Sandage-Loeb drift | `z=2:-0.798` / `z=3:-3.743` / `z=4:-6.515` / `z=5:-9.083` | `z=2:-0.225` / `z=3:-2.935` / `z=4:-5.513` / `z=5:-7.912` | `z=2.0:-0.790` / `z=3.0:-3.686` / `z=4.0:-6.420` / `z=5.0:-8.957` | category change: legacy -> recomputed |
| 12. S8 and Weyl response | `Sigma=0.811377`, `S8=0.833872` | `S8_flat=0.831702` | `Sigma=0.811377`, `S8=0.793375` | category change: legacy -> recomputed |

## Detailed Notes

- Pantheon+: `IO chi2 = 1757.479817`, `Planck chi2 = 1759.694785`, `Delta chi2 = -2.214967`.
- TDCOSMO: `IO chi2 = 31.597640`, `Planck chi2 = 34.462261`.
- AP: `IO chi2 = 7.883415`, `Planck chi2 = 6.702670`.
- Observer-frame FRW age on the active branch: `13.543919214135 Gyr`.
- Paper 29 carried scorecard: `CC = 14.701524`, `BAO = 27.735229`, `combined = 42.436753`.
- Planck carried scorecard: `CC = 15.153309`, `BAO = 31.251011`, `combined = 46.404320`.

## Baryon Slots

- `omega_b,geom = 0.020995719061703`
- `omega_b,eff = 0.028989171056714`
- `omega_b,clustering = 0.017035452644274`
- `omega_b,naive = 0.049791422650873`

## S8 / Weyl Response

- `Sigma_IO = x^(-1/2) = 0.811377433381070`
- `sigma8_clustering = 0.953281584319239`
- `S8_clustering = 1.027724133515123`
- `S8_weyl_response = 0.833872169675285`

