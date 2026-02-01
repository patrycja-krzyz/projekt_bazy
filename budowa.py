import mysql.connector
from pathlib import Path


class Baza:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "haslo_maslo67",
            database = "AiBtcQuantLandia"
            )
        self.cursor = self.con.cursor(buffered=True)

    def zamknij_polaczenie(self):
        self.cursor.close()
        self.con.close()

    def stworz_tabele(self):
        sql_path = Path(__file__).parent / "szkielet.sql"

        with open(sql_path, "r", encoding="utf-8") as f:
            komendy = f.read()

        for komenda in komendy.split(';'): #rozdzielam komendy
            komenda = komenda.strip()
            if komenda:
                self.cursor.execute(komenda)
        self.con.commit()

    def show_tables(self):
        self.cursor.execute("SHOW TABLES")
        for (table_name,) in self.cursor:
            print(table_name)

    def count_table(self, name):
        self.cursor.execute(f"SELECT COUNT(*) FROM {name}")
        result = self.cursor.fetchone()
        print(result[0])

    def describe_table(self, name):
        self.cursor.execute(f"DESCRIBE {name}")
        for row in self.cursor:
            print(row)

    def show_table(self, name):
        self.cursor.execute(f"SELECT * FROM {name}")
        for row in self.cursor:
            print(row)

    def clear_table(self, name):
        self.cursor.execute(f"DELETE FROM {name}")
        self.con.commit()

    def clear_truncate_table(self, name):
        cur = self.con.cursor() 

        cur.execute("SHOW FULL PROCESSLIST")
        for row in cur.fetchall():
            print(row)
        cur.execute("KILL 151")
        cur.execute("SET FOREIGN_KEY_CHECKS=0")
        cur.execute(f"TRUNCATE TABLE `{name}`")         
        cur.execute("SET FOREIGN_KEY_CHECKS=1")

        self.con.commit()
        cur.close()
    def show_cons(self):
        self.cursor.execute("SHOW FULL PROCESSLIST")
        for row in self.cursor.fetchall():
            print(row)
        self.con.commit()

    def kill_cons(self, *ids):
        for id in ids:
            self.cursor.execute(f"KILL {id}")
        self.con.commit()
    def reset_db(self):

        self.cursor.execute("DROP DATABASE IF EXISTS aibtcquantlandia")
        self.cursor.execute("CREATE DATABASE aibtcquantlandia")
        self.cursor.execute("USE aibtcquantlandia")





def create_db():
    con0 = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "haslo_maslo67")
    cursor0 = con0.cursor()
    cursor0.execute("""
        CREATE DATABASE IF NOT EXISTS AiBtcQuantLandia
        DEFAULT CHARACTER SET utf8mb4
        DEFAULT COLLATE utf8mb4_polish_ci
    """)
    con0.commit()
    cursor0.close()
    con0.close()

