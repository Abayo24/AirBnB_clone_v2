#!/usr/bin/python3
""" """
import unittest
from models.user import User
from models.place import Place
from models.review import Review

class TestUser(unittest.TestCase):
    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertTrue(hasattr(user, 'places'))
        self.assertTrue(hasattr(user, 'reviews'))

    def test_relationships(self):
        user = User()
        self.assertIsInstance(user.places, relationship)
        self.assertEqual(user.places.property.mapper.class_, Place)
        self.assertIsInstance(user.reviews, relationship)
        self.assertEqual(user.reviews.property.mapper.class_, Review)

    def test_docstrings(self):
        self.assertIsNotNone(User.__doc__)
        # Add more assertions for other methods and classes if needed

if __name__ == '__main__':
    unittest.main()

