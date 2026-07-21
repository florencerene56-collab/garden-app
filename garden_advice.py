"""
garden_advice.py

Prints gardening advice based on a hardcoded season and plant type.
The plant type block gives fertilizer and pest control advice.
The season block gives water and weather advice.
All advice will be a string and printed in the console.
"""


def get_advice(season, plant_type):
    """Return combined gardening advice for a season and plant type."""
    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


# values are hardcoded for season and plant type
season = "summer"
plant_type = "flower"

# Get advice and print it
print(get_advice(season, plant_type))
