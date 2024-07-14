from requests import get


class ISSNotifier:
    """Rest client to fetch from the sunrise sunset api"""

    ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"

    def __init__(self) -> None:
        pass

    def get_position(self):
        """Get the latitude and longitude"""

        response = get(self.ISS_ENDPOINT)

        return response.json()
