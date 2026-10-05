import json

def open_json(filename: str) -> dict[str, Any]:
    data: dict = {}
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
