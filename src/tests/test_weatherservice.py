"""
User Stories:
  1. As a user, the user can search for the city and see the corresponding weather forecast of the day
  2. As a user, the user can search by location coordinates and see the corresponding weather forecast of the day.
  3. As a user, the user can input no. of days for the next weather forecast
"""

from weatherservice import WeatherService

def test_weather_by_city():
    service = WeatherService()

    forecast = service.get_weather_by_city("Örebro")
    assert forecast[0]["temp"] == 2
    assert forecast[0]["condition"] == "Cloudy"

    # Unknown city returns default
    unknown = service.get_weather_by_city("UnknownCity")
    assert unknown["condition"] == "Unknown"


def test_weather_by_location():
    service = WeatherService()

    # simulate coordinates (e.g., Örebro)
    latitude, longitude = 59.2753, 15.2134
    forecast = service.get_weather_by_coords(latitude, longitude)

    # Check that forecast contains temp and condition
    assert "temp" in forecast[0]
    assert "condition" in forecast[0]

    # Dummy check for value
    assert forecast[0]["condition"] == "Cloudy"


def test_variable_days_forecast():
    service = WeatherService()

    # Request 2-day forecast
    forecast_2 = service.get_nday_forecast("Stockholm", 2)
    assert len(forecast_2) == 2

    # Request 5-day forecast
    forecast_5 = service.get_nday_forecast("Stockholm", 7)
    assert len(forecast_5) == 7

    # Check each day has required keys
    for day in forecast_5:
        assert "temp" in day
        assert "condition" in day

def test_unknown_city_nday_forecast():
    service = WeatherService()

    forecast = service.get_nday_forecast("UnknownCity", 3)
    assert forecast == []