from core.conversation import Conversation
from core.message import sanitize_input
from layers.input_layer import set_prompt

def PromptLayer(client, model) -> list[dict]:
    """Continue the conversation:"""
    user_input = set_prompt("You: ", type=str)
    answer = generate_response(client=client, model=model, user_input=user_input)
    print("Bot: ", answer, end="\n")

def generate_response(client, model, user_input) -> list[dict]:
    conversation = Conversation()
    conversation.add_user(sanitize_input(user_input))
    user_prompt = conversation.serialize()
    response = client.chat(model=model, messages=user_prompt, stream=False)
    answer = response['message']['content']
    conversation.add_assistant(answer)
    return answer
