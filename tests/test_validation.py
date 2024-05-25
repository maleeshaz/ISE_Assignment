import unittest
from validation import Validation

class TestValidation(unittest.TestCase):
    def test_validate_date(self):
        self.assertTrue(Validation.validate_date("2000-01-01"))
        self.assertFalse(Validation.validate_date("1900-01-01"))
        self.assertFalse(Validation.validate_date("2025-01-01"))
        self.assertFalse(Validation.validate_date("2000-13-01"))
        self.assertFalse(Validation.validate_date("2000-01-32"))
        self.assertFalse(Validation.validate_date("2000/01/01"))

    def test_validate_year(self):
        self.assertTrue(Validation.validate_year("2000"))
        self.assertFalse(Validation.validate_year("1900"))
        self.assertFalse(Validation.validate_year("2025"))
        self.assertFalse(Validation.validate_year("abcd"))

if __name__ == '__main__':
    unittest.main()
