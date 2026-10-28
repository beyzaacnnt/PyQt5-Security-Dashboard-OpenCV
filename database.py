import sqlite3

class DatabaseManager:
    def __init__(self, db_name="security_logs.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS access_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_name TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                access_status TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def log_access(self, person_name, status="GRANTED"):
        self.cursor.execute("INSERT INTO access_logs (person_name, access_status) VALUES (?, ?)", (person_name, status))
        self.conn.commit()

    def close(self):
        self.conn.close()
