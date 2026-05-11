# test_chitoken.py
"""
Tests for ChiToken module.
"""

import unittest
from chitoken import ChiToken

class TestChiToken(unittest.TestCase):
    """Test cases for ChiToken class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChiToken()
        self.assertIsInstance(instance, ChiToken)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChiToken()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
