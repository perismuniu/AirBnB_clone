#!/usr/bin/python3

import models
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_create_base_model_with_no_arguments(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_create_base_model_with_attributes(self):
        data = {
            'name': 'Test Model',
            'value': 42
        }
        model = BaseModel(**data)
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.value, 42)

    def test_create_base_model_with_invalid_attributes(self):
        data = {
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000'
        }
        model = BaseModel(**data)
        # created_at and updated_at should not be directly set using kwargs
        self.assertNotEqual(model.created_at, '2022-01-01T00:00:00.000')
        self.assertNotEqual(model.updated_at, '2022-01-02T00:00:00.000')

    def test_save_method_updates_updated_at(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

    def test_from_dict_method(self):
        data = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000',
            'name': 'Test Model',
            'value': 42
        }
        model = BaseModel.from_dict(data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.value, 42)

    def test_str_representation(self):
        model = BaseModel(id='123', name='Test Model', value=42)
        expected_str = "[BaseModel] (123) {'id': '123', 'name': 'Test Model', 'value': 42}"
        self.assertEqual(str(model), expected_str)

if __name__ == '__main__':
    unittest.main()
