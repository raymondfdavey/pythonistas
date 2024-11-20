"""
A simple contacts application

In this example, we refactor the code to use Object Oriented Programming. This
results in a more elegent program without the need for any global variables.
"""


class ContactsBook:
    """A simple contacts application."""
    def __init__(self, contacts=None):
        """
        Data is stored in the contacts attribute. 
        This is a dictionary where the key is a person's name. 
        The associated value in each case is a 3-tuple of the form:
        (email, position, extension).
        """
        if contacts is None:
            self.contacts = {}
        else:
            self.contacts = contacts

    def list_all_contacts(self):
        """Iterate through the dictionary to show all contacts."""
        for k, v in self.contacts.items():
            email, position, extension = v  # Unpack the tuple
            print(f'{k}: email: {email}, position: {position}, ext: {extension}')
        print("-" * 20)  # Print a line to separate the output

    def add_new_contact(self, name, email, position, extension):
        """Add a new key/value pairing to the dictionary."""
        self.contacts[name] = (email, position, extension)

    def search_by_name(self, name):
        """Search for person by name and display contact details."""
        if name in self.contacts:  # Check if key is in the dictionary
            v = self.contacts[name]
            email, position, extension = v
            print(f'{name}: email: {email}, position: {position}, ext: {extension}')
        else:
            print(f'Sorry, {name} not in the contacts list')
        print("-" * 20)  # Print a line to separate the output

    def print_all_keys(self):
        """Print all keys in the dictionary."""
        for k in self.contacts:  # Iterate through the keys
            print(k)
        print("-" * 20)  # Print a line to separate the output


def main():

    # We could have kept the initial contacts in the class as a setup_contacts
    # method, but it's better to be explicit about what we're doing here...
    initial_contacts = {
                'jane': ('jane@acme.com', 'manager', 1546),
                'rod': ('rod@acme.com', 'programmer', 8724),
                'freddy': ('freddy@acme.com', 'support', 8524)
            }

    cb = ContactsBook(initial_contacts)

    cb.list_all_contacts()

    cb.add_new_contact('samira', 'samira@acme.com', 'legal', 6245)
    cb.add_new_contact('john', 'john@acme.com', 'maintenance', 6134)
    cb.list_all_contacts()

    cb.search_by_name('freddy')
    cb.search_by_name('samira')
    cb.search_by_name('david')  # Not in our contacts list...

    # Print out all keys to confirm...
    cb.print_all_keys()

if __name__ == "__main__":
    main()
