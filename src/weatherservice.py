"""
User Stories:
  1. User can search for the city and see the corresponding weather forecast of the day
  2. User can search by location coordinates and see the corresponding weather forecast of the day.
  3. User can input no. of days for the next weather forecast
"""


class WeatherService:
    def __init__(self):
        self.weather_data = {
        "Örebro": [
            {"temp": 2, "condition": "Cloudy"},
            {"temp": 7, "condition": "Rainy"},
            {"temp": 8, "condition": "Cloudy"},
            {"temp": 11, "condition": "Cloudy"},
            {"temp": 11, "condition": "Sunny"},
            {"temp": 9, "condition": "Partly Sunny"},
            {"temp": 10, "condition": "Sunny"},
        ],

        "Gothenburg": [
            {"temp": 5, "condition": "Cloudy"},
            {"temp": 4, "condition": "Snowy"},
            {"temp": 6, "condition": "Cloudy"},
            {"temp": 8, "condition": "Partly Sunny"},
            {"temp": 8, "condition": "Cloudy"},
            {"temp": 9, "condition": "Sunny"},
            {"temp": 8, "condition": "Partly Sunny"},
        ],
        "Stockholm": [
            {"temp": 4, "condition": "Snowy"},
            {"temp": 5, "condition": "Partly Sunny"},
            {"temp": 7, "condition": "Cloudy"},
            {"temp": 12, "condition": "Sunny"},
            {"temp": 10, "condition": "Sunny"},
            {"temp": 8, "condition": "Sunny"},
            {"temp": 8, "condition": "Partly Sunny"},
        ]
    }


    def get_weather_by_city(self, city_name):
        return self.weather_data.get(
            city_name,
            {"temp": None, "condition": "Unknown"}
        )

    def get_weather_by_coords(self, lat, lon):
        # Mock: always return Örebro
        return self.weather_data.get("Örebro")

    def get_nday_forecast(self, city_name, n_days):
        forecast = self.forecast_data.get(city_name, [])

        if not forecast:
            return []

        if n_days <= len(forecast):
            return forecast[:n_days]
        else:
            extra_days = [forecast[-1]] * (n_days - len(forecast))
            return forecast + extra_days