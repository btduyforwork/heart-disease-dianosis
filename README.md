## 🫀 Heart Disease Prediction: An Robust Machine Learning Pipeline

### 📌 Overview
This project delivers a robust learning system designed to assist in the early diagnosis of heart disease. Leveraging the Cleveland Clinic clinical dataset, the primary objective was to transform raw medical records into a highly reliable, deployable predictive tool. This repository demonstrates a complete data science lifecycle—from rigorous statistical analysis to the deployment of an interactive website.
<p align="center">
 <img width="600" height="auto" alt="image" src="https://github.com/user-attachments/assets/dbdcd0eb-bcda-4e1a-9775-20c0c70ddef8" />
</p>

### 🚀 Key Contributions & Methodology

* **Exploratory Data Analysis (EDA):** Conducted in-depth statistical analysis and multivariate visualizations to unearth critical medical risk factors. Successfully isolated high-impact discriminators, notably *Chest Pain Type (cp)* and demographic distributions.
* **Advanced Feature Engineering:** Engineered a robust, leak-proof preprocessing architecture using `scikit-learn` Pipelines. Optimized the dataset's predictive capacity through continuous variable discretization (binning), numerical scaling, and One-Hot Encoding for categorical features.
* **Predictive Modeling & Optimization:** Designed a progressive modeling strategy. Established strong baselines (Decision Tree, Naive Bayes) before advancing to state-of-the-art Ensemble classifiers. Trained, hyperparameter-tuned, and evaluated **Random Forest, Gradient Boosting, and XGBoost** models to minimize overfitting and maximize diagnostic precision. 
* **Application Deployment:** Bridged the gap between machine learning and real-world utility by architecting an interactive Web Application using **Streamlit**. The deployed app allows users to input clinical parameters and instantly receive a diagnostic risk assessment.

### 🛠️ Technologies Used
* **Data Manipulation:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-learn, XGBoost, Random Forest, Gradient Boosting
* **Data Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit
