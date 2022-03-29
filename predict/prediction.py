import joblib
import pandas as pd
from flask import jsonify

model = joblib.load("model/finalized_model.pkl")


def predict(data: pd.DataFrame):
    prediction = model.predict(data)
    response = {"prediction": f"{int(prediction[0]):.2f}", "error": None}
    return jsonify(response)
