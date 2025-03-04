import csv 

def add_expense():
    
        Category = input("Category :" ).strip()
        Date = input("Date (DD-MM-YYYY) : ")
        Amount = input("Amount : ").strip()

        with open("expenses,csv", "a", newline="") as file:

              writer = csv.writer(file)
              writer.writerow([Category,Date,Amount])

        print("Expense added")

def view_expenses():
    try:
        with open("expenses,csv", "r") as file: 
            for row in csv.reader(file):
                print(row)
    except FileNotFoundError:
        print('No expenses found')

while True:
    choice = input('\n1. Add Expense\n2. View Expense\n3. Exit\nChoose:')
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice =='3':
        break
    else:
        print('Invalid choice.')        


