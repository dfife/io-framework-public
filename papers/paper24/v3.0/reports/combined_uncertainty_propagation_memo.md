# Paper 24 v3.0 Combined Uncertainty Propagation Memo

Classification: `VERIFIED / Monte Carlo combined uncertainty propagation`

This memo records the public-bundle output needed to close Paper 24 v3.0
Open Problem item 6: combined propagation of the imported ground-state
`Q_GS` uncertainty and the Henderson excited-state `B(E2)` uncertainty through
the Paper 24 branch-sum lithium calculation.

Update relative to the first public draft of script 06: the earlier run used
`Q_GS(7Be) = 0.068 +/- 0.005 b` under a Navratil/NCSM attribution that did not
verify bidirectionally. The current run uses the directly reported Pastore et
al. (2013) GFMC value from Table II:
`Q(7Be, 3/2-) = -6.7(1) e fm^2 = -0.067(1) b`. Paper 24 samples the magnitude
`|Q_GS| = 0.067 b`; the sign is not used in the rate-squared deformation
arithmetic.

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

- `Q_GS(7Be) = 0.067 +/- 0.001 b`, sampled as a positive Gaussian from
  Pastore et al. (2013), Phys. Rev. C 87, 035503, Table II.
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
unnecessary for this local uncertainty propagation. The central Henderson row
was regenerated with the Pastore `Q_GS` value before this Monte Carlo run.

## Results

Central Henderson primary row after the Pastore correction:

```text
R_34,tot = 0.31003925909097196
Li-7/H = 1.7414708079857392e-10
Li-7 residual = +0.520873574147546 observational sigma
D/H = 2.5072097840055007e-05 (-0.659673866483311 sigma)
Y_p = 0.24770877182909237 (+0.6771929572730941 sigma)
```

Monte Carlo output:

```text
R_34,tot median = 0.3101525034206116
R_34,tot 1sigma band = [0.29916180906504, 0.32325040678126793]
R_34,tot 2sigma band = [0.28962711454283396, 0.33999418351986627]

Li-7/H median = 1.7420833548579086e-10
Li-7/H 1sigma band = [1.6825948263859496e-10, 1.8128758354571006e-10]
Li-7/H 2sigma band = [1.6309216298133606e-10, 1.9032198926995218e-10]
```

Observation comparison:

```text
Observed Li-7/H = 1.58e-10 +/- 0.31e-10
Central residual = +0.520873574147546 observational sigma
Median residual = +0.5228495317997051 observational sigma
Observed central value inside predicted 1sigma band: false
Observed central value inside predicted 2sigma band: false
```

The predicted nuclear-input band and the observational error bar answer
different questions. The scorecard residual uses the observational denominator
and remains within one observational sigma. The Monte Carlo band is a
prediction-side nuclear-input propagation with the observational central value
held fixed; its 2sigma lower quantile is `1.6309e-10`, slightly above the
observed central `1.58e-10`, by about `0.16` observational sigma.

## Manuscript Handoff Text

Suggested new subsection title:

```text
8.x Combined Uncertainty Propagation for the Lithium Prediction
```

Suggested subsection text:

```text
The central lithium scorecard uses the Henderson primary import row:
Li-7/H = 1.7414708079857392e-10, corresponding to +0.520874 sigma against
the Paper 24 observational denominator Li-7/H = (1.58 +/- 0.31)e-10. To audit
the imported nuclear-input uncertainty, we propagated the ground-state
quadrupole input from Pastore et al. (2013), who report
Q(7Be, 3/2-) = -6.7(1) e fm^2 in Table II, i.e. -0.067(1) b. The Paper 24
rate dressing uses the magnitude |Q_GS| = 0.067 b, because the overall sign of
the quadrupole moment does not enter the rate-squared deformation magnitude.
The excited-state input is the Henderson et al. (2019) transition strength
B(E2; 3/2- -> 1/2-) = 26(6)_stat(3)_syst e^2 fm^4.

The Monte Carlo used N = 100000 samples with fixed seed 240630. Q_GS was
sampled as a positive Gaussian with mean 0.067 b and sigma 0.001 b. Henderson's
statistical and systematic terms were sampled independently; detailed balance
was applied sample-by-sample to obtain B(E2; 1/2- -> 3/2-) =
2 B(E2; 3/2- -> 1/2-). Non-positive transition-strength samples were rejected,
and the nonlinear sqrt(B(E2)) and Gamow-exponential response were propagated
directly rather than symmetrized.

Each sample was propagated through Q_GS -> R_gs and
B(E2) -> q_trans,ex -> R_ex, then combined as
R_34,tot = f_gs R_gs + (1 - f_gs) R_ex. Running a full PRyMordial network for
every sample is computationally unnecessary for this local uncertainty band;
instead we used the banked Paper 24 PRyMordial sensitivity map
Li-7/H(sample) = Li-7/H(central) [R_34,tot(sample) / R_34,tot(central)]^0.963
for the 3He(alpha,gamma)7Be channel.

The resulting R_34,tot quantiles are median 0.3101525, 1sigma
[0.2991618, 0.3232504], and 2sigma [0.2896271, 0.3399942]. The corresponding
Li-7/H quantiles are median 1.7421e-10, 1sigma
[1.6826e-10, 1.8129e-10], and 2sigma [1.6309e-10, 1.9032e-10]. The scorecard
comparison uses the observational denominator, for which the central prediction
is +0.520874 sigma from the observed Spite-plateau value. The prediction-side
Monte Carlo band is narrower than the observational error bar; the observed
central value lies just below the prediction-side 2sigma lower quantile but
well within one observational sigma of the central prediction.

STATUS: VERIFIED (Monte Carlo propagation; reproducible in
papers/paper24/v3.0/scripts/06_combined_uncertainty_propagation.py).

Chain: Premise 1 (closed interior geometry fixes x and the branch projection)
+ Premise 2 (A=7 nuclear inputs imported from exterior nuclear physics without
IO retuning) + Pastore et al. 2013 Phys. Rev. C 87, 035503 Table II
Q(7Be, 3/2-) = -6.7(1) e fm^2 + Henderson et al. 2019 Phys. Rev. C 99,
064320 B(E2) input + Sbordone et al. 2010 Spite-plateau observational
denominator as adopted in the IO observational convention + Paper 24 v3.0
branch-sum formula R_34,tot = f_gs R_gs + (1 - f_gs) R_ex + banked Paper 24
PRyMordial sensitivity exponent 0.963 + standard Monte Carlo propagation with
fixed seed.
```

Suggested scorecard note:

```text
Li-7/H = 1.741e-10 (+0.52 sigma; combined Q_GS + Henderson 1sigma/2sigma
band in Sec. 8.x).
```

Suggested Open Problems update:

```text
Combined Q_GS + Henderson uncertainty propagation: CLOSED. See Sec. 8.x.
STATUS: VERIFIED.
```

Suggested version-history sentence:

```text
Switched the ground-state quadrupole import from the unverified Navratil/NCSM
attribution to Pastore et al. (2013) Table II, regenerated the Henderson
primary lithium row and combined Q_GS + Henderson B(E2) Monte Carlo, and added
Sec. 8.x with the prediction-side Li-7/H 1sigma band [1.6826, 1.8129]e-10 and
2sigma band [1.6309, 1.9032]e-10.
```
