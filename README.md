# AI-Powered Smart Travel Planner

🔗 **Live Demo:** [smart-travel-planner123.streamlit.app](https://smart-travel-planner123.streamlit.app/)

A travel planning web app built with Python and Streamlit...

A travel planning web app built with Python and Streamlit. It suggests destinations based on your daily budget and trip preferences, shows live weather for any city, and generates a day-wise itinerary automatically.

This is a working prototype (MVP) — built as the first version of a larger AI/ML based travel planning system.

## Features

- Live weather lookup using the OpenWeather API
- Destination recommendations based on budget and trip type
- Day-wise itinerary generation based on top attractions
- Simple scoring system to rank destinations by how well they fit the user's budget

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests (OpenWeather API)

## Project Structure

```
Smart-Travel-Planner/
├── app.py                  
├── weather_engine.py        
├── recommender.py           
├── itinerary_generator.py   
├── data/
│   └── destinations.csv
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository
```
git clone https://github.com/harshdharmik29/Smart-Travel-Planner.git
cd Smart-Travel-Planner
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Add your OpenWeather API key in `weather_engine.py`
```python
API_KEY = "your_api_key_here"
```
You can get a free key from openweathermap.org.

4. Run the app
```
streamlit run app.py
```

## How it works

- Enter a city to check the current weather
- Set your daily budget, preferred trip type, and number of days in the sidebar
- Click "Find Recommendations" to view matching destinations
- Expand the itinerary section on any destination to see a day-by-day plan

## Sample Destinations

The app currently includes a small dataset covering Nagpur, Goa, Manali, Jaipur, Rishikesh, and Udaipur. More destinations can be added by editing `data/destinations.csv` — no code changes needed.

## Future Improvements

- ML-based recommendation engine
- Clustering for destination grouping
- Traffic and crowd prediction
- Review sentiment analysis
- Map-based route suggestions
- Multi-language support

## Author

Harsh Dharmik