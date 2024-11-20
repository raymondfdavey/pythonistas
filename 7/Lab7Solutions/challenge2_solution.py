# A unit test class for the online shopping application...
# Place this file in the same directory as challenge2.py so that the
# interpreter can find the class to import.

import unittest

from challenge2 import Customer, Item


class TestShoppingApplication(unittest.TestCase):

    def setUp(self):
        self.c1 = Customer('bob', 'bob@acme.com')
        self.c2 = Customer('alice', 'alice@acme.com')
        self.c3 = Customer('jimmy', 'jimmy@acme.com')
        self.i1 = Item('small table', 50.0)
        self.i2 = Item('table lamp', 30.0)
        self.i3 = Item('rug', 100.0)

    def tearDown(self):
        del self.c1
        del self.c2
        del self.i1
        del self.i2
        del self.i3

    # First test case...
    def test_1(self):
        self.c1.buy_item(self.i1)
        self.c1.buy_item(self.i2)
        self.c2.buy_item(self.i1)
        self.c2.buy_item(self.i3)

        self.assertEqual(self.c1.show_cost(), 80.0)
        self.assertEqual(self.c2.show_cost(), 150.00)
        self.assertEqual(self.c3.show_cost(), 0.0)

        self.assertTrue(self.c1.remove_item(self.i1))
        self.assertFalse(self.c1.remove_item(self.i3))
        self.assertTrue(self.c1.remove_item_by_name('table lamp'))
        self.assertTrue(self.c2.remove_item_by_name('small table'))
        self.assertEqual(self.c1.show_cost(), 0.0)
        self.assertEqual(self.c2.show_cost(), 100.0)

    # Second test case...
    def test_2(self):
        self.c1.buy_item(self.i1)
        self.c1.buy_item(self.i2)
        self.c2.buy_item(self.i1)
        self.c2.buy_item(self.i3)
        self.c3.buy_item(self.i3)

        self.i3.change_name('red rug')
        self.assertEqual(self.i3.name, 'red rug')
        self.assertEqual(self.c1.show_cost(), 80.0)
        self.assertEqual(self.c2.show_cost(), 150.0)
        self.assertEqual(self.c3.show_cost(), 100.0)
        self.assertTrue(self.c1.discount_basket(10.0))
        self.assertEqual(self.c1.show_cost(), 72.0)
        self.assertFalse(self.c2.discount_basket(60.0))
        self.assertEqual(self.c2.show_cost(), 150.0)
