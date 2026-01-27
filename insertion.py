from generators.guests import generate_guests
from generators.attractions import generate_attractions
from generators.prices import generate_prices
from generators.payments import generate_payments, generate_payment_ticket
from generators.incident_type import generate_incident_types
from generators.incidents import generate_incidents
from generators.insuranse import generate_guest_insurance, generate_insurance
from generators.employees import generate_employees
from generators.costs import generate_costs
from generators.malfunctions import generate_malfunctions
from generators.inspections import generate_inspections


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

def df_to_sql(baza, df, table: str, columns: list[str], batch_size: int = 100):
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

def insert_insurance(baza):

    insurance = generate_insurance()
    guest_insurance = generate_guest_insurance(baza)


    if table_row_count(baza.cursor, "insurance") > 0:
        print("Insurance table already has data. Skipping insertion.")
    else:
        df_to_sql(baza,
                  insurance,
                  "insurance",
                  columns= ["name", "coverage_amount"])
        
    if table_row_count(baza.cursor, "guest_insurance") > 0:
        print("Guest_insurance table already has data. Skipping insertion.")
    else:
        df_to_sql(baza,
                  guest_insurance,
                  "guest_insurance",
                  columns=["guest_id", "insurance_id"])
    

def insert_employees(baza, min_salary, max_salary, number_of_months):
    if table_row_count(baza.cursor, "employees") > 0:
        print("Employees table already has data. Skipping insertion")
        return
    
    employees = generate_employees(baza, min_salary, max_salary, number_of_months)

    df_to_sql(baza,
              employees,
              "employees",
              ["first_name", "last_name", "position", "salary", "hire_date", "attraction_id"])
    
def insert_costs(baza, min_amount, max_amount):
    if table_row_count(baza.cursor, "costs") > 0:
        print("Costs table already has data. Skipping insertion")
        return
    
    costs = generate_costs(baza, min_amount, max_amount)

    df_to_sql(baza,
              costs,
              "costs",
              ["cost_type", "amount", "how_often", "attraction_id"])

def insert_malfunctions(baza, possible_malfunctions_per_attraction, min_amount, max_amount, max_days_to_fix):
    if table_row_count(baza.cursor, "malfunctions") > 0:
        print("Malfunctions table already has data. Skipping insertion")
        return
    
    malfunctions = generate_malfunctions(baza, possible_malfunctions_per_attraction, min_amount, max_amount, max_days_to_fix)

    df_to_sql(baza,
              malfunctions,
              "malfunctions",
              ["attraction_id", "accident_date", "fix_date", "comment", "fix_cost"])
    
def insert_inspections(baza, num):
    if table_row_count(baza.cursor, "inspections") > 0:
        print("Inspections table already has data. Skipping insertion")
        return
    
    inspections = generate_inspections(baza, num)

    df_to_sql(baza,
              inspections,
              "inspections",
              ["attraction_id", "inspection_date", "result"])

def insert_data(baza):
    insert_guests(baza)
    insert_attractions(baza)
    insert_prices(baza)
    insert_payments(baza)
    insert_incident_types(baza)
    insert_incidents(baza, 50)
    insert_insurance(baza)
    insert_employees(baza, 5000, 7000, 6)
    insert_costs(baza, 20000, 30000)
    insert_malfunctions(baza, 3, 2000, 20000, 30)
    insert_inspections(baza, 200)