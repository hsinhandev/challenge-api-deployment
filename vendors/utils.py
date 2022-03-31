PREDICTQUERY_EXAMPLE = """
    {
        "data": {
            "area": int,
            "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
            "rooms-number": int,
            "zip-code": int,
            "land-area": Optional[int],
            "garden": Optional[bool],
            "garden-area": Optional[int],
            "equipped-kitchen": Optional[bool],
            "full-address": Optional[str],
            "swimming-pool": Optional[bool],
            "furnished": Optional[bool],
            "open-fire": Optional[bool],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional[
                "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
            ],
        }
    }
    """

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
