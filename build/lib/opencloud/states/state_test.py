

import time
import unittest
from opencloud.states import StateLoader, StateTemplate


test_state = StateTemplate('state', 'HELLO', 'BYE', None, None) # STATE TEMPLATE FOR UNIT TESTING


class AddState(unittest.TestCase):
    def test_add_state(self):
        self.state = test_state
        self.stateloader = StateLoader()
        self.stateloader.addState(self.state)
        self.assertTrue(self.stateloader.isExisted("state")) # UNIT TEST


class SetStateWithName(unittest.TestCase):
    def test_set_with_name(self):
        self.state = test_state
        self.stateloader = StateLoader()
        self.stateloader.addState(self.state)
        self.stateloader.setState("state")
        self.assertTrue(self.stateloader.isExisted('state')) # UNIT TEST
        self.stateloader.stopState()


class SetStateWithID(unittest.TestCase):
    def test_set_with_id(self):
        self.state = test_state
        self.stateloader = StateLoader()
        self.stateloader.addState(self.state)
        self.stateloader.setState('state')
        self.assertTrue(self.stateloader.isActive()) # UNIT TEST
        self.stateloader.stopState()


class SetStateWithoutAutostart(unittest.TestCase):
    def test_without_startup(self):
        self.state = test_state
        self.stateloader = StateLoader()
        self.stateloader.addState(self.state)
        self.stateloader.setState('state', auto_start=False)
        self.stateloader.startState()
        self.stateloader.stopState()
        self.assertFalse(self.stateloader.isActive())


if __name__ == '__main__':
    unittest.main()
