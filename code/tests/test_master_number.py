import unittest
from master_number import MasterNumber

class TestMasterNumber(unittest.TestCase):
    def test_is_master_number(self):
        self.assertTrue(MasterNumber.is_master_number(11))
        self.assertTrue(MasterNumber.is_master_number(22))
        self.assertTrue(MasterNumber.is_master_number(33))
        self.assertFalse(MasterNumber.is_master_number(10))
        self.assertFalse(MasterNumber.is_master_number(7))

if __name__ == '__main__':
    unittest.main()
