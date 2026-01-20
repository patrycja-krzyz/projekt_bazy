import mysql.connector


class Baza:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "haslo_maslo67",
            database = "AiBtcQuantLandia"
            )
        self.cursor = self.con.cursor()

    def zamknij_polaczenie(self):
        self.cursor.close()
        self.con.close()

    def stworz_tabele(self):
        with open("szkielet.sql", "r", encoding="utf-8") as f:
            komendy = f.read()
        for komenda in komendy.split(';'): #rozdzielam komendy
            komenda = komenda.strip()
            if komenda:
                self.cursor.execute(komenda)
        self.con.commit()


    #tu dodawanie danych???
