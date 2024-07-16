from os import getenv

from dotenv import load_dotenv

from open_weather_client import OpenWeatherClient
from projects.RainAlert.twilio_client import TwilioClient

load_dotenv()

MY_LAT = 4.710989
MY_LNG = -74.072090

# Open Weather Credentials
API_KEY = getenv("API_KEY")

# Twilio credentials
ACCOUNT_SID = getenv("ACCOUNT_SID")
AUTH_TOKEN = getenv("AUTH_TOKEN")

weather_client = OpenWeatherClient(api_key=API_KEY)
twilio_client = TwilioClient(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)

today_forecast = weather_client.get_forecast(lat=MY_LAT, lon=MY_LNG)


def is_rainy_day(forecast: list) -> bool:
    for forecast_hour in forecast["list"]:
        for weather in forecast_hour["weather"]:
            if weather["id"] < 700:
                return True

    return False


today_will_rain = is_rainy_day(today_forecast)

if today_will_rain:
    print("Today is rainy, about to send a message")
    message = twilio_client.send_message(to="+573193189542", body="Today will rain")

    print(message.status)

print("Forecast completed")
