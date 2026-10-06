# Hidden patterns — executed values (2026-10-06 anchor)

Source: `python experiments/run_all.py` → `benchmarks/benchmark_results.json` + Galton sim.

- Galton 20k: {0:22,1:173,2:948,3:2289,4:4027,5:4979,6:4114,7:2291,8:919,9:221,10:17}, chi2=18.35, top=5. Theory 20000*C(10,k)/1024 → {0:19.5,1:195.3,2:878.9,3:2343.8,4:4101.6,5:4921.9,...}. Fit good.
- BTC 31 closes 80046.71→85908.05, log-gain 0.07067, mean|diff| 892.98, up 13/30.
- logret mu=0.00235557, sigma=0.01950587, skew=1.5447, kurt=6.3786 → heavy right tail vs Normal.
- BTC-JPY corr=0.4531 (n=22, fragile, hypothesis only).
- sine7d R2=0.02594 → null weekly cycle.
- FTC roundtrip err <1e-9 (structural) vs CLT approximate (asymptotic).

Next PhD tests: longer panel, FX returns normality, options smile, lowest-shaky-floor RCT.
