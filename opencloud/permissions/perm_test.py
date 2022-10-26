

import unittest
from opencloud.permissions import Permission, PermissionLoader


test_permission = Permission('permission', True)


class AddPermission(unittest.TestCase):
    def test_addPermission(self):
        self.permission = test_permission
        self.loader = PermissionLoader()
        self.loader.addPermission(self.permission)
        self.assertTrue(self.loader.hasPermission('permission'))


class ChangePermissionStatus(unittest.TestCase):
    def test_change_status(self):
        self.permission = test_permission
        self.loader = PermissionLoader()
        self.loader.addPermission(self.permission)
        self.loader.setPermissionStatus('permission', False)
        self.assertFalse(self.loader.getPermissionStatus('permission'))


class DeletePermission(unittest.TestCase):
    def test_delete_permission(self):
        self.permission = test_permission
        self.loader = PermissionLoader()
        self.loader.addPermission(self.permission)
        self.loader.deletePermission('permission')
        self.assertFalse(self.loader.hasPermission('permission'))


if __name__ == '__main__':
    unittest.main()
