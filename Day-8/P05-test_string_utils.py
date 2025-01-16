import unittest
from string_utils import is_palindrome

class TestStringUtils(unittest.TestCase):
    def test_palindrome_01(self):
        self.assertTrue(is_palindrome("madam"))
    # def test_02(self):
        self.assertFalse(is_palindrome("world"))
        # Test for edge cases
    # def test_03(self):
        self.assertTrue(is_palindrome(""))  # Empty string is considered a palindrome
        self.assertTrue(is_palindrome("a"))  # Single character is a palindrome
        self.assertFalse(is_palindrome("ab")) 
if __name__=="__main__":
    unittest.main()