#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the AmenityModel class."""
    def test_amenity_instantiation(self):
        amenity = Amenity()
        # ... (rest of the test methods for Amenity)

if __name__ == "__main__":
    unittest.main()
