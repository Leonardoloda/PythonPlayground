from requests import get


class NewsClient:
    NEWS_URL = "https://newsapi.org/v2/everything"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_news(self, q: str, from_: str) -> dict:
        response = get(self.NEWS_URL, params={
            "apiKey": self.api_key,
            "sortBy": "publishedAt",
            "q": q,
            "from": from_
        })

        return response.json()
