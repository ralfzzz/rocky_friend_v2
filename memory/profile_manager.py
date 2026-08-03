from database.database import Database


class ProfileManager:

    def __init__(self):

        self.db = Database()

    def set(self, key, value):

        self.db.save(key, value)

    def get(self, key):

        return self.db.get(key)

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