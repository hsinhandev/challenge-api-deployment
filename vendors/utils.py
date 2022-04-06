import json

PREDICT_QUERY_EXAMPLE = """
    {
        "data": {
                "living_area": "Union[PositiveInt, float]",
                "property_type": "APARTMENT | HOUSE",
                "post_code": "int",
                "bedrooms": "PositiveInt",
                "has_garden": "Optional[bool]",
                "garden_surface": "Optional[PositiveInt]",
                "kitchen_type": "Optional[USA uninstalled | Not installed | Installed | USA installed | Semi equipped | USA semi equipped | Hyper equipped | USA hyper equipped]",
                "has_swimming_pool": "Optional[bool]",
                "has_furnished": "Optional[bool]",
                "has_terrace": "Optional[bool]",
                "terrace_surface": "Optional[PositiveInt]",
                "frontages": "Optional[PositiveInt]",
                "building_condition": "Optional[As new | Just renovated | To be done up | To renovate | To restore]"
        }
    }
    """
PREDICT_QUERY_JSON = json.loads(PREDICT_QUERY_EXAMPLE)

dummies_field = {"property_type", "post_code", "property_sub_type", "region"}
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
