from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()
email_data = data.get_user_emails()

ORIGIN_CITY_IATA = "OPO"

for row in data.get_data():
    cheapest_price = row["lowestPrice"]
    if row["iataCode"] == "":
        city_code = flightSearch.search_code(row['city'])
        data.write_data(city_code, row["id"])
    else:
        city_code = row["iataCode"]

    found_flights = flightSearch.search_flights(city_code, ORIGIN_CITY_IATA)
    if found_flights is None:
        print(f"Did not find route for {city_code}")
        continue

    flight_data = FlightData(found_flights)
    if flight_data.price < cheapest_price:
        message = flight_data.format_data()
        notificationManager.send_emails(message, email_data)
