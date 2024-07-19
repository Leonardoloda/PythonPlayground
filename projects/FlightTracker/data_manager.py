from requests import get, put


class DataManager:
    URL = "https://api.sheety.co/d7c73a0a228fcfcbb405d430492cc56f/flightData/"

    def __init__(self, token: str, sheet: str) -> None:
        self._token = token
        self._sheet = sheet

        self.URL = self.URL + self._sheet

    def get_auth_header(self):
        return {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

    def get_rows(self):
        headers = self.get_auth_header()

        response = get(self.URL, headers=headers)
        response.raise_for_status()

        return response.json()

    def update_row(self, row: str, payload: dict):
        headers = self.get_auth_header()
        body = {
            "flight": payload
        }

        response = put(f"{self.URL}/{row}", json=body, headers=headers)
        print(response.text)
        response.raise_for_status()

        return response.json()
