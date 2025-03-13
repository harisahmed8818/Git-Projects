class Employee:
    def __init__(self, name, salary, bonus_percent):
        self.name = name
        self.salary = salary
        self.bonus_percent = bonus_percent

    def calculate_bonus(self):
        return (self.salary * self.bonus_percent)/100

    def update_bonus(self, new_percent): 
        self.bonus_percent = new_percent   

# Example Usage
emp = Employee('Haris',50000,10)
print('Bonus :',emp.calculate_bonus())  

emp.update_bonus(15)
print('Updated bonus :',emp.calculate_bonus)
