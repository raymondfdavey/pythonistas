import unittest

class TestHigherThanFifty(unittest.TestCase):
    def test_basic_cases(self):
        # Test values above 50
        self.assertTrue(isHigherThanFifty(60))  # This will fail!
        self.assertTrue(isHigherThanFifty(100)) # This will fail!
        
        # Test values below 50
        self.assertFalse(isHigherThanFifty(40))  # This will fail!
        self.assertFalse(isHigherThanFifty(0))   # This will fail!
    
    def test_boundary_value(self):
        # Test the boundary value (50)
        self.assertFalse(isHigherThanFifty(50))  # This should work as is
    
    def test_negative_numbers(self):
        # Test negative numbers
        self.assertFalse(isHigherThanFifty(-10))  # This will fail!
    
    def test_types(self):
        # Test that it works with floats
        self.assertTrue(isHigherThanFifty(50.1))  # This will fail!
        
        # Test that it raises TypeError for invalid inputs
        with self.assertRaises(TypeError):
            isHigherThanFifty("51")
        with self.assertRaises(TypeError):
            isHigherThanFifty(None)



# bugs - mistakes in the functioning of your code - it doesn't do what you want

def isHigherThanFifty(x):
    if x < 50:
        return True
    else:
        return False

isHigherThanFifty(100)
# how to check this is doing what we want?


if __name__ == '__main__':
    unittest.main(failfast=False, verbosity=2)
    # unittest.main()