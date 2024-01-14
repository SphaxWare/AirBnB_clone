#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the ReviewModel class."""
    def test_review_instantiation(self):
        review = Review()
        # ... (rest of the test methods for Review)

if __name__ == "__main__":
    unittest.main()
