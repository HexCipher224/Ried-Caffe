import unittest

from utils.validators import validate_name, validate_price


class TestInventory(unittest.TestCase):


    def test_item_name(self):

        self.assertTrue(validate_name("Coffee"))



    def test_empty_name(self):

        self.assertFalse(validate_name(""))



    def test_valid_price(self):

        self.assertTrue(validate_price(250))



    def test_negative_price(self):

        self.assertFalse(validate_price(-50))



if __name__ == "__main__":
    unittest.main()