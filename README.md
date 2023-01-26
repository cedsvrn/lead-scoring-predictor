# Lead Scoring Predictor project

The objective of this Lead Scoring predictor project is to:
1. Create a Lead Scoring predictor for an insurance company
2. Push the model into production for both real-time and batch use cases

In this repository, we will explore multiple predictors such as:
- Logistic regression
- Random Forest
- Support Vector Machine

On the deployment side:
- To complete batch use cases we will insert daily lead predictions into a BigQuery database
- A FastAPI dockerized service has been built to send real time predictions to consumer applications
