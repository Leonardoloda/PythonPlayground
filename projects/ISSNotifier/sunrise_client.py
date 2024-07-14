from requests import get


class SunriseClient:
    """Rest client to fetch from the sunrise sunset api"""

    SUNRISE_ENDPOINT = "https://api.sunrise-sunset.org/json"

    def __init__(self) -> None:
        pass

    def get_current_sunset(self, lat, lng):
        """Get the sunset for the a particular latitude and longitude"""

        params = {"lat": lat, "lng": lng, "formatted": 0}

        response = get(self.SUNRISE_ENDPOINT, params=params)

        return response.json()
