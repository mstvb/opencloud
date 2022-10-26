

from opencloud.states import StateTemplate, StateLoader
from opencloud.database import Database
from opencloud.permissions import Permission, PermissionLoader


if __name__ == '__main__':
    loader = StateLoader()
    state = StateTemplate('state', None, None, '', '')
    loader.addState(state)
    loader.setState('state', auto_start=False)
    loader.startState()
    loader.stopState()