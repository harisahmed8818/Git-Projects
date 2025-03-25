# Base class
class Crew:
    def __init__(self, name):
        self.name = name

    def report_status(self):
        return f"{self.name} is ready."

# Roles
class Engineer(Crew):
    def fix(self):
        return f"{self.name} is fixing."

class Pilot(Crew):
    def fly(self):
        return f"{self.name} is flying."

    def report_status(self):
        return f"Pilot {self.name} is checking systems."

class Scientist(Crew):
    def research(self):
        return f"{self.name} is researching."

    def report_status(self):
        return f"Scientist {self.name} is analyzing data."

# Multiple roles
class PilotScientist(Pilot, Scientist):
    def report_status(self):
        return f"{self.name} is flying and researching."

# Creating objects
a = Engineer("Alice")
b = Pilot("Bob")
c = Scientist("Charlie")
d = PilotScientist("David")

# Testing methods
print(a.fix())  
print(b.fly())  
print(c.research())  
print(d.fly())  
print(d.research())  

# Checking status
print(a.report_status())  
print(b.report_status())  
print(c.report_status())  
print(d.report_status())  
