import pytest
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.layers.input_layer import set_prompt

def test_set_prompt(monkeypatch):
    test_input = iter(['Hello!'])
    monkeypatch.setattr('builtins.input', lambda _: next(test_input))

    result = set_prompt()
    assert result == "Hello!"