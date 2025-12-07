from contact_book import ContactBook
    

if __name__ == "__main__":
    book = ContactBook()
    while True:
        print("\nWelcom to contact book application")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contacts")
        print("4. Delete Contacts")
        print("5. Quit")

        user_choice = input("Please choose an option: ")

        if user_choice == "5":
            break
        elif user_choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            book.add_contact(name.capitalize(), phone, email)

        elif user_choice == "2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            book.update_contact(name.capitalize(), phone, email)

        elif user_choice == "3":
            print("List of contacts: ")
            book.view_contacts()
        
        elif user_choice == "4":
            name = input("Enter contact name: ")
            book.delete_contact(name.capitalize())