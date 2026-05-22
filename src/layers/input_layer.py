from core.message import validate_prompt

def set_prompt(prompt="Enter a value...", type=str) -> str:
    """
    Prompt the user for input
    """
    while True:
        try:
            user_input = input(prompt)
            validate_prompt({ "role": "user", "content": user_input })
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            continue