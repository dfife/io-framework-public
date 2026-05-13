# Paper 24 v3.0 Combined Uncertainty Propagation Memo

Classification: `VERIFIED / Monte Carlo combined uncertainty propagation`

This memo records the public-bundle output needed to close Paper 24 v3.0
Open Problem item 6: combined propagation of the imported ground-state
`Q_GS` uncertainty and the Henderson excited-state `B(E2)` uncertainty through
the Paper 24 branch-sum lithium calculation.

Source-citation caveat: the public script propagates the banked Paper 24 v3.0
input `Q_GS(7Be) = 0.068 +/- 0.005 b`. A source-level manuscript check should
verify the exact external citation for that banked value before presenting
item 6 as closed all the way to the Navratil/NCSM literature. The propagation
arithmetic is complete; the source citation should not be treated as silently
verified by this script.

## Method

Script:

```text
papers/paper24/v3.0/scripts/06_combined_uncertainty_propagation.py
```

Frozen output:

```text
papers/paper24/v3.0/results/combined_uncertainty_propagation_results.json
```

The script runs `N = 100000` Monte Carlo samples with fixed seed `240630`.
The input distributions are:

- `Q_GS(7Be) = 0.068 +/- 0.005 b`, sampled as a positive Gaussian from the
  banked Paper 24 v3.0 input.
- Henderson `B(E2; 3/2- -> 1/2-) = 26(6)_stat(3)_syst e^2 fm^4`, sampled
  with independent statistical and systematic Gaussian terms and rejected if
  non-positive.
- Detailed balance gives `B(E2 down) = 2 B(E2 up)` for
  `1/2- -> 3/2-`.

Each sample is propagated through:

```text
Q_GS -> R_gs
B(E2 up) -> B(E2 down) -> q_trans,ex -> R_ex
R_34,tot = f_gs R_gs + (1 - f_gs) R_ex
Li7/H(sample) = Li7/H(central) * (R_34,tot(sample) / R_34,tot(central))^0.963
```

The final mapping uses the banked Paper 24 PRyMordial sensitivity exponent for
the `3He(alpha,gamma)7Be` channel. The bundle does not run 100000 full
PRyMordial networks; that would be impractical for reviewer validation and is
unnecessary for this local uncertainty propagation.

## Results

Central Henderson primary row:

```text
R_34,tot = 0.306711121403594
Li-7/H = 1.7239845810965594e-10
Li-7 residual = +0.46446639063406275 sigma
```

Monte Carlo output:

```text
R_34,tot median = 0.3078455831618201
R_34,tot 1sigma band = [0.2887060172587597, 0.3291362181137696]
R_34,tot 2sigma band = [0.271209264065951, 0.3535019845014519]

Li-7/H median = 1.7301248914205407e-10
Li-7/H 1sigma band = [1.6264166644761962e-10, 1.8452092390522347e-10]
Li-7/H 2sigma band = [1.531387503371378e-10, 1.9765791200856804e-10]
```

Observation comparison:

```text
Observed Li-7/H = 1.58e-10 +/- 0.31e-10
Central residual = +0.46446639063406275 sigma
Median residual = +0.48427384329206674 sigma
Observed central value inside predicted 1sigma band: false
Observed central value inside predicted 2sigma band: true
```

The central Paper 24 v3.0 scorecard remains unchanged. The combined imported
nuclear-input band is asymmetric after nonlinear propagation and should be
reported by quantiles, not by a symmetrized `+/-` error.

## Manuscript Handoff Text

Suggested new subsection title:

```text
8.x Combined Uncertainty Propagation for the Lithium Prediction
```

Suggested subsection text:

```text
The central lithium scorecard uses the Henderson primary import row:
Li-7/H = 1.7239845810965594e-10, corresponding to +0.464466 sigma against
the Paper 24 observational denominator Li-7/H = (1.58 +/- 0.31)e-10. To audit
the imported nuclear-input uncertainty, we propagated the ground-state
quadrupole input Q_GS(7Be) = 0.068 +/- 0.005 b and the Henderson et al. (2019)
excited-state transition strength B(E2; 3/2- -> 1/2-) = 26(6)_stat(3)_syst
e^2 fm^4 through the full Paper 24 branch-sum chain. Henderson's statistical
and systematic terms were sampled independently; detailed balance was applied
sample-by-sample to obtain B(E2; 1/2- -> 3/2-) = 2 B(E2; 3/2- -> 1/2-).
Non-positive transition-strength samples were rejected, and the nonlinear
sqrt(B(E2)) and Gamow-exponential response were propagated directly rather
than symmetrized.

The Monte Carlo used N = 100000 samples with fixed seed 240630. Each sample
was propagated through Q_GS -> R_gs and B(E2) -> q_trans,ex -> R_ex, then
combined as R_34,tot = f_gs R_gs + (1 - f_gs) R_ex. Running a full PRyMordial
network for every sample is computationally unnecessary for this local
uncertainty band; instead we used the banked Paper 24 PRyMordial sensitivity
map Li-7/H(sample) = Li-7/H(central) [R_34,tot(sample) /
R_34,tot(central)]^0.963 for the 3He(alpha,gamma)7Be channel.

The resulting R_34,tot quantiles are median 0.3078456, 1sigma
[0.2887060, 0.3291362], and 2sigma [0.2712093, 0.3535020]. The corresponding
Li-7/H quantiles are median 1.7301e-10, 1sigma
[1.6264e-10, 1.8452e-10], and 2sigma [1.5314e-10, 1.9766e-10]. The observed
Spite-plateau central value lies inside the predicted 2sigma nuclear-input
band, while the central scorecard remains within one observational sigma.

STATUS: VERIFIED (Monte Carlo propagation; reproducible in
papers/paper24/v3.0/scripts/06_combined_uncertainty_propagation.py).

Chain: Premise 1 (closed interior geometry fixes x and the branch projection)
+ Premise 2 (A=7 nuclear inputs imported from exterior nuclear physics without
IO retuning) + banked Paper 24 v3.0 Q_GS input, pending exact source-citation
verification + Henderson et al. 2019 Phys. Rev. C 99, 064320 B(E2) input +
Paper 24 v3.0 branch-sum formula R_34,tot = f_gs R_gs + (1 - f_gs) R_ex +
banked Paper 24 PRyMordial sensitivity exponent 0.963 + standard Monte Carlo
propagation with fixed seed.
```

Suggested scorecard note:

```text
Li-7/H = 1.724e-10 (+0.46 sigma; combined Q_GS + Henderson 1sigma/2sigma
band in Sec. 8.x).
```

Suggested Open Problems update:

```text
Combined Q_GS + Henderson uncertainty propagation: CLOSED. See Sec. 8.x.
STATUS: VERIFIED.
```

Suggested version-history sentence:

```text
Closed the combined Q_GS + Henderson B(E2) uncertainty-propagation item by
adding Sec. 8.x and public-bundle script 06, yielding Li-7/H 1sigma
[1.6264, 1.8452]e-10 and 2sigma [1.5314, 1.9766]e-10.
```
