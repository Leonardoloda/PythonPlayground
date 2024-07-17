from requests import get


class AlphaVantageClient:
    NEWS_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_prices(self, stock: str) -> dict:
        response = get(self.NEWS_URL, params={
            "function": "TIME_SERIES_DAILY",
            "symbol": stock,
            "apikey": self.api_key
        })

        response.raise_for_status()

        return response.json()
