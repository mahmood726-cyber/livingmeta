# Multi-Persona Review: LivingMeta.html (5 new features — commit e29f193)
### Date: 2026-03-16
### Status: REVIEW CLEAN — All 5 P0 fixed, all 11 P1 fixed

---

## Reviewers
1. Statistical Methodologist
2. Security Auditor
3. UX/Accessibility Reviewer
4. Software Engineer
5. Domain Expert (Cochrane/PRISMA specialist)

## P0 — Critical (5) — ALL FIXED

- [FIXED] P0-1 (Stat+Sec+Eng+Domain): Hardcoded z=1.96 in NMA Bucher CIs — now uses `normalQuantile(1 - alpha/2)` with confLevel
- [FIXED] P0-2 (Stat+Eng+Domain): NMA consistency test formula wrong (tested null not inconsistency) — now correctly reports "not estimable" for star networks, reserves Q-test for closed-loop networks
- [FIXED] P0-3 (Stat+Eng): Evidence timeline `trialNames[i]` misaligned with year-sorted cumulative — sorted trials by year before mapping names
- [FIXED] P0-4 (Domain): Methods report overclaimed TSA boundaries (Pocock/Lan-DeMets not implemented) — corrected to "O'Brien-Fleming alpha-spending boundaries"
- [FIXED] P0-5 (A11y): NMA league table used color alone for significance — added asterisk `*` text indicator + footnote

## P1 — Important (11) — ALL FIXED

- [FIXED] P1-1 (Sec): Unescaped `nctId` in renderDataQuality innerHTML — added `escapeHtml()`
- [FIXED] P1-2 (Sec): CSS injection via `r.color` in NMA render — added `safeColor()` validator (hex-only)
- [FIXED] P1-3 (Stat): No seDiff=0 guard in Bucher comparisons — added `if (seDiff < 1e-15) continue`
- [FIXED] P1-4 (Stat): compositeMap defined but never used (dead code) — removed
- [FIXED] P1-5 (Stat+Domain): 4pt MACE detection preempted 5pt — reordered: 5pt > 4pt > 3pt
- [FIXED] P1-6 (Stat+Eng): Methods report `Qp=NaN` rendered literal "NaN" — now shows "N/A"
- [FIXED] P1-7 (Stat): Methods report hardcoded "95% CI" despite dynamic confLevel — now uses `(confLevel*100) + '% CI'`
- [FIXED] P1-8 (A11y): NMA 2-column grid no responsive breakpoint — changed to `repeat(auto-fit,minmax(320px,1fr))`
- [FIXED] P1-9 (A11y): Methods report `<pre>` block not keyboard-scrollable — added `tabindex="0" role="region" aria-label`
- [FIXED] P1-10 (A11y): `#22c55e` green on white had ~3.0:1 contrast — replaced with `#16a34a` (~4.6:1) in all new features
- [FIXED] P1-11 (Stat+Domain): Timeline y-axis hardcoded "Pooled OR" — now dynamic based on `trackResult.measure`

## P2 — Minor (9) — OPEN (by design / low priority)

- [OPEN] P2-1: Evidence timeline Plotly chart has no text alternative for screen readers
- [OPEN] P2-2: NMA network graph similarly lacks text alternative (ranking table partially mitigates)
- [OPEN] P2-3: Data quality `opacity:0.6` on labels borderline contrast
- [OPEN] P2-4: Harmonization italic + opacity on "assumed" text
- [OPEN] P2-5: NCT ID regex doesn't trim whitespace
- [OPEN] P2-6: `escapeHtml` in plain-text report may double-escape on render
- [OPEN] P2-7: P-score direction not parameterized (correct for HR/lower-is-better)
- [OPEN] P2-8: Data quality A-F grading is custom (not GRADE-aligned)
- [OPEN] P2-9: Blob URL revoke timing could use setTimeout for safety

## Test Results
- **65/65 tests pass** (51 original + 14 new feature tests)
- **636/636 div balance**
- **0 JS errors in browser console**
- **14,680 lines, 764 KB**

## Previous Review (2026-03-15, 40-topic expansion)
All P0 fixed, 12/14 P1 fixed. See git history for details.
