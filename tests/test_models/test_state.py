#!/usr/bin/python3
""" """
import unittest
from models.state import State
from models.city import City

class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertTrue(hasattr(state, 'cities'))

    def test_relationship(self):
        state = State()
        self.assertTrue(hasattr(state, 'cities'))
        self.assertIsInstance(state.cities, relationship)
        self.assertEqual(state.cities.property.mapper.class_, City)

    def test_getter_method(self):
        # Assuming HBNB_TYPE_STORAGE environment variable is set
        # appropriately for testing purposes
        state = State()
        cities = state.cities
        self.assertIsInstance(cities, list)
        # Add more assertions based on your expected behavior

    def test_docstrings(self):
        self.assertIsNotNone(State.__doc__)
        # Add more assertions for other methods and classes if needed

if __name__ == '__main__':
    unittest.main()
