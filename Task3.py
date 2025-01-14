# Implement-a-Simple-Contact-Management-System
import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    print()

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Editing {name}. Leave fields blank to keep existing values.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    save_contacts(contacts)
    print("Contact updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    save_contacts(contacts)
    print("Contact deleted successfully.")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
          
