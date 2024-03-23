#!/usr/bin/python3
""" """
import unittest
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class TestPlace(unittest.TestCase):
    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))

    def test_relationships(self):
        place = Place()
        self.assertIsInstance(place.reviews, relationship)
        self.assertEqual(place.reviews.property.mapper.class_, Review)
        self.assertIsInstance(place.amenities, relationship)
        self.assertEqual(place.amenities.property.mapper.class_, Amenity)

    # Add more tests for other methods or properties as needed

if __name__ == '__main__':
    unittest.main()

