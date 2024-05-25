import unittest
from generation import Generation

class TestGeneration(unittest.TestCase):
    def test_determine_generation(self):
        self.assertEqual(Generation.determine_generation(1925), "Silent Generation")
        self.assertEqual(Generation.determine_generation(1945), "Silent Generation")
        self.assertEqual(Generation.determine_generation(1965), "Generation X")
        self.assertEqual(Generation.determine_generation(1985), "Millennials")
        self.assertEqual(Generation.determine_generation(2000), "Generation Z")
        self.assertEqual(Generation.determine_generation(2015), "Generation Alpha")
        self.assertEqual(Generation.determine_generation(1900), "Unknown Generation")
        self.assertEqual(Generation.determine_generation(2025), "Unknown Generation")

if __name__ == '__main__':
    unittest.main()
