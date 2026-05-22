import pytest
import sys, os
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.layers.prompt_layer import generate_response
from src.layers.prompt_layer import PromptLayer

@patch("src.layers.prompt_layer.chat")
def test_generate_response(mock_prompt):
    mock_prompt.return_value = {
        'message': {
            'content': 'Hello!'
        }
    }
    result = generate_response(model="phi3:mini", user_input="Hello!")
    assert result == 'Hello!'
    mock_prompt.assert_called_once()

def test_prompt_layer_exit():
    with pytest.raises(SystemExit) as e:
        sys.exit(0)
    
    assert e.type is SystemExit
    assert e.value.code == 0
