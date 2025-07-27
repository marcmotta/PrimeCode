# test_primecode.py
"""
Tests for PrimeCode module.
"""

import unittest
from primecode import PrimeCode

class TestPrimeCode(unittest.TestCase):
    """Test cases for PrimeCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeCode()
        self.assertIsInstance(instance, PrimeCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
