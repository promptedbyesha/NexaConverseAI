# type: ignore
from typing import Dict, List
from transformers import pipeline

class EntityExtractor:
    def __init__(self):
        # Load a robust NER pipeline (supports English, fine-tuned on CoNLL03)
        
        self.ner = pipeline(
            "ner",
            model="dbmdz/bert-large-cased-finetuned-conll03-english",
            aggregation_strategy="simple"
        )

    def extract(self, text: str) -> Dict[str, List[str]]:
        results = self.ner(text)
        entities = {}
        for entity in results:
            label = entity['entity_group']
            value = entity['word']
            if label not in entities:
                entities[label] = []
            entities[label].append(value)
        return entities
