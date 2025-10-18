from transformers import pipeline

class IntentRecognizer:
    def __init__(self):
        # Use a classification pipeline (binary/positive/negative for demo);
        # for real intent classification, fine-tune on your own intent data!
        self.classifier = pipeline("text-classification", model="promptsbyesha/NexaConverseAI-IntentModel")
        self.intent_labels = ["greeting", "goodbye", "order_status", "fallback"]

    def predict(self, text: str) -> str:
        result = self.classifier(text)[0]
        label = result['label']
        # Map sentiment/classification output to your intents
        if label == "POSITIVE":
            if any(word in text.lower() for word in ["hello", "hi", "hey"]):
                return "greeting"
            # add more advanced mapping logic for your intents if needed
            return "order_status"
        elif label == "NEGATIVE":
            if any(word in text.lower() for word in ["bye", "goodbye", "see you"]):
                return "goodbye"
            return "fallback"
        else:
            return "fallback"
