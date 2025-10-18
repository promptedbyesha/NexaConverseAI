def should_engage(history: list) -> bool:
    # Placeholder: Engage if conversation stalls (>3 turns with fallback)
    if len(history) >= 3 and all(x['intent'] == "fallback" for x in history[-3:]):
        return True
    return False
