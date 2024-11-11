import requests
from datetime import datetime, timedelta


class FlightSearch:

    def __init__(self):
        self.kiwi_API_KEY = "api key"
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
            "nights_in_dst_to": 18,
            "nights_in_dst_from": 3,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "EUR",
            "max_stopovers": 0,
        }

        data = requests.get(url=f"{self.kiwi_endpoint}/v2/search", params=flight_params, headers=self.flight_header)
        data.raise_for_status()
        try:
            return_data = data.json()["data"][0]
        except IndexError:
            flight_params["max_stopovers"] = 1
            data = requests.get(url=f"{self.kiwi_endpoint}/v2/search", params=flight_params, headers=self.flight_header)
            data.raise_for_status()

            try:
                return_data = data.json()["data"][0]
            except IndexError:
                return None
            else:
                print(f"{return_data['cityTo']}: {return_data['price']}€."
                      f"\n{flight_params['max_stopovers']} stop over, via {return_data['route'][0]['cityTo']}")
                return return_data
        else:
            print(f"{return_data['cityTo']}: {return_data['price']}€")
            return return_data
