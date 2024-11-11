import requests
from datetime import datetime

MY_LAT = 41.545448
MY_LONG = -8.426507
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # HTTP status codes: https://www.webfx.com/web-development/glossary/http-status-codes/
# print(f"Status Code: {response.status_code}")
# response.raise_for_status()  # Raises error if unsuccessful response
#
# data = response.json()
# print(data)

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# URL for viewing JSON in browser: Endpoint + ? + param1=value1 + & + param2=value2 + & + ....
# Ex: https://api.sunrise-sunset.org/json?lat=41.545448&long=-8.426507

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
