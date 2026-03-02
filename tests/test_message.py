import pytest
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.core.message import validate_prompt

def test_validate_prompt_is_valid():
    conversation = { "role": "user", "content": "Hello!" }
    assert validate_prompt(conversation) is True

def test_validate_prompt_is_invalid():
    with pytest.raises(ValueError):
        validate_prompt({ "role": "user", "content": "" })

    