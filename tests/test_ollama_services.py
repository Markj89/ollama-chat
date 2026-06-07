import pytest
import sys, os
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.services.ollama_services import check_url

# @patch("src.services.ollama_services")
def test_ollama_services():
    result = check_url("http://localhost:11434/api/chat")
    assert result == False
