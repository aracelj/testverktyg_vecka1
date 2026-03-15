"""
User Stories:
  1. As a user, the user can search for the city and see the corresponding weather forecast of the day
  2. As a user, the user can search by location coordinates and see the corresponding weather forecast of the day.
  3. As a user, the user can input no. of days for the next weather forecast
"""

class WeatherService:
    def __init__(self):
        self.weather_data = {}  # “database”

    def get_weather_by_city(self, city_name):
        return self.weather_data.get(city_name, {"temp": None, "condition": "Unknown"})

    def get_weather_by_coords(self, lat, lon):
        # For dummy purposes, return Örebro for any coordinates
        return self.weather_data["Örebro"]

    def get_nday_forecast(self, city_name, n_days):
        # Return up to n_days; repeat last day if n_days > available data
        forecast = self.weather_data.get(city_name, [])
        if not forecast:
            return []

        # If n_days > length of available forecast, repeat last day
        if n_days <= len(forecast):
            return forecast[:n_days]
        else:
            extra_days = [forecast[-1]] * (n_days - len(forecast))
            return forecast + extra_days

