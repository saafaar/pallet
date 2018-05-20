class MatchUseCase(object):

    def __init__(self, freight_id, freight, cargo_id, cargo):
        self.cargo = cargo
        self.freight = freight
        self.freight_id = freight_id
        self.cargo_id = cargo_id

    @property
    def match(s):
        return ((s.cargo.size_z <= s.freight.size_z) and
                (s.cargo.weight <= s.freight.weight) and
                (s.cargo.start_date <= s.freight.dept_date) and
                ((s.cargo.size_y <= s.freight.size_y and s.cargo.size_x <= s.freight.size_x) or
                 (s.cargo.size_y <= s.freight.size_x and s.cargo.size_x <= s.freight.size_y)))

    def coordinates(s):
        if s.match():
            freight_coordinates = {'id':s.freight_id, 'coordinates' : [s.freight.dept_latitude, s.freight.dept_longitude]}
            cargo_coordinates = {'id':s.cargo_id, 'coordinates':[s.cargo.latitude, s.cargo.longitude]}
            return freight_coordinates, cargo_coordinates
