class Car:
    def __init__(self, number, model):
        self.number = number
        self.model = model

    def __str__(self):
        pass

    def __eq__(self, other):
        pass


class Parking:
    def __init__(self, places_count=10):
        self.places = []

    def park(self, car):
        pass

    def leave(self, car):
        pass

    def __str__(self):
        pass

    def free(self):
        pass


bmw = Car("a123aa", "BMW")
audi = Car("c523ta", "Audi")
garage = Parking()
garage.park(bmw)
garage.park(audi)
print(garage.free())
print(garage)
garage.leave(bmw)
