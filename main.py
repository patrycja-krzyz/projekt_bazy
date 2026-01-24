from budowa import Baza
from budowa import create_db
from insertion import insert_guests, insert_attractions, insert_prices, insert_payments




baza = Baza()



baza.stworz_tabele()

# baza.show_tables()


# baza.clear_table("prices")
# baza.clear_truncate_table("payment_ticket")
# baza.clear_truncate_table("payments")
insert_guests(baza)
insert_attractions(baza)
insert_prices(baza)
insert_payments(baza)

# baza.show_table("payments")
# baza.show_table("payment_ticket")
baza.count_table("payment_ticket")

baza.cursor.execute("""
    SELECT COUNT(DISTINCT payment_id)
    FROM payment_ticket
""")

(count,) = baza.cursor.fetchone()
print(count)
# baza.show_table("attractions")




baza.zamknij_polaczenie()