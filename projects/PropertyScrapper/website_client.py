from requests import get


class WebsiteClient:

    @staticmethod
    def fetch_page(url: str) -> str:
        response = get(url)

        return response.text
