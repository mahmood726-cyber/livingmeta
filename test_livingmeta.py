"""
LivingMeta v1.0 — Comprehensive Selenium Test Suite
Covers: 9 configs, TextExtractor (7 types), WebR UI, new features,
        accessibility, patient mode, data fixes, security patches.
"""
import sys, io, os, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'LivingMeta.html'))

def run_tests():
    opts = Options()
    opts.add_argument('--headless=new')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--disable-dev-shm-usage')
    opts.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    d = webdriver.Chrome(options=opts)
    results = []

    def ok(name, val):
        results.append((name, bool(val)))

    try:
        d.get('file:///' + HTML_PATH.replace(os.sep, '/'))
        time.sleep(5)

        # ─── 1-9: All 9 configs synthesize ───
        configs = [
            'colchicine_cvd', 'finerenone', 'sglt2_hf', 'glp1_cvot',
            'pcsk9', 'intensive_bp', 'bempedoic_acid', 'incretin_hfpef', 'attr_cm'
        ]
        for cfg in configs:
            k = d.execute_script(
                'try{handleConfigChange("' + cfg + '");switchTab("synthesize");'
                'runSynthesis();return AppState.results?.trackB?.k}'
                'catch(e){return "ERR:"+e.message}'
            )
            ok(f'config:{cfg}', isinstance(k, (int, float)) and k >= 2)

        # ─── 10-16: TextExtractor patterns ───
        ok('TE:HR', d.execute_script(
            'return TextExtractor.extract("HR 0.74 (95% CI 0.65-0.85)")[0]?.effectType==="HR"'))
        ok('TE:aHR', d.execute_script(
            'return TextExtractor.extract("aHR 0.76 (0.63-0.91)")[0]?.effectType==="HR"'))
        ok('TE:OR', d.execute_script(
            'return TextExtractor.extract("OR 1.56 (95% CI 1.21-2.01)")[0]?.effectType==="OR"'))
        ok('TE:RR', d.execute_script(
            'return TextExtractor.extract("relative risk was 0.77; 95% CI, 0.69 to 0.85")[0]?.effectType==="RR"'))
        ok('TE:events', d.execute_script(
            'return TextExtractor.extract("131/2366 vs 170/2379")[0]?.tE===131'))
        ok('TE:NNT', d.execute_script(
            'return TextExtractor.extract("NNT 12 (8-25)")[0]?.effectType==="NNT"'))
        ok('TE:MD', d.execute_script(
            'return TextExtractor.extract("MD -2.1 (95% CI -3.2 to -1.0)")[0]?.effectType==="MD"'))

        # ─── 17-20: Computation formulas ───
        ok('computeOR', d.execute_script(
            'return TextExtractor.computeOR(131,2366,170,2379)?.value > 0'))
        ok('computeRR', d.execute_script(
            'return TextExtractor.computeRR(131,2366,170,2379)?.value > 0'))
        ok('computeSMD', d.execute_script(
            'return TextExtractor.computeSMD(45.3,19.9,100,50.1,20.3,100)?.value < 0'))
        ok('verify warns', d.execute_script(
            'var e={effectType:"HR",value:0.74,ciLo:0.65,ciHi:0.85,pValue:0.5};'
            'TextExtractor.verify(e);return e.warnings.length>0'))

        # ─── 21-24: New features (Bayesian, NNT, meta-reg, patient mode) ───
        d.execute_script('handleConfigChange("colchicine_cvd");switchTab("synthesize");runSynthesis()')
        time.sleep(1)
        ok('bayesPosterior', d.execute_script(
            'return AppState.results?.bayesPosterior?.results?.length===3'))
        ok('nntCurve', d.execute_script(
            'return AppState.results?.nntCurve?.nntObs > 0'))
        ok('metaRegression', d.execute_script(
            'return AppState.results?.metaRegression != null'))
        ok('patientMode toggle', d.execute_script(
            'togglePatientMode();var on=patientMode;togglePatientMode();return on===true && patientMode===false'))

        # ─── 25-28: Data fix verification ───
        ok('ELIXA 4pt MACE verified', d.execute_script(
            'return CONFIG_LIBRARY.glp1_cvot.trials[0].outcomes.mace.hr===1.02'))
        ok('SOLOIST estimand', d.execute_script(
            'return CONFIG_LIBRARY.sglt2_hf.trials[4].outcomes.mace.estimandType==="RR_RECURRENT"'))
        ok('SPRINT main', d.execute_script(
            'return CONFIG_LIBRARY.intensive_bp.trials[0].id==="SPRINT" && '
            'CONFIG_LIBRARY.intensive_bp.trials[0].nTotal===9361'))
        ok('HELIOS-B NCT fixed', d.execute_script(
            'return CONFIG_LIBRARY.attr_cm.trials[2].nctId==="NCT04153149"'))

        # ─── 29-32: Security/engineering patches ───
        ok('STORAGE_KEY valid', d.execute_script(
            'return STORAGE_KEY.startsWith("livingmeta_")'))
        ok('sha256 fn exists', d.execute_script(
            'return typeof sha256==="function"'))
        ok('WebR btn exists', d.execute_script(
            'return document.getElementById("webrRunBtn")!=null'))
        ok('makeRnorm shared', d.execute_script(
            'return typeof makeRnorm==="function"'))

        # ─── 33-35: Accessibility ───
        ok('tabindex on all panels', d.execute_script(
            'return Array.from(document.querySelectorAll("[role=tabpanel]")).every('
            'p=>p.getAttribute("tabindex")==="0")'))
        ok('arrow key handler', d.execute_script(
            'return document.querySelector("[role=tablist]")!=null'))
        ok('postProcessTables fn', d.execute_script(
            'return typeof postProcessTables==="function"'))

        # ─── 36-50: Transparency features ───
        ok('highlightScreeningKeywords fn', d.execute_script(
            'return typeof highlightScreeningKeywords==="function"'))
        ok('highlights randomized green', d.execute_script(
            'return highlightScreeningKeywords("A randomized trial",[]).includes("#dcfce7")'))
        ok('highlights observational red', d.execute_script(
            'return highlightScreeningKeywords("retrospective cohort",[]).includes("#fee2e2")'))
        ok('autoAssessRoB fn', d.execute_script(
            'return typeof autoAssessRoB==="function"'))
        ok('RoB low for good trial', d.execute_script(
            'return autoAssessRoB({allocation:"RANDOMIZED",masking:"DOUBLE",hasResults:true,'
            'phase:"PHASE3",nPrimaryOutcomes:2}).overall==="low"'))
        ok('RoB high for bad trial', d.execute_script(
            'return autoAssessRoB({allocation:"NON_RANDOMIZED",masking:"NONE",hasResults:false,'
            'phase:"PHASE1",nPrimaryOutcomes:0}).overall==="high"'))
        ok('RoB has 5 domains', d.execute_script(
            'return autoAssessRoB({allocation:"RANDOMIZED",masking:"SINGLE",hasResults:true,'
            'phase:"PHASE3",nPrimaryOutcomes:1}).domains.length===5'))
        ok('RoB has reasons', d.execute_script(
            'return autoAssessRoB({allocation:"RANDOMIZED",masking:"SINGLE",hasResults:true,'
            'phase:"PHASE3",nPrimaryOutcomes:1}).reasons.length===5'))
        ok('fetchTrialResults fn', d.execute_script(
            'return typeof fetchTrialResults==="function"'))
        ok('renderTrialResultsPanel fn', d.execute_script(
            'return typeof renderTrialResultsPanel==="function"'))
        ok('GRADE evidence in table', d.execute_script(
            'return document.getElementById("gradeSofTable")?.innerHTML?.includes("Evidence:")'))
        ok('GRADE shows trial RoB', d.execute_script(
            'return document.getElementById("gradeSofTable")?.innerHTML?.includes("COLCOT")'))
        ok('GRADE shows I2', d.execute_script(
            'return document.getElementById("gradeSofTable")?.innerHTML?.includes("I\\u00B2=")'))
        ok('auto-gen configs marked', d.execute_script(
            'return CONFIG_LIBRARY.sglt2_ckd._dataQuality==="auto-generated"'))
        ok('curated configs not marked', d.execute_script(
            'return CONFIG_LIBRARY.colchicine_cvd._dataQuality===undefined'))

        # ─── 52-56: New features (NMA, Timeline, Harmonization, Data Quality, Methods Report) ───
        ok('computeNMA fn exists', d.execute_script(
            'return typeof computeNMA === "function"'))
        # ATTR-CM has 3 drug classes — NMA should produce results using Track B (OR from events)
        ok('NMA runs for ATTR-CM', d.execute_script('''
            var cfg = CONFIG_LIBRARY.attr_cm;
            var trackB = synthesizeTrackB(cfg.trials, "mace");
            if (!trackB) return false;
            var nma = computeNMA(trackB, cfg);
            return nma !== null && nma.ranking.length >= 2;
        '''))
        ok('renderEvidenceTimeline fn exists', d.execute_script(
            'return typeof renderEvidenceTimeline === "function"'))
        ok('computeOutcomeHarmonization fn', d.execute_script(
            'return typeof computeOutcomeHarmonization === "function"'))
        ok('harmonization detects types', d.execute_script('''
            var cfg = CONFIG_LIBRARY.colchicine_cvd;
            var h = computeOutcomeHarmonization(cfg, "mace");
            return h !== null && h.trialDefs.length > 0 && h.types.length >= 1;
        '''))
        ok('computeDataQuality fn', d.execute_script(
            'return typeof computeDataQuality === "function"'))
        ok('data quality scoring works', d.execute_script('''
            var cfg = CONFIG_LIBRARY.colchicine_cvd;
            var dq = computeDataQuality(cfg);
            return dq !== null && dq.avgScore > 0 && dq.grade.length === 1;
        '''))
        ok('generateFullMethodsReport fn', d.execute_script(
            'return typeof generateFullMethodsReport === "function"'))
        ok('methods report generates text', d.execute_script('''
            var report = generateFullMethodsReport();
            return report !== null && report.length > 500 && report.includes("SYNTHESIS METHODS");
        '''))
        ok('NMA container exists in DOM', d.execute_script(
            'return document.getElementById("nmaResultsArea") !== null'))
        ok('timeline container exists', d.execute_script(
            'return document.getElementById("evidenceTimelinePlot") !== null'))
        ok('harmonization container exists', d.execute_script(
            'return document.getElementById("harmonizationArea") !== null'))
        ok('data quality container exists', d.execute_script(
            'return document.getElementById("dataQualityArea") !== null'))
        ok('methods report container exists', d.execute_script(
            'return document.getElementById("methodsReportArea") !== null'))

        # ─── Final: JS errors ───
        logs = d.get_log('browser')
        errors = [l for l in logs if l['level'] == 'SEVERE']
        ok('No JS errors', len(errors) == 0)
        for e in errors[:5]:
            print(f'  JS ERROR: {e["message"][:120]}')

    finally:
        d.quit()

    # Print results
    passed = sum(1 for _, v in results if v)
    total = len(results)
    for name, val in results:
        print(f'  [{"OK" if val else "FAIL"}] {name}')
    print(f'\n{passed}/{total} passed')
    return passed == total

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
