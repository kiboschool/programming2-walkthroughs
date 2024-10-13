
from phonebook import Phonebook

def run_interface():

    phonebook = Phonebook()
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
            print(phonebook.add_contact(name, number))
        elif choice == 2:
            name = input('Enter name: ')
            print(phonebook.find_contact(name))
        elif choice == 3:
            name = input('Enter name: ')
            number = input('Enter a phone number: ')
            print(phonebook.update_contact_number(name, number))
        elif choice == 4:
            name = input('Enter name: ')
            print(phonebook.block_contact(name))
        elif choice == 5:
            print(phonebook.list_contacts())
        elif choice == 6:
            phonebook.include_blocked_contacts = True
            print('We will now include blocked contacts')
        elif choice == 7:
            phonebook.include_blocked_contacts = False
            print('We will now not include blocked contacts')
        elif choice == 8:
            break
        else:
            print("Unrecognized option.")

        input("Press Enter to continue.")

if __name__ == "__main__":
    run_interface()

