from requests import get


class OpenWeatherClient:
    CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_current_weather(self, lat: float, lon: float) -> dict:
        response = get(self.CURRENT_WEATHER_URL, params={
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
        })

        response.raise_for_status()

        return response.json()

    def get_forecast(self, lat: float, lon: float) -> dict:
        response = get(self.FORECAST_URL, params={
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "cnt": 4
        })

        response.raise_for_status()

        return response.json()
