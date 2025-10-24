
import json
import os
FILE_NAME = "contacts.json"
def load_contacts():
    """Load contacts from file if exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}
def save_contacts(contacts):
    """Save contacts to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)
def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    if name in contacts:
        print("⚠ Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")
def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("📭 No contacts available.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"- {name} | Phone: {info['phone']} | Email: {info['email']}")
        print()
def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the contact name to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Editing {name}...")
    phone = input(f"Enter new phone number (leave blank to keep {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email (leave blank to keep {contacts[name]['email']}): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print(f"Contact {name} updated successfully!")
def delete_contact(contacts):
    """Delete a contact by name."""
    name = input("Enter the contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")
def menu():
    """Main menu loop."""
    contacts = load_contacts()
    while True:
        print("\n==== Contact Management System ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save & Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


menu()