from ollama import chat
from core.conversation import Conversation
from core.message import validate_prompt, sanitize_input

def PromptLayer(model):
    """Continue the conversation:"""
    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                break
                
  
            validate_prompt({ "role": "user", "content": user_input })
        except ValueError as e:
                print(f"Error: {e}")
                continue

        conversation = Conversation()
        conversation.add_user(sanitize_input(user_input))
        user_prompt = conversation.serialize()

        response = chat(model=model, messages=user_prompt, stream=False)
        answer = response['message']['content']
        conversation.add_assistant(answer)
        print("Bot: ", answer, end="\n")