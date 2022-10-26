

class PermissionLoader:
    def __init__(self):
        self.permissions = dict()


    def addPermission(self, perm):
        if "getPermissionName" and "getPermissionStatus" in dir(perm):
            self.permissions[perm.getPermissionName()] = perm
        else:
            pass


    def getPermission(self, perm_name: str):
        return self.permissions[perm_name]


    def hasPermission(self, perm_name: str):
        return True if self.permissions[perm_name] else False


    def deletePermission(self, perm_name: str):
        if perm_name in self.permissions:
            del self.permissions[perm_name]
