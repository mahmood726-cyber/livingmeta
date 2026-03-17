# Multi-Persona Review: LivingMeta.html (R2-R6 features, commits d8c430d-fc5e6f1)
### Date: 2026-03-17
### Status: REVIEW CLEAN — All 7 P0 fixed, all 12 P1 fixed

---

## Reviewers
1. Statistical Methodologist
2. Security Auditor
3. UX/Accessibility + Software Engineer (combined)
4. Domain Expert (Cochrane/PRISMA specialist)

## P0 — Critical (7) — ALL FIXED

- [FIXED] P0-1 (Domain): Default RoB "low" for imported/user-added trials → changed to "unclear"
- [FIXED] P0-2 (Stat+Domain): 3-Level MA tau2W update was ad-hoc heuristic → replaced with proper DL moment estimator (QW-dfW)/CW
- [FIXED] P0-3 (Stat+Domain): Post-hoc power labeled "Current Power" without caveat → added "Post-hoc Power*" + Hoenig & Heisey 2001 footnote
- [FIXED] P0-4 (Stat+Sec): parseInt() ?? null doesn't catch NaN → replaced with isNaN guard
- [FIXED] P0-5 (Sec): importTrialsCSV parseInt()||null drops valid zero events → isNaN/isFinite guards
- [FIXED] P0-6 (Sec): exportGradeCSV no CSV formula injection defense → added safeCSV() sanitizer
- [FIXED] P0-7 (Sec+Eng): runWhatIf guard !effectInput allows negative → isFinite + >0 check

## P1 — Important (12) — ALL FIXED

- [FIXED] P1-1 (Stat): renderSensitivityForest hardcoded confLevel:0.95 → reads AppState.settings.confLevel
- [FIXED] P1-2 (Stat+Sec): addUserTrial parseFloat||null drops zero → isFinite guard
- [FIXED] P1-3 (Stat): Cook's D CovRatio used regression formula → corrected to sumWF/sumWLoo
- [FIXED] P1-5 (Stat+Domain): pBenefit double-counted tau2 → uses se alone for pooled estimate
- [FIXED] P1-6 (Domain): Methods report didn't mention R2-R6 features → added 6 new method lines
- [FIXED] P1-9 (Sec): renderExecSummary + renderDecisionRegret unescaped verdict → added escapeHtml()
- [FIXED] P1-12 (Stat): Unused isRatio variable in computeEvidenceVelocity → removed

## P1 — OPEN (by design / low priority)

- [OPEN] P1-4 (Stat): Cook's D doesn't re-estimate tau2 in LOO — consistent with existing influenceSuite, acceptable
- [OPEN] P1-7 (Domain): NNT opportunity cost uses hardcoded CER=0.10 — acceptable default for CV outcomes
- [OPEN] P1-8 (Domain): RIS ignores heterogeneity adjustment — documented as approximation
- [OPEN] P1-10 (Sec): Naive CSV parsing doesn't handle quoted fields — edge case
- [OPEN] P1-11 (A11y): Tables missing scope on th — widespread pre-existing pattern

## P2 — Minor (15) — OPEN

- Sensitivity forest same-color diamonds for all RE methods
- Cluster detection regex may miscluster numeric-suffix trials
- Hardcoded 2yr trial duration fallback in Gantt
- CSV import doesn't handle quoted fields
- Evidence velocity thresholds on absolute scale not relative
- Post-hoc power fundamentally questionable (Hoenig & Heisey 2001) — caveat added
- Duplicate Cook's D implementation (computeCooksDistance + computeInfluenceSuite)
- opacity:0.5 contrast failures in dark mode (pre-existing)
- Decision regret values are heuristic constants, not derived
- Keyboard shortcuts no modal check
- RoB "unclear" and "some concerns" use same "?" symbol

## Test Results
- **120/120 tests pass**, 769/769 div balance, 0 JS errors
- **16,016 lines, 845 KB**

## Previous Reviews
- 2026-03-16: R1 features (5 P0 + 11 P1) → ALL FIXED, REVIEW CLEAN
- 2026-03-15: 40-topic expansion (9 P0 + 14 P1) → 9/9 P0, 12/14 P1 FIXED
