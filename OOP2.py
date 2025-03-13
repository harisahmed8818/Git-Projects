class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return f'Deposited {amount} , New balance : {self.balance}' 

    def withdraw(self, amount):
        if amount > self.balance: 
         return f'Insufficient balance !'

        self.balance -= amount 
        return f'Withdrew {amount} , New balance : {self.balance}'

    def get_balance(self):
        return f'Current balance : {self.balance}'

wallet = Wallet("Haris",500)
print(wallet.get_balance())

print(wallet.deposit(200))
print(wallet.withdraw(100))
print(wallet.withdraw(900))