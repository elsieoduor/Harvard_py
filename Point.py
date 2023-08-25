#Creating a point with a python class.
#A class is used for creating a new object that stores info and preforms actions

class Point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y

p = Point(2, 4)
print(p.x)
print(p.y)

#A class representing airplane flights
class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
        def add_passenger(self, name):
            if not self.open_seats():
                return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
        def open_seats(self):
            return self.capacity - len(self.passengers)

