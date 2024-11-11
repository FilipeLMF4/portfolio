import requests
from datetime import datetime, timedelta


class FlightSearch:

    def __init__(self):
        self.kiwi_API_KEY = "API key"
        self.kiwi_endpoint = "https://api.tequila.kiwi.com"
        self.flight_header = {"apikey": self.kiwi_API_KEY}

    def search_code(self, city):
        city_params = {
            "term": city,
            "location_types": "city",
            "limit": 1
        }

        flight_data = requests.get(f"{self.kiwi_endpoint}/locations/query", params=city_params, headers=self.flight_header)
        return flight_data.json()["locations"][0]["code"]

    def search_flights(self, dest_city, origin_city):
        tomorrow = datetime.now() + timedelta(days=1)
        end_date = tomorrow + timedelta(days=6 * 30)

        flight_params = {
            "fly_from": origin_city,
            "fly_to": dest_city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "return_from": tomorrow.strftime("%d/%m/%Y"),
            "return_to": end_date.strftime("%d/%m/%Y"),
            "nights_in_dst_to": 15,
            "nights_in_dst_from": 2,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "one_for_city": 1,
            "curr": "EUR",
        }

        data = requests.get(url=f"{self.kiwi_endpoint}/v2/search", params=flight_params, headers=self.flight_header)
        data.raise_for_status()
        return data.json()["data"][0]
