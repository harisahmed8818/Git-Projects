from abc import ABC , abstractclassmethod

# Abstract Class

class User(ABC):

    def __init__(self, name, user_id):

        self.name = name
        self.user_id = user_id

    def search_books(self):
        print(f'{self.name} ID : {self.user_id} is searching for books...')

@abstractclassmethod
def access_library(self):
    pass


class Member(User):

    def access_library(self):
        print(f'{self.name} ID : {self.user_id} (Member) can access the library.')

    def borrow_books(self):
        print('Member has borrowed a book.')


class Librarian(User):

    def access_library(self):
        print(f'{self.name} ID :{self.user_id} (Librarian) can access the library.')

    def add_remove_books(self):
        print('Librarian has add/removed a book.')
        

class Guests(User):
    def access_library(self):
        print(f'{self.name} ID : {self.user_id} (Guest) cannot borrrow books or access the library.')   
        
def create_user():
    name = input('Enter Your Name : ')
    user_id = input('Enter Your ID : ')

    while True:
        print('Select Your role :')
        print('1. Member')
        print('2. Librarian')
        print('3. Guest')

        role = input('Enter you choice (1/2/3):')

        if role == "1":
            return Member(name, user_id)
        elif role == "2":
            return Librarian(name, user_id)
        elif role == "3":
            return Guests(name, user_id)
        else:
            print('Invalid choice ! Please enter 1-3.')

user = create_user()

user.search_books()
user.access_library()

if type(user) == Member:
    user.borrow_books()
elif type(user) == Librarian:
    user.add_remove_books()