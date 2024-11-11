import requests
from datetime import datetime
import smtplib
import time

APP_PASS = "Your Password"
MY_EMAIL = "Your email"
MY_LAT = 41.545448  # Your latitude
MY_LONG = -8.426507  # Your longitude


def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT-5 < iss_latitude < MY_LAT+5) and (MY_LONG-5 < iss_longitude < MY_LONG+5):
        return True
    else:
        return False


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # No need to close connection this way
            connection.starttls()  # Makes connection secure
            connection.login(user=MY_EMAIL, password=APP_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nLook Up! The ISS is above you in the sky."
            )
