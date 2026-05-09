# Paper 20 v2.0 Reproducibility Bundle

Classification: `verified / public-reproducibility-support`

This bundle supports Paper 20 v2.0, "The Radiation Scope-Boundary Theorem,
the Acoustic Theorems, and the Big Bang Nucleosynthesis Radiation Algebra."
It replaces the unpublished `paper20-v1.8` bundle. The v1.8 bundle is not
preserved because Paper 20 was overhauled before publication.

The v2.0 manuscript is a scope-reduced release. It keeps only the live Paper
20 surfaces:

- Radiation Scope-Boundary Theorem 20.3.
- Acoustic History Reduction Theorem 20.1.
- Acoustic Phase-Calibration Theorem 20.2.
- Big Bang nucleosynthesis radiation algebra Theorems 20.RAD1, 20.RAD2, and
  20.RAD3.
- Corrected Big Bang nucleosynthesis comparison values inherited from the
  Paper 20 wrapper correction and Paper 22 v1.5/v1.6 amplitude framework.
- Paper 17 v1.5 R4/FIRAS readout-normalization inheritance.

Removed from this bundle, because v2.0 removes them from the active paper:
the bare package reconstruction, assembly-gap diagnostic, torsion-Lambda
branch, Delta N_eff target search, and reduced-to-full extension sketch.

## Quickstart

```bash
git clone https://github.com/dfife/io-framework-public.git
cd io-framework-public/papers/paper20/v2.0
python3 scripts/08_validate_expected_outputs.py
```

Expected final line:

```text
SUMMARY total_checks=22 pass_count=22 fail_count=0
```

The validator uses only Python standard-library modules and the frozen JSON
outputs included in this bundle.

## Headline Reproduced Values

```text
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255 K
Counts as independent CMB-temperature prediction: false

J_theta = x^(-1/2) * sqrt(1 + gamma_BI^2) = 0.8339461798286282
theta*_pred = 0.599 deg (rounded manuscript value)

Corrected BBN comparison row:
D/H   = 2.510410594954571e-5  (-0.5529801682 sigma)
Y_p   = 0.24781814417284279   (+0.7045360432 sigma)
Li7/H = 5.363335812718549e-10 (+12.2043090733 sigma)
chi2(D/H + Y_p) = 0.8021581025844415

N_eff = 3.044388520277016
delta N_eff kinetic correction = 0.044388520277015786
rho_fermion / rho_gamma = 4.375 pre-decoupling
bulk-vacuum equation of state = 5/3
rho_vac / rho_rad at BBN = O(1e-93) or smaller than required by many orders
```

## Claim Boundary

- `IMPORTED/EMPIRICAL`: FIRAS observer-side thermal datum and standard
  literature inputs such as Standard Model light-species bookkeeping.
- `DERIVED/THEOREM`: Acoustic History Reduction under the stated acoustic
  horizon premise package and the math-only identities explicitly labeled as
  theorem-grade in the manuscript.
- `DERIVED/CONDITIONAL_VERIFIED`: Acoustic Phase-Calibration after routing
  AC1 through Paper 21, and the admissible radiation-algebra constructions
  whose premise chains are explicit.
- `DERIVED/NO-GO`: reduced-stack radiation species-count no-go, measurement
  geometry no-go for abundance-ratio rescue, and bulk-vacuum radiation-source
  no-go.
- `OPEN/PREMISE_GAP`: full unreduced radiation-sector completion where the
  required carrier is supplied only by later papers.

## Review Note

The v2.0 draft contains one small acoustic reporting ambiguity: the manuscript
uses the rounded claim "0.429%" together with "9.2 sigma." The exact frozen
outputs distinguish the two rows. The legacy exact row gives 0.429% and
9.85 sigma; the current bipartite rounded row gives 0.401% and 9.21 sigma.
The bundle therefore records both and validates the manuscript-facing rounded
prediction `theta* = 0.599 deg` plus the exact `J_theta` factor.

## Citation

```text
David Fife, Paper 20 v2.0 Reproducibility Bundle,
Interior Observer Framework public reproducibility repository,
GitHub release paper20-v2.0, May 2026.
https://github.com/dfife/io-framework-public/releases/tag/paper20-v2.0
```

Machine-readable citation metadata is provided in `CITATION.cff`.
