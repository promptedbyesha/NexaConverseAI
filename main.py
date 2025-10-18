from fastapi import FastAPI, Query
from modules.intent_recognition import IntentRecognizer
from modules.entity_extraction import EntityExtractor
from modules.sentiment_analysis import SentimentAnalyzer
from modules.dialogue_manager import DialogueManager

app = FastAPI()

# Instantiate modules globally for reuse/context
intent_model = IntentRecognizer()
entity_model = EntityExtractor()
sentiment_model = SentimentAnalyzer()
dialogue_manager = DialogueManager(intent_model, entity_model, sentiment_model)

@app.get("/")
async def home():
    return {"message": "Welcome to NexaConverse AI!"}

@app.post("/chat")
async def chat(user_input: str = Query(...)):
    response = dialogue_manager.handle_conversation(user_input)
    return {"response": response}
