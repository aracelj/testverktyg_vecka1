class WeatherService:
    def __init__(self):
        # dummy data
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

            "Gothenburg":[
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

    def get_weather_by_city(self, city_name):
        return self.weather_data.get(city_name, {"temp": None, "condition": "Unknown"})

    def get_weather_by_coords(self, lat, lon):
        # For dummy purposes, return Örebro for any coordinates
        return self.weather_data["Örebro"]