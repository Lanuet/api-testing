import jsonschema
import pytest
import requests
from hamcrest import *
from jsonschema import ValidationError

from support.connect_db import DBConnection

API_URL = "https://dev-pvis.teko.vn/api/branches/"
PARAMS = {
    "DISABLE_SIGN": "2018"
}

SCHEMA = {
    "type": "object",
    "properties": {
        "total": {"type": "integer"},
        "data": {
            "type": "object",
            "properties": {
                "ma_bp": {"type": "string"},
                "ten_bp": {"type": "string"},
                "ten_bp2": {"type": "string"},
                "ma_pn": {"type": "string"},
                "ksd": {"type": "string"},
                "central": {"type": "string"}
            }
        }
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


class TestConfig():
    def setup_module(self):
        pass

    def teardown_module(self):
        pass

    @classmethod
    def setup_class(self):
        pass

    @classmethod
    def teardown_class(self):
        pass

    def __init__(self, db_connection, api_url, params):
        self.api_url = api_url
        self.params = params
        self.db_connection = db_connection

    def setup_method(self):
        print("Setup method")
        self.db = DBConnection(self.db_connection).connect_to_db()
        # self.response = requests.get(API_URL, PARAMS)
        self.response = requests.get(self.api_url, self.params)

    def teardown_method(self):
        print("Teardown method")
        self.db.close()

    def test_validate_schema(self):
        assert_that(self.response.status_code, equal_to(200))
        _json = self.response.json()
        jsonschema.validate(_json, SCHEMA)
        _data = _json["data"]
        jsonschema.validate(_data, DATA_SCHEMA)
        if _json["total"] != len(_data):
            raise ValidationError("number of branches is not correct")
        for k, v in _data.items():
            if k == v["ma_bp"]:
                raise ValidationError("name != ma_bp")

    def test_2(self):
        _json = self.response.json()
        assert _json["total"] == 58

