class Match(object):
    def __init__(self, freight_id, cargo_id, origin, destination, distance, travel_time):
        self.freight_id = freight_id
        self.cargo_id = cargo_id
        self.distance = distance
        self.origin = origin
        self.destination = destination
        self.travel_time = travel_time

