import unittest
from phonebook import Phonebook


class TestAddressBook(unittest.TestCase):
    def test_search_name(self):
        phonebook = create_example()
        found = phonebook.find_contact('Adam')
        self.assertEqual('01 111 1234', found)

    def test_search_non_existent(self):
        phonebook = create_example()
        found = phonebook.find_contact('William')
        self.assertEqual('William not found', found)

    def test_search_blocked_and_included(self):
        phonebook = create_example()
        phonebook.include_blocked_contacts = True
        found = phonebook.find_contact('David')
        self.assertEqual('04 444 1234', found)

    def test_search_blocked_and_not_included(self):
        phonebook = create_example()
        phonebook.include_blocked_contacts = False
        found = phonebook.find_contact('David')
        self.assertEqual('David not found', found)

    def test_update(self):
        phonebook = create_example()
        result = phonebook.update_contact_number('Adam', '01 111 5555')
        self.assertEqual('Adam updated', result)

    def test_update_blocked(self):
        phonebook = create_example()
        result = phonebook.update_contact_number('David', '09 999 5555')
        self.assertEqual('David updated', result)

    def test_update_non_existent(self):
        phonebook = create_example()
        result = phonebook.update_contact_number('William', '09 999 5555')
        self.assertEqual('William not found', result)
   
    def test_block_name(self):
        phonebook = create_example()
        include_blocked_contacts = False

        # at first, it will be found
        result = phonebook.find_contact('Adam')
        self.assertEqual('01 111 1234', result)

        # now block it
        result = phonebook.block_contact('Adam')
        self.assertEqual('Adam blocked', result)

        # because it's blocked, now it won't be found
        result = phonebook.find_contact( 'Adam')
        self.assertEqual('Adam not found', result)

    def test_block_non_existent_name(self):
        phonebook = create_example()
        result = phonebook.block_contact('William')
        self.assertEqual('William not found', result)

    def test_block_already_blocked_name(self):
        phonebook = create_example()
        result = phonebook.block_contact('Adam')
        self.assertEqual('Adam blocked', result)
        result = phonebook.block_contact('Adam')
        self.assertEqual('Adam not found', result)

    def test_list_including_blocked(self):
        phonebook = create_example()
        phonebook.include_blocked_contacts = True
        result = phonebook.list_contacts()
        self.assertEqual('Adam: 01 111 1234\nBetty: 02 222 1234\nCarl: 03 333 1234\nDavid: 04 444 1234', result.strip())

    def test_list_not_including_blocked(self):
        phonebook = create_example()
        phonebook.include_blocked_contacts = False
        result = phonebook.list_contacts()
        self.assertEqual('Adam: 01 111 1234\nBetty: 02 222 1234\nCarl: 03 333 1234', result.strip())
    
    def test_add_name(self):
        phonebook = create_example()
        result = phonebook.add_contact('Emily', '07 777 1234')
        self.assertEqual('Emily added', result)
        found = phonebook.find_contact('Emily')
        self.assertEqual('07 777 1234', found)


def create_example():
    phonebook = Phonebook()
    
    # add some example names
    phonebook.add_contact('Adam', '01 111 1234')
    phonebook.add_contact('Betty', '02 222 1234')
    phonebook.add_contact('Carl', '03 333 1234')
    phonebook.add_contact('David', '04 444 1234')
    phonebook.block_contact('David')
    return phonebook

if __name__ == '__main__':
    unittest.main()

