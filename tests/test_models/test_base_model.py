#!/usr/bin/python3


import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init_with_args(self):
        # Test if the __init__ method works with keyword arguments
        data = {
            'id': '1',
            'created_at': '2023-10-01T12:34:56.789',
            'updated_at': '2023-10-02T10:20:30.456',
            'name': 'Test Model'
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, '1')
        self.assertEqual(instance.created_at, datetime(2023, 10, 1, 12, 34, 56, 789000))
        self.assertEqual(instance.updated_at, datetime(2023, 10, 2, 10, 20, 30, 456000))
        self.assertEqual(instance.name, 'Test Model')

    def test_init_with_no_args(self):
        # Test if the __init__ method works without any arguments
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_method(self):
        # Test the save method to ensure 'updated_at' is updated
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method to ensure it returns the expected dictionary
        instance = BaseModel(id='1', name='Test Model')
        expected_dict = {
            '__class__': 'BaseModel',
            'id': '1',
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
            'name': 'Test Model'
        }
        self.assertEqual(instance.to_dict(), expected_dict)

    def test_from_dict_method(self):
        # Test the from_dict method to ensure it recreates an instance correctly
        data = {
            '__class__': 'BaseModel',
            'id': '1',
            'created_at': '2023-10-01T12:34:56.789',
            'updated_at': '2023-10-02T10:20:30.456',
            'name': 'Test Model'
        }
        instance = BaseModel.from_dict(data)
        self.assertIsInstance(instance, BaseModel)
        self.assertEqual(instance.id, '1')
        self.assertEqual(instance.created_at, datetime(2023, 10, 1, 12, 34, 56, 789000))
        self.assertEqual(instance.updated_at, datetime(2023, 10, 2, 10, 20, 30, 456000))
        self.assertEqual(instance.name, 'Test Model')

if __name__ == '__main__':
=======
"""Test class for BaseModel"""
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import unittest

class BaseModel_tests(unittest.TestCase):
    """class to do TDD on the BaseModel class"""
    
    def test_init(self):
        """test the init method of the BaseModel"""
        example = BaseModel()
        self.assertIsInstance(example.id, str)
        self.assertIsInstance(example.created_at, datetime)
        self.assertIsInstance(example.updated_at, datetime)

    def test_to_dict(self):
        """tests the to dict method if it return a dictionary"""
        my_instance = BaseModel()
        data = my_instance.to_dict()
        self.assertIsInstance(data, dict)

    def test_from_dict(self):
        """test if the from_dict method recreates the instance correctly"""
        instance_2 = BaseModel()


if __name__ == "__main__":
>>>>>>> 868615a6be4735b0cea9325785f139c72870912c
    unittest.main()
