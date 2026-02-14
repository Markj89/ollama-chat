import re

def validate_prompt(conversation: list[dict]) -> bool:
    if not conversation["content"].strip():
        raise ValueError("Did you forget something? make sure to add your prompt")
    
    return True

def sanitize_input(user_input):
    return re.sub(r'[^a-zA-Z0-9]', '', user_input)