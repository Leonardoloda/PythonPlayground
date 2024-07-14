from iss_client import ISSNotifier
from sunrise_client import SunriseClient

from datetime import datetime

MY_LAT = 5.2270
MY_LNG = -38.7198

DEFAULT_OFFSET = 10

iss_client = ISSNotifier()
sunrise_client = SunriseClient()

day_night_schedule = sunrise_client.get_current_sunset(lat=MY_LAT, lng=MY_LNG)
position = iss_client.get_position()

now = datetime.now()


def is_after_sunset(sunset_limit):
    """Checks if it's currently after sunset"""
    return (
        sunset_limit.hour < datetime.now().hour
        and sunset_limit.minute < datetime.now().minute
    )


def is_before_sunrise(sunrise_limit):
    """Checks if its currently before sunrise"""
    return (
        sunrise_limit.hour < datetime.now().hour
        and sunrise_limit.minute < datetime.now().minute
    )


def is_within_lat(current_lat, target_lat, offset=DEFAULT_OFFSET):
    """Check if an object is within a  lat"""
    return target_lat - offset < current_lat < target_lat + offset


def is_within_lng(current_lng, target_lng, offset=DEFAULT_OFFSET):
    """check if it's withing the lng"""
    return target_lng - offset < current_lng < target_lng + offset


satellite_lat = float(position["iss_position"]["latitude"])
satellite_lng = float(position["iss_position"]["longitude"])

sunrise = datetime.fromisoformat(day_night_schedule["results"]["sunrise"])
sunset = datetime.fromisoformat(day_night_schedule["results"]["sunset"])

is_dark = is_after_sunset(sunset) and is_before_sunrise(sunrise)
is_close = is_within_lat(MY_LAT, satellite_lat, 100) and is_within_lng(
    MY_LNG, satellite_lng, 100
)

print("Is dark out there?", "yes" if is_dark else "no")
print("Is it close out there?", "yes" if is_close else "no")


if is_dark and is_close:
    print("Look up")
