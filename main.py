# pierwszy sposób
from budowa import Baza
import sqlite3

park = Baza()

# do wypróbowania
park.cursor.execute(
    "INSERT INTO attractions (attraction_name, built_date) VALUES (?, ?)",
    ("Rollercoaster", "2009-11-21")
)
park.cursor.execute("SELECT * FROM attractions")
wyniki = park.cursor.fetchall()
for wiersz in wyniki:
    print(wiersz)

# park.zamknij()



# #drugi sposób - wybierzcie sobie który
# import sqlite3

# con = sqlite3.connect("park.db") #jeśli baza nie istnieje, to ją utworzy w pracującym folderze
# cursor = con.cursor()

# with open("budowa2.sql", "r", encoding="utf-8") as f:
#     cursor.executescript(f.read())

# #do wypróbowania
# cursor.execute(
#     "INSERT INTO attractions (attraction_name, built_date) VALUES (?, ?)",
#     ("Rollercoaster", "2009-11-21")
# )
# cursor.execute("SELECT * FROM attractions")
# wyniki = cursor.fetchall()
# for wiersz in wyniki:
#     print(wiersz)


# con.commit()
# cursor.close()
# con.close()