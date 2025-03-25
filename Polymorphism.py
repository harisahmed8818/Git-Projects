# # Runtime Polymorphism
# # Overriding a method

# class Animal:
#     def speak(self):
#         return 'Some animal sound'

# class Dog(Animal):
#     def speak(self): #Overriding the speak() method in both Dog & Cat classes.
#         return ' Barking'

# class Cat(Animal):
#     def speak(self):
#         return 'Meow'

# Animals = [Dog(),Cat()]
# for animal in Animals:
#  print(animal.speak())


# # Overriding with super() 

# class Animal1:
#     def speak(self):
#         return 'Some animal sound'

# class Dog1(Animal1):
#     def speak(self): 
#        return super().speak() + ' but bark mostly'

# dog = Dog1()
# print(dog.speak()) # The super().speak() calls the parent class method first, then adds aditional behaviour.



# # Compile-Time Polymorphism
# # Overloading method

# class Math:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# math = Math()
# print(math.add(2,3,4))
# print(math.add(6,7))
# print(math.add(2))

# Using *args

class Math1:
    def add(self, *num):
        return sum(num)

math = Math1        
print(math.add(5,6))
print(math.add(5,8,9,109,6,55,3))
