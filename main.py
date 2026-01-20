import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haslo_maslo67",
    database = "AiBtcQuantLandia"
)

cursor = con.cursor()

#tworzenie tabel
with open("budowa1.sql", "r", encoding="utf-8") as f:
    komendy = f.read()
for komenda in komendy.split(';'): #rozdzielam komendy
    komenda = komenda.strip()
    if komendy:
        cursor.execute(komenda)

con.commit()