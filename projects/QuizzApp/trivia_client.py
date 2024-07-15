from requests import get


class OpenTriviaClient:
    URL = "https://opentdb.com/api.php"

    def __init__(self):
        pass

    def fetch_trivia(self, amount=10, type="boolean"):
        response = get(self.URL, params={
            "amount": amount,
            "type": type
        })

        return response.json()
