


class Permission:
    def __init__(self, perm_name: str, perm_status: bool):
        self.data = {'perm_name': perm_name, 'perm_status': perm_status}


    def setStatus(self, status: bool):
        self.data['perm_status'] = status


    def getPermissionStatus(self):
        return self.data['perm_status']


    def getPermissionName(self):
        return self.data['perm_name']