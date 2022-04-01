from typing import Optional, Literal, Union
from pydantic import BaseModel, validator, PositiveInt


class PredictQuery(BaseModel):
    living_area: Union[PositiveInt, float]
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
