import unittest

from backpack import Backpack


# Unit test class for Backpack.
# https://docs.python.org/3/library/unittest.html

class TestBackPack(unittest.TestCase):

    def setUp(self):  # Method called by unittest to prepare the test fixture.
        """Runs prior to each unit test method (optional)."""
        self.b1 = Backpack(3)

    def tearDown(self):  # Method called by unittest to after the test runs.
        """Runs after each unit test method (optional)."""
        self.b1.contents.clear()

    def test_1(self):
        """For ease here we define one unit test with lots of tests within it."""
        self.b1.add_item('book')
        self.b1.add_item('pen')
        self.assertTrue(self.b1.check_item('book'))
        self.assertTrue(self.b1.check_item('pen'))
        self.assertFalse(self.b1.check_item('balloon'))
        self.assertEqual(len(self.b1.contents), 2)
        self.assertTrue(self.b1.add_item('candle'))
        self.assertFalse(self.b1.add_item('map'))  # Capacity is 3
