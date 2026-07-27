class PromptBuilder:

    def __init__(self):

        self.cached_system = None

        self.cached_profile = None

    def update_system(self, text):

        self.cached_system = text

    def update_profile(self, text):

        self.cached_profile = text

    def build(self, history):

        messages = [

            {

                "role":"system",

                "content":self.cached_system

            }

        ]

        if self.cached_profile:

            messages.append({

                "role":"system",

                "content":self.cached_profile

            })

        messages.extend(history)

        return messages