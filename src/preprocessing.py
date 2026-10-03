import numpy as np

TARGET='isFraud'
DROP=['nameOrig','nameDest','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFlaggedFraud',TARGET]

def prepare_features(df):
    data=df.copy()
    data['hour']=data['step']%24
    data['day']=((data['step']-1)//24)+1
    data['log_amount']=np.log1p(data['amount'])
    return data.drop(columns=DROP,errors='ignore'),data[TARGET].astype(int)
