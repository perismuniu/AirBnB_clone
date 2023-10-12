#!/usr/bin/python3
"""Test class for BaseModel"""
from datetime import datetime
from models.base_model import BaseModel
import unittest

class BaseModel_tests(unittest.TestCase):
    """class to do TDD on the BaseModel class"""
    
    def test_init(self):
        example = BaseModel()
        self.assertIsInstance(example.id, str)
        self.assertIsInstance(example.created_at, datetime)
        self.assertIsInstance(example.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
