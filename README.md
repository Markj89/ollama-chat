# Ollama Chat

A local CLI Ollama Chatbot where the user can send prompts to the LLM based on their choice and stream responses. The chat also maintains conversation history.

## Architecture

The system includes:
- **Ollama**

## Quick Start

### Local Development Setup
This project currently uses ollama phi3:mini as an example

1. Go to your Terminal and create the Virtual Environment:
    ```
    # Create the virtual environment
   python -m venv ollama-env
   source ollama-env/bin/activate
   ollama serve
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run app.py:
    ```
    py (or python/python3) app.py


This will change to uvicorn in later iterations.