import sqlite3

class CreateTable:
    def __init__(self, connection):
        self.connection = connection
    #Create User Table
    def create_user_table(self):
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            admin BOOLEAN NOT NULL
        );
        """
        self.connection.cursor.execute(create_users_table_query)
        self.connection.conn.commit()

    # Create Vehicle Table
    def create_vehicle_table(self):
        create_vehicle_table_query = """
        CREATE TABLE IF NOT EXISTS vehicles (
        id             INTEGER   PRIMARY KEY,
        brand          TEXT (20),
        type           TEXT (10),
        makeYear       INTEGER,
        doors          INTEGER,
        price_Per_Week NUMERIC,
        avalability    INTEGER,
        reg_Number     TEXT (10) ,
        bed_length     NUMERIC
        );
            """
        self.connection.cursor.execute(create_vehicle_table_query)
        self.connection.conn.commit()