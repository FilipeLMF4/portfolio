from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

ORIGIN_CITY_IATA = "OPO"

for row in data.get_data():
    cheapest_price = row["lowestPrice"]
    if row["iataCode"] == "":
        city_code = flightSearch.search_code(row['city'])
        data.write_data(city_code, row["id"])
    else:
        city_code = row["iataCode"]

    flight_data = FlightData(flightSearch.search_flights(city_code, ORIGIN_CITY_IATA))
    if flight_data.price < cheapest_price:
        notificationManager.send_message(flight_data.format_data())
