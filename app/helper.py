from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st
import joblib
import pandas as pd
import json

PROJECT_ROOT = Path.cwd().resolve()

while PROJECT_ROOT.name != "heart-disease-dianosis" and PROJECT_ROOT != PROJECT_ROOT.parent:
    PROJECT_ROOT = PROJECT_ROOT.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
from app.preprocessing import (
    AddNewFeaturesTransformer,to_feature_dataframe,select_feature_columns
)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
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
    "Gradient Boosting":TRAINED_MODEL_DIR / "gradientboosting_fe_dt.joblib",
}

@st.cache_resource(show_spinner=False)
def load_artifact(model_selected: str):
    model_path = MODEL_PATHS[model_selected]
    return joblib.load(model_path)

def prediction_function(model_selected, profile):
    artifact=load_artifact(model_selected)
    pipeline=artifact["pipeline"]
    print("pipeline: ",pipeline)
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

