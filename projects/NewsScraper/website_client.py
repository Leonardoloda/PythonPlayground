from requests import get


class WebsiteClient:
    def __init__(self, url: str) -> None:
        self._url = url

    def get_website(self):
        response = get(self._url)

        return response.text
