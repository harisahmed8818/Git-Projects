class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed: {self.speed} km/h")

class ElectricVehicle:
    def __init__(self):
        self.battery = 100

    def charge_battery(self):
        self.battery = 100
        print("Battery charged.")

class HybridCar(Car, ElectricVehicle):
    def __init__(self):
        Car.__init__(self)
        ElectricVehicle.__init__(self)

# Example Usage
hybrid = HybridCar()
hybrid.accelerate(30)  # Speed up
hybrid.charge_battery()  # Charge battery
