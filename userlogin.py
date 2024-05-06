import sqlite3
class UserLogin:
    def __init__(self, connection):
        self.connection = connection

    def login(self, username, password):
        try:
            self.connection.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = self.connection.cursor.fetchone()
            if user:
                print("Login successful!")
                return username
            else:
                print("Invalid username or password.")
                return False
        except sqlite3.Error as e:
            print(f"Error authenticating user: {e}")
            return False