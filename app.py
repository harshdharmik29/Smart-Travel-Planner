"""
app.py
AI-Powered Smart Travel Planner - Streamlit MVP
Takes user input (city, budget, trip type, duration), fetches live weather,
recommends destinations from a small dataset, and generates a day-wise itinerary.
"""

import streamlit as st
from weather_engine import get_weather
from recommender import load_destinations, recommend_destinations, get_budget_label
from itinerary_generator import generate_itinerary

st.set_page_config(page_title="AI Smart Travel Planner", page_icon="🧳", layout="wide")

# ----------------- Helper: icons -----------------
TYPE_ICONS = {
    "City/Heritage": "🏛️",
    "Beach": "🏖️",
    "Hill Station": "⛰️",
    "Adventure": "🧗",
}

BUDGET_COLORS = {
    "Budget": "🟢",
    "Mid-range": "🟡",
    "Luxury": "🔵",
}


def weather_icon(condition: str) -> str:
    condition = condition.lower()
    if "rain" in condition:
        return "🌧️"
    if "cloud" in condition:
        return "☁️"
    if "clear" in condition:
        return "☀️"
    if "snow" in condition:
        return "❄️"
    if "thunder" in condition:
        return "⛈️"
    if "mist" in condition or "fog" in condition or "haze" in condition:
        return "🌫️"
    return "🌤️"


# ----------------- Header -----------------
st.title("🧳 AI-Powered Smart Travel Planner")
st.caption("Personalized trip suggestions based on weather, budget & preferences")

# ----------------- Sidebar Inputs -----------------
st.sidebar.header("✈️ Plan Your Trip")

city_input = st.sidebar.text_input("📍 City to check weather", value="Nagpur")

budget_input = st.sidebar.number_input(
    "💰 Your daily budget (₹)", min_value=200, max_value=10000, value=1000, step=100
)

trip_type = st.sidebar.selectbox(
    "🎯 Preferred trip type",
    ["Any", "City/Heritage", "Beach", "Hill Station", "Adventure"]
)

num_days = st.sidebar.slider("📅 Trip duration (days)", min_value=1, max_value=7, value=3)

search_clicked = st.sidebar.button("🔍 Find Recommendations", use_container_width=True)

# ----------------- Weather Section -----------------
st.subheader("🌤️ Current Weather")

if city_input:
    weather = get_weather(city_input)
    if weather:
        icon = weather_icon(weather["condition"])
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(f"{icon} Condition", weather["condition"].title())
        col2.metric("🌡️ Temperature", f"{weather['temperature']} °C")
        col3.metric("🤔 Feels Like", f"{weather['feels_like']} °C")
        col4.metric("💧 Humidity", f"{weather['humidity']}%")
    else:
        st.warning("⚠️ Could not fetch live weather. Add your API key in weather_engine.py")

st.divider()

# ----------------- Recommendations Section -----------------
st.subheader("📍 Recommended Destinations")

if search_clicked:
    df = load_destinations("data/destinations.csv")
    preferred = None if trip_type == "Any" else trip_type
    results = recommend_destinations(df, budget_input, preferred)

    if results.empty:
        st.info("No destinations found matching your budget. Try increasing it.")
    else:
        for _, row in results.iterrows():
            label = get_budget_label(budget_input, row)
            type_icon = TYPE_ICONS.get(row["type"], "📍")
            budget_icon = BUDGET_COLORS.get(label, "")

            with st.container(border=True):
                left, right = st.columns([2, 1])

                with left:
                    st.markdown(f"### {type_icon} {row['city']}, {row['state']}")
                    st.write(f"**Type:** {row['type']}")
                    st.write(f"**Best time to visit:** {row['best_months']}")
                    st.write(f"**Attractions:** {row['attractions']}")

                with right:
                    st.metric("Match Score", f"{min(row['budget_fit'], 100):.0f}/100")
                    st.write(f"**Budget fit:** {budget_icon} {label}")
                    st.write(f"**Daily range:** ₹{row['budget_low']} – ₹{row['budget_high']}")
                    st.progress(min(int(row['budget_fit']), 100))

                with st.expander(f"📅 View {num_days}-Day Itinerary for {row['city']}"):
                    itinerary = generate_itinerary(row['city'], row['attractions'], num_days)
                    for day_plan in itinerary:
                        st.markdown(f"**Day {day_plan['day']}:** {day_plan['plan']}")
else:
    st.write("👈 Set your preferences in the sidebar and click **Find Recommendations**.")