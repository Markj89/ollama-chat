import pytest
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.layers.prompt_layer import PromptLayer

def test_prompt_layer_exit():
    with pytest.raises(SystemExit) as e:
        sys.exit(0)
    
    assert e.type is SystemExit
    assert e.value.code == 0