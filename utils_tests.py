import unittest
from utils import utils

class UtilsTests(unittest.TestCase):
    
    def setUp(self):
        self.u = utils()
        
    # Unit tests for Utils to check invalid input type and functionality
    def test_reverse_int(self):
        self.assertEqual(self.u.reversed(1234), 4321)
    
    def test_reverse_float(self):
        with self.assertRaises(TypeError):
            self.u.reversed(3.1415926)
            
    def test_reverse_string(self):
        with self.assertRaises(TypeError):
            self.u.reversed("Hello")
    
    # Unit tests for formatter functionality and invalid input type
    def test_format_int(self):
        self.assertEqual(self.u.formatter(10), ("0b1010", "0o12"))
    
    def test_format_float(self):
        with self.assertRaises(TypeError):
            self.u.formatter(2026.914)
    
    def test_format_string(self):
        with self.assertRaises(TypeError):
            self.u.formatter("YilingZha")
            

if __name__ == "__main__":
    unittest.main()
    
    
    