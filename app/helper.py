from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "notebooks" / "cleveland.csv"
TRAINED_MODEL_DIR = PROJECT_ROOT / "models" / "trained_models"
RANDOM_FOREST_RAW_PATH = TRAINED_MODEL_DIR / "randomforest_raw.joblib"
COLUMNS = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 
    'ca', 'thal', 'target'
]
MODEL_PATHS={
    "Random Forest":TRAINED_MODEL_DIR / "randomforest_raw.joblib",
    "XGBoost":TRAINED_MODEL_DIR / "xgboost.joblib",
    "Gradient Boosting":TRAINED_MODEL_DIR / "gradient_boosting.joblib",
}


def load_random_forest_raw_data() -> dict:
    """Load the model and related data pipeline"""
    return joblib.load(RANDOM_FOREST_RAW_PATH)

def predict_heart_disease(profile:dict[str,float]):
    artifact=load_random_forest_raw_data()
    pipeline=artifact["pipeline"]
    raw_input_df=pd.DataFrame([profile], columns=COLUMNS[:-1])
    prediction = int(pipeline.predict(raw_input_df)[0])
    prediction_prob=float(pipeline.predict_proba(raw_input_df)[0, 1])
    return prediction, prediction_prob

def prediction_function(model_selected, profile):
    model_path=MODEL_PATHS[model_selected]
    artifact=joblib.load(model_path)
    pipeline=artifact["pipeline"]
    raw_input_df=pd.DataFrame([profile], columns=COLUMNS[:-1])
    prediction = int(pipeline.predict(raw_input_df)[0])
    prediction_prob=float(pipeline.predict_proba(raw_input_df)[0, 1])
    return prediction, prediction_prob




# sample_profile = {
#     "age": 54.0,
#     "sex": 1.0,
#     "cp": 4.0,
#     "trestbps": 130.0,
#     "chol": 246.0,
#     "fbs": 0.0,
#     "restecg": 1.0,
#     "thalach": 150.0,
#     "exang": 0.0,
#     "oldpeak": 1.0,
#     "slope": 2.0,
#     "ca": 0.0,
#     "thal": 3.0,
# }


