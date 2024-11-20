class Customer:
    """A class to represent a customer for our cafe."""

    def __init__(self, name, loyalty_discount):
        self.name = name
        self.loyalty_discount = loyalty_discount

class Order:
    """A schedule of items ordered and the cost for a particular customer."""

    def __init__(self, customer):
        self.customer = customer
        self.items_ordered = []
        self.cost = 0.0

    def add_to_order(self, item):
        """Add an item to the order and update the cost."""
        self.items_ordered.append(item)
        self.cost += item.price

    def summarise_order(self):
        """Display a summary of the order, including any loyalty discount."""
        print(f'Customer: {self.customer.name}')
        print(f'Total items ordered: {len(self.items_ordered)}')
        for i in self.items_ordered:
            i.display_details()
        # Apply any loyalty discounts...
        if self.customer.loyalty_discount is True:
            savings = 0
            for i in self.items_ordered:
                savings += i.discount
            self.cost -= savings
            print(f'Today you saved £{savings:.2f}')
        print(f'Total cost: £{self.cost:.2f}')

class Item:
    """A super class for all food and drink that can be ordered in the cafe."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink(Item):
    """A sub class of Item and serves as a super class for all drink items we can purchase."""

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
        self.discount = 0.10

class Tea(Drink):
    """A sub class of Drink to represent a cup of tea that we can order."""

    def __init__(self, name, price, size, flavour):
        super().__init__(name, price, size)
        self.flavour = flavour

    def display_details(self):
        """Display details of the tea, including the flavour."""
        print(f'{self.name} £{self.price:.2f}, {self.size}, {self.flavour}')

class MineralWater(Drink):
    """A sub class of Drink to represent bottled water that we can order."""

    def __init__(self, name, price, size, is_carbonated):
        super().__init__(name, price, size)
        self.is_carbonated = is_carbonated

    def display_details(self):
        """Display details of the water, including whether it is carbonated."""
        print(f'{self.name} £{self.price:.2f}, {self.size}')
        if self.is_carbonated:
            print('Sparking water')
        else:
            print('Still water')

class Cake(Item):
    """A sub class of Item to represent a tasty item we can order."""

    def __init__(self, name, price, slice_size, kind, has_nuts):
        super().__init__(name, price)
        self.slice_size = slice_size
        self.kind = kind
        self.has_nuts = has_nuts
        self.discount = 0.0  # No discount on cakes

    def display_details(self):
        """Display details of the cake, including whether it contains nuts."""
        print(f'{self.name} £{self.price:.2f}, {self.slice_size}, {self.kind}')
        if self.has_nuts:
            print('Warning: contains nuts!')
        else:
            print('Free of nuts.')

class Sandwich(Item):
    """A sub class of Item to represent a tasty item we can order."""

    def __init__(self, name, price, bread_type, filling):
        super().__init__(name, price)
        self.bread_type = bread_type
        self.filling = filling
        self.discount = 0.20

    def display_details(self):
        """Display details of the sandwich, including the type of bread and filling."""
        print(f'{self.name} £{self.price:.2f}, {self.bread_type}, {self.filling} filling')


def main():
    # Create two customers...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items...
    order1 = Order(cust1)
    order1.add_to_order(Tea('Black tea', 2.00, 'large', 'Earl Gray'))
    order1.add_to_order(Sandwich('Club special', 4.50, 'brown', 'chicken'))

    order2 = Order(cust2)
    order2.add_to_order(MineralWater('Evian', 1.50, 'small', False))
    order2.add_to_order(Sandwich('Simple sandwich', 1.50, 'white', 'cheese'))
    order2.add_to_order(Cake('Chocolate dream', 2.30, 'medium', 'chocolate', True))

    # Summarise our orders...
    order1.summarise_order()
    print()
    order2.summarise_order()
    print()


if __name__ == "__main__":
    main()
