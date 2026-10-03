# AI-Based Fraud Detection System

## Project idea
A machine-learning system that estimates whether a mobile-money transaction is likely to be fraudulent.

## Dataset
PaySim is a synthetic mobile-money transaction dataset. The public release contains about 6.36 million transactions and a very small fraud class.

## Important feature decision
The project deliberately excludes `nameOrig`, `nameDest`, all four balance fields, and `isFlaggedFraud`. Account IDs are high-cardinality identifiers. More importantly, PaySim documentation warns that balance fields can leak the fraud outcome because fraudulent transactions are cancelled. `isFlaggedFraud` is an existing rule-based flag rather than an independent ML feature.

## Features
Original: `step`, `type`, `amount`. Engineered: `hour`, `day`, `log_amount`.

## Target
`isFraud`: 0 = legitimate, 1 = fraud. Because the classes are highly imbalanced, accuracy alone is inadequate. Evaluate precision, recall, F1, ROC-AUC, PR-AUC and the confusion matrix.

## Model
Random Forest is used because fraud patterns may be nonlinear and involve interactions. It needs no feature scaling and supports class weighting. It is a starting model, not a claim that it is universally optimal.

## Large-file handling
`MAX_ROWS = 500_000` in `src/train.py`. When the downloaded file is larger, a stratified sample is created to make training practical on ordinary computers. Set it to `None` only if the machine has sufficient RAM and training time.

## Structure
```text
ai_based_fraud_detection_system/
├── data/
├── models/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   └── predictor.py
├── app.py
├── predict.py
├── requirements.txt
├── README.md
└── PROJECT_OVERVIEW.txt
```

## Run
1. Put the downloaded Kaggle PaySim CSV in `data/`.
2. `python -m venv venv`
3. Linux/macOS: `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python src/train.py`
6. `python predict.py`
7. `streamlit run app.py`

## Risk categories
LOW <20%, MODERATE 20-50%, HIGH 50-80%, VERY HIGH >=80%. These are application-level educational thresholds, not banking policy thresholds or calibrated regulatory standards.

## Presentation questions
- What is PaySim?
- Why is fraud detection imbalanced?
- Why remove account IDs?
- Why exclude balance fields?
- Why exclude `isFlaggedFraud`?
- Why create `hour`, `day`, and `log_amount`?
- Why Random Forest?
- Why is accuracy insufficient?
- What are precision, recall, F1, ROC-AUC and PR-AUC?
- What is a false negative?
- What is the `.joblib` file?
- What would a production fraud system need that this project does not have?

## Architecture
Transaction input -> feature engineering -> one-hot encoding -> Random Forest -> fraud probability -> risk category -> recommendation.

## Disclaimer
This is an educational project using synthetic data. It should not be deployed directly as a real banking fraud decision system without representative data, validation, threshold calibration, monitoring, security controls, and domain review.
