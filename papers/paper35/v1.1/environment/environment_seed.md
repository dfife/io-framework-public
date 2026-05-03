# Environment Seed and Randomness

The public Paper 35 v1.1 bundle is deterministic.

- Scripts 01-06 and 08-09 use no random numbers.
- Script 07 fetches public DESI DR2 mean/covariance files and computes fixed
  deterministic quantities.
- The flat-CPL values in script 07 are a fixed-point verification of the prior
  lab optimization output, not a stochastic refit. No random seed is required
  for public validation.

No random seed is needed to reproduce the frozen JSON outputs.
