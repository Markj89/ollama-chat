# conftest.py
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_ollama_chat(mocker):
    # Setup your mock here
    return mocker.patch('src.layers.prompt_layer.generate_response', return_value={"role": "user", 'content': 'Hello!'})
