#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.place import Place

class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_relationship(self):
        city = City()
        self.assertIsInstance(city.places, relationship)
        self.assertEqual(city.places.property.mapper.class_, Place)

    # Add more tests for other methods or properties as needed

if __name__ == '__main__':
    unittest.main()

