


class Database:
    def __init__(self):
        self.data = dict()


    def addDataGroup(self, data_group_name: str):
        self.data[data_group_name] = dict()


    def removeDataGroup(self, data_group_name: str):
        del self.data[data_group_name]


    def getDataGroup(self, data_group_name: str):
        try:
            return self.data[data_group_name]
        except KeyError:
            return 'Datagroup not exist'


    def addDataGroupData(self, data_group_name: str, key: str, value):
        self.data[data_group_name][key] = value


    def removeDataGroupData(self, data_group_name: str, key: str):
        del self.data[data_group_name][key]


    def getDataGroupData(self, data_group_name: str, key: str):
        try:
            return self.data[data_group_name][key]
        except KeyError:
            return 'Datagroup / Key not exist'