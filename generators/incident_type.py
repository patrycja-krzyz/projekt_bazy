import pandas as pd

def generate_incident_types() -> pd.DataFrame:
    data = {
        "name": [
        "Mechanical failure",
        "Electrical malfunction",
        "Software system error",
        "Operator mistake",
        "Safety system failure",
        "Fire hazard",
        "Power outage",
        "Minor equipment damage",
        "Structural instability",
        "Emergency evacuation"
        ],
        "risk_level": [5, 4, 3, 3, 5, 5, 2, 1, 4, 5]
    }

    df_incident_type = pd.DataFrame(data)
    return df_incident_type