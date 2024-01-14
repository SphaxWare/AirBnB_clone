#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    TestState
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the StateModel class."""
    def test_state_instantiation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
