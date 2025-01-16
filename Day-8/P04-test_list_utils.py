import unittest
from list_utils import generate_list

class  TestListUtils(unittest.TestCase):
    def test_generate_list_01(self):
        self.assertListEqual(generate_list(5),[0,1,2,3,4])
    def test_generate_list_02(self):
        self.assertListEqual(generate_list(2),[0,1])
if __name__=="__main__":
    unittest.main()