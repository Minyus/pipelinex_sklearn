from typing import List
import pandas as pd


def train_model(model, df: pd.DataFrame, cols_features: List[str], col_target: str):
    # TODO: Add validation (Hold-out or Cross-Validation)
    # TODO: Add error handling
    model.fit(df[cols_features], df[col_target])
    return model


def run_inference(model, df: pd.DataFrame, cols_features: List[str]):
    df["pred_proba"] = model.predict_proba(df[cols_features])[:, 1]
    return df
