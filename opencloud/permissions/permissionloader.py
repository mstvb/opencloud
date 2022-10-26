

class PermissionLoader:
    def __init__(self):
        self.permissions = dict()


    def addPermission(self, perm):
        if "getPermissionName" and "getPermissionStatus" in dir(perm):
            self.permissions[perm.getPermissionName()] = perm
        else:
            pass


    def setPermissionStatus(self, perm_name: str, status: bool):
        if perm_name in self.permissions:
            permission = self.permissions[perm_name]
            permission.setStatus(status)
        else:
            pass


    def getPermissionStatus(self, perm_name: str):
        return self.permissions[perm_name].getPermissionStatus()


    def getPermission(self, perm_name: str):
        return self.permissions[perm_name]


    def hasPermission(self, perm_name: str):
        return True if perm_name in self.permissions else False


    def deletePermission(self, perm_name: str):
        if perm_name in self.permissions:
            del self.permissions[perm_name]
