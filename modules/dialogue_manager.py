class DialogueManager:
    def __init__(self, intent_recognizer, entity_extractor, sentiment_analyzer):
        self.intent_recognizer = intent_recognizer
        self.entity_extractor = entity_extractor
        self.sentiment_analyzer = sentiment_analyzer
        self.history = []  # Basic conversation memory

    def handle_conversation(self, user_input: str, user_context: dict = None) -> str:
        intent = self.intent_recognizer.predict(user_input)
        entities = self.entity_extractor.extract(user_input)
        sentiment = self.sentiment_analyzer.analyze(user_input)
        self.history.append({"intent": intent, "entities": entities, "sentiment": sentiment, "input": user_input})

        # Branching for demonstration (expandable for business logic/multi-turn):
        if intent == "greeting":
            return "Hi there! How can I assist you today?"
        elif intent == "goodbye":
            return "Goodbye! Have a wonderful day."
        elif intent == "order_status":
            return "Please provide your order number so I can check the status."
        else:
            return "I'm not sure I understand. Can you please clarify?"
