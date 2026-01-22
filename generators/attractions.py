import random
import pandas as pd
from .generate_dates import generate_date

ADJECTIVES = [
    "Wild", "Extreme", "Mighty", "Dark", "Golden", "Frozen", "Hidden", "Lost",
    "Epic", "Silent", "Rapid", "Furious", "Electric", "Infinite", "Savage",
    "Ancient", "Mystic", "Secret", "Burning", "Stormy", "Twisted", "Flying",
    "Raging", "Phantom", "Shadowy", "Crimson", "Icy", "Blazing", "Roaring",
    "Iron", "Steel", "Cosmic", "Brave", "Legendary", "Massive", "Rapid",
    "Glorious", "Savage", "Broken", "Cursed", "Haunted", "Thunderous",
    "Shattered", "Celestial", "Solar", "Lunar", "Obsidian", "Vicious",
    "Feral", "Grim", "Fearless", "Endless", "Savage", "Frozen", "Infernal",
    "Vortex", "Turbo", "Steep", "Colossal", "Whispering", "Shining",
    "Ruthless", "Chaotic", "Hidden", "Final", "Eternal", "Reckless",
    "Electric", "Stormborn", "Gravity", "Dangerous", "Unholy", "Sacred",
    "Swift", "Midnight", "Neon", "Blinding", "Titanic", "Merciless",
    "Savage", "Radiant", "Volcanic", "Astral", "Darkened", "Savage"
]
NOUNS = [
    "Ride", "Coaster", "Drop", "Fall", "Storm", "Fury", "Twister", "Loop",
    "Tunnel", "Track", "Cliff", "Spiral", "Rush", "Edge", "Peak", "Plunge",
    "Vortex", "Flight", "Rocket", "Tower", "Canyon", "Wave", "Inferno",
    "Maze", "Labyrinth", "Cyclone", "Whirl", "Beast", "Dragon", "Phantom",
    "Shadow", "Blade", "Machine", "Engine", "Pulse", "Strike", "Force",
    "Velocity", "Gravity", "Orbit", "Galaxy", "Void", "Abyss", "Rift",
    "Crash", "Surge", "Breaker", "Thunder", "Rampage", "Fallout", "Zone",
    "Core", "Sector", "Gate", "Portal", "Chasm", "Reactor", "Spike",
    "Dash", "Rush", "Claw", "Fang", "Howl", "Roar", "Skull", "Ember",
    "Ash", "Flame", "Spark", "Volt", "Stormfront", "Dropzone", "Summit",
    "Drift", "Vault", "Pit", "Track", "Crossing", "Run", "Strike"
]


def generate_attractions(num, adjectives=ADJECTIVES, nouns=NOUNS) -> pd.DataFrame:

    dates = []
    for i in range(num):
        year = random.randint(2000, 2020)
        date = generate_date(year=year)
        dates.append(date)
        dates.append(date)

    names = []
    for i in range(num):
        random_name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        names.append(random_name)
        names.append(random_name)  

    if_vr = []
    for i in range(num):
        if_vr.append(True)
        if_vr.append(False)

    dataframe_attractions = pd.DataFrame({
        "attraction_name": names,
        "vr": if_vr,
        "built_date": dates
        
        })

    return dataframe_attractions

