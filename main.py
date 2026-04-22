# 4-m
class CarFuel:
    def __init__(self,model, fuel):
        self.model = model
        self.fuel = fuel

    def drive(self, km):
        self.fuel = km
        print(f"{km} yurildi" )

    def refuel(self, amount):
        self.fuel = amount
        print(f"{amount} fuel oshadi")

    def info(self):
        print(f"10 km yurildi,{self.model}: {self.fuel} ")


c1 = CarFuel("yoqilg'i", 20)
c1.info()
