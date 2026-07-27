from database.database import Database


class LongMemory:

    def __init__(self):

        self.db = Database()

    def remember(self, key, value):

        self.db.save(key, value)

    def recall(self, key):

        return self.db.get(key)