import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from mlProject.utils.common import save_json
from mlflow.models import ModelSignature
from mlflow.types import Schema, ColSpec

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        # Create an input example (this should match your model's input shape)
        input_example = test_data.drop([self.config.target_column], axis=1).iloc[0:1]  # Take the first row as an example

        # Define the model signature
        input_schema = Schema([
            ColSpec("float", "fixed acidity"),  # Replace with your actual feature names and types
            ColSpec("float", "volatile acidity"),
            ColSpec("float", "citric acid"),
            ColSpec("float", "residual sugar"),
            ColSpec("float", "chlorides"),
            ColSpec("float", "free sulfur dioxide"),
            ColSpec("float", "total sulfur dioxide"),
            ColSpec("float", "density"),
            ColSpec("float", "pH"),
            ColSpec("float", "sulphates"),
            ColSpec("float", "alcohol"),
        ])

        # Create the model signature
        signature = ModelSignature(inputs=input_schema)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path = Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Model registry does not work with file store

            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # Please refer to the doc for more information
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model,
                                         "model",
                                         registered_model_name = "ElasticnetModel",
                                         signature=signature,
                                         input_example=input_example.to_dict(orient="records")[0]
                                         )
            else:
                mlflow.sklearn.log_model(model,
                                         "model",
                                         signature=signature,
                                         input_example=input_example.to_dict(orient="records")[0]
                                         )