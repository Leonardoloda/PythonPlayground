class Car:
    pass


car = Car()

# Class attributes can be assigned with the . syntax
car.brand = "Toyota"
car.model = "2024"

print("Car 1 created with empty class", car.model)


## However they can be created in the constructor so that they're alwaya ssigned
class CarV2:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "2024"


car2 = CarV2()

print("Car 2 created with static attributes", car2.model)


## THey can also be send as parameters to the ocnstructor

class CarV3:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car3 = CarV3(brand="Toyota", model="2024")
print("Car 3 with custom attributes", car3.model)


# However you can also use default values
class CarV4:
    def __init__(self, brand, model=2024):
        self.brand = brand
        self.model = model


car4 = CarV4(brand="Toyota")
print("Car 4 with default attributes", car4.model)


class CarV5:
    def __init__(self, brand, model=2024):
        self.brand = brand
        self.model = model

    def set_model(self, model):
        self.model = model


car5 = CarV5(brand="Toyota", model="2024")
car5.set_model(model="2020")

print("Car 5 with custom methods", car5.model)
