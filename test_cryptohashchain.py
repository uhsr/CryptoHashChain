# test_cryptohashchain.py
"""
Tests for CryptoHashChain module.
"""

import unittest
from cryptohashchain import CryptoHashChain

class TestCryptoHashChain(unittest.TestCase):
    """Test cases for CryptoHashChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoHashChain()
        self.assertIsInstance(instance, CryptoHashChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoHashChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
