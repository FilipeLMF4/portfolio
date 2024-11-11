class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.price = data["price"]
        self.departure_city = data["cityFrom"]
        self.departure_airport = data["flyFrom"]
        self.destination_city = data["cityTo"]
        self.destination_airport = data["flyTo"]
        departure_route = data["route"][0]
        return_route = data["route"][1]
        self.departure_date = departure_route["local_departure"].split("T")[0]
        self.return_date = return_route["local_departure"].split("T")[0]
        self.via_city = ""

        if self.destination_city != data["route"][0]["cityTo"]:
            self.via_city = data["route"][0]["cityTo"]

    def format_data(self):
        message = f"Low price alert! Only {self.price}€ to fly "\
                  f"from {self.departure_city}-{self.departure_airport} "\
                  f"to {self.destination_city}-{self.destination_airport}, "\
                  f"from {self.departure_date} to {self.return_date}."

        if self.via_city != "":
            message += f"\nFlight has 1 stop over, via {self.via_city}"

        return message