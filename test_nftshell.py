# test_nftshell.py
"""
Tests for NftShell module.
"""

import unittest
from nftshell import NftShell

class TestNftShell(unittest.TestCase):
    """Test cases for NftShell class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftShell()
        self.assertIsInstance(instance, NftShell)

    def test_run_method(self):
        """Test the run method."""
        instance = NftShell()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
