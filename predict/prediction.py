import joblib
import pandas as pd

model = joblib.load("model/finalized_model.pkl")


def predict(data: dict):
    prediction = model.predict(data["prediction"])
    response = {"prediction": f"{int(prediction[0]):.2f}", "error": None}
    return response
