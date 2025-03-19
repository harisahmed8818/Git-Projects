class Bird:
    def fly(self):
        print('Birds can fly.')

class Fish:
    def swim(self):
        print('Fish can swim.')

class Penguin(Bird,Fish):
    def fly(self):
        super().fly()
        print('But penguins cannot fly.')   
Penguin().fly()        
        
