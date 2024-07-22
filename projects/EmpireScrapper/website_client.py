from requests import get


class WebsiteClient:
    def __init__(self, url: str) -> None:
        self._url = url

    def change_website(self, url):
        self._url = url

    def fetch_page(self):
        response = get(self._url)

        return response.text
