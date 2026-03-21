import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

        self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL)
                        ''')

    def save(self, score):
        self.conn.execute('INSERT INTO data (name, score, date) VALUES (:name,:score,:date)', score)
        self.conn.commit()

    def show_results(self) -> list:
        return self.conn.execute('SELECT * FROM data ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.conn.close()