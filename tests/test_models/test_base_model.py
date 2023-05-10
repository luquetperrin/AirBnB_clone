#!/usr/bin/python3

"""Unittests for base_model.py on BaseModel class."""
from models.base_model import BaseModel


import unittest
import datetime

class TestBaseModel(unittest.TestCase):
    """Defines tests on methods."""

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        pass

    def test_is_instance(self):
        """Checks whether the object is an instance of base class."""
        self.assertEqual(type(BaseModel()).__name__, "BaseModel")

    def test_different_id(self):
        """Tests if two objects have diffrent ids."""
        self.my_model2 = BaseModel()
        self.assertNotEqual(self.my_model.id, self.my_model2)

    def test_attribute_type(self):
        """Tests the type of attributes."""
        self.assertEqual(str, type(self.my_model.id))
        self.assertEqual(datetime.datetime, type(self.my_model.created_at))
        self.assertEqual(datetime.datetime, type(self.my_model.updated_at))

    def test_save(self):
        """Tests if updated_at changes."""
        before_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(before_update, self.my_model.updated_at)

    def test_to_dict(self):
        self.assertEqual(type(self.my_model.to_dict()), dict)
        self.assertEqual(type(self.my_model.to_dict()["updated_at"]), str)
        self.assertEqual(type(self.my_model.to_dict()["created_at"]), str)
        self.assertIn("__class__", self.my_model.to_dict())
if __name__ == '__main__':
    unittest.main()
