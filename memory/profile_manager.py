from database.database import Database


class ProfileManager:

    def __init__(self, db):

        self.db = db

        self.cache = {}

        self.load_cache()

    def set(self, key, value):

        self.cache[key] = value

        self.db.save(key, value)

    def get(self, key):

        return self.cache.get(key)

    def build_profile(self):

        profile = []

        fields = [

            "name",
            "job",
            "city",
            "language",
            "favorite_language",
            "favorite_food"

        ]

        for field in fields:

            value = self.get(field)

            if value:

                profile.append(f"{field}: {value}")

        return "\n".join(profile)

    def load_cache(self):

        fields = [

            "name",

            "job",

            "city",

            "language",

            "favorite_language",

            "favorite_food"

        ]

        for field in fields:

            value = self.db.get(field)

            if value:

                self.cache[field] = value