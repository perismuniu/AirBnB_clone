#!/usr/bin/python3
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
    unittest.main()
