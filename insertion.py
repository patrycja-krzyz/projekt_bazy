from generators.guests import generate_guests
from generators.attractions import generate_attractions


def table_row_count(cursor, table_name) -> int:
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

def df_to_sql(baza, df, table: str, columns: list[str], batch_size: int):
    rows = [tuple(r) for r in df[columns].to_numpy()]
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


    
