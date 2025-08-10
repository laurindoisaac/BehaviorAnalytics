# test_behavioranalytics.py
"""
Tests for BehaviorAnalytics module.
"""

import unittest
from behavioranalytics import BehaviorAnalytics

class TestBehaviorAnalytics(unittest.TestCase):
    """Test cases for BehaviorAnalytics class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BehaviorAnalytics()
        self.assertIsInstance(instance, BehaviorAnalytics)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BehaviorAnalytics()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
