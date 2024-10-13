

class Phonebook:
    def __init__(self):
        self.contacts = {}
        
        # by default, the program doesn't include blocked contacts,
        # but it can be configured to include them.
        self.include_blocked_contacts = False
        
    def add_contact(self, name, number):
        self.contacts[name] = {
            'number': number,
            'is_blocked': False,
        }
        
        return f"{name} added"

    def find_contact(self, name):
        if name in self.contacts:
            if (self.include_blocked_contacts or not self.contacts[name]['is_blocked']):
                return self.contacts[name]['number']
            else:
                return f"{name} not found"
        else:
            return f"{name} not found"


    def block_contact(self, name):
        if name in self.contacts:
            if (self.contacts[name]['is_blocked']):
                return f"{name} not found"
                
            self.contacts[name]['is_blocked'] = True
            return f"{name} blocked"
        else:
            return f"{name} not found"
    
    def update_contact_number(self, name, number):
        if name in self.contacts:
            self.contacts[name]['number'] = number
            return f"{name} updated"
        else:
            return f"{name} not found"

    def list_contacts(self):
        result = ""
        for name in self.contacts:
            contact = self.contacts[name]
            if self.include_blocked_contacts or not contact['is_blocked']:
                result += f"\n{name}: {contact['number']}"
        

        return result


