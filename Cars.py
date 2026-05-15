
class Car:
    wheels = 4
    def __init__(self):
        self.make = "BMW"
        self.model = "VD100"

    @classmethod
    def infowheels(cls):
        return cls.wheels

    @staticmethod
    def info():
        print("This is a static method")

C1 =Car()
c2= Car()
Car.wheels = 2
print(C1.make,C1.model,C1.wheels)
print(c2.make,c2.model,Car.wheels)

print(Car.infowheels())
Car.info()
