import os

import joblib
from fastapi import FastAPI
from schema import ChurnInfo, ChurnPrediction
from utils.data_processing import format_input_data
from utils.logging import logger

# Creating FastAPI instance
app = FastAPI()

# Loading model with default path models/model.pkl
clf = joblib.load(os.environ.get("MODEL_PATH", "models/model.pkl"))


# Creating an endpoint to receive the data
# to make prediction on
@app.post("/predict", response_model=ChurnPrediction)
def predict(data: ChurnInfo):
    # Predicting the class
    logger.info("Make predictions...")
    # Convert data to pandas DataFrame and make predictions
    price = clf.predict_proba(format_input_data(data))[0][0]

    # Return the result
    return ChurnPrediction(Price=price)
