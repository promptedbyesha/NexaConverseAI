from typing import Dict, List

class EntityExtractor:
    def __init__(self, model=None):
        self.model = model

    def extract(self, text: str) -> Dict[str, str]:
        # Placeholder logic; ready to swap for real entity model
        output = {}
        if "order" in text.lower():
            output["entity"] = "order"
        # Plug ML model or spaCy here in future
        return output
