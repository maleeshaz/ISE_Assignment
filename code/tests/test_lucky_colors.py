import unittest
from luck_colors import LuckyColour

class TestLuckyColour(unittest.TestCase):
    def test_get_lucky_colour(self):
        self.assertEqual(LuckyColour.get_lucky_colour(1), "Red")
        self.assertEqual(LuckyColour.get_lucky_colour(11), "Silver")
        self.assertEqual(LuckyColour.get_lucky_colour(22), "Brown")
        self.assertEqual(LuckyColour.get_lucky_colour(33), "White")
        self.assertEqual(LuckyColour.get_lucky_colour(7), "Violet")

if __name__ == '__main__':
    unittest.main()
