import requests


class DataManager:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/165a242f0a4568d9bcf7ccb27dacea11/flightDeals/prices"

    def get_data(self):
        response = requests.get(self.sheety_endpoint)
        return response.json()["prices"]

    def write_data(self, code, row_id):
        write_params = {
            "price": {
                "iataCode": code
            }
        }

        requests.put(url=f"{self.sheety_endpoint}/{row_id}", json=write_params)

    def get_user_emails(self):
        response = requests.get(url="https://api.sheety.co/165a242f0a4568d9bcf7ccb27dacea11/flightDeals/users")
        data = response.json()
        destination_data = data["users"]
        return destination_data
