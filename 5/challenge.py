# You need to create the 8 classes complete with their attributes and methods.


class Customer:
    def __init__(self, name, discount):
        self.name = name
        self.loyaltyDiscount = discount
    
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.itemsOrdered = []
        self.cost = 0
        
    def addToOrder(self, item):
        self.itemsOrdered.append(item)
        if self.customer.loyaltyDiscount:
            self.cost += (item.price - item.discount)
        else:
            self.cost += item.price
        
    def summariseOrder(self):
        print("ORDER SUMMARY")
        print(f"Order for {self.customer.name}:")
        print(f"{len(self.itemsOrdered)} items:")
        print("----------")
        for item in self.itemsOrdered:
            item.displayDetails()
        print("----------")
        print(f"TOTAL COST = £{self.cost}")
        if self.customer.loyaltyDiscount:
            print(f"Today your discount got you {str(sum([item.discount for item in self.itemsOrdered]))}")
                
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Drink(Item):
    
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
        self.discount = 0.10

    
class Tea(Drink):
    def __init__(self, name, price, size, flavour):
        super().__init__(name, price, size)
        self.flavour = flavour
    def displayDetails(self):
        print("Tea:")
        print(f'    {self.name=}')
        print(f'    £{self.price=}')
        print(f'    {self.size=}')
        print(f'    {self.flavour=}')
    
class MineralWater(Drink):
    def __init__(self, name, price, size, isCarbonated):
        super().__init__(name, price, size)
        self.isCarbonated = isCarbonated
    def displayDetails(self):
        print("Mineral Water:")
        print(f'    {self.name=}')
        print(f'    £{self.price=}')
        print(f'    {self.size=}')
        print(f'    {self.isCarbonated=}')
    
class Cake(Item):
    def __init__(self, name, price, size, type, hasNuts):
        super().__init__(name, price)
        self.sliceSize = size
        self.type = type
        self.hasNuts = hasNuts
        self.discount = 0.00

    def displayDetails(self):
        print("Cake:")
        print(f'    {self.name=}')
        print(f'    £{self.price=}')
        print(f'    {self.sliceSize=}')
        print(f'    {self.type=}')
        if self.hasNuts:
            print(f'CAUTION, CAKE HAS NUTS')
        else:
            print("NO NUTS IN THIS CAKE")
    
class Sandwich(Item):
    def __init__(self, name, price, breadType, filling):
        super().__init__(name, price)
        self.breadType = breadType
        self.filling = filling
        self.discount = 0.20
        
    def displayDetails(self):
        print("Sandwich:")
        print(f'    {self.name=}')
        print(f'    £{self.price=}')
        print(f'    {self.breadType}')
        print(f'    {self.filling=}')

def main():
    # Create two customers...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items...
    order1 = Order(cust1)
    order1.addToOrder(Tea('Black tea', 2.00, 'large', 'Earl Gray'))
    order1.addToOrder(Sandwich('Club special', 4.50, 'brown', 'chicken'))

    order2 = Order(cust2)
    order2.addToOrder(MineralWater('Evian', 1.50, 'small', False))
    order2.addToOrder(Sandwich('Simple sandwich', 1.50, 'white', 'cheese'))
    order2.addToOrder(Cake('Chocolate dream', 2.30, 'medium', 'chocolate', True))

    # Summarise our orders...
    order1.summariseOrder()
    print()
    order2.summariseOrder()
    print()


if __name__ == "__main__":
    main()
