import pandas as pd
import joblib
from pydantic import ValidationError
from vendors.schema import PredictQuery


model_columns = joblib.load("model/model_columns.pkl")
dummies_field = ("property_type", "post_code", "property_sub_type", "region")
kitchen_type_map = {
    "USA uninstalled": 0,
    "Not installed": 0,
    "Installed": 1,
    "USA installed": 1,
    "Semi equipped": 1,
    "USA semi equipped": 1,
    "Hyper equipped": 2,
    "USA hyper equipped": 2,
}
building_condition_map = {
    "As new": 6,
    "Just renovated": 5,
    "Good": 4,
    "To be done up": 3,
    "To renovate": 2,
    "To restore": 1,
}


def preprocess(query: dict):
    try:
        _query = PredictQuery(**query)
        df = pd.DataFrame(dict(_query), index=[0])
        df.replace({False: 0, True: 1}, inplace=True)
        df = df.replace(
            {
                "kitchen_type": kitchen_type_map,
                "building_condition": building_condition_map,
            }
        )

        df = pd.get_dummies(
            df, columns=[c for c in df.columns.tolist() if c in dummies_field]
        )

        df = df.reindex(columns=model_columns, fill_value=0)
        return {"prediction": df, "error": None}

    except ValidationError as e:
        response = ""
        for err in e.errors():
            field = err["loc"][0]
            message = err["msg"]
            response = f"{response}Missing field {field}: {message}."
        return {"prediction": None, "error": response}
