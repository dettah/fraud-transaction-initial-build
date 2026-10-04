import streamlit as st
from src.predictor import analyze_transaction

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# REFINED STYLES
# ============================================================
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: #080D19;
    color: #E2E8F0;
}

.main .block-container {
    max-width: 920px;
    padding-top: 1.8rem;
    padding-bottom: 4rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* ---------- Top bar ---------- */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 3.2rem;
}

.logo-wrap {
    display: flex;
    align-items: center;
    gap: 11px;
}

.logo-mark {
    width: 34px;
    height: 34px;
    background: #FACC15;
    color: #080D19;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 800;
}

.logo-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #F8FAFC;
    letter-spacing: -0.3px;
}

.status {
    font-size: 11px;
    font-weight: 600;
    color: #FACC15;
    background: rgba(250, 204, 21, 0.07);
    border: 1px solid rgba(250, 204, 21, 0.22);
    padding: 4px 11px;
    border-radius: 999px;
    letter-spacing: 0.5px;
}

/* ---------- Centered Hero ---------- */
.hero {
    text-align: center;
    margin-bottom: 2.8rem;
}

.hero-eyebrow {
    font-size: 11px;
    font-weight: 600;
    color: #FACC15;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 38px;
    font-weight: 700;
    color: #F8FAFC;
    letter-spacing: -1.1px;
    line-height: 1.15;
    margin: 0 auto 14px auto;
    max-width: 540px;
}

.hero-title span {
    color: #FACC15;
}

.hero-desc {
    font-size: 15px;
    color: #94A3B8;
    line-height: 1.65;
    max-width: 480px;
    margin: 0 auto;
}

/* ---------- Notice ---------- */
.notice {
    background: rgba(30, 41, 59, 0.55);
    border: 1px solid #1E293B;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 12.5px;
    color: #94A3B8;
    text-align: center;
    margin-bottom: 2.4rem;
    line-height: 1.55;
}

/* ---------- Form section ---------- */
.form-label {
    font-size: 11px;
    font-weight: 600;
    color: #64748B;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 14px;
    text-align: center;
}

.form-shell {
    background: #0F172A;
    border: 1px solid #1E293B;
    border-radius: 14px;
    padding: 28px 28px 20px 28px;
    margin-bottom: 1.5rem;
}

/* Inputs */
label {
    color: #94A3B8 !important;
    font-size: 12.5px !important;
    font-weight: 500 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #080D19 !important;
    border: 1px solid #334155 !important;
    border-radius: 9px !important;
}

div[data-baseweb="input"] input {
    color: #F1F5F9 !important;
    font-size: 14px !important;
}

/* Button */
div.stButton > button {
    background: #FACC15 !important;
    color: #080D19 !important;
    border: none !important;
    border-radius: 9px !important;
    height: 48px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.2px !important;
    transition: all 0.18s ease !important;
}

div.stButton > button:hover {
    background: #EAB308 !important;
    color: #080D19 !important;
    box-shadow: 0 8px 24px rgba(250, 204, 21, 0.18);
    transform: translateY(-1px);
}

/* ---------- Results ---------- */
.results-label {
    font-size: 11px;
    font-weight: 600;
    color: #64748B;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-align: center;
    margin: 2.6rem 0 1.1rem 0;
}

.metric-card {
    background: #0F172A;
    border: 1px solid #1E293B;
    border-radius: 12px;
    padding: 22px 16px;
    text-align: center;
}

.metric-label {
    font-size: 11px;
    font-weight: 500;
    color: #64748B;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #F8FAFC;
    letter-spacing: -0.6px;
}

.metric-value.accent {
    color: #FACC15;
}

/* Status */
.status-box {
    border-radius: 10px;
    padding: 14px 18px;
    font-weight: 600;
    font-size: 13.5px;
    text-align: center;
    margin: 1.1rem 0;
    letter-spacing: 0.2px;
}

.status-fraud {
    background: rgba(127, 29, 29, 0.28);
    border: 1px solid #7F1D1D;
    color: #FCA5A5;
}

.status-legit {
    background: rgba(6, 78, 59, 0.28);
    border: 1px solid #065F46;
    color: #6EE7B7;
}

/* Recommendation */
.reco-card {
    background: #0F172A;
    border: 1px solid #1E293B;
    border-radius: 12px;
    padding: 18px 20px;
}

.reco-label {
    font-size: 11px;
    font-weight: 600;
    color: #64748B;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.reco-text {
    font-size: 14px;
    color: #CBD5E1;
    line-height: 1.65;
}

/* Footer */
.footer {
    margin-top: 4rem;
    padding-top: 1.2rem;
    border-top: 1px solid #1E293B;
    font-size: 12px;
    color: #475569;
    text-align: center;
}

/* Mobile */
@media (max-width: 768px) {
    .hero-title {
        font-size: 28px;
    }
    .form-shell {
        padding: 20px 16px 12px 16px;
    }
}
</style>
""")

# ============================================================
# TOP BAR
# ============================================================
st.html("""
<div class="topbar">
    <div class="logo-wrap">
        <div class="logo-mark">🛡️</div>
        <div class="logo-text">FraudGuard AI</div>
    </div>
    <div class="status">LIVE</div>
</div>
""")

# ============================================================
# CENTERED HERO
# ============================================================
st.html("""
<div class="hero">
    <div class="hero-eyebrow">Real-time Risk Engine</div>
    <div class="hero-title">Transaction Risk<br><span>Analysis</span></div>
    <div class="hero-desc">
        Enter transaction details to receive an instant fraud probability estimate 
        powered by a trained machine learning model.
    </div>
</div>
""")

st.html("""
<div class="notice">
    PaySim is synthetic data. The probability shown is a model estimate only and 
    should not be treated as a definitive decision in production systems.
</div>
""")

# ============================================================
# FORM
# ============================================================
st.html('<div class="form-label">Transaction Details</div>')

with st.container():
    # Row 1
    c1, c2, c3 = st.columns(3)
    with c1:
        step = st.number_input("Step / Hour", min_value=1, max_value=744, value=100, step=1)
    with c2:
        typ = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])
    with c3:
        amount = st.number_input("Amount", min_value=0.0, value=10000.0, step=100.0, format="%.2f")

    # Row 2
    c4, c5 = st.columns(2)
    with c4:
        oldbalance_org = st.number_input(
            "Origin Balance (Before)",
            min_value=0.0,
            value=50000.0,
            step=100.0,
            format="%.2f"
        )
    with c5:
        oldbalance_dest = st.number_input(
            "Destination Balance (Before)",
            min_value=0.0,
            value=50000.0,
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
        r = analyze_transaction(step, typ, amount, oldbalance_org, oldbalance_dest)

        st.html('<div class="results-label">Analysis Result</div>')

        m1, m2, m3 = st.columns(3)

        with m1:
            st.html(f"""
            <div class="metric-card">
                <div class="metric-label">Fraud Probability</div>
                <div class="metric-value accent">{r['fraud_probability']*100:.2f}%</div>
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

        if r["prediction"]:
            st.html('<div class="status-box status-fraud">⚠  MODEL PREDICTION — FRAUD DETECTED</div>')
        else:
            st.html('<div class="status-box status-legit">✓  MODEL PREDICTION — LEGITIMATE TRANSACTION</div>')

        st.html(f"""
        <div class="reco-card">
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