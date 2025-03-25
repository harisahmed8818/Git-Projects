class Device:
    def __init__(self, name, status):
        self.name = name
        self.status = "OFF"

    def toggle_status(self):
        self.status = "ON" if self.status == "OFF" else "OFF"
        print(f"{self.name} is now {self.status}")

class SmartBulb(Device):
    def __init__(self, name):
        self.name = name
        self.status = 'OFF'
        self.brightness = 50 

    def adjust_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name} brightness set to {self.brightness}%")
        else:
            print("Brightness must be between 0 to 100")    

# Example Usage
bulb = SmartBulb("Room Light")
print(bulb.name)
print(bulb.brightness)
bulb.toggle_status()      # Turns ON
bulb.adjust_brightness(80)  # Sets brightness to 80%
