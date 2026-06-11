import unittest

from tools.validators import validate_quantity
from tools.helpers import calculate_change


class TestOrders(unittest.TestCase):

    def test_valid_quantity(self):
        self.assertTrue(validate_quantity(3))


    def test_invalid_quantity(self):
        self.assertFalse(validate_quantity(0))


    def test_change_calculation(self):
        change = calculate_change(500, 300)

        self.assertEqual(change, 200)



if __name__ == "__main__":
    unittest.main()