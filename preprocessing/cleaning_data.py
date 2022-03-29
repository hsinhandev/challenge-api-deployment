from typing import Dict
import pandas as pd
import joblib
from flask import jsonify

required_fields = (
    "living_area",
    "property_type",
    "bedrooms",
    "post_code",
)
model_columns = joblib.load("model/model_columns.pkl")
dummies_field = ("property_type", "post_code", "property_sub_type", "region")


def preprocess(query: Dict):
    is_input_valid = all(query.get(key) is not None for key in required_fields)

    if not is_input_valid:
        raise ValueError("Invalid input")
        return jsonify(message=f"Please fill required_fields"), 400

    df = pd.get_dummies(pd.DataFrame([query]), columns=["property_type", "post_code"])
    df = df.reindex(columns=model_columns, fill_value=0)
    # df.to_csv("output.csv")

    return df
