# External Dependencies

The public Paper 21 v2.0 bundle uses Python standard-library modules only.

PRyMordial is not redistributed in this repository. Paper 21's corrected BBN
abundance values are frozen from the private-lab PRyMordial correction audit;
the public scripts validate:

- the YPCMB wrapper convention (`PRyMresults()[3]`),
- the IO Framework Conventions v2.0 observational denominators,
- the scorecard pulls and chi-square,
- the puncture-load and AC1 arithmetic.

The convention reference is:

```text
https://dfife.github.io/data/conventions_v2.md
```

No external observational dataset is redistributed in this bundle.

The R4 optical readout normalization is inherited from Paper 17 v1.5:

```text
R4_FIRAS = 1.0031014644
T_obs(R4) = T_IO x^(R4_FIRAS K_gauge)
```

The FIRAS temperature is used only as the empirical optical readout datum
already documented by Paper 17 v1.5. Paper 21's active Big Bang
nucleosynthesis branch assignment uses `T_IO`, not `T_obs`.
