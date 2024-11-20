# A unit test class for the contacts class...
# Place this file in the same directory as challenge1.py so that the
# interpreter can find the class to import.

import unittest

from challenge1 import ContactsBook


class TestContactsBook(unittest.TestCase):

    def setUp(self):
        self.b1 = ContactsBook()

    def tearDown(self):
        del self.b1  # Clears the old object away ready for the next test case

    # First test case...
    def test_1(self):
        # Add a new contact
        self.assertTrue(self.b1.add_new_contact('william', 'will@acme.com', 'junior', 1234))
        self.assertEqual(self.b1.get_number_of_contacts(), 4)

        # Try to add the same contact again...
        self.assertFalse(self.b1.add_new_contact('william', 'will@acme.com', 'junior', 1234))
        self.assertEqual(self.b1.get_number_of_contacts(), 4)

    # Second test case...
    def test_2(self):

        # Get an email adddress for rod...
        self.assertEqual(self.b1.get_email('rod'), 'rod@acme.com')

        # Try change rod's email address...
        self.assertTrue(self.b1.update_email('rod', 'roddy@acme.com'))

        # Check it...
        self.assertEqual(self.b1.get_email('rod'), 'roddy@acme.com')

        # Look up rod by name...
        self.assertTrue(self.b1.search_by_name('rod'))

        # Look up an unknown person...
        self.assertFalse(self.b1.search_by_name('joshua'))
