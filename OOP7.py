class Vehicle:
    def start(self):
        print('Vehicle is starting.')

class Car(Vehicle):
    def start(self):
        super().start()
        print('Car is starting.')

class ElectricCar(Vehicle):
    def start(self):
        super().start() 
        print('Electric car is starting .')

ecar = ElectricCar()    
ecar.start()  
Car().start()