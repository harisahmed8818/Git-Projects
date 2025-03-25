# Base class
class Instrument:
    def __init__(self):
        print("Instrument initialized")

class MeasuringDevice(Instrument):
    def __init__(self):
        super().__init__()  
        print("Measuring Device initialized")

class ElectricDevice(Instrument):
    def __init__(self):
        super().__init__() 
        print("Electric Device initialized")

# Multiple Inheritance (Diamond Problem)
class DigitalScale(MeasuringDevice, ElectricDevice):
    def __init__(self):
        super().__init__()  # Resolves multiple initializations
        print("Digital Scale initialized")

# Creating object
scale = DigitalScale()
