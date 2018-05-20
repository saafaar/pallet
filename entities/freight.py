class Freight(object):
    def __init__(self, name, fare, size_x, size_y, size_z, weight, count, dept_latitude, dept_longitude, dept_date, arrival_latitude, arrival_longitude, arrival_date):

        self.name = name
        self.fare = fare
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        self.count = count
        self.weight = weight
        self.dept_latitude = dept_latitude
        self.dept_longitude = dept_longitude
        self.dept_date = dept_date
        self.arrival_latitude = arrival_latitude
        self.arrival_longitude = arrival_longitude
        self.arrival_date = arrival_date
