"""Script to train the ML models and register them as .pkl files."""
import os
import pickle

from datetime import datetime
from models import RandomForestPredictor
from conf import FULL_COLUMN, ID_COLUMN, FEATURE_COLUMNS, DATASET, TABLE, MODEL_FOLDER

from google.cloud import bigquery


class BigQueryConnector():
    """Read and write data to BigQuery."""

    def __init__(self, conf_bq_path):
        """Init BigQuery connector."""
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = conf_bq_path
        self.client = bigquery.Client()
        pass 

    def read(self, query):
        """Read SQL query and return pandas dataframe."""
        df_result = self.client.query(query).to_dataframe()
        return df_result

    def write(self, df, dataset, table):
        """Write pandas datframe to bigquery table."""
        table_id = f"orn-lead-scoring-predictor.{dataset}.{table}"

        # FIXME : delete data before inserting

        print(f"Insert rows to {table_id}.")
        rows_to_insert = df.to_dict('records')
        
        errors = self.client.insert_rows_json(table_id, rows_to_insert)
        if errors == []:
            print(f"New rows have been inserted to {table_id}.")
        else:
            print("Encountered errors while inserting new rows: {}".format(errors))


def get_lead_data(bq_connector):
    """Get lead data by reading bigquery table."""
    sql_query = "SELECT * FROM `lead_scoring.long_quotes`;"
    df_result = bq_connector.read(sql_query)
    df_result = df_result[FULL_COLUMN]
    return df_result


if __name__ == "__main__":
    database = "demo_db"
    model_name = "random_forest"

    active_models = {"random_forest"}

    assert model_name in active_models, 'Error: Unidentified model!'

    date = datetime.today().strftime('%Y-%m-%d')

    # BigQuery connector
    conf_bq_path = "../secrets/GOOGLE_APPLICATION_CREDENTIALS.json"
    bq_connector = BigQueryConnector(conf_bq_path)

    # Get data
    lead_data = get_lead_data(bq_connector)

    # Fit, get recommendations and register new model
    if model_name == "random_forest":
        model = RandomForestPredictor().fit(lead_data)

        # Register
        pickle.dump(model, open(f"{MODEL_FOLDER}/rf_pipeline.pkl", 'wb'))

        # Insert predictions
        y_scores = model.predict_score(lead_data[FEATURE_COLUMNS])
        X_pred = lead_data[[ID_COLUMN]]
        X_pred["score"] = y_scores
        X_pred["date"] = date
        bq_connector.write(X_pred, DATASET, TABLE)
