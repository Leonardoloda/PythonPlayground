# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from os import getenv

from dotenv import load_dotenv

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from mail_client import EmailClient
from notification_manager import NotificationManager
from twilio_client import TwilioClient

load_dotenv()

SHEETY_TOKEN = getenv('SHEETY_TOKEN')
AMADEUS_API_KEY = getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = getenv('AMADEUS_API_SECRET')

ACCOUNT_SID = getenv('ACCOUNT_SID')
SECRET_KEY = getenv('SECRET_KEY')
AUTH_TOKEN = getenv('AUTH_TOKEN')

EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')

FLIGHTS_SHEET = "flights"
USERS_SHEET = "users"

ORIGIN = "SYD"

flights_sheet = DataManager(token=SHEETY_TOKEN, sheet=FLIGHTS_SHEET)
users_sheet = DataManager(token=SHEETY_TOKEN, sheet=USERS_SHEET)

twilio_client = TwilioClient(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)
email_client = EmailClient(email=EMAIL, password=PASSWORD)
amadeus_client = FlightSearch(api_key=AMADEUS_API_KEY, api_secret=AMADEUS_API_SECRET)

users_data = users_sheet.get_rows()
users = users_data["users"]

notification_manager = NotificationManager(mail_client=email_client, message_client=twilio_client, users=users)

flight_data = FlightData()

cities_sheet = flights_sheet.get_rows()
subscribed_cities = cities_sheet["flights"]

for city in subscribed_cities:
    added_price = False

    if not city.get("iataCode"):
        city_code = amadeus_client.get_city_code(city["city"])
        city["iataCode"] = city_code

        flights_sheet.update_row(row=city["id"], payload=city)

    flights_response = amadeus_client.get_available_flights(from_=ORIGIN, to=city["iataCode"])
    available_flights = flights_response['data']

    try:
        if len(available_flights) == 0:
            print("No direct flights fount, looking again")

            flights_response = amadeus_client.get_available_flights(from_=ORIGIN, to=city["iataCode"], non_stop="false")
            available_flights = flights_response['data']

        cheapest_flight = flight_data.find_cheapest_flight(flights=available_flights)

        cheapest_flight_price = float(cheapest_flight["price"]["total"])

        if not city.get("lowestPrice") or cheapest_flight_price < city["lowestPrice"]:
            city["lowestPrice"] = cheapest_flight_price
            flights_sheet.update_row(row=city["id"], payload=city)
            notification_manager.trigger_price_alert(from_=ORIGIN, to=city["iataCode"], price=str(city["lowestPrice"]))
            continue;

    except KeyError:
        print("No direct flights, trying to check again with indirect flies")
