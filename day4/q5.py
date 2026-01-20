class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


# Objects
v1 = Vehicle("Toyota", "Corolla")
c1 = Car("Toyota", "Corolla", 5)
b1 = Bike("Yamaha", "R15", 155)

# Output
print("Vehicle Brand:", v1.brand)
print("Car Model:", c1.model)
print("Car Seats:", c1.seats)
print("Bike Engine CC:", b1.engine_cc)
