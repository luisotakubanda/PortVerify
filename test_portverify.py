# test_portverify.py
"""
Tests for PortVerify module.
"""

import unittest
from portverify import PortVerify

class TestPortVerify(unittest.TestCase):
    """Test cases for PortVerify class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortVerify()
        self.assertIsInstance(instance, PortVerify)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortVerify()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
