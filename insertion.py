from generators.guests import generate_guests
from generators.attractions import generate_attractions
from generators.prices import generate_prices
from generators.payments import generate_payments, generate_payment_ticket
from generators.incident_type import generate_incident_types
from generators.incidents import generate_incidents


def table_row_count(cursor, table_name) -> int:
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

import numpy as np

def _py(x):
    if x is None:
        return None
    if isinstance(x, np.generic):        # sometimes np data_types are not understandable for sql
        return x.item()
    return x

def df_to_sql(baza, df, table: str, columns: list[str], batch_size: int):
    df = df.where(df.notna(), None)  
    rows = [tuple(map(_py, row)) for row in df.to_numpy()]
    placeholders = ", ".join(["%s"] * len(columns))
    sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"

    for i in range(0, len(rows), batch_size):
        baza.cursor.executemany(sql, rows[i:i+batch_size])
    baza.con.commit()

def insert_guests(baza):
    if table_row_count(baza.cursor, "guests") > 0:
        print("Guests table already has data. Skipping insertion.")
        return
    
    guests = generate_guests(1000)
    
    df_to_sql(
        baza,
        guests,
        table="guests",
        columns=["first_name", "last_name", "birth_date"],
        batch_size=1000
    )

def insert_attractions(baza):
    if table_row_count(baza.cursor, "attractions") > 0:
        print("Attractions table already has data. Skipping insertion.")
        return
    
    attractions = generate_attractions(25)
    
    df_to_sql(
        baza,
        attractions,
        table="attractions",
        columns=["attraction_name", "vr", "built_date"],
        batch_size=50
    )

def insert_prices(baza):
    if table_row_count(baza.cursor, "prices") > 0:
        print("Prices table already has data. Skipping insertion.")
        return
    
    prices = generate_prices(25)

    df_to_sql(
        baza,
        prices,
        table="prices",
        columns=["amount", "attraction_id"],
        batch_size=100
    )

def insert_payments(baza):
    
    
    payments_tickets = generate_payment_ticket(baza)
    payments = generate_payments(baza, payments_tickets)

    if table_row_count(baza.cursor, "payments") > 0:
        print("Payments table already has data. Skipping insertion.")
    else:
        df_to_sql(
            baza,
            payments,
            table="payments",
            columns=["payment_date", "amount", "guest_id"],
            batch_size=len(payments)
        
        )

    if table_row_count(baza.cursor, "payment_ticket") > 0:
        print("Payments_tickets table already has data. Skipping insertion.")
    else:
        df_to_sql(
            baza,
            payments_tickets,
            table="payment_ticket",
            columns=["payment_id", "ticket_id"],
            batch_size=len(payments)
        )


def insert_incident_types(baza):
    if table_row_count(baza.cursor, "incident_type") > 0:
        print("Incident_type table already has data. Skipping insertion.")
        return
    
    incident_types = generate_incident_types()
    
    df_to_sql(
        baza,
        incident_types,
        table="incident_type",
        columns=["name", "risk_level"],
        batch_size=100
    )

def insert_incidents(baza, num):
    if table_row_count(baza.cursor, "incidents") > 0:
        print("Incidents table already has data. Skipping insertion.")
        return
    
    incidents = generate_incidents(baza, num)

    df_to_sql(
        baza, 
        incidents,
        table="incidents",
        columns=["incident_type_id", "guest_id", "attraction_id", "incident_date", "description"],
        batch_size=num
    )

def insert_data(baza):
    insert_guests(baza)
    insert_attractions(baza)
    insert_prices(baza)
    insert_payments(baza)
    insert_incident_types(baza)
    insert_incidents(baza, 50)