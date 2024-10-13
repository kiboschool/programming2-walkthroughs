
from phonebook import add_contact, find_contact, block_contact, \
    update_contact_number, list_contacts

def run_interface():
    contacts = {}
    blocked_contacts = {}
    
    # by default, the program doesn't include blocked contacts,
    # but it can be configured to include them.
    include_blocked_contacts = False
    while True:
        print('\nMenu')
        print('1. Add a contact')
        print('2. Find a contact')
        print('3. Update a contact')
        print('4. Block a contact')
        print('5. List all contacts')
        print('6. Include blocked contacts')
        print('7. Don\'t include blocked contacts')
        print('8. Exit')

    
        choice = input('Enter your choice: ')
        if choice.isnumeric():
            choice = int(choice)

        if choice == 1:
            name = input('Enter name: ')
            number = input('Enter a phone number: ')
            print(add_contact(contacts, name, number))
        elif choice == 2:
            name = input('Enter name: ')
            print(find_contact(contacts, blocked_contacts, include_blocked_contacts, name))
        elif choice == 3:
            name = input('Enter name: ')
            number = input('Enter a phone number: ')
            print(update_contact_number(contacts, blocked_contacts, name, number))
        elif choice == 4:
            name = input('Enter name: ')
            print(block_contact(contacts, blocked_contacts, name))
        elif choice == 5:
            print(list_contacts(contacts, blocked_contacts, include_blocked_contacts))
        elif choice == 6:
            include_blocked_contacts = True
            print('We will now include blocked contacts')
        elif choice == 7:
            include_blocked_contacts = False
            print('We will now not include blocked contacts')
        elif choice == 8:
            break
        else:
            print("Unrecognized option.")

        input("Press Enter to continue.")

if __name__ == "__main__":
    run_interface()

