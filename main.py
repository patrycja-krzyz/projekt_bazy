from budowa import Baza
from budowa import create_db
from insertion import insert_data


baza = Baza()
baza.reset_db()
baza = Baza()


baza.stworz_tabele()
insert_data(baza)

baza.zamknij_polaczenie()