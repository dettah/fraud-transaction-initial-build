import streamlit as st
from src.predictor import analyze_transaction
st.set_page_config(page_title='AI Fraud Detection',page_icon='🔐')
st.title('🔐 AI-Based Fraud Detection System')
st.write('Estimate the probability that a mobile-money transaction is fraudulent.')
st.info('PaySim is synthetic data. The displayed probability is a model estimate, not a guarantee.')
step=st.number_input('Transaction Step / Hour',1,744,100,1)
typ=st.selectbox('Transaction Type',['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER'])
amount=st.number_input('Transaction Amount',min_value=0.0,value=10000.0,step=100.0)
if st.button('Analyze Transaction'):
    try:
        r=analyze_transaction(step,typ,amount)
        st.metric('Fraud Probability',f"{r['fraud_probability']*100:.2f}%")
        c1,c2=st.columns(2)
        c1.write('**Risk Level**'); c1.write(r['risk_level']); c2.write('**Priority**'); c2.write(r['priority'])
        st.write('**Model Prediction**'); st.error('FRAUD') if r['prediction'] else st.success('LEGITIMATE')
        st.write('**Recommended Action**'); st.write(r['recommendation'])
    except FileNotFoundError as e: st.error(str(e))
st.caption('Educational project. Do not use directly as a production banking decision system.')

