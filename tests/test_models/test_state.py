#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):

    def test_state_name_default(self):
        state = State()
        self.assertEqual(state.name, "", "Default state name should be an empty string")

    def test_state_name_assignment(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California", "State name assignment failed")

    def test_state_str_representation(self):
        state = State()
        state.name = "New York"
        self.assertEqual(str(state), "State(name='New York')", "String representation is incorrect")

    def test_state_to_dict(self):
        state = State()
        state_data = state.to_dict()
        expected_data = {
            'id': state.id,
            'created_at': state.created_at.isoformat(),
            'updated_at': state.updated_at.isoformat(),
            'name': state.name,
        }
        self.assertEqual(state_data, expected_data, "to_dict() output is incorrect")

if __name__ == '__main__':
    unittest.main()
