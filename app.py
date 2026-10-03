import streamlit as st
from src.predictor import analyze_transaction

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# BADASS DARK + YELLOW THEME
# ============================================================
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0a0a0a;
    color: #f5f5f5;
}

.main .block-container {
    max-width: 900px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* Header */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2.5rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid #262626;
}

.brand {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-icon {
    width: 42px;
    height: 42px;
    background: #facc15;
    color: #0a0a0a;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
}

.brand-text h1 {
    font-size: 18px;
    font-weight: 700;
    color: #fafafa;
    margin: 0;
    letter-spacing: -0.3px;
}

.brand-text p {
    font-size: 12px;
    color: #a3a3a3;
    margin: 2px 0 0 0;
}

.badge {
    background: #1c1917;
    border: 1px solid #facc15;
    color: #facc15;
    font-size: 11px;
    font-weight: 600;
    padding: 5px 12px;
    border-radius: 999px;
    letter-spacing: 0.5px;
}

/* Hero */
.hero-title {
    font-size: 32px;
    font-weight: 800;
    color: #fafafa;
    letter-spacing: -0.8px;
    margin-bottom: 8px;
    line-height: 1.2;
}

.hero-title span {
    color: #facc15;
}

.hero-desc {
    font-size: 15px;
    color: #a3a3a3;
    max-width: 560px;
    line-height: 1.6;
    margin-bottom: 2rem;
}

/* Alert */
.alert {
    background: #1c1917;
    border-left: 3px solid #facc15;
    padding: 14px 18px;
    font-size: 13px;
    color: #d4d4d4;
    margin-bottom: 2.2rem;
    border-radius: 0 6px 6px 0;
}

/* Form */
.section-label {
    font-size: 12px;
    font-weight: 600;
    color: #facc15;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 16px;
}

/* Inputs */
label {
    color: #d4d4d4 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #171717 !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
    color: #fafafa !important;
}

div[data-baseweb="input"] input {
    color: #fafafa !important;
}

/* Button */
div.stButton > button {
    background: #facc15 !important;
    color: #0a0a0a !important;
    border: none !important;
    border-radius: 8px !important;
    height: 48px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 0.3px !important;
    transition: all 0.15s ease !important;
}

div.stButton > button:hover {
    background: #eab308 !important;
    color: #0a0a0a !important;
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(250, 204, 21, 0.25);
}

/* Results */
.results-header {
    font-size: 14px;
    font-weight: 600;
    color: #facc15;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 2.5rem 0 1.2rem 0;
}

.metric-card {
    background: #171717;
    border: 1px solid #333;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
}

.metric-label {
    font-size: 12px;
    color: #a3a3a3;
    font-weight: 500;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    color: #fafafa;
    letter-spacing: -0.5px;
}

.metric-value.yellow {
    color: #facc15;
}

/* Status boxes */
.status-fraud {
    background: #450a0a;
    border: 1px solid #991b1b;
    color: #fca5a5;
    padding: 14px 18px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    text-align: center;
    margin: 1rem 0;
}

.status-legit {
    background: #052e16;
    border: 1px solid #166534;
    color: #86efac;
    padding: 14px 18px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    text-align: center;
    margin: 1rem 0;
}

/* Recommendation */
.reco-box {
    background: #171717;
    border: 1px solid #333;
    border-radius: 10px;
    padding: 18px 20px;
    margin-top: 1rem;
}

.reco-label {
    font-size: 11px;
    font-weight: 600;
    color: #facc15;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
}

.reco-text {
    font-size: 14px;
    color: #d4d4d4;
    line-height: 1.6;
}

/* Footer */
.footer {
    margin-top: 3.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid #262626;
    font-size: 12px;
    color: #737373;
    text-align: center;
}
</style>
""")

# ============================================================
# HEADER
# ============================================================
st.html("""
<div class="header">
    <div class="brand">
        <div class="brand-icon"> </div>
        <div class="brand-text">
            <h1>FRAUDGUARD AI</h1>
            <p>Real-time transaction risk engine</p>
        </div>
    </div>
    <div class="badge">LIVE MODEL</div>
</div>
""")

# ============================================================
# HERO
# ============================================================
st.html("""
<div class="hero-title">Transaction Risk <span>Analysis</span></div>
<div class="hero-desc">
    Enter transaction details to receive an instant fraud probability estimate 
    powered by a trained machine learning model.
</div>
""")

st.html("""
<div class="alert">
    PaySim is synthetic data. The probability shown is a model estimate only and 
    should not be treated as a definitive decision in production systems.
</div>
""")

# ============================================================
# INPUT FORM
# ============================================================
st.html('<div class="section-label">Transaction Details</div>')

col1, col2, col3 = st.columns(3)

with col1:
    step = st.number_input(
        "Step / Hour",
        min_value=1,
        max_value=744,
        value=100,
        step=1
    )

with col2:
    typ = st.selectbox(
        "Transaction Type",
        ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
    )

with col3:
    amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f"
    )

st.write("")
analyze = st.button("Analyze Transaction", use_container_width=True)

# ============================================================
# RESULTS
# ============================================================
if analyze:
    try:
        r = analyze_transaction(step, typ, amount)

        st.html('<div class="results-header">Analysis Result</div>')

        # Metrics
        m1, m2, m3 = st.columns(3)

        with m1:
            st.html(f"""
            <div class="metric-card">
                <div class="metric-label">Fraud Probability</div>
                <div class="metric-value yellow">{r['fraud_probability']*100:.2f}%</div>
            </div>
            """)

        with m2:
            st.html(f"""
            <div class="metric-card">
                <div class="metric-label">Risk Level</div>
                <div class="metric-value">{r['risk_level']}</div>
            </div>
            """)

        with m3:
            st.html(f"""
            <div class="metric-card">
                <div class="metric-label">Priority</div>
                <div class="metric-value">{r['priority']}</div>
            </div>
            """)

        # Prediction status
        if r["prediction"]:
            st.html('<div class="status-fraud">⚠ MODEL PREDICTION: FRAUD DETECTED</div>')
        else:
            st.html('<div class="status-legit">✓ MODEL PREDICTION: LEGITIMATE TRANSACTION</div>')

        # Recommendation
        st.html(f"""
        <div class="reco-box">
            <div class="reco-label">Recommended Action</div>
            <div class="reco-text">{r['recommendation']}</div>
        </div>
        """)

    except FileNotFoundError as e:
        st.error(str(e))

# ============================================================
# FOOTER
# ============================================================
st.html("""
<div class="footer">
    Educational project · Not intended for production banking decisions
</div>
""")