# Initialize an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

# Function to search for a contact by name or phone number
def search_contact(query):
    results = []
    for contact in contacts:
        if query in contact["Name"] or query in contact["Phone"]:
            results.append(contact)
    return results

# Function to update contact details
def update_contact(index, name, phone, email, address):
    contact = contacts[index]
    contact["Name"] = name
    contact["Phone"] = phone
    contact["Email"] = email
    contact["Address"] = address
    print("Contact updated successfully!")

# Function to delete a contact
def delete_contact(index):
    del contacts[index]
    print("Contact deleted successfully!")

# User interface
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("\nSearch Results:")
            for index, contact in enumerate(results, start=1):
                print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")
        else:
            print("No matching contacts found.")
    elif choice == "4":
        view_contacts()
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            update_contact(index, name, phone, email, address)
        else:
            print("Invalid index. Please enter a valid index.")
    elif choice == "5":
        view_contacts()
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            delete_contact(index)
        else:
            print("Invalid index. Please enter a valid index.")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please select a valid option.")
