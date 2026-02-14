class Conversation:
    def __init__(self):
        self.message = []

    def add_user(self, content: str) -> str:
        self.message.append({ "role": "user", "content": content })

    def add_assistant(self, content: str) -> list[dict]:
        self.message.append({ "role": "assistant", "content": content })

    def serialize(self) -> list[dict]:
        return self.message