# Paper 24 v2.3 Excited-State Import Recalculation

Classification: `verified / recomputation / PAPER24_V22_EXCITED_STATE_IMPORT`

## Verdict

Outcome: `B`, with a stable lithium conclusion.

The imported primary Henderson response does not reproduce the stated comparison value `R_ex = 0.666` as an exact central number under every convention. The corrected excited-state de-excitation convention gives:

- `R_ex(T9_eff) = 0.598746399`
- `R_34,tot(T9_eff) = 0.306711121`
- PRyMordial rerun: `Li7/H = 1.7239845810965594e-10` (`+0.464466 sigma`)
- `D/H = 2.5072194689896718e-05` (`-0.659351 sigma`)
- `Y_p = 0.2477087716917260` (`+0.677193 sigma`)

This means v2.3 should not say the central value is literally unchanged. It can say the primary-source excited-state response preserves the Paper 24 lithium result within the imported-source/convention band.

## Source Verification

Henderson 2019 reports `B(E2; 3/2- -> 1/2-) = 26(6)(3) e^2 fm^4`. The combined uncertainty used here is `6.708204 e^2 fm^4`.

Spin-multiplicity check:

`(2J_i+1) B(i->f) = (2J_f+1) B(f->i)`.

For Henderson's published upward `3/2- -> 1/2-` value:

`B(E2; 1/2- -> 3/2-) = 2 * 26 = 52.000000 e^2 fm^4`.

The Gemini statement that the factor gives about `13 e^2 fm^4` is rejected; it uses the inverse factor.

## Computation Rule

The import rule used here replaces the v2.1 cluster-deformation scale with the measured transition response:

`q_scale[b] = sqrt(B(E2)[e^2 fm^4]) / 100`

`q_trans,ex = q_scale * <F0>_amp,ex`

where `<F0>_amp,ex = 0.243206947874386` is the existing Paper 24 excited-branch amplitude-weighted Coulomb average.

Then:

`R_ex(T9) = exp[-epsilon_n * ((q_trans,ex/x)/Q_d) * nu_34(T9)]`

and:

`R_34,tot = f_gs R_gs + (1-f_gs) R_ex`.

## Henderson Cases

Primary excited-state de-excitation convention:

- `B(E2) = 52.000000 e^2 fm^4`
- `q_scale = 0.072111025509 b`
- `q_trans,ex = 0.017537902422 b`
- `R_ex(T9_eff) = 0.598746399`
- `R_ex(T9_eff)` 1-sigma B(E2) range = `0.562540169` to `0.642864359` (larger B gives stronger suppression)
- `Li7/H = 1.7239845810965594e-10`

Published upward Coulomb-excitation convention:

- `B(E2) = 26.000000 e^2 fm^4`
- `q_scale = 0.050990195136 b`
- `q_trans,ex = 0.012401169731 b`
- `R_ex(T9_eff) = 0.695804053`
- `R_ex(T9_eff)` 1-sigma B(E2) range = `0.665781730` to `0.731677820` (larger B gives stronger suppression)
- `Li7/H = 1.8722765602073408e-10`

Rejected half-factor diagnostic:

- `B(E2) = 13.000000 e^2 fm^4`
- `R_ex(T9_eff) = 0.773787050`
- `Li7/H = 1.9910571801847104e-10`
- This case is not load-bearing.

Paper 24 v2.1 comparison:

- stated comparison `R_ex = 0.666`
- old amplitude-weighted `q_trans,ex = 0.016538072455 b`
- old-q effective `R_ex(T9_eff) = 0.616512976`
- old-q effective `R_34,tot(T9_eff) = 0.311841442`

The corrected Henderson de-excitation scale `q_scale=0.072111 b` is close to the old cluster scale `0.068 b`; this is the important physical stability check.

## Lichtenstadt / Li-7 Mirror Cross-Check

The Lichtenstadt form-factor source is a mirror diagnostic, not an independent Be-7 import without an isospin/operator assumption. The TUNL A=7 table gives the Li-7 evaluated Coulomb-excitation value:

- `B(E2; 3/2- -> 1/2-) = 8.300000 +/- 0.500000 e^2 fm^4`

The TUNL electron-scattering C2 gamma-width row gives:

- `Gamma_gamma0(C2) = 2.800e-07 +/- 1.600e-07 eV`
- inferred `B(E2 down) = 13.987005 +/- 7.992574 e^2 fm^4`
- inferred `B(E2 up) = 6.993503 +/- 3.996287 e^2 fm^4`

This is consistent with the evaluated Li-7 E2 scale within the large C2-width uncertainty. Henderson's Be/Li evaluated-up ratio is:

- `B(E2)_Be / B(E2)_Li = 3.132530 +/- 0.829955`.

## TUNL Lifetime / Width Cross-Check

TUNL gives the Be-7 first excited-state lifetime:

- `tau = 192.000000 +/- 25.000000 fs`
- total width from lifetime: `3.428187e-03 eV`
- Henderson-implied E2 partial width: `6.101177e-07 eV`
- E2 fraction of total width: `1.779709e-04`

This confirms the lifetime is M1 dominated and cannot determine `R_ex` by itself. It is only a consistency check.

## Claim Boundary

- `verified`: Henderson numeric, spin-factor correction, TUNL lifetime, Li-7 mirror C2/evaluated-scale consistency, and PRyMordial reruns.
- `conditional`: the import rule mapping measured `B(E2)` to the Paper 24 TT branch-dressing scale.
- `not used`: Fasano 2021 and McCoy 2020 theoretical derivations as load-bearing imports.
- `not authoritative`: Odell/BRICK ANCs for this recomputation until author-verified data are received.

## References

- Henderson et al., Phys. Rev. C 99, 064320 (2019), DOI `10.1103/PhysRevC.99.064320`.
- Lichtenstadt et al., Phys. Lett. B 219, 394-398 (1989), DOI `10.1016/0370-2693(89)91083-6`.
- Tilley et al., Nucl. Phys. A 708, 3-163 (2002), DOI `10.1016/S0375-9474(02)00597-3`.
- Odell et al., Front. Phys. 10:888476 (2022), DOI `10.3389/fphy.2022.888476`.
