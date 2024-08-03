from requests import get


class Client:
    """Receives a url to fetch the needed info"""

    def __init__(self) -> None:
        pass

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    def fetch_response(self, params: dict = {}) -> dict:
        """Send a GET request"""

        response = get(self._url, params=params)

        return response.json()
