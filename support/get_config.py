import json


def load_settings(file_name):
    global settings
    with open(file_name) as f:
        settings = json.load(f)
    return settings
