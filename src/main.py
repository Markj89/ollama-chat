from ollama import chat
from layers.prompt_layer import PromptLayer
import time
import sys

# Chat-capable model
model = "phi3:mini"
old_conversation = []

# Intro
intro = [
    {"role": "system", "content": "Your are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

def main():
    try:
        print("AI Chat bot has started, press Ctrl+C to exit")
        reply = chat(model=model, messages=intro)
        print("Bot: ", reply.message.content)
        time.sleep(1)
        PromptLayer(model)
        
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Exiting out.")
        sys.exit(0)

if __name__ == "__main__":
    # First Response
    main()