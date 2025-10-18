import json

def load_json_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json_file(data, filepath: str):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)