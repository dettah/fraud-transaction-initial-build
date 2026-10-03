from src.predictor import analyze_transaction
print('='*60); print('AI-BASED FRAUD DETECTION SYSTEM'); print('='*60)
step=int(input('Enter transaction step/hour (1-744): ')); typ=input('Enter transaction type (CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER): ').strip().upper(); amount=float(input('Enter transaction amount: '))
r=analyze_transaction(step,typ,amount)
print('\nFRAUD ANALYSIS RESULT'); print(f"Fraud Probability: {r['fraud_probability']*100:.2f}%"); print(f"Risk Level: {r['risk_level']}"); print(f"Priority: {r['priority']}"); print('Model Prediction:', 'FRAUD' if r['prediction'] else 'LEGITIMATE'); print('Recommendation:',r['recommendation'])
