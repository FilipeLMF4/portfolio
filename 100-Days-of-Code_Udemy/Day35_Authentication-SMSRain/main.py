import requests
from twilio.rest import Client
# TWILIO_RECOVERY_CODE = "MAB2DC6E56PDECDQLXE5XNNW"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "API Key"
account_sid = "Account SID"
auth_token = "Token"

LATITUDE = 41.545448
LONGITUDE = -8.426507

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()["list"]

will_rain = False
for result in data:
    condition_code = result["weather"][0]["id"]
    if int(condition_code) < 700 and not will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella!",
            from_='+18326788987',
            to='+351913315437'
        )
        print(message.status)
        will_rain = True
