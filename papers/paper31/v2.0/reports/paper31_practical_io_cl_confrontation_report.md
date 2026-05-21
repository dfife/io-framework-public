# Paper 31 Practical IO C_l Confrontation

Date: 2026-04-03

## Scope

This is a direct fixed-parameter confrontation against the local Planck 2018
Plik-lite TTTEEE package with low-ell TT bins. It is **not** a fit.
The TE/EE confrontation is therefore high-ell only; low-ell EE is not binned here.
The IO cases also omit astrophysical reionization in the CLASS layer on purpose.

The practical calculator uses exactly the surviving Paper 31 ingredients:

- closed `S^3` / curved FRW transfer backbone
- derived baryon-assignment map
- exact curved Weyl kernel
- inherited recombination class under Premise 2
- optical-history complement only as a conditional candidate branch
- explicit labeling of the open Stage-2 thermodynamics seam

## Fixed constants

- `x = 1.519`
- `gamma = 0.2375`
- `f_Gamma = 1/(1+gamma^2) = 0.946605531726076`
- `K_gauge = log(1+gamma^2) = 0.05487281774291466`
- `tau_cov,IO = K_gauge/2 = 0.02743640887145733`
- `A_s^native = 2.0072459972737347e-09`
- `lcmb_rescale = x^(-1/2) = 0.8113740489243784`
- `lcmb_curved_shift = -3`
- `lcmb_curved_order = -1/4`
- active Schur background: `H0 = 68.91`, `Omega_k = -0.005613722564239`

## Baryon map used

- chemistry / local opacity inventory: `omega_b,geom = 0.02108` (`derived / scoped`)
- reduced visibility/readout class: `omega_b,eff = 0.0291` (`derived / scoped`)
- clustering branch: `omega_b,clustering = 0.017053042566349` (`derived / no-go` for CMB metric source)
- `R`-loading exact slot: `open`

The practical calculator therefore compares two IO compressions:

1. control compression: `omega_b = 0.0271`
2. structured conditional branch: `omega_b,struct = 0.02594110201749857` with `(c_vis, d_drag, h_hier) = (f_Gamma^2, 1, f_Gamma^3)`

## Stage-2 boundary

This run inherits the accepted exterior recombination class under Premise 2.
The exact IO local Stage-2 atomic-radiative renormalization remains open.
The geometry and harmonic layer are already non-flat: the local CLASS build uses
closed-FRW transfer and hyperspherical-harmonic machinery when `Omega_k < 0`.
The remaining practical leak is Stage-2 thermodynamics/recombination, not flat
line-of-sight geometry.
The inherited late reionization history is left out of the CLASS run here, because
Paper 31 does not license identifying the source-side `tau_cov = K_gauge/2` with
astrophysical `tau_reio` inside `reio_camb`.
So these spectra are practical conditional confrontations, not a theorem-closed
exact IO-native Boltzmann solution.
Low-ell EE remains a separate inherited-reionization sector and is not directly
binned by the local Plik-lite package used here.

## Data path

- Plik-lite: `/opt/cosmology-lab/tmp/planck-lite-py/data/planck2018_plik_lite/cl_cmb_plik_v22.dat`
- covariance: `/opt/cosmology-lab/tmp/planck-lite-py/data/planck2018_plik_lite/c_matrix_plik_v22.dat`
- low-ell TT bins: `/opt/cosmology-lab/tmp/planck-lite-py/data/planck2018_low_ell/CTT_bin_low_ell_2018.dat`

## Main fixed-case residuals

### IO derived backbone + inherited recombination (control compression)

- status: `conditional / scoped practical`
- total `chi2_TTTEEE+lowTT = 3445.283862`
- `A_eff source proxy = 1.9000701645543414e-09`
- `100*theta_s = 1.051794672`
- `z_rec = 1085.242323`
- `rs_rec = 138.049592 Mpc`
- note: Closed S^3 background and exact curved Weyl kernel are fixed. A_s is the native IO value. No astrophysical reionization history is inserted into the CLASS layer here, because Paper 31 does not license identifying the source-side tau_cov proxy with CLASS tau_reio. Exact Stage-2 local renormalization and exact R-loading slot remain open. The background package is the active Schur branch, not the retired 67.58 mixed branch.

Diagonal sigma residual summary `(model-Planck)/sigma`:

- TT low: mean `+1.863214`, rms `2.248662`, max `|sigma| = 3.122148`
- TT high: mean `+0.854664`, rms `2.510939`, max `|sigma| = 6.227336`
- TE: mean `+0.768828`, rms `2.448107`, max `|sigma| = 6.679759`
- EE: mean `-0.455773`, rms `1.781101`, max `|sigma| = 5.058382`

### IO practical structured branch + optical-history complement candidate

- status: `conditional / scoped practical`
- total `chi2_TTTEEE+lowTT = 2135.722987`
- `A_eff source proxy = 1.9000701645543414e-09`
- `100*theta_s = 1.056106033`
- `z_rec = 1086.286533`
- `rs_rec = 138.617451 Mpc`
- note: Uses the Paper 31 structured branch candidate: omega_b,struct plus (c_vis, d_drag, h_hier) = (f_Gamma^2, 1, f_Gamma^3). This is the best current practical high-ell CMB branch. No astrophysical reionization history is inserted into the CLASS layer here. It remains conditional because the post-bridge optical-history complement and exact typed thermodynamics law are not derived. The background package is the active Schur branch, not the retired 67.58 mixed branch.

Diagonal sigma residual summary `(model-Planck)/sigma`:

- TT low: mean `+1.840278`, rms `2.207910`, max `|sigma| = 3.060213`
- TT high: mean `-0.155647`, rms `2.060371`, max `|sigma| = 5.328952`
- TE: mean `-0.045088`, rms `1.939488`, max `|sigma| = 5.103519`
- EE: mean `+0.246761`, rms `1.390016`, max `|sigma| = 4.660567`

### Flat LCDM Planck 2018 reference

- status: `external reference`
- total `chi2_TTTEEE+lowTT = 619.314107`
- `A_eff source proxy = 1.8839589960775909e-09`
- `100*theta_s = 1.040370920`
- `z_rec = 1088.783081`
- `rs_rec = 144.547551 Mpc`
- note: Fixed Planck-like LCDM reference used only to calibrate the residual machinery. This is not an IO prediction.

Diagonal sigma residual summary `(model-Planck)/sigma`:

- TT low: mean `+1.288656`, rms `1.490818`, max `|sigma| = 2.038259`
- TT high: mean `+0.106997`, rms `0.931772`, max `|sigma| = 3.338999`
- TE: mean `-0.045569`, rms `0.994440`, max `|sigma| = 2.798344`
- EE: mean `-0.080061`, rms `0.989230`, max `|sigma| = 2.498334`

## Fixed-case comparison

- structured conditional minus IO backbone control: `Delta chi2 = -1309.560874`
- structured conditional minus LCDM reference: `Delta chi2 = +1516.408881`
- covariance-block change TT high: `-492.726850`
- covariance-block change TE: `-539.994350`
- covariance-block change EE: `-311.561795`

So the structured fixed branch gains most strongly in `TE` and `EE`, while the
remaining dominant failure is still a negative high-ell `TT` shape wall.

## Largest residual bins on the practical IO branch

### TT

- `ell~779`: model `0.026431700394879312`, data `0.02431014801866934`, residual `+5.328952 sigma`
- `ell~464`: model `0.05834626403252204`, data `0.06478587456759065`, residual `-5.181020 sigma`
- `ell~734`: model `0.02593979338739052`, data `0.02387604389151558`, residual `+5.173952 sigma`
- `ell~716`: model `0.025423043979768373`, data `0.02336150088305026`, residual `+5.171853 sigma`
- `ell~1184`: model `0.00474385707535288`, data `0.005089812287678942`, residual `-4.742977 sigma`
- `ell~725`: model `0.025672671211927407`, data `0.02380640044993535`, residual `+4.688693 sigma`
- `ell~770`: model `0.0265396550888492`, data `0.02485440715008229`, residual `+4.218721 sigma`
- `ell~1157`: model `0.005395396922984557`, data `0.005724065270291641`, residual `-4.024658 sigma`

### TE

- `ell~653`: model `-0.0005332446605431471`, data `-0.0002262107564763694`, residual `-5.103519 sigma`
- `ell~662`: model `-0.0007291461965261579`, data `-0.000428549853731005`, residual `-5.074542 sigma`
- `ell~194`: model `-0.004985292724111684`, data `-0.003013468022313202`, residual `-4.366322 sigma`
- `ell~644`: model `-0.00033739785070389407`, data `-7.613088815049663e-05`, residual `-4.266133 sigma`
- `ell~635`: model `-0.0001489995969935946`, data `0.000117323699327342`, residual `-4.263898 sigma`
- `ell~203`: model `-0.0027953868414056057`, data `-0.001094632274544606`, residual `-4.098008 sigma`
- `ell~707`: model `-0.0014773765919370548`, data `-0.00125466391939437`, residual `-4.008228 sigma`
- `ell~842`: model `-9.895972191171008e-06`, data `-0.0001581509173892687`, residual `+3.914618 sigma`

### EE

- `ell~590`: model `0.0003345797457583238`, data `0.0002753843951509043`, residual `+4.660567 sigma`
- `ell~599`: model `0.00037105808943208875`, data `0.0003186175356020685`, residual `+3.946269 sigma`
- `ell~149`: model `0.0003716495484591375`, data `0.0002827521695864853`, residual `+3.395391 sigma`
- `ell~626`: model `0.000466388187966371`, data `0.0004159953775114264`, residual `+3.376773 sigma`
- `ell~905`: model `0.00021816330939038783`, data `0.0001784174198948312`, residual `+3.340780 sigma`
- `ell~167`: model `0.0002625715085507079`, data `0.0001915773606985458`, residual `+3.300285 sigma`
- `ell~572`: model `0.00026358054416357793`, data `0.0002279597651277145`, residual `+3.086180 sigma`
- `ell~97`: model `0.0005599779891357315`, data `0.000379873029008304`, residual `+2.994596 sigma`

## Exact D_l samples on the practical IO branch

### TT

- target `220` -> `ell = 220`, `Dl = 6109.354068674714`
- target `546` -> `ell = 546`, `Dl = 2469.7847221827114`
- target `800` -> `ell = 800`, `Dl = 2618.1103612766788`
- target `1000` -> `ell = 1000`, `Dl = 1057.4479541415017`
- target `1500` -> `ell = 1500`, `Dl = 657.6652193380909`
- target `2000` -> `ell = 2000`, `Dl = 229.77414445860384`

### TE

- target `150` -> `ell = 150`, `Dl = -53.335619528925506`
- target `300` -> `ell = 300`, `Dl = 124.12973637329797`
- target `450` -> `ell = 450`, `Dl = -61.866642294876534`
- target `800` -> `ell = 800`, `Dl = -77.98731708275899`
- target `1200` -> `ell = 1200`, `Dl = 1.0852087887341622`

### EE

- target `150` -> `ell = 150`, `Dl = 1.3199002238278654`
- target `300` -> `ell = 300`, `Dl = 8.91052200015873`
- target `450` -> `ell = 450`, `Dl = 15.735990165371154`
- target `800` -> `ell = 800`, `Dl = 15.437257614298685`
- target `1200` -> `ell = 1200`, `Dl = 20.006552617922164`

## Verdict

- `verified`: a practical fixed-IO `C_l` calculator now exists on the local patched CLASS stack.
- `derived / scoped`: the exact curved Weyl kernel is active in the confrontation.
- `conditional / scoped`: the best practical IO branch remains the structured optical-history candidate.
- `open`: the exact Stage-2 atomic-radiative renormalization law and the exact `R`-loading slot.

So this deliverable is an honest confrontation layer: fixed IO values, fixed conditional branch choice where Paper 31 requires it, no illicit `tau_cov -> tau_reio` identification, and explicit residuals against Planck.

## Archive files

- [paper31_practical_io_cl_confrontation_results.json](/opt/cosmology-lab/results/paper31/paper31_practical_io_cl_confrontation_results.json)
- [paper31_practical_io_cl_confrontation_cls.csv](/opt/cosmology-lab/results/paper31/paper31_practical_io_cl_confrontation_cls.csv)
- [paper31_practical_io_cl_confrontation_residual_bins.csv](/opt/cosmology-lab/results/paper31/paper31_practical_io_cl_confrontation_residual_bins.csv)
- [paper31_practical_io_cl_confrontation_residuals.png](/opt/cosmology-lab/results/paper31/paper31_practical_io_cl_confrontation_residuals.png)
