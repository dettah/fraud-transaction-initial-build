from pathlib import Path
import pandas as pd
from datasets import load_dataset


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXPECTED = [
    "step", "type", "amount", "nameOrig", "oldbalanceOrg",
    "newbalanceOrig", "nameDest", "oldbalanceDest",
    "newbalanceDest", "isFraud", "isFlaggedFraud"
]

DATASET_ID = "LordNR/AMLGraphX-Paysim"


def find_dataset():
    """Kept for compatibility. Always returns None because we load from Hugging Face."""
    return None


def load_data(max_rows=500_000, random_state=42):
    # Load from Hugging Face (streaming)
    stream = (
        load_dataset(DATASET_ID, split="train", streaming=True)
        .shuffle(seed=random_state, buffer_size=100_000)
    )
    rows = list(stream.take(max_rows if max_rows is not None else 300_000))
    df = pd.DataFrame(rows)

    # Validate columns
    missing = [c for c in EXPECTED if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing expected columns: {missing}")

    # Keep the same stratified sampling logic you already had
    if max_rows is not None and len(df) > max_rows:
        fraud = df[df.isFraud == 1]
        legit = df[df.isFraud == 0]
        fraud_n = min(len(fraud), max(1000, int(max_rows * len(fraud) / len(df))))
        legit_n = max_rows - fraud_n
        df = pd.concat(
            [
                fraud.sample(fraud_n, random_state=random_state),
                legit.sample(legit_n, random_state=random_state),
            ],
            ignore_index=True,
        )
        df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)

    return df