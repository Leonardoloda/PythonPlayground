class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    def find_cheapest_flight(self, flights: list) -> dict:
        lowest_price = float('inf')
        cheapest_flight = {}

        if len(flights) == 0:
            print("No available flights, skipping price logic")
            return {}

        for flight in flights:
            flight_price = float(flight['price']['total'])

            if flight_price < lowest_price:
                lower_price = flight_price
                cheapest_flight = flight

        return cheapest_flight
