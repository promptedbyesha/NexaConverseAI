import os
from utils.helpers import load_json_file

def load_intents(intents_folder: str):
    intents = []
    for file in os.listdir(intents_folder):
        if file.endswith(".json"):
            path = os.path.join(intents_folder, file)
            data = load_json_file(path)
            intents.extend(data.get("intents", []))
    return intents

def load_entities(entities_folder: str):
    entities = {}
    for file in os.listdir(entities_folder):
        if file.endswith(".json"):
            path = os.path.join(entities_folder, file)
            data = load_json_file(path)
            entities.update(data)
    return entities
