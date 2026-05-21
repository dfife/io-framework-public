# Paper 31 Legacy-Branch Full Recomputation

Active source package:

- `H0 = 67.57585653582628`
- `Omega_m = 0.34868395067621694`
- `Omega_k = -0.04579112576013168`
- `Omega_Lambda = 0.69701575761593`
- `Omega_r = 9.141746798467538e-05`
- `omega_b,geom = 0.020995719061702847`
- `omega_b,eff = 0.02898917105671435`
- `omega_b,clustering = 0.01703545264427447`
- `r_d = 144.01351425392883`
- `eta = 0.036124605346983495`
- `Sigma_IO = 0.8113774333810703`

| Item | Recomputed legacy-branch value | Old Schur value | Flag |
| --- | --- | --- | --- |
| 1. Geometric pre-drag ruler | `r_d = 144.013514253929 Mpc`; same active hybrid computation as Paper 29 = `True` | `143.062502836870 Mpc` | changed numerically |
| 2. BAO galaxy block closure | target `r_d = 147.089909600711 Mpc`; kernel proxy `r_eff = 148.378124571145 Mpc`; residual `= +0.875801%`; `chi2_gal = 25.995084730417` | target `= 143.958948796224 Mpc`; residual `= 0.046000%` | qualitative change: old scalar near-hit does not survive |
| 3. sigma8 -> S8_raw -> S8_weyl | `sigma8 = 0.953281584319239`; `S8_raw = 1.027724133515123`; `S8_weyl = 0.833872169675285`; `pull_weyl(~0.79±0.02) = +2.194σ` | `sigma8 = 0.949`; `S8_lens = 0.793` | qualitative change: old on-target S8 claim does not survive |
| 4. E_G pipeline | `alpha_Phi = 2.005`; `1sigma = [1.785, 2.247]`; `E_G(0.57,no-slip) = 0.423415947410` | `alpha_Phi = 1.992`; `1sigma = [1.772, 2.234]` | no qualitative change |
| 5. Reionization transport factors | `R_reio(5) = 1.621689161`; `R_reio(10) = 1.579842957`; `R_reio(14) = 1.568400981`; `R_reio(20) = 1.559884367` | `R_reio(5) ≈ 1.64`; `R_reio(10) ≈ 1.59`; `R_reio(14) ≈ 1.58`; `R_reio(20) ≈ 1.57` | no qualitative change |
| 6. tau reconciliation | `tau_cov,IO = 0.02743640887145733` | `tau_cov,IO = 0.02743640887145733` | unchanged |
| 7. Structured bulk candidate | `omega_b,struct = 0.02143434229616185` | `omega_b,struct = 0.025941102017499` | qualitative change: formula/value no longer the old structured point |
| 8. CMB Weyl half-order kernel | `lcmb_rescale = 0.811377433381070`; `lcmb_tilt = -0.500`; `A_L_surrogate = 0.658333339400053` | `lcmb_rescale = 0.811374048924378`; `A_L_surrogate = 0.658327827169274` | no qualitative change |
| 9. Observable-class map numerics | active slots should read `H0 = 67.575856535826`, `Omega_m = 0.348683950676217`, `Omega_k = -0.045791125760132`, `r_d = 144.013514253929`, `Sigma_IO = 0.811377433381070` | map file still contains the Schur fixed-slot numerics | qualitative change: map is numerically stale |
| 10. Lyalpha BAO conditional consistency | target `r_d = 142.837502285500 Mpc`; raw residual `= +0.823322%`; shifted residual `= -0.134500%`; `chi2_raw = 1.740144570926`; `chi2_shifted = 0.301395017943` | target `= 140.790554518058 Mpc`; `chi2_raw = 6.176391241793`; `r_shifted = 141.703409059919 Mpc` | no qualitative change |

## Notes

- Item 2 uses the Paper 29 derived/scoped galaxy kernel exactly as implemented in the live block-split evaluator: `D_M -> D_M / exp(eta)`, `D_H -> D_H / exp(eta/2)` on the galaxy/quasar block only.
- Item 2 therefore does not admit a unique scalar effective ruler. The reported `r_eff` is an information-weighted proxy built from the current galaxy block quantity weights.
- Item 5 follows the existing Paper 31 Step 522 homogeneous-OS transport convention so it stays comparable to the published Schur-era values.
- Item 9 is a numerical verification against the current map file, not an edit of the map file itself.
