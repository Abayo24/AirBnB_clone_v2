#!/usr/bin/python3
""" """
import unittest
from models.review import Review
from models.place import Place
from models.user import User

class TestReview(unittest.TestCase):
    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_relationships(self):
        review = Review()
        self.assertIsInstance(review.place, relationship)
        self.assertEqual(review.place.property.mapper.class_, Place)
        self.assertIsInstance(review.user, relationship)
        self.assertEqual(review.user.property.mapper.class_, User)

    def test_docstrings(self):
        self.assertIsNotNone(Review.__doc__)
        # Add more assertions for other methods and classes if needed

if __name__ == '__main__':
    unittest.main()

