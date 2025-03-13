# Defining a class named 'Person'
class Person: 

    name = ''
    occupation =''
    networth = 0

    # Method to display person's details
    def info(self):

    # Print formatted information about the person 
      print(f"{self.name} is a {self.occupation} and has a Networth of : ${self.networth:,}USD")

a = Person() 
b = Person() 
c = Person() 

a.name = 'Ayaan'
a.occupation = 'Software Developer'

b.name = 'Jhon'
b.occupation = 'Web Designer'
b.networth = 100000

c.name = 'Ali'
c.occupation = 'Software Engineer'
c.networth = 230000

a.info()
b.info()
c.info()