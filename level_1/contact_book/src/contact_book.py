from collections import defaultdict
from typing import Dict, Optional

from colorama import Fore, Style
from prettytable import PrettyTable, TableStyle

class ContactBook:
    def __init__(self) -> None:
        """
        Initialize a new ContactBook.

        Uses a defaultdict to store contacts where each contact name maps
        to a dictionary containing their phone number and email address.
        """
        self.contacts = defaultdict(dict)

    def add_contact(self,name: str,phone: str, email: Optional[str] =None) -> None:
        """
        Add a new contact to the contact book.

        """
        if name in self.contacts.keys() :
            print("Contact Already Exist")
            return
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email

    def view_contacts(self):
        """ 
        Display all contacts in a table.
        """
        table = PrettyTable()
        table.field_names = ["Contact Name", "Phone", "Email"]
        for name, info in self.contacts.items():
            colored_name = f"{Fore.CYAN}{name}{Style.RESET_ALL}"
            colored_phone = f"{Fore.YELLOW}{info['phone']}{Style.RESET_ALL}"
            colored_email = f"{Fore.GREEN}{info['email']}{Style.RESET_ALL}"
            table.add_row([colored_name, colored_phone, colored_email])
        table.sortby = "Contact Name"
        table.set_style(TableStyle.SINGLE_BORDER)
        print (table)
    
    def delete_contact(self, name: str) -> None:
        """ 
        Delete a contact by name.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")
    
    def update_contact(self, name: str, phone: Optional[str] = None,
                       email: Optional[str] = None) -> None:
        """ Update an existing contact's information
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print("Contact updated successfully")
        else:
            print("Contact not found")