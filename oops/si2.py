class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def displayVehicle(self):
        print("Brand :", self.brand)
        print("Speed :", self.speed)


class Car(Vehicle):
    def __init__(self, brand, speed, fuelType):
        super().__init__(brand, speed)
        self.fuelType = fuelType

    def displayCar(self):
        super().displayVehicle()
        print("Fuel Type :", self.fuelType)

c = Car("Tata", 180, "Diesel")
c.displayCar()
