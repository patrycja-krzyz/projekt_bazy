import sqlite3

class Baza:
    def __init__(self):
        self.con = sqlite3.connect("park.db") #jeśli baza nie istnieje, to ją utworzy w pracującym folderze
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS attractions (
            attraction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            attraction_name TEXT,
            built_date TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usage (
            usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
            attraction_id INTEGER,
            FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accident (
            accident_id INTEGER PRIMARY KEY AUTOINCREMENT,
            accident_date TEXT,
            fix_date TEXT,
            comment TEXT
        )
        """)

        self.con.commit()

    def zamknij(self):
        self.con.close()
        self.cursor.close()
