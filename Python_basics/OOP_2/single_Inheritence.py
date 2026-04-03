class Car:
    color="black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1= Toyotacar("Fortuner")

print(car1.color)