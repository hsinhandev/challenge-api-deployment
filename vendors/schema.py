from typing import Optional, Literal
from pydantic import BaseModel, validator, PositiveInt


class PredictQuery(BaseModel):
    living_area: PositiveInt
    property_type: Literal["APARTMENT", "HOUSE"]
    post_code: int
    bedrooms: PositiveInt
    has_garden: Optional[bool] = False
    garden_surface: Optional[PositiveInt] = 0
    kitchen_type: Optional[
        Literal[
            "USA uninstalled",
            "Not installed",
            "Installed",
            "USA installed",
            "Semi equipped",
            "USA semi equipped",
            "Hyper equipped",
            "USA hyper equipped",
        ]
    ] = "Not installed"
    has_swimming_pool: Optional[bool] = False
    has_furnished: Optional[bool] = False
    has_terrace: Optional[bool] = False
    terrace_surface: Optional[PositiveInt] = 0
    frontages: Optional[PositiveInt] = 0
    building_condition: Optional[
        Literal[
            "As new", "Just renovated", "To be done up", "To renovate", "To restore"
        ]
    ] = "To renovate"

    @validator("post_code")
    @classmethod
    def post_code_valid(cls, value):
        if len(str(value)) != 4:
            raise ValueError(
                "⚠️ This postal code doesn't belongs to Belgium. It must be 4 digits"
            )
        return value


# from pydantic import ValidationError

# try:
#     external_data = {
#         "living_area": 20,
#         "property_type": "HOUSE",
#         "post_code": "1000",
#         "bedrooms": 2,
#         "building_condition": "As new",
#         "region": "Brussels",
#     }
#     query = PredictQuery(**external_data)
#     print(f"{query = }")
# except ValidationError as e:
#     for err in e.errors():
#         field = err["loc"][0]
#         message = err["msg"]
#         print(f"Missing field {field}: {message}")
