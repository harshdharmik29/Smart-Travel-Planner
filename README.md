# 🧳 AI-Powered Smart Travel Planner

A simple AI-assisted travel planning app built with **Streamlit**. It recommends destinations based on your **budget** and **trip preferences**, shows **live weather**, and generates a **day-wise itinerary** automatically.

> 🚧 This is an MVP (Minimum Viable Product) built in a single day as a starting point for a larger AI/ML-powered travel planner.

---

## 🚀 Features

- 🌤️ **Live weather lookup** for any city (OpenWeather API)
- 💰 **Budget-based recommendations** from a curated destination dataset
- 🏷️ **Trip type filtering** (Beach, Hill Station, City/Heritage, Adventure)
- 📅 **Auto-generated day-wise itinerary** based on attractions
- 🎯 Simple rule-based scoring (no heavy ML needed for MVP)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI/frontend
- **Pandas** – dataset handling
- **Requests** – OpenWeather API calls

---

## 📂 Project Structure

```
travel-planner/
├── app.py                  # Main Streamlit app
├── weather_engine.py        # Fetches live weather data
├── recommender.py           # Budget-based recommendation logic
├── itinerary_generator.py   # Day-wise itinerary generator
├── data/
│   └── destinations.csv     # Sample destination dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/travel-planner.git
   cd travel-planner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your OpenWeather API key**

   Open `weather_engine.py` and replace:
   ```python
   API_KEY = "YOUR_OPENWEATHER_API_KEY"
   ```
   with your free API key from [openweathermap.org](https://openweathermap.org/api).

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🎯 How It Works

1. Enter a **city** to check live weather conditions.
2. Set your **daily budget** and **preferred trip type** in the sidebar.
3. Choose your **trip duration** (1–7 days).
4. Click **Find Recommendations** to see matching destinations.
5. Expand the **itinerary section** on any destination to see a day-wise plan.

---

## 📊 Sample Dataset

The app ships with a small dataset (`data/destinations.csv`) covering:

| City | Type | Budget Range (₹/day) |
|------|------|------------------------|
| Nagpur | City/Heritage | 800 – 3000 |
| Goa | Beach | 1200 – 6000 |
| Manali | Hill Station | 1000 – 5000 |
| Jaipur | City/Heritage | 900 – 4500 |
| Rishikesh | Adventure | 700 – 3500 |
| Udaipur | City/Heritage | 1100 – 5500 |

You can add more cities by appending rows to this CSV — no code changes required.

---

## 📈 Future Scope

- 🤖 ML-based recommendation engine (collaborative filtering)
- 📊 KMeans clustering for destination grouping
- 🚦 Real-time traffic & crowd prediction
- 💬 Sentiment analysis on hotel/place reviews
- 🗺️ Google Maps route optimization
- 🔔 Real-time weather/price alerts
- 🌐 Multi-language support
- 🎙️ Voice assistant integration

---

## 👨‍💻 Author

**Harsh** | AI/ML Enthusiast | Recommendation Systems
