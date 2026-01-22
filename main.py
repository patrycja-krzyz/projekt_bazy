from budowa import Baza
from budowa import create_db
from insertion import insert_guests, insert_attractions




baza = Baza()



baza.stworz_tabele()

# baza.show_tables()


# baza.clear_table("guests")

insert_guests(baza)
insert_attractions(baza)

baza.show_table("attractions")




baza.zamknij_polaczenie()