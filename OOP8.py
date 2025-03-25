from abc import ABC, abstractmethod

class Appliance:
    def turn_on(self):
        print('Appliance is now ON')

    @abstractmethod
    def turn_off(self):
        print('FIVE')
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        super().turn_on()
        print('Washing Machine is ready to use.')

    def turn_off(self):
        print('Washing Machine is now OFF.')    

wm = WashingMachine()
wm.turn_on()
wm.turn_off()        
    
