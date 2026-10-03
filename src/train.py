from pathlib import Path
import sys,joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,average_precision_score,classification_report,confusion_matrix
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.data_loader import load_data
from src.preprocessing import prepare_features



ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'models'; OUT.mkdir(exist_ok=True)
MAX_ROWS=500_000
df=load_data(MAX_ROWS)

print(f'Rows used: {len(df):,}'); print(f'Fraud rows: {df.isFraud.sum():,}'); print(f'Fraud rate: {df.isFraud.mean()*100:.4f}%')

X,y=prepare_features(df)
cat=['type']; num=['step','amount','hour','day','log_amount']
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.20,random_state=42,stratify=y)
prep=ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),cat),('num','passthrough',num)])
Xtr=prep.fit_transform(Xtr); Xte=prep.transform(Xte)
model=RandomForestClassifier(n_estimators=200,random_state=42,class_weight='balanced_subsample',min_samples_leaf=2,n_jobs=-1)
print('Training Random Forest...'); model.fit(Xtr,ytr)
pred=model.predict(Xte); prob=model.predict_proba(Xte)[:,1]
print('\nMODEL EVALUATION'); print(f'Accuracy:  {accuracy_score(yte,pred):.4f}'); print(f'Precision: {precision_score(yte,pred,zero_division=0):.4f}'); print(f'Recall:    {recall_score(yte,pred,zero_division=0):.4f}'); print(f'F1:        {f1_score(yte,pred,zero_division=0):.4f}'); print(f'ROC-AUC:   {roc_auc_score(yte,prob):.4f}'); print(f'PR-AUC:    {average_precision_score(yte,prob):.4f}')
print('\nCLASSIFICATION REPORT\n',classification_report(yte,pred,target_names=['Legitimate','Fraud'],zero_division=0)); print('CONFUSION MATRIX\n',confusion_matrix(yte,pred))

joblib.dump({'model':model,'preprocessor':prep},OUT/'fraud_detection_model.joblib')
print(f'\nSaved: {OUT/"fraud_detection_model.joblib"}')
