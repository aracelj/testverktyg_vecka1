"""
User Stories:
  1. As a user, the user can search for the city and see the corresponding weather forecast of the day
  2. As a user, the user can search by location coordinates and see the corresponding weather forecast of the day.
  3. As a user, the user can input no. of days for the next weather forecast
"""
import pytest
from weatherservice import WeatherService


# --- Fixtures ---
@pytest.fixture
def weather_service():
    service = WeatherService()
    # dummy data
    service.weather_data = {
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
    return service


def test_weather_by_city(weather_service):
    forecast = weather_service.get_weather_by_city("Örebro")
    assert forecast[0]["temp"] == 2
    assert forecast[0]["condition"] == "Cloudy"

    # Unknown city returns default
    unknown = weather_service.get_weather_by_city("UnknownCity")
    assert unknown["condition"] == "Unknown"


def test_weather_by_location(weather_service):
    # simulate coordinates (e.g., Örebro)
    latitude, longitude = 59.2753, 15.2134
    forecast = weather_service.get_weather_by_coords(latitude, longitude)

    # Check that forecast contains temp and condition
    assert "temp" in forecast[0]
    assert "condition" in forecast[0]

    # Dummy check for value
    assert forecast[0]["condition"] == "Cloudy"


def test_variable_days_forecast(weather_service):
    #service = WeatherService()    # Request 2-day forecast
    forecast_2 = weather_service.get_nday_forecast("Stockholm", 2)
    assert len(forecast_2) == 2

    # Request 5-day forecast
    forecast_5 = weather_service.get_nday_forecast("Stockholm", 5)
    assert len(forecast_5) == 5

    # Check each day has required keys
    for day in forecast_5:
        assert "temp" in day
        assert "condition" in day

def test_unknown_city_nday_forecast(weather_service):
    forecast = weather_service.get_nday_forecast("UnknownCity", 3)
    assert forecast == []