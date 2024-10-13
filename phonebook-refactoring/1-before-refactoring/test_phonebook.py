
import unittest
from phonebook import add_contact, find_contact, block_contact, update_contact_number, list_contacts


class TestAddressBook(unittest.TestCase):
    def test_search_name(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        found = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'Adam')
        self.assertEqual('01 111 1234', found)

    def test_search_non_existent(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        found = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'William')
        self.assertEqual('William not found', found)

    def test_search_blocked_and_included(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        include_blocked_contacts = True
        found = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'David')
        self.assertEqual('04 444 1234', found)

    def test_search_blocked_and_not_included(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        include_blocked_contacts = False
        found = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'David')
        self.assertEqual('David not found', found)

    def test_update(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = update_contact_number(contacts, blocked_contacts, 'Adam', '01 111 5555')
        self.assertEqual('Adam updated', result)

    def test_update_blocked(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = update_contact_number(contacts, blocked_contacts, 'David', '09 999 5555')
        self.assertEqual('David updated', result)

    def test_update_non_existent(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = update_contact_number(contacts, blocked_contacts, 'William', '09 999 5555')
        self.assertEqual('William not found', result)
   
    def test_block_name(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        include_blocked_contacts = False

        # at first, it will be found
        result = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'Adam')
        self.assertEqual('01 111 1234', result)

        # now block it
        result = block_contact(contacts, blocked_contacts, 'Adam')
        self.assertEqual('Adam blocked', result)

        # because it's blocked, now it won't be found
        result = find_contact(contacts, blocked_contacts, include_blocked_contacts,  'Adam')
        self.assertEqual('Adam not found', result)

    def test_block_non_existent_name(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = block_contact(contacts, blocked_contacts, 'William')
        self.assertEqual('William not found', result)

    def test_block_already_blocked_name(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = block_contact(contacts, blocked_contacts, 'Adam')
        self.assertEqual('Adam blocked', result)
        result = block_contact(contacts, blocked_contacts, 'Adam')
        self.assertEqual('Adam not found', result)

    def test_list_including_blocked(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        include_blocked_contacts = True
        result = list_contacts(contacts, blocked_contacts, include_blocked_contacts)
        self.assertEqual('Adam: 01 111 1234\nBetty: 02 222 1234\nCarl: 03 333 1234\nDavid: 04 444 1234\n', result)

    def test_list_not_including_blocked(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        include_blocked_contacts = False
        result = list_contacts(contacts, blocked_contacts, include_blocked_contacts)
        self.assertEqual('Adam: 01 111 1234\nBetty: 02 222 1234\nCarl: 03 333 1234\n', result)
    
    def test_add_name(self):
        contacts, blocked_contacts, include_blocked_contacts = create_example()
        result = add_contact(contacts, 'Emily', '07 777 1234')
        self.assertEqual('Emily added', result)
        found = find_contact(contacts, blocked_contacts, include_blocked_contacts, 'Emily')
        self.assertEqual('07 777 1234', found)



def create_example():
    contacts = {}
    blocked_contacts = {}
    include_blocked_contacts = False
    
    # add some example names
    add_contact(contacts, 'Adam', '01 111 1234')
    add_contact(contacts, 'Betty', '02 222 1234')
    add_contact(contacts, 'Carl', '03 333 1234')
    add_contact(contacts, 'David', '04 444 1234')
    block_contact(contacts, blocked_contacts, 'David')
    return contacts, blocked_contacts, include_blocked_contacts

if __name__ == '__main__':
    unittest.main()

