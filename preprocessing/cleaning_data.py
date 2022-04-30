import pandas as pd
import joblib
from pydantic import ValidationError
from vendors.schema import PredictQuery
from vendors.utils import dummies_field, kitchen_type_map, building_condition_map

model_columns = joblib.load("model/model_columns.pkl")


def preprocess(payload: dict):
    try:
        _query = PredictQuery(**payload)
    except ValidationError as e:
        response = []
        for err in e.errors():
            field = err["loc"][0]
            message = err["msg"]
            response.append({"field": field, "message": message})
        return {"prediction": None, "error": response}
    else:
        df = pd.DataFrame(dict(_query), index=[0])
        df.replace({False: 0, True: 1}, inplace=True)
        df = df.replace(
            {
                "kitchen_type": kitchen_type_map,
                "building_condition": building_condition_map,
            }
        )

        df = pd.get_dummies(
            df, columns=df.columns.intersection(dummies_field).to_list()
        )
        df = df.reindex(columns=model_columns, fill_value=0)

    return {"prediction": df, "error": None}
