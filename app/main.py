from __future__ import annotations

import streamlit as st
from helper import prediction_function


st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="wide",
)


def selectbox_value(label: str, options: dict[str, float]) -> float:
    selected_label = st.selectbox(label, list(options.keys()))
    return options[selected_label]


st.markdown(
    """
    <style>
    .stApp {
        background: #FFFFFF;
        color: #222222;
        font-family: "Segoe UI", Arial, sans-serif;
    }
    .block-container {
        max-width: 1220px;
        padding-top: 2.2rem;
        padding-bottom: 2rem;
    }
    .page-title {
        margin: 0;
        color: #2f6db5;
        text-align: center;
        font-size: 3.2rem;
        line-height: 1.1;
        font-weight: 800;
        letter-spacing: 0;
    }
    .info-panel {
        display: flex;
        gap: 1rem;
        align-items: flex-start;
        border-radius: 8px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.78);
        box-shadow: 0 8px 20px rgba(48, 67, 92, 0.08);
    }
    .info-panel.overview {
        border-left: 6px solid #2f6db5;
        margin-top: 2.2rem;
    }
    .info-panel.disclaimer {
        border-left: 6px solid #cf3657;
        background: rgba(255, 249, 249, 0.86);
    }
    .panel-icon {
        flex: 0 0 auto;
        width: 1.75rem;
        padding-top: 0.15rem;
        font-size: 1.15rem;
        text-align: center;
    }
    .info-panel h3 {
        margin: 0 0 0.5rem;
        font-size: 1.2rem;
        line-height: 1.25;
        letter-spacing: 0;
    }
    .info-panel.overview h3 {
        color: #2f5f9f;
    }
    .info-panel.disclaimer h3 {
        color: #222222;
    }
    .info-panel p {
        margin: 0.35rem 0;
        font-size: 1rem;
        line-height: 1.5;
    }
    .page-subtitle {
        margin: 1rem 0 2.4rem;
        color: #858585;
        text-align: center;
        font-size: 1.25rem;
        font-style: italic;
        font-weight: 800;
        letter-spacing: 0;
    }
    div[data-testid="stForm"] {
        border: 1px solid #d8e1ee;
        border-radius: 8px;
        padding: 1.25rem;
        background: rgba(255, 255, 255, 0.86);
        box-shadow: 0 8px 20px rgba(48, 67, 92, 0.08);
    }
    .stButton button {
        border-radius: 8px;
        border: 1px solid #f97316 !important;
        background: #f97316 !important;
        color: #ffffff !important;
        font-weight: 800;
    }
    .stButton button:hover {
        border-color: #ea580c !important;
        background: #ea580c !important;
        color: #ffffff !important;
    }
    div[data-testid="stAlert"] {
        border-radius: 8px;
    }
    .intro-copy {
        margin: 0.25rem 0 1.35rem;
        font-size: 1rem;
        color: #30343b;
    }
    .demo-note {
        border-left: 4px solid #d9dde4;
        padding: 0.35rem 0 0.35rem 0.9rem;
        margin-bottom: 1rem;
        color: #333333;
    }
    .section-header {
        margin-top: 0.95rem;
        padding: 0.35rem 0.55rem;
        border-radius: 6px 6px 0 0;
        background: #d8dadd;
        color: #333333;
        font-size: 1rem;
        font-weight: 800;
    }
    .model-panel-marker + div {
        border: 1px solid #d8e1ee;
        border-radius: 8px;
        padding: 0.95rem 1rem 1rem;
        margin-bottom: 1.2rem;
        background: #ffffff;
        box-shadow: 0 8px 20px rgba(48, 67, 92, 0.08);
    }
    .input-panel-marker + div {
        border: 1px solid #d8e1ee;
        border-radius: 8px;
        padding: 0.95rem 1rem 1rem;
        background: #ffffff;
        box-shadow: 0 8px 20px rgba(48, 67, 92, 0.08);
    }
    .assessment-card {
        border: 2px solid #6f9d3f;
        border-radius: 8px;
        padding: 1.65rem;
        margin-top: 3.8rem;
        background: rgba(255, 255, 255, 0.72);
    }
    .assessment-eyebrow {
        color: #6f727a;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.18rem;
        text-transform: uppercase;
    }
    .assessment-title {
        margin: 1rem 0;
        color: #6f9d3f;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: 0;
    }
    .risk-scale {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.25rem;
        margin: 1.4rem 0 0.35rem;
    }
    .risk-scale span {
        display: block;
        height: 0.38rem;
        border-radius: 8px;
    }
    .risk-labels {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.25rem;
        color: #8f949c;
        font-size: 0.72rem;
        text-align: center;
    }
    .probability-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.6rem;
        color: #6f727a;
        font-weight: 800;
    }
    .probability-value {
        color: #6f9d3f;
        font-size: 1.25rem;
    }
    .progress-track {
        width: 100%;
        height: 0.55rem;
        border-radius: 8px;
        background: #e4e5e8;
        overflow: hidden;
        margin-top: 0.55rem;
    }
    .progress-fill {
        width: 0%;
        height: 100%;
        border-radius: 8px;
        background: #6f9d3f;
    }
    .assessment-note {
        border-left: 3px solid #6f9d3f;
        border-radius: 6px;
        padding: 1rem;
        margin-top: 1.35rem;
        background: rgba(255, 255, 255, 0.58);
        color: #555c66;
        font-size: 0.92rem;
        line-height: 1.5;
    }
    .stButton button[kind="secondary"] {
        border-color: #f97316 !important;
        background: #f97316 !important;
        color: #ffffff !important;
        font-weight: 800;
    }
    .stButton button[kind="secondary"]:hover {
        border-color: #ea580c !important;
        background: #ea580c !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 class="page-title">Heart Disease Diagnosis Project</h1>
    <div class="info-panel overview">
        <div class="panel-icon">🫀</div>
        <div>
            <h4>About this demo</h4>
            <p>Predict heart disease risk from patient data with optimized ML models trained on the Cleveland dataset.</p>
            <p><strong>Dataset:</strong> Cleveland Heart Disease <strong></p>
            <p>Models:</strong> Random Forest, XGBoost, Gradient Boosting</p>
        </div>
    </div>
    <div class="info-panel disclaimer">
        <div class="panel-icon">⚠️</div>
        <div>
            <h4>Educational Use Only</h4>
            <p>This interactive heart disease prediction demo is provided strictly for educational purposes. It is not intended for clinical use and must not be relied upon for medical advice, diagnosis, treatment, or decision-making. Always consult a qualified healthcare professional.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p class="intro-copy">Enter routine patient examination values to generate a cardiovascular disease risk estimate.</p>
    <div class="demo-note"><strong>Demo only.</strong> Not a medical device. Not for clinical use.</div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="model-panel-marker"></div>', unsafe_allow_html=True)
  

input_col, result_col = st.columns([1.28, 1], gap="large")

with input_col:
        st.markdown('<div class="input-panel-marker"></div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-header">Prediction Model</div>', unsafe_allow_html=True)
            selected_model = st.selectbox(
            "Model",
            [
            "Random Forest",
            "XGBoost",
            "Gradient Boosting",
            ],
        )
        st.markdown('<div class="section-header">Demographics</div>', unsafe_allow_html=True)
        demographics_left, demographics_right = st.columns(2)
        with demographics_left:
            age = st.number_input("Age", min_value=18, max_value=100, value=54, step=1)
            cp = selectbox_value(
                "Chest pain type",
                {
                    "Typical angina": 1.0,
                    "Atypical angina": 2.0,
                    "Non-anginal pain": 3.0,
                    "Asymptomatic": 4.0,
                },
            )
        with demographics_right:
            sex = selectbox_value(
                "Sex",
                {
                    "Male": 1.0,
                    "Female": 0.0,
                },
            )

        st.markdown('<div class="section-header">Blood Pressure And Labs</div>', unsafe_allow_html=True)
        labs_left, labs_right = st.columns(2)
        with labs_left:
            trestbps = st.number_input(
                "Resting blood pressure",
                min_value=80,
                max_value=220,
                value=130,
                step=1,
                help="mm Hg",
            )
            chol = st.number_input(
                "Serum cholesterol",
                min_value=100,
                max_value=650,
                value=246,
                step=1,
                help="mg/dl",
            )
        with labs_right:
            fbs = selectbox_value(
                "Fasting blood sugar > 120 mg/dl",
                {
                    "No": 0.0,
                    "Yes": 1.0,
                },
            )
            restecg = selectbox_value(
                "Resting ECG",
                {
                    "Normal": 0.0,
                    "ST-T wave abnormality": 1.0,
                    "Left ventricular hypertrophy": 2.0,
                },
            )

        st.markdown('<div class="section-header">Exercise And ECG</div>', unsafe_allow_html=True)
        exercise_left, exercise_right = st.columns(2)
        with exercise_left:
            thalach = st.number_input(
                "Maximum heart rate",
                min_value=60,
                max_value=230,
                value=150,
                step=1,
            )
            oldpeak = st.number_input(
                "ST depression",
                min_value=0.0,
                max_value=7.0,
                value=1.0,
                step=0.1,
            )
        with exercise_right:
            exang = selectbox_value(
                "Exercise induced angina",
                {
                    "No": 0.0,
                    "Yes": 1.0,
                },
            )
            slope = selectbox_value(
                "Peak exercise ST slope",
                {
                    "Upsloping": 1.0,
                    "Flat": 2.0,
                    "Downsloping": 3.0,
                },
            )

        st.markdown('<div class="section-header">Clinical Imaging</div>', unsafe_allow_html=True)
        imaging_left, imaging_right = st.columns(2)
        with imaging_left:
            ca = st.number_input(
                "Major vessels colored",
                min_value=0,
                max_value=3,
                value=0,
                step=1,
            )
        with imaging_right:
            thal = selectbox_value(
                "Thalassemia",
                {
                    "Normal": 3.0,
                    "Fixed defect": 6.0,
                    "Reversible defect": 7.0,
                },
            )

submitted = st.button("Analyse Patient", use_container_width=True)

profile = {
    "age": float(age),
    "sex": sex,
    "cp": cp,
    "trestbps": float(trestbps),
    "chol": float(chol),
    "fbs": fbs,
    "restecg": restecg,
    "thalach": float(thalach),
    "exang": exang,
    "oldpeak": float(oldpeak),
    "slope": slope,
    "ca": float(ca),
    "thal": thal,
}


if submitted:
    prediction, probability = prediction_function(selected_model, profile)
    if probability >= 0.65:
        assessment_title = "High Risk"
    elif probability >= 0.35:
        assessment_title = "Moderate Risk"
    else:
        assessment_title = "Low Risk"

    probability_text = f"{probability:.1%}"
    progress_width = f"{probability * 100:.1f}%"
else:
    prediction = None
    probability = 0.0
    assessment_title = "Ready For Input"
    probability_text = "--"
    progress_width = "0%"

with result_col:
    st.markdown(
        f"""
<div class="assessment-card">
<div class="assessment-eyebrow">Assessment Result</div>
<div class="assessment-title">{assessment_title}</div>
<div class="risk-scale">
<span style="background:#9fcca6;"></span>
<span style="background:#bfd29c;"></span>
<span style="background:#efc28f;"></span>
<span style="background:#eead98;"></span>
<span style="background:#e49ba0;"></span>
</div>
<div class="risk-labels">
<div>Low</div>
<div>Moderate</div>
<div>Borderline</div>
<div>High</div>
<div>Very High</div>
</div>
<div class="probability-row">
<span>Heart Disease Probability</span>
<span class="probability-value">{probability_text}</span>
</div>
<div class="progress-track">
<div class="progress-fill" style="width:{progress_width};"></div>
</div>
<div class="assessment-note">
Complete the patient values and analyse the profile. This result is for educational use only.
</div>
</div>
""",
        unsafe_allow_html=True,
    )
