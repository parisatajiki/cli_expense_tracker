import json

def read_json(filename, default_value):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return default_value

def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
