import os
from layers.prompt_layer import PromptLayer
import time
import sys
from dotenv import load_dotenv
from services.ollama_services import ollama_client, check_url

load_dotenv()

# Chat-capable model
BASE_MODEL = os.getenv("OLLAMA_MODEL")
BASE_URL = os.getenv("OLLAMA_URL")

# Intro
intro = [
    {"role": "system", "content": "Your are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

def main():
    try:
        if not check_url(BASE_URL):
            sys.exit()
        
        client = ollama_client(BASE_URL)
        print("AI Chat bot has started, press Ctrl+C to exit")
        reply = client.chat(model=BASE_MODEL, messages=intro)
        print("Bot: ", reply.message.content)
        time.sleep(1)
        while True:
            PromptLayer(client, BASE_MODEL)
        
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Exiting out.")
        sys.exit(0)

if __name__ == "__main__":
    # First Response
    main()