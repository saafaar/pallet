import json


class CargoEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'name': o.name,
                'size_x': o.size_x,
                'size_y': o.size_y,
                'size_z': o.size_z,
                'weight': o.weight,
                'latitude': o.latitude,
                'longitude': o.longitude,
                'start_date': o.start_date
            }
            return to_serialize
        except AttributeError:
            return super().default(o)


class FreightEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'name': o.name,
                'size_x': o.size_x,
                'size_y': o.size_y,
                'size_z': o.size_z,
                'count': o.count,
                'weight': o.weight,
                'dept_latitude': o.dept_latitude,
                'dept_longitude': o.dept_longitude,
                'dept_date': o.dept_date
            }
            return to_serialize
        except AttributeError:
            return super().default(o)


class MatchEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                'freight_id': o.freight_id,
                'cargo_id': o.cargo_id,
                'distance': o.distance,
                'origin' : o.origin,
                'destination' : o.destination,
                'travel_time' : o.travel_time
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
