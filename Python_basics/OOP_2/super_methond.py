class Car:
    def __init__(self,type):
        self.fuel=type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stoped...")

class Toyotacar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
   
car1=Toyotacar("Prius","Electric")
print(car1.fuel)