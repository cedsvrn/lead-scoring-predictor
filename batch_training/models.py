"""Listing ML models for lead score predcitions."""
import numpy as np
import pandas as pd

from conf import FEATURE_COLUMNS, TARGET_COLUMN

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class LeadScorePredictor():
    """Predictor remplate class."""

    def __init__(self):
        """Init template."""
        pass 

    def fit(self, X):
        """Fit template function."""
        pass 

    def predict(self, X):
        """Predict template function."""
        pass 

    def predict_score(self, X):
        """Predict score template function."""
        pass


class RandomForestPredictor(LeadScorePredictor):
    """Random forest predictor."""

    def fit(self, X):
        """Fitting the RandmForestPredictor."""
        X_quotes = X[FEATURE_COLUMNS]
        y_quotes = X[TARGET_COLUMN]
        y_quotes = np.where(y_quotes, 1, 0)

        imputer = SimpleImputer(strategy="most_frequent")
        categorical_encoder = OneHotEncoder(handle_unknown='ignore')

        categorical_pipeline = Pipeline(
            [("imputer", imputer), ("encoder", categorical_encoder)]
        )

        preprocess_pipeline = ColumnTransformer(transformers=[
            ("category", categorical_pipeline, FEATURE_COLUMNS)
        ])

        self.rf_pipeline = Pipeline(
            [
                ("preprocess", preprocess_pipeline),
                ("classifier", RandomForestClassifier(random_state=0, class_weight='balanced',
                                                      max_depth=7, 
                                                      min_samples_split=2, 
                                                      n_estimators=100))
            ]
        )
        self.rf_pipeline.fit(X_quotes, y_quotes)

        return self
    
    def predict_score(self, X):
        """Predict score template function."""
        preds = self.rf_pipeline.predict_proba(X[FEATURE_COLUMNS])
        df_preds = pd.DataFrame(data=preds, columns=['neg_score', 'pos_score'])
        return df_preds["pos_score"]
