"""
User Stories:
  1. User can search for the city and see the corresponding weather forecast of the day
  2. User can search by location coordinates and see the corresponding weather forecast of the day.
  3. User can input no. of days for the next weather forecast
"""
import pytest
from weatherservice import WeatherService


# --- Fixtures ---
@pytest.fixture
def mock_weather_service(mocker):
    service = mocker.Mock(spec=WeatherService)
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

    # Mock get_weather_by_city to return data from weather_data
    def get_weather_by_city(city_name):
        return service.weather_data.get(city_name, {"temp": None, "condition": "Unknown"})

    service.get_weather_by_city.side_effect = get_weather_by_city

    # Mock get_weather_by_coords to always return Örebro data
    def get_weather_by_coords(lat, lon):
        return service.weather_data["Örebro"]

    service.get_weather_by_coords.side_effect = get_weather_by_coords

    # Mock get_nday_forecast to mimic your class logic
    def get_nday_forecast(city_name, n_days):
        forecast = service.weather_data.get(city_name, [])
        if not forecast:
            return []
        if n_days <= len(forecast):
            return forecast[:n_days]
        else:
            extra_days = [forecast[-1]] * (n_days - len(forecast))
            return forecast + extra_days

    service.get_nday_forecast.side_effect = get_nday_forecast

    return service


def test_weather_by_city(mock_weather_service):
    forecast = mock_weather_service.get_weather_by_city("Örebro")
    assert forecast[0]["temp"] == 2
    assert forecast[0]["condition"] == "Cloudy"

    # Unknown city returns default
    unknown = mock_weather_service.get_weather_by_city("UnknownCity")
    assert unknown["condition"] == "Unknown"


def test_weather_by_location(mock_weather_service):
    # simulate coordinates (e.g., Örebro)
    latitude, longitude = 59.2753, 15.2134
    forecast = mock_weather_service.get_weather_by_coords(latitude, longitude)

    # Check that forecast contains temp and condition
    assert "temp" in forecast[0]
    assert "condition" in forecast[0]

    # Dummy check for value
    assert forecast[0]["condition"] == "Cloudy"


def test_variable_days_forecast(mock_weather_service):
    forecast_2 = mock_weather_service.get_nday_forecast("Stockholm", 2)
    assert len(forecast_2) == 2

    # Request 5-day forecast
    forecast_5 = mock_weather_service.get_nday_forecast("Stockholm", 5)
    assert len(forecast_5) == 5

    # Check each day has required keys
    for day in forecast_5:
        assert "temp" in day
        assert "condition" in day

def test_unknown_city_nday_forecast(mock_weather_service):
    # For this test, override the return for unknown city
    mock_weather_service.get_nday_forecast.return_value = []

    forecast = mock_weather_service.get_nday_forecast("UnknownCity", 3)
    assert forecast == []
    mock_weather_service.get_nday_forecast.assert_called_once_with("UnknownCity", 3)