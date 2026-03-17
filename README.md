# LivingMeta v2.0

**Browser-Based Living Meta-Analysis Engine with 85+ Statistical Methods**

A single-file HTML application (895 KB) for complete living systematic reviews -- from trial discovery through certified synthesis -- with in-browser R validation. No installation required.

## Quick Start

1. Download `LivingMeta.html`
2. Open in any modern browser (Chrome, Firefox, Edge, Safari)
3. Select a clinical configuration from the dropdown
4. Click **Run Analysis** in the Synthesize tab
5. Results appear instantly with 85+ statistical analyses

No server, no installation, no internet needed (after initial CDN load).

## Features

### Clinical Configurations
- **40 pre-configured topics** across cardiovascular, renal, metabolic, and rare disease
- 9 curated configs (45 landmark RCTs, ~200K patients) validated against R metafor
- 31 auto-generated configs via CT.gov API integration

### Statistical Engine (85+ Methods)
- **6 tau-squared estimators**: DL, REML, PM, HS, HE, EB
- **HKSJ adjustment** with IQWiG modification
- **Network Meta-Analysis**: Bucher indirect comparisons, P-scores, league tables
- **Three-Level MA**: Clustered studies (Konstantopoulos 2011)
- **Bayesian**: Grid approximation, RoBMA, three-prior sensitivity
- **Trial Sequential Analysis**: O'Brien-Fleming alpha-spending
- **25+ publication bias methods**: Egger, Begg, trim-fill, PET-PEESE, Copas, Doi/LFK, Harbord, Z-curve
- **Influence diagnostics**: Cook's D, DFBETAS, DFFITS, outlier detection, exclusion sensitivity matrix
- **Decision analysis**: Decision regret, P(benefit), opportunity cost, power calculator
- **Advanced**: Drapery plot, MCID analysis, confidence distribution, sceptical p-value, E-value

### Interactive Tools
- **What-If Scenario**: Add hypothetical trial, preview impact instantly
- **Patient Risk Calculator**: Baseline risk slider with ARD/NNT output
- **Effect Size Converter**: OR/RR/HR/NNT bidirectional conversion
- **CI Method Comparison**: Wald vs HKSJ vs t-dist side-by-side
- **Trial Editor**: Add/edit/remove trials with form UI
- **CSV Import**: Paste or drag-and-drop trial data

### Visualization (20+ Charts)
Forest plot (downloadable SVG/PNG), sensitivity forest, funnel with contours, Galbraith, Baujat, L'Abbe, drapery plot, waterfall chart, evidence timeline, NMA network graph, heterogeneity pie, trial Gantt, study weights bubble, Cook's D bar chart, NNT curve, sparklines

### Export (16 Formats)
JSON bundle, PDF report, CSV data, SVG/PNG forest, RevMan XML, PRISMA 2020 SVG, R script, screening CSV/JSON, GRADE SoF CSV, summary statistics CSV, methods report, print CSS

### Validation
- **WebR**: In-browser R + metafor comparison (30+ metrics)
- **R baseline badge**: Instant offline validation
- **TruthCert**: SHA-256 hash certification
- **160 automated tests** (Selenium)

### UX
- PRISMA 2020 workflow progress tracker
- Executive summary bar (visible on all tabs)
- Keyboard shortcuts (1-8 tabs, Ctrl+Enter synthesize)
- Dark mode with WCAG AA contrast
- Auto-save with version snapshots
- URL state sharing (shareable analysis links)
- Print-friendly CSS

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `1`-`8` | Switch tabs |
| `Ctrl+Enter` | Run synthesis |
| `Ctrl+E` | Export bundle |
| `?` | Show shortcut help |

## Testing

```bash
python test_livingmeta.py
# 160/160 tests pass
```

Requires: Python 3, Selenium, ChromeDriver.

## Quality Assurance

Three rounds of multi-persona code review (Statistical Methodologist, Security Auditor, UX/Accessibility, Software Engineer, Domain Expert). 17 P0 + 30+ P1 issues identified and resolved. REVIEW CLEAN.

## Citation

If you use LivingMeta in your research, please cite:

> [AUTHOR_PLACEHOLDER]. LivingMeta: A Browser-Based Living Meta-Analysis Engine with 85+ Statistical Methods. 2026. https://github.com/mahmood726-cyber/livingmeta

## License

[LICENSE_PLACEHOLDER]
