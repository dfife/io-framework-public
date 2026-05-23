# Paper 35 visible transfer operator class theorem

## Discipline label

- label state: `CONDITIONAL_VERIFIED`
- registry check: Vectors 1-4 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: verified recursively through the cited Paper 35 portal/support chain to assumed-good Papers 1-31 nodes and the inline-verified Paper 32 bridge-support and active-branch nodes where touched; all remaining non-Premise inputs are the explicit admissions listed here.
- admitted inputs surfaced here: `ADMITTED_CARRIER(current Paper 32 neutral singlet fermionic source carrier)`; `ADMITTED_PORTAL_CLASS(type-I singlet-fermion portal on the hierarchical N1 slice)`; `ADMITTED_SLICE(support-crossing slice M1 = T_f,target and R = R_eta)`.
- usage rule: this theorem may be cited as a premise because it is `CONDITIONAL_VERIFIED`.
## Headline

- status: `derived / sharpened Paper 35 boundary`
- The remaining baryogenesis debt is no longer the operator class of V_tr. The minimal visible transfer class is fixed to the Weinberg operator on the visible side and to the type-I neutrino portal on the renormalizable UV side, subject to the current IO source-carrier placement. What remains open is the coefficient/rate theorem: the Yukawa-Majorana data and their nonthermal support-branch evolution. The obvious local thermal implementation is killed.

## Theorem 1: Visible Delta(B-L)=2 Operator Uniqueness

- status: `derived / exact external+internal EFT theorem`
- exact visible operator class: `O5 = c5_ij (L_i H)(L_j H) / Lambda + h.c.`
- Within the visible Standard-Model field algebra, the unique lowest-dimension gauge-invariant operator carrying Delta(B-L)=2 is the Weinberg class O5 = (L H)(L H)/Lambda. No lower-dimension visible operator satisfies Lorentz invariance, gauge invariance, and Delta(B-L)=2 simultaneously.
- proof spine:
  - A Delta(B-L)=2 visible operator must contain two lepton doublets L, contributing total hypercharge -1 and total mass dimension 3.
  - One Higgs doublet H raises hypercharge by +1/2 only, so LLH cannot be hypercharge-neutral.
  - Two Higgs doublets raise hypercharge by +1 and permit SU(2) singlet contraction epsilon_ab L^a H^b.
  - The resulting operator (L H)(L H) has total dimension 5 and is gauge invariant.
  - Therefore dimension < 5 is impossible and the dimension-5 Weinberg class is unique.

## Theorem 2: Neutrino-Portal UV Uniqueness

- status: `derived / exact operator-class reduction under current IO carrier placement`
- portal class: `V_tr^(I) = y_{i a} epsilon_ab L_i^a H^b N_a + h.c.`
- source mass sector: `H_M = (1/2) M_ab N_a N_b + h.c.`
- effective visible operator: `c5 = y^T M^{-1} y`
- Under the current IO carrier constraints, the unique renormalizable UV completion class capable of generating the visible Weinberg operator is the type-I neutrino portal: a gauge-singlet fermion N with portal coupling y L H N and a Majorana mass term (1/2) M N N. Type-II and type-III completions are excluded because they require, respectively, a scalar SU(2)_L triplet or a fermion SU(2)_L triplet, neither of which is compatible with the admitted neutral singlet fermionic source carrier.
- proof spine:
  - A renormalizable interaction linear in a singlet fermion N must pair N with a visible operator of canonical dimension 5/2.
  - Among Standard-Model monomials with one fermion and one scalar, only L H is both gauge neutral and Lorentz-compatible with N.
  - Therefore y L H N is the unique renormalizable portal for a singlet fermionic source.
  - A Majorana mass term M N N is the unique gauge-invariant dimension-3 singlet mass term that breaks visible B-L by two units after integrating out N.
  - Integrating out N yields the Weinberg operator, while alternative tree-level completions require gauge-charged mediators not admitted by the current IO source carrier.

## Theorem 3: Local Thermalization No-Go

- status: `derived / exact conditional_verified no-go on the support-crossing slice`
- conditional slice:
  - identify the lightest singlet mass with the previously fixed target M1 = T_f,target
  - identify the active source crossing with the previously fixed support radius R_eta
  - use the standard tree-level decay width Gamma_D = (Y^dagger Y) M1 / (8 pi hbar)
  - impose local rate equality Gamma_D = H_support(R_eta)
- support rate law: `H_support(R) = c sqrt(r_s/R - 1) / R`
- exact numerics:
  - `M1 = 2.200393859747780e+13 GeV`
  - `R_eta = 2.903618612979499e+12 m`
  - `H_support(R_eta) = 1.566614172843635e+03 s^-1`
  - `Y^dagger Y = 1.177788348930236e-33`
  - `|y| = 3.431892115044172e-17`
  - `m_tilde = 1.620560787071966e-33 eV`
  - `m_* = 1.069040871302631e-03 eV`
  - `K = 1.515901618520258e-30`
- On the natural local-support implementation of the unique type-I portal class, the exact Yukawa norm required by Gamma_D = H_support(R_eta) is so small that the washout parameter is K << 1 and the standard thermal-equilibrium source assumption fails catastrophically. Therefore the support-crossing implementation cannot be ordinary thermal type-I leptogenesis with equilibrium initial abundance.

## Remaining Open Debt

- `a theorem selecting the Yukawa/Majorana coefficient data inside the type-I portal class`
- `a support-branch production/transfer theorem for the singlet source abundance`
- `a CP-asymmetry theorem fixing epsilon1 from IO boundary data`
- `a visible B-L transfer theorem beyond the killed local thermal-equilibrium slice`

## Sources

- https://arxiv.org/abs/2104.08248
- https://cds.cern.ch/record/2772611/files/2106.05913.pdf
- https://arxiv.org/abs/hep-ph/0502169
- https://arxiv.org/abs/hep-ph/0202239

