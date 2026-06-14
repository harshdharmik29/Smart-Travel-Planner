"""
itinerary_generator.py
Generates a simple day-wise itinerary by distributing a destination's
attractions across the number of days the user is travelling.
This is template-based (no ML) - good enough for an MVP demo.
"""


def generate_itinerary(city: str, attractions: str, num_days: int) -> list:
    """
    Splits the attractions (comma-separated string) across num_days
    and returns a list of dicts: [{"day": 1, "plan": "..."}]
    """
    # Clean and split attraction list
    attraction_list = [a.strip() for a in attractions.split(",") if a.strip()]

    if not attraction_list:
        return [{"day": i + 1, "plan": f"Explore {city} at your own pace."} for i in range(num_days)]

    itinerary = []
    total = len(attraction_list)

    # Distribute attractions evenly across days
    per_day = max(1, -(-total // num_days))  # ceiling division

    for day in range(num_days):
        start = day * per_day
        chunk = attraction_list[start:start + per_day]

        if chunk:
            plan = f"Visit {', '.join(chunk)}."
        else:
            plan = f"Free day - relax, local food tour, or revisit favorite spots in {city}."

        # Add a generic morning/evening template touch
        if day == 0:
            plan = f"Arrival in {city}. " + plan + " Check into hotel and rest in the evening."
        elif day == num_days - 1:
            plan = plan + " Pack up and depart in the evening."

        itinerary.append({"day": day + 1, "plan": plan})

    return itinerary
