from typing import List, Dict

class IntentRecognizer:
    def __init__(self, model=None):
        # model: Placeholder for transformer, spaCy, or rule-based; can be swapped out
        self.model = model
        self.intent_labels = ["greeting", "goodbye", "order_status", "fallback"]

    def predict(self, text: str) -> str:
        # Placeholder: Replace with model inference logic
        # Example rule: just for placeholder, returns fallback for unknown
        lowered = text.lower()
        if any(greet in lowered for greet in ["hello", "hi", "hey"]):
            return "greeting"
        elif any(bye in lowered for bye in ["bye", "goodbye", "see you"]):
            return "goodbye"
        elif "order" in lowered or "status" in lowered:
            return "order_status"
        else:
            return "fallback" # For unknowns, out-of-distribution, etc.
