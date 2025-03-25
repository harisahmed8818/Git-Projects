class Bird:
    def fly(self):
        print('Birds can fly.')

class Fish:
    def fly(self):
        print('Crow can fly.')
    def swim(self):
        print('Fish can swim.')

# Defining a class Penguin which inherits from Bird and Fish.

class Penguin(Fish,Bird):
    def fly(self): 
        super().fly()
        # Calling the fly() method of the parent class (Bird) using super()
        
        print('But penguins cannot fly.')   
Penguin().fly()        
        
