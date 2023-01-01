import datetime

class car:
    def __init__(self,brand1,color1):
        car.brand=brand1
        car.color=color1
    def car_print(self):
        print("The brand of this car is "+self.brand+"\nThe color of this car is "+self.color)
car1=car("benchi","green")
car1.car_print()

timenow=datetime.datetime.now()
print(timenow)

