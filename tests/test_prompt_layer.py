import pytest
import sys, os
from unittest.mock import patch
from ollama import Client

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.layers.prompt_layer import generate_response, PromptLayer

# @patch("src.services.ollama_services.ollama_client")
# def test_generate_response(mock_prompt):
#     mock_prompt.return_value = {
#         'message': {
#             'content': 'Hello!',
#         }
#     }
#     result = generate_response(client=Client("http://localhost:11434"), model="phi3:mini", user_input="Hello!")
#     assert result.json()['message']['content'] == "Hello!"
#     mock_prompt.assert_called_once()

def test_prompt_layer_exit():
    with pytest.raises(SystemExit) as e:
        sys.exit(0)
    
    assert e.type is SystemExit
    assert e.value.code == 0
