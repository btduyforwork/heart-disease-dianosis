from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

def add_new_features_func(df):
    df = df.copy()
    if {'chol','age'} <= set(df.columns):
        df['chol_per_age'] = df['chol']/df['age']
    if {'trestbps','age'} <= set(df.columns):
        df['bps_per_age'] = df['trestbps']/df['age']
    if {'thalach','age'} <= set(df.columns):
        df['hr_ratio'] = df['thalach']/df['age']
    if 'age' in df.columns:
        df['age_bin'] = pd.cut(
            df['age'], bins=5, labels=False
        ).astype('category')
    return df

class AddNewFeaturesTransformer(
    BaseEstimator,
    TransformerMixin
):
    def __init__(self):
        self.new_features = []
    def fit(self, X, y=None):
        self.columns=X.columns.tolist()
        X_with_new = add_new_features_func(X)
        self.new_features_ = [
            col for col in X_with_new.columns if col not in X.columns
        ]
        return self
    def transform(self, X):
        return add_new_features_func(X) 
    
def to_feature_dataframe(X, feature_names):
    return pd.DataFrame(X, columns=feature_names)


def select_feature_columns(X, selected_features):
    return X[selected_features]