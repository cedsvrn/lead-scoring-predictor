"""Main Fast API file."""
import pickle
import pandas as pd

from app.models import UserFeatures
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
async def root():
    """Root path."""
    return {"message": "healthy"}


@app.post("/score/")
async def score(userFeatures: UserFeatures):
    """Score path."""
    json_user_features = jsonable_encoder(userFeatures)
    X = pd.json_normalize(json_user_features)

    rf_pipeline_pkl = pickle.load(open('app/models_pkl/rf_pipeline.pkl', 'rb'))
    result = rf_pipeline_pkl.predict_proba(X)
    result_raw = rf_pipeline_pkl.predict(X)

    return (str(result), '/', str(result_raw))
