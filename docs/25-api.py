# we need to install a python module ot handle requests
import requests

ENDPOINT = "http://api.open-notify.org/iss-now.json"

# We can set up a url and send a http request
response = requests.get(url=ENDPOINT)

# we'll get a response class with all of the info
print(response)

# you can try to catch status
if response.status_code == 404:
    raise Exception("Endpoint not fount")

# but you can also just catch any exception by using the included
response.raise_for_status()

# You can get the actual data by getting it as a dict
data = response.json()

print(data["iss_position"])


# you can also send parameters in it
SUNRISE_ENDPOINT = "https://api.sunrise-sunset.org/json"
MY_LAT = 4.710989
MY_LNG = -74.072090

# parameters are defined as a dict
parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

# they're included in the request
response = requests.get(
    SUNRISE_ENDPOINT,
    params=parameters,
)

response.raise_for_status()

print(response.json())
