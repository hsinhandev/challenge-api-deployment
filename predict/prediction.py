import joblib
import pandas as pd

model = joblib.load("model/finalized_model.pkl")


def predict(data: pd.DataFrame):
    if data is not None:
        prediction = model.predict(data)
        response = {"prediction": f"{int(prediction[0]):.2f}", "error": None}
        return response

    return {"prediction": None, "error": "Please fill required_fields"}
