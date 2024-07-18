from requests import post


class NutritionixClient:
    URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    def __init__(self, api_key: str, app_id: str) -> None:
        self._api_key = api_key
        self._app_id = app_id

    def generate_auth_header(self):
        return {
            'x-app-id': self._app_id,
            'x-app-key': self._api_key
        }

    def parse_exercise(self, prompt: str) -> dict:
        headers = self.generate_auth_header()
        body = {
            "query": prompt
        }

        response = post(self.URL, headers=headers, json=body)

        return response.json()
