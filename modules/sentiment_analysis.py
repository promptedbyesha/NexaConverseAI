class SentimentAnalyzer:
    def __init__(self, model=None):
        self.model = model

    def analyze(self, text: str) -> str:
        # Placeholder for real sentiment model
        neg = ["bad", "angry", "frustrated"]
        if any(word in text.lower() for word in neg):
            return "negative"
        return "positive"
