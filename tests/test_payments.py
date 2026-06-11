import unittest

from utils.validators import validate_payment


class TestPayments(unittest.TestCase):


    def test_payment_success(self):

        result = validate_payment(500, 300)

        self.assertTrue(result)



    def test_payment_failure(self):

        result = validate_payment(100, 300)

        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()