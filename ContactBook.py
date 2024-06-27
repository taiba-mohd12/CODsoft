class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'Name': name,
            'Phone Number': phone_number,
            'Email': email,
            'Address': address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!\n")

    def view_contact_list(self):
        print("\nContact List:")
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact['Name']} - {contact['Phone Number']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts
                   if query.lower() in contact['Name'].lower() or
                   query in contact['Phone Number']]
        
        if not results:
            print(f"No contacts found for '{query}'.")
        else:
            print("\nSearch Results:")
            for result in results:
                print(f"{result['Name']} - {result['Phone Number']}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact['Name'] == name:
                contact['Phone Number'] = new_phone_number
                contact['Email'] = new_email
                contact['Address'] = new_address
                print(f"Contact '{name}' updated successfully!\n")
                return
        print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['Name'] == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!\n")
                return
        print(f"No contact found with the name '{name}'.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "_main_":
    main()