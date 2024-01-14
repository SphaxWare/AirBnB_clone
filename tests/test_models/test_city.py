#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the CityModel class."""
    def test_city_instantiation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
