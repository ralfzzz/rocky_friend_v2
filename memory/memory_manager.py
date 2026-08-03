from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory


class MemoryManager:

    def __init__(self):

        self.short = ShortMemory()

        self.long = LongMemory()

    def remember(self, key, value):

        self.long.remember(key, value)

    def recall(self, key):

        return self.long.recall(key)

    def add_chat(self, role, content):

        self.short.add(role, content)

    def history(self):

        return self.short.get()