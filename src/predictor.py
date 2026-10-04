from pathlib import Path
import joblib,numpy as np,pandas as pd

ROOT=Path(__file__).resolve().parents[1]; MODEL=ROOT/'models'/'fraud_detection_model.joblib'

def load_artifact():
    if not MODEL.exists(): raise FileNotFoundError('Trained model not found. Run: python src/train.py')
    return joblib.load(MODEL)
def build_input(step,transaction_type,amount,oldbalance_org,oldbalance_dest,):
    step=int(step); amount=float(amount)
    return pd.DataFrame([{'step':step,'type':transaction_type,'amount':amount,'hour':step%24,'day':((step-1)//24)+1,'log_amount':np.log1p(amount),"oldbalanceOrg": oldbalance_org,"oldbalanceDest": oldbalance_dest}])
def risk_level(p):
    if p<.20:return 'LOW'
    if p<.50:return 'MODERATE'
    if p<.80:return 'HIGH'
    return 'VERY HIGH'
def analyze_transaction(step,transaction_type,amount,oldbalance_org,oldbalance_dest,):
    a=load_artifact(); X=a['preprocessor'].transform(build_input(step,transaction_type,amount,oldbalance_org,oldbalance_dest,)); pred=int(a['model'].predict(X)[0]); p=float(a['model'].predict_proba(X)[0][1]); risk=risk_level(p)
    rec={'LOW':'Continue normal transaction monitoring.','MODERATE':'Consider additional monitoring or secondary checks.','HIGH':'Consider additional verification before allowing the transaction.','VERY HIGH':'Flag transaction for enhanced review before completing it.'}[risk]
    pri={'LOW':'NORMAL','MODERATE':'MEDIUM','HIGH':'HIGH','VERY HIGH':'CRITICAL'}[risk]
    return {'fraud_probability':p,'prediction':pred,'risk_level':risk,'priority':pri,'recommendation':rec}

