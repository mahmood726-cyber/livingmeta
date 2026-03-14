# Multi-Persona Review: LivingMeta.html (40-topic expansion)
### Date: 2026-03-14
### Summary: 9 P0, 14 P1, 11 P2

---

## P0 — Critical (9)

### Data Quality (from Statistical + Domain review)
- **P0-New1** Domain: ALL 31 new configs have tE=0/cE=0 placeholder events — Track B (OR) synthesis produces meaningless OR~1.0 (lines 2600-4300)
  - Fix: Run Python pipeline to fill event counts from publications, or mark these as "HR-only" configs
- **P0-New2** Domain: COMPASS 'mace' HR is 1.70 = MAJOR BLEEDING, not efficacy (0.76). VOYAGER similar (1.43). CT.gov auto-scraping grabbed wrong outcome (line 3170)
  - Fix: Manually correct COMPASS HR to 0.76 and VOYAGER to published efficacy HR
- **P0-New3** Domain: 7 trials have NEGATIVE HR values (HbA1c change, LDL % change stored as 'hr') — NaN in synthesis (lines 2747, 3261, 3276, 3292, 3476, 3491, 3902)
  - Fix: Remove or reclassify these outcomes as MD type, not HR
- **P0-New4** Domain: Semaglutide/tirzepatide obesity configs map weight loss ORs (11.22, 23.99) to 'mace' — extreme pooled effect (lines 3333, 3342)
  - Fix: Use MD (mean weight change) as primary outcome, not binary responder OR
- **P0-New5** Domain: PARADIGM-HF has NO HR data — empty outcomes, published HR 0.80 missing (line 2832)
  - Fix: Manually add HR 0.80 (0.73-0.87)
- **P0-New6** Domain: CANTOS HR slightly off (0.86 vs published 0.85), year wrong (2019 vs 2017) (line 3131)
  - Fix: Correct HR to 0.85 (0.74-0.98), year to 2017

### Engineering/Security
- **P0-New7** Eng: STORAGE_KEY is const — config switches within session persist to WRONG key, data lost on reload (line 4313)
  - Fix: Make STORAGE_KEY dynamic or redirect URL on config switch
- **P0-New8** Eng: DEFAULT_STATE whitelist drops discovered, pubmedResults, settings, results on reload — hours of work lost (lines 4375-4383)
  - Fix: Add all runtime fields to DEFAULT_STATE
- **P0-New9** Sec: Patient mode innerHTML uses unescaped config PICO text (lines 13152-13158)
  - Fix: Wrap intervention/comparator/outcomeName in escapeHtml()

---

## P1 — Important (14)

- **P1-New1** Domain: All 31 new configs lack event counts — Track B, MH-OR, Peto, Fragility, NNT all broken
- **P1-New2** Domain: VERTIS CV 'mace' HR -0.75 = HbA1c mean diff, not MACE HR (published 0.97)
- **P1-New3** Domain: ORION-4 year: 2049 (CT.gov estimated completion, not publication year)
- **P1-New4** Domain: RE-LY year: 0 (missing date parse)
- **P1-New5** Domain: ~12 trial IDs are truncated CT.gov titles ("BI 10773", "Cardiovascular Outco", etc.)
- **P1-New6** Domain: "Preterm Functional E" (NCT04531566) is wrong trial — neonatal echo, not T1DM insulin
- **P1-New7** Domain: VALOR-HCM 'mace' HR 58.93 = response PERCENTAGE, not HR
- **P1-New8** Domain: DAPA-MI 'mace' HR 1.34 = WIN RATIO, not HR
- **P1-New9** Domain: 12 single-trial configs cannot compute heterogeneity (k=1)
- **P1-New10** Domain: COAPT missing CI upper bound (hrHi: null)
- **P1-New11** Eng: handleConfigChange doesn't purge Plotly — memory leak on rapid switching
- **P1-New12** Eng: Stale results visible on Synthesis/Bias/GRADE tabs after config switch
- **P1-New13** Eng: chi2CDF shadowed by local function in computeFragilityIndex
- **P1-New14** UX: 40 options in flat dropdown — needs optgroup by therapeutic area

---

## P2 — Minor (11)

- P2-New1: All new configs lack ghostProtocols/publishedBenchmarks
- P2-New2: EMPA-REG nTotal 7064 vs published 7020
- P2-New3: DECLARE 'mace' HR 0.83 = CV death/HFH co-primary, not 3-pt MACE (0.93)
- P2-New4: 'mace' key used for non-MACE outcomes (HbA1c, weight, SBP, 6MWD, TIR) in 7 configs
- P2-New5: Mixed estimand types (HR + MD) in same trial outcomes object
- P2-New6: All new configs have blanket "low" RoB (placeholder, not assessed)
- P2-New7: CANVAS N=4330 (alone) vs CANVAS Program 10142
- P2-New8: Two VTE trials share same id "Efficacy and Safety"
- P2-New9: NCT ID regex inconsistency (7-digit vs 8-digit)
- P2-New10: Tailwind CDN is development version, not production
- P2-New11: FNV-1a fallback hash is non-cryptographic (documented)

---

## False Positive Watch
- DOR = exp(mu1 + mu2) — NOT flagged
- tE=0 with continuity correction producing OR~1 is a REAL issue, not false positive
- Negative HR values causing NaN is a REAL issue, not false positive

---

## STATUS: REVIEW COMPLETE, FIXES PENDING
## The 9 original configs (colchicine through ATTR-CM) remain clean from prior review.
## The 31 auto-generated configs need significant manual curation before publication-readiness.
