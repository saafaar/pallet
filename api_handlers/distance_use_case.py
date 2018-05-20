import requests
from pallet.entities.match import Match

class DistanceUseCase(object):
    def __init__(self, freight_coordinates, cargo_coordinates):
        self.freight_coordinates = freight_coordinates
        self.cargo_coordinates = cargo_coordinates

    def get_distances(self):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"

        querystring = {"origins": self.freight_coordinates['coordinates'], "destinations": self.cargo_coordinates['coordinates'], "key": "AIzaSyBSS3F2UnzvT7JDbUzQdG3V6-hlTTRQyLU"}

        headers = {}

        response = requests.request("GET", url, headers=headers, params=querystring)

        body = response.json()

        list_of_matches = []

        for i in range(len(self.freight_coordinates)):
            for j in range(len(self.cargo_coordinates)):
                list_of_matches.append(Match(self.freight_coordinates[i]['id'], self.cargo_coordinates[j]['id'],
                                             body["origin_addresses"][i], body["destination_addresses"][j],
                                             body["rows"][i]["elements"][j]["distance"]["value"],
                                             body["rows"][i]["elements"][j]["duration"]["value"]))

        return list_of_matches





