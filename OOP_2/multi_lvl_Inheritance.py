class Car:
    color="black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")

class Toyotacar(Car):
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyotacar):
    def __init__(self, type):
        self.type= type

car1=Fortuner("diesel")
car1.start()