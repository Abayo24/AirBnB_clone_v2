#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up test resources."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down test resources."""
        del self.amenity

    def test_instance(self):
        """Test instantiation of Amenity."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attribute(self):
        """Test the name attribute."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.name, str)

    def test_place_amenities_relationship(self):
        """Test the place_amenities relationship."""
        self.assertTrue(hasattr(self.amenity, 'place_amenities'))
        self.assertEqual(self.amenity.place_amenities, [])

    def test_amenity_str_representation(self):
        """Test the __str__ method of Amenity."""
        expected_str = "[{}] ({}) {}".format(
            self.amenity.__class__.__name__, self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_amenity_docstring(self):
        """Test if Amenity class and its methods have docstrings."""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)

if __name__ == '__main__':
    unittest.main()

