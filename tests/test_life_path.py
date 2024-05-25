import unittest
from life_path import LifePath

class TestLifePath(unittest.TestCase):
    def test_calculate_life_path_number(self):
        self.assertEqual(LifePath.calculate_life_path_number("1990-12-17"), 3)
        self.assertEqual(LifePath.calculate_life_path_number("2000-01-01"), 4)
        self.assertEqual(LifePath.calculate_life_path_number("1963-07-11"), 11)
        self.assertEqual(LifePath.calculate_life_path_number("1988-08-08"), 22)
        self.assertEqual(LifePath.calculate_life_path_number("1977-07-07"), 33)

if __name__ == '__main__':
    unittest.main()
