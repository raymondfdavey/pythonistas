# A class to allow us to pickup and put down items...
# Backpack is limited to number of items set by capacity.
# This example incorporates a user defined exception.

class Backpack2:
    """A class to store and retrieve named items with a set capacity."""
    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity

    def add_item(self, item):
        """Adds an item to our backpack."""
        if len(self.contents) < self.capacity:
            self.contents.append(item)
            return True
        return False

    def remove_item(self, item):
        """Removes an item from our backpack."""
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            self.contents.remove(item)
        except NotInBackpackError:
            print('Exception handled here...')
        finally:
            print('Carrying on...')

    def check_item(self, item):
        """Returns True if item is in backpack, False otherwise."""
        return item in self.contents


class NotInBackpackError(Exception):
    def __init__(self, item, message):
        print(f'{item} {message}')


def main():
    b1 = Backpack2(3)
    b1.add_item('pen')
    b1.add_item('medkit')
    b1.remove_item('pen')
    b1.remove_item('sword')

if __name__ == '__main__':
    main()