import unittest
from master_number import MasterNumber
from generation import Generation
from validation import Validation

class TestNumerologyApp(unittest.TestCase):

    def setUp(self):
        self.numerology = MasterNumber()
        self.generation = Generation()
        self.validator = Validation()

    # Black-Box Tests
    def test_life_path_number_valid(self):
        self.assertEqual(self.numerology.calculate_life_path_number("1990-07-25"), 6)
        self.assertEqual(self.numerology.calculate_life_path_number("2000-02-29"), 5)

    def test_life_path_number_invalid(self):
        with self.assertRaises(ValueError):
            self.numerology.calculate_life_path_number("2025-07-25")
        with self.assertRaises(ValueError):
            self.numerology.calculate_life_path_number("1990-13-25")

    def test_master_number(self):
        self.assertTrue(self.numerology.is_master_number(11))
        self.assertFalse(self.numerology.is_master_number(10))

    def test_lucky_colour(self):
        self.assertEqual(self.numerology.get_lucky_colour(1), "Red")
        self.assertEqual(self.numerology.get_lucky_colour(6), "Green")

    def test_generation(self):
        self.assertEqual(self.generation.get_generation("1990-07-25"), "Millennials")
        self.assertEqual(self.generation.get_generation("1975-04-20"), "Generation X")

    # White-Box Tests
    def test_date_validation_valid(self):
        self.assertTrue(self.validator.validate_date("1990-07-25"))
        self.assertTrue(self.validator.validate_date("2000-02-29"))

    def test_date_validation_invalid(self):
        self.assertFalse(self.validator.validate_date("2025-07-25"))
        self.assertFalse(self.validator.validate_date("1990-13-25"))

    def test_edge_cases(self):
        self.assertEqual(self.numerology.calculate_life_path_number("1901-01-01"), 4)
        self.assertEqual(self.numerology.calculate_life_path_number("2024-12-31"), 5)
        self.assertEqual(self.generation.get_generation("1945-12-31"), "Silent Generation")

if __name__ == "__main__":
    unittest.main()
