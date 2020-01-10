class Car:
    def __init__(self, model, color="", horses=0):
        self.velocity = 0
        self.model = model
        self.color = color
        self.horses = horses
        # self.unknown_value = None

    def speedUp(self, vel):
        self.velocity += vel

    def __str__(self):
        return self.model + " " + self.color


bmw = Car("BMW", "Red", 300)
# bmw.model = "BMW"
# bmw.color = "Red"
# bmw.horses = 300
bmw.speedUp(10)
print(bmw.velocity)

audi = Car("Audi", "Blue", 315)
# audi.model = "Audi"
# bmw.color = "Blue"
# bmw.horses = 315

print(bmw.model, audi.model)
print(bmw.color, audi.color)

str_bmw = str(bmw)
print(bmw)
print(bmw.__dict__)
