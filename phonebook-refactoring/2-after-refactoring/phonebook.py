

class Phonebook:
    def __init__(self):
        self.contacts = {}
        self.blocked_contacts = {}
        
        # by default, the program doesn't include blocked contacts,
        # but it can be configured to include them.
        self.include_blocked_contacts = False
        
    def add_contact(self, name, number):
        self.contacts[name] = number
        return f"{name} added"

    def find_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        
        if self.include_blocked_contacts:
            if name in self.blocked_contacts:
                return self.blocked_contacts[name]

        return f"{name} not found"


    def block_contact(self, name):
        if name in self.contacts:
            number = self.contacts[name]
            self.blocked_contacts[name] = number
            del self.contacts[name]
            return f"{name} blocked"
        else:
            return f"{name} not found"
        
    def update_contact_number(self, name, number):
        if name in self.contacts:
            self.contacts[name] = number
            return f"{name} updated"
        
        if name in self.blocked_contacts:
            self.blocked_contacts[name] = number
            return f"{name} updated"

        return f"{name} not found"

    def list_contacts(self):
        result = ""
        for name in self.contacts:
            number = self.contacts[name]
            result += f"{name}: {number}\n"
        
        if self.include_blocked_contacts:
            for name in self.blocked_contacts:
                number = self.blocked_contacts[name]
                result += f"{name}: {number}\n"

        return result


