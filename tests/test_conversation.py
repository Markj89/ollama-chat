import pytest
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from src.core.conversation import Conversation

def test_conversation_add_user():
    conversation = Conversation()
    conversation.add_user("What is the the capitol of Illinois?")
    assert conversation.serialize() == [{"role": "user", "content": "What is the the capitol of Illinois?"}]