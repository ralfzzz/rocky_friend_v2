class PromptBuilder:

    def __init__(self, personality, profile, history):

        self.personality = personality

        self.profile = profile

        self.history = history

    def build(self):

        messages = []

        messages.append({

            "role": "system",

            "content": self.personality

        })

        if self.profile:

            messages.append({

                "role": "system",

                "content": "User Profile\n" + self.profile

            })

        messages.extend(self.history)

        return messages