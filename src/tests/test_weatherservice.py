
import pytest



# --- Fixtures ---
@pytest.fixture
def weather_service():
    return WeatherService()




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
    # For this test, override the return for unknown city
    weather_service.get_nday_forecast.return_value = []

    forecast = weather_service.get_nday_forecast("UnknownCity", 3)
    assert forecast == []
    weather_service.get_nday_forecast.assert_called_once_with("UnknownCity", 3)