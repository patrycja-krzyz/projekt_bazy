import pandas as pd
import random


def generate_insurance() -> pd.DataFrame:
    names = ["full insurance", "full children insurance", "partial insurance", "partial children insurance", "senior insurance"]
    amount = [100000, 150000, 50000, 75000, 150000]

    df = pd.DataFrame({
        "name": names,
        "coverage_amount": amount
    })
    return df

def generate_guest_insurance(baza) -> pd.DataFrame:
    guests = pd.read_sql("SELECT guest_id, birth_date FROM guests", con=baza.con)
    insurances = []
    today_year = pd.Timestamp.today().normalize().year
    for row in guests["birth_date"]:
        birth_year = pd.to_datetime(row).year
        age = today_year - birth_year
        if age <= 18:
            insurances.append(random.choice([2, 4]))
        elif age <= 65:
            insurances.append(random.choice([1, 3]))
        else:
            insurances.append(5)
        
    guests["insurance"] = insurances

    df = pd.DataFrame({
        "guest_id": guests["guest_id"],
        "insurance_id": guests["insurance"]
    })

    return df


