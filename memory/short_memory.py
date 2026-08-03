class ShortMemory:

    def __init__(self):

        self.messages = []

        self.limit = 10

    def add(self, role, content):

        self.messages.append({

            "role": role,

            "content": content

        })

        if len(self.messages) > self.limit:

            self.messages.pop(0)

    def get(self):

        return self.messages