
# Contact Book Application

import json


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("Contacts saved successfully!")


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Load saved contacts
contacts = load_contacts()


# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully!")


# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")


# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ")

    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print("Contact not found!")


# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ")

    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact successfully deleted!")
    else:
        print("Contact not found!")


# Menu
def menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    return input("Enter your choice: ").strip()


# Main program
while True:
    user_choice = menu()

    if user_choice == "1":
        add_contact(contacts)
    elif user_choice == "2":
        view_contacts(contacts)
    elif user_choice == "3":
        search_contact(contacts)
    elif user_choice == "4":
        update_contact(contacts)
    elif user_choice == "5":
        delete_contact(contacts)
    elif user_choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
