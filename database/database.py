import sqlite3

DB_NAME = "database/memory.db"


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(DB_NAME)

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profile(

                key TEXT PRIMARY KEY,

                value TEXT

            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                category TEXT,

                content TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
        """)

        self.conn.commit()

    def save(self, key, value):

        self.cursor.execute("""

            INSERT OR REPLACE INTO

            user_profile(key,value)

            VALUES(?,?)

        """, (key, value))

        self.conn.commit()

    def get(self, key):

        self.cursor.execute("""

            SELECT value

            FROM user_profile

            WHERE key=?

        """, (key,))

        row = self.cursor.fetchone()

        if row:

            return row[0]

        return None

    def save_memory(self, category, content):

        self.cursor.execute("""

            INSERT INTO memories(category, content)

            VALUES(?,?)

        """, (category, content))

        self.conn.commit()