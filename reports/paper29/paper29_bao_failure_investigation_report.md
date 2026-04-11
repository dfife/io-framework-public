# Paper 29 BAO χ² failure investigation on the i.i.d. branch

## Headline

- `derived`: the BAO failure is not a generic distance-integral bug.
- `derived`: with the user's carried universal ruler `r_d = 143.3 Mpc`, the failure is almost entirely the galaxy/quasar block, not Lyα.
- `verified`: a blockwise effective-ruler repair can reduce BAO χ² from `94.36149688498531` to `18.69455749443472`.
- `derived`: this repair is not theorem-grade on the current clean stack. A first-principles rebuild of the i.i.d. raw rulers from the rebuilt slot formulas gives `126–131 Mpc`, not `143–147 Mpc`.

## Inputs

- IO i.i.d. branch: `H0 = 67.57585653582628`, `Omega_m = 0.34868395067621694`, `Omega_k = -0.04579112576013168`, `Omega_r = 0.0001226`, `Omega_lambda_eval = 0.6969845750839148`
- Planck reference BAO χ²: `28.693892246596665`
- baseline carried ruler: `r_d = 143.3 Mpc`

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

| raw ruler case | `r_d` [Mpc] | BAO χ² |
|---|---:|---:|
| `baseline_carried_universal_rd` | `143.3` | `94.36149688498531` |
| `rebuilt_iid_geom_projected` | `126.14246120316851` | `3387.1691619039448` |
| `rebuilt_iid_eff_projected` | `118.1453440592955` | `7474.731411336498` |
| `rebuilt_iid_clust_projected` | `130.99467997791825` | `1831.0275236446082` |
| `legacy_transplanted_geom_small` | `144.15060015039327` | `65.37086343599168` |
| `legacy_transplanted_clust_small` | `147.63986853811437` | `43.84168455502238` |
| `best_universal_effective_rd` | `146.37650251955117` | `34.30000226473537` |

The crucial point is that the clean rebuilt i.i.d. raw rulers (`126.142...`, `118.145...`, `130.994...`) make BAO catastrophically worse. So the carried `143.3 Mpc` was already a soft Schur-era import, not a clean i.i.d. theorem output.

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
| `legacy_small_clustering_galaxy_plus_lya_raw_baseline` | `147.63986853811437` | `143.3` | `20.47237436302415` |

## Combined impact

- original combined CC+BAO χ²: `109.06315858748277`
- Planck combined CC+BAO χ²: `43.77291370446457`
- conditional repaired combined CC+BAO χ²: `33.39621919693218`

## Conclusion

- `derived`: the source of the published BAO failure is the universal-ruler assumption on a block-mixed BAO observable, together with a carried Schur-era ruler value (`143.3 Mpc`) that is not the clean i.i.d. raw output.
- `verified`: if one allows block-specific effective readout rulers, the BAO χ² can be cut from `94.36149688498531` to `18.69455749443472` and the combined CC+BAO χ² to `33.39621919693218`.
- `derived`: this is not a theorem-grade closure. Under the current clean Papers 9–28 stack, the first-principles i.i.d. raw ruler rebuild lands at `126–131 Mpc`, so the needed `142–147 Mpc` effective rulers require an additional BAO readout theorem or an explicit observational selection.
- `headline resolution`: a theorem-grade BAO fix is impossible under the current stack. The strongest surviving repair is conditional and blockwise, not derived.

## Files

- baseline residual table: `paper29_bao_failure_investigation_baseline_residuals.csv`
- repaired residual table: `paper29_bao_failure_investigation_repaired_residuals.csv`
