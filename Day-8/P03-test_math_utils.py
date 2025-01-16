import unittest
from Math_utils import add,subtract
class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(2,8),10)
    def test_sub(self):
        self.assertEqual(subtract(4,2),2)
        
if __name__ == "__main__":
    unittest.main()