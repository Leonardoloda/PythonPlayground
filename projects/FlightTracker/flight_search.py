from datetime import datetime, timedelta

from requests import get, post


class FlightSearch:
    CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

    def __init__(self, api_key: str, api_secret: str) -> None:
        self._api_key = api_key
        self._api_secret = api_secret

        self._token = self.generate_token()

    def generate_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = post(url=self.TOKEN_ENDPOINT, headers=header, data=body)
        response_json = response.json()

        return response_json['access_token']

    def generate_auth_header(self):
        return {
            'Authorization': 'Bearer ' + self._token,
        }

    def get_city_code(self, search: str):
        headers = self.generate_auth_header()
        query = {
            "keyword": search,
            "include": "AIRPORTS",
        }

        response = get(url=self.CITIES_ENDPOINT, headers=headers, params=query)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {search}.")
            return None
        except KeyError:
            print(f"KeyError: No airport code found for {search}.")
            return None

        return code

    def get_available_flights(self, from_: str, to: str, non_stop: str = "true"):
        tomorrow = datetime.now() + timedelta(days=1)
        six_months = timedelta(days=6 * 30)

        headers = self.generate_auth_header()
        params = {
            "originLocationCode": from_,
            "destinationLocationCode": to,
            "departureDate": tomorrow.strftime("%Y-%m-%d"),
            "returnDate": (tomorrow + six_months).strftime("%Y-%m-%d"),
            "adults": 1,
            "max": "10",
            "nonStop": non_stop,
        }

        response = get(url=self.OFFERS_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()

        return response.json()
