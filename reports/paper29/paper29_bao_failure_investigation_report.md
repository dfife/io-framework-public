# Paper 29 BAO χ² failure investigation on the i.i.d. branch

## Headline

- `derived`: the BAO failure is not a generic distance-integral bug.
- `derived`: with the user's carried universal ruler `r_d = 143.3 Mpc`, the failure is almost entirely the galaxy/quasar block, not Lyα.
- `verified`: a blockwise effective-ruler repair can reduce BAO χ² from `94.36149688498531` to `18.69455749443472`.
- `derived`: this repair is not theorem-grade on the current clean stack. An independent drag-ruler rebuild from an explicit drag-redshift fit plus sound-horizon integral gives raw i.i.d. rulers far below the `143–147 Mpc` range required by BAO.

## Inputs

- IO i.i.d. branch: `H0 = 67.57585653582628`, `Omega_m = 0.34868395067621694`, `Omega_k = -0.04579112576013168`, `Omega_r = 0.0001226`, `Omega_lambda_eval = 0.6969845750839148`
- Planck reference BAO χ²: `28.693892246596665`
- baseline carried ruler: `r_d = 143.3 Mpc`
- independent raw-ruler method: Eisenstein-Hu `z_drag` fit plus direct `r_d = ∫ c_s(z)/H(z) dz` evaluation on the fixed background

## Baseline BAO failure split

- total BAO χ²: `94.36149688498531`
- galaxy/quasar block χ² (`z < 2`): `93.84973288789105`
- Lyα block χ² (`z = 2.33`): `0.5117639970942675`
- `DV/r_d` subblock χ²: `13.956447267124371`
- `DM/r_d` subblock χ²: `38.47125417836284`
- `DH/r_d` subblock χ²: `17.864702593747214`
- `DM/r_d + DH/r_d` subblock χ²: `80.40504961786094`

## Curvature-only checks

| distance curvature slot | BAO χ² with `r_d = 143.3` |
|---|---:|
| `0.0` | `108.68272890264709` |
| `-0.04579112576013168` | `94.36149688498531` |
| `-0.13` | `78.44132912201063` |

Interpretation: using the geometric curvature in the `sin()` distance law helps only modestly. The dominant miss is shared by radial and transverse ratios, so curvature alone cannot fix it.

## Rebuilt i.i.d. raw ruler check

- derived `x = 1.5189873277742727`
- derived `Delta = 5.624029175326855`
- derived `omega_m = 0.15922640008111233`
- current rebuilt slot formulas give:
  - `omega_b,geom(projected) = 0.04979142265087259`
  - `omega_b,eff(projected) = 0.06874792257132821`
  - `omega_b,clust(projected) = 0.040399636714857086`

### Method self-check

- Planck validation branch with `omega_b = 0.02237` gives `z_drag = 1020.7170041025374`, `r_d = 150.60673061016593 Mpc`
- compared to published Planck `r_d = 147.09 Mpc`, the independent approximation shifts by `Δr_d = 3.516730610165922 Mpc` (`0.023908699504833247` fractional)

| raw ruler case | `r_d` [Mpc] | BAO χ² |
|---|---:|---:|
| `baseline_carried_universal_rd` | `143.3` | `94.36149688498531` |
| `rebuilt_iid_geom_projected` | `119.35671697962852` | `6712.262979090998` |
| `rebuilt_iid_eff_projected` | `111.58630122453062` | `12701.075082308149` |
| `rebuilt_iid_clust_projected` | `124.09725463682976` | `4234.313102398228` |
| `legacy_transplanted_geom_small` | `137.13486395470997` | `626.101617375417` |
| `legacy_transplanted_clust_small` | `140.66796607206828` | `248.9016703573142` |
| `best_universal_effective_rd` | `146.37650251955117` | `34.30000226473537` |

The crucial point is that even the independent rebuilt i.i.d. raw rulers lie far below the BAO-required range. The projected-slot rulers are approximately `119.357`, `111.586`, and `124.097 Mpc`; even the small carried baryon slots only give approximately `137.135` and `140.685 Mpc`. So the carried `143.3 Mpc` was already a soft Schur-era import, not a clean i.i.d. theorem output.

## Effective-ruler scans

- best universal effective ruler on the fixed i.i.d. geometry: `r_d,eff = 146.37650251955117 Mpc` -> `chi2 = 34.30000226473537`
- best blockwise effective rulers on the fixed i.i.d. geometry:
  - galaxy/quasar block: `r_d,gal = 147.0843116339564 Mpc`
  - Lyα block: `r_d,lya = 142.82224746086274 Mpc`
  - full 13-point BAO `chi2 = 18.69455749443472`

## Strongest conditional repairs

| repair | `r_d,gal` [Mpc] | `r_d,lya` [Mpc] | BAO χ² |
|---|---:|---:|---:|
| `best_blockwise_effective_rulers` | `147.0843116339564` | `142.82224746086274` | `18.69455749443472` |
| `best_galaxy_effective_plus_lya_raw_baseline` | `147.0843116339564` | `143.3` | `18.9410816646038` |
| `legacy_small_clustering_galaxy_plus_lya_raw_baseline` | `140.66796607206828` | `143.3` | `243.94632373973394` |

## Combined impact

- original combined CC+BAO χ²: `109.06315858748277`
- Planck combined CC+BAO χ²: `43.77291370446457`
- conditional repaired combined CC+BAO χ²: `33.39621919693218`

## Conclusion

- `derived`: the source of the published BAO failure is the universal-ruler assumption on a block-mixed BAO observable, together with a carried Schur-era ruler value (`143.3 Mpc`) that is not the clean i.i.d. raw output.
- `verified`: if one allows block-specific effective readout rulers, the BAO χ² can be cut from `94.36149688498531` to `18.69455749443472` and the combined CC+BAO χ² to `33.39621919693218`.
- `derived`: this is not a theorem-grade closure. Under the current clean Papers 9–28 stack, the independent raw ruler rebuild lands at `111–124 Mpc` for the projected slots, and only `137–141 Mpc` even for the small carried baryon slots, so the needed `142–147 Mpc` effective rulers require an additional BAO readout theorem or an explicit observational selection.
- `headline resolution`: a theorem-grade BAO fix is impossible under the current stack. The strongest surviving repair is conditional and blockwise, not derived.

## Files

- baseline residual table: `paper29_bao_failure_investigation_baseline_residuals.csv`
- repaired residual table: `paper29_bao_failure_investigation_repaired_residuals.csv`
