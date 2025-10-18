def handle_input(input_data):
    # Support text input for now
    if isinstance(input_data, str):
        return {"type": "text", "content": input_data}
    # Extend for voice/image/video later
    return {"type": "unsupported", "content": None}