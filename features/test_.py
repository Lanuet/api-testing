import jsonschema
import requests
from hamcrest import *
from jsonschema import ValidationError

API_URL = "https://dev-pvis.teko.vn/api/branches/"
PARAMS = {
    "DISABLE_SIGN": "2018"
}

SCHEMA = {
    "type": "object",
    "properties": {
        "total": {"type": "integer"},
        "data": {"type": "object"}
    }
}

DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "ma_bp": {"type": "string"},
        "ten_bp": {"type": "string"},
        "ten_bp2": {"type": "string"},
        "ma_pn": {"type": "string"},
        "ksd": {"type": "string"},
        "central": {"type": "string"},
    }
}


def test_validate_schema():
    response = requests.get(API_URL, PARAMS)
    assert_that(response.status_code, equal_to(200))
    _json = requests.get(API_URL, PARAMS).json()
    jsonschema.validate(_json, SCHEMA)
    _data = _json["data"]
    jsonschema.validate(_data, DATA_SCHEMA)
    if _json["total"] != len(_data):
        raise ValidationError("number of branches is not correct")
    for k, v in _data.items():
        if k != v["ma_bp"]:
            raise ValidationError("name != ma_bp")
