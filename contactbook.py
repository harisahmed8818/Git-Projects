import json
import os

# Function to load contacts from a JSON file
def load_contacts(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

# Function to save contacts to a JSON file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")

# Main function to run the contact book
def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {'phone': phone, 'email': email}
            save_contacts(filename, contacts)
            print(f"Contact '{name}' added.")

        elif choice == '2':
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"Found: {name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '3':
            name = input("Enter name to update: ")
            if name in contacts:
                phone = input("Enter new phone (leave blank to skip): ")
                email = input("Enter new email (leave blank to skip): ")
                if phone:
                    contacts[name]['phone'] = phone
                if email:
                    contacts[name]['email'] = email
                save_contacts(filename, contacts)
                print(f"Contact '{name}' updated.")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '4':
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                save_contacts(filename, contacts)
                print(f"Contact '{name}' deleted.")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '5':
            display_contacts(contacts)

        elif choice == '6':
            print("Exiting the contact book.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
