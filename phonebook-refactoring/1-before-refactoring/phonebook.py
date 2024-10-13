
def add_contact(contacts, name, number):
    contacts[name] = number
    return f"{name} added"

def find_contact(contacts, blocked_contacts, include_blocked_contacts, name):
    if name in contacts:
        return contacts[name]
    
    if include_blocked_contacts:
        if name in blocked_contacts:
            return blocked_contacts[name]

    return f"{name} not found"


def block_contact(contacts, blocked_contacts, name):
    if name in contacts:
        number = contacts[name]
        blocked_contacts[name] = number
        del contacts[name]
        return f"{name} blocked"
    else:
        return f"{name} not found"
    
def update_contact_number(contacts, blocked_contacts, name, number):
    if name in contacts:
        contacts[name] = number
        return f"{name} updated"
    
    if name in blocked_contacts:
        blocked_contacts[name] = number
        return f"{name} updated"

    return f"{name} not found"

def list_contacts(contacts, blocked_contacts, include_blocked_contacts):
    result = ""
    for name in contacts:
        number = contacts[name]
        result += f"{name}: {number}\n"
    
    if include_blocked_contacts:
        for name in blocked_contacts:
            number = blocked_contacts[name]
            result += f"{name}: {number}\n"

    return result


