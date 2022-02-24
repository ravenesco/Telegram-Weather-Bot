from pyowm import OWM
from config import OPEN_WEATHER_API_KEY
from datetime import datetime

owm = OWM(OPEN_WEATHER_API_KEY)
mgr = owm.weather_manager()


def get_forecast(lat, lon):
    observation = mgr.forecast_at_coords(lat, lon, "3h", 5)
    forecast = observation.forecast
    location_name = f"{forecast.location.name}, {forecast.location.country}"
    weathers = forecast.weathers
    results = []

    for weather in weathers:
        results.append(
            f"Location: {location_name}\n"
            f"Time: {datetime.utcfromtimestamp(weather.ref_time).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Status: {weather.detailed_status.capitalize()}\n"
            f"Humidity: {weather.humidity}\n"
            f"Wind: {round(weather.wnd['speed'])} m/s\n"
            f"Temp: {round(weather.temp['temp'] - 273.15)}°C\n")

    return "-------------------------------------------\n".join(results)
