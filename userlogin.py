import csv
import hashlib

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to sign up a new user
def sign_up():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    # Save the username and hashed password to a CSV file
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])
    print("User signed up successfully!")

# Function to log in a user
def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    # Check if the username and hashed password match any entry in the CSV file
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == hashed_password:
                print("Login successful!")
                return
    print("Login failed: Incorrect username or password.")

# Main function to run the authentication system
def main():
    while True:
        print("User Authentication System")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            log_in()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()