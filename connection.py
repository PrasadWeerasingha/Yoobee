import sqlite3

class Connection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite DB: {e}")



    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection to database closed.")

