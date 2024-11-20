# A class to allow us to pickup and put down named things...
# Backpack is limited to number of items set by capacity

class Backpack:
    """A class to store and retrieve named items with a set capacity."""
    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity

    def add_item(self, to_add):
        """Adds an item to our backpack."""
        if len(self.contents) < self.capacity:
            self.contents.append(to_add)
            return True
        else:
            return False

    def remove_item(self, to_remove):
        """Removes an item from our backpack.
           Throws a ValueError exception if the item is not in the list.
        """
        self.contents.remove(to_remove)

    def check_item(self, to_check):
        """Returns true if item is in backpack, false otherwise."""
        return to_check in self.contents
