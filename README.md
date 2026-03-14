# LivingMeta v1.0

**Self-Discovering Certified Living Meta-Analysis Engine**

A single-file, browser-based tool for living systematic reviews with integrated trial discovery, automated text extraction, comprehensive statistical synthesis, and in-browser R validation.

## Quick Start

1. Download `LivingMeta.html`
2. Open in any modern browser (Chrome, Firefox, Edge, Safari)
3. Select a clinical configuration from the dropdown
4. Click **Synthesize** to run the analysis

No installation, server, or internet connection required (after initial load).

## Features

- **9 clinical configurations**: Colchicine CVD, Finerenone, SGLT2i HF, GLP-1 CVOTs, PCSK9, Intensive BP, Bempedoic Acid, Incretins HFpEF, ATTR-CM (45 trials, ~200K patients)
- **6 tau-squared estimators**: DL, REML, PM, HS, HE, EB
- **HKSJ adjustment** with IQWiG modification
- **Fixed-effect methods**: IV, Mantel-Haenszel, Peto
- **20+ advanced analyses**: Bayesian posterior, TSA, Copas, fragility index, NNT curve, meta-regression, sceptical p-value, z-curve, and more
- **TextExtractor**: 50+ patterns auto-extract HR/OR/RR/MD/SMD from abstracts
- **WebR validation**: In-browser R + metafor, 30+ metric comparison
- **GRADE assessment**: Automated certainty of evidence
- **Patient mode**: Traffic-light summary for shared decision-making
- **Accessible**: WCAG AA, keyboard navigation, dark mode

## Testing

```bash
python test_livingmeta.py
```

Requires: Python 3.x, Selenium, Chrome/ChromeDriver.

## File Structure

```
LivingMeta.html          # The app (single file, ~550 KB)
test_livingmeta.py       # 36-assertion Selenium test suite
MANUSCRIPT_LIVINGMETA.md # Software tool paper
PRISMA_ScR_CHECKLIST.csv # PRISMA for Scoping Reviews
README.md                # This file
```

## Technical Details

- **Architecture**: Single HTML file with embedded CSS + JavaScript
- **Dependencies**: Plotly.js (CDN), optionally WebR (CDN, ~20 MB cached)
- **Statistical engine**: Pure JavaScript, no server required
- **TextExtractor**: Ported from rct_data_extractor_v2 (83.6% accuracy on 1,290 PDFs)
- **Tested**: 36/36 Selenium assertions, 531/531 div balance, 0 JS errors

## License

MIT

## Citation

If you use LivingMeta in your research, please cite:

> [AUTHOR]. LivingMeta: A Single-File, Browser-Based Living Meta-Analysis Engine with Integrated Trial Discovery and In-Browser R Validation. 2026. Available at: [GITHUB_URL]
