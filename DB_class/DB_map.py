import pickle
import DB_class.user_param.param_path as path_define


class GameMaps:
    __map_list = []
    __db_init = False
    __map = {
        "mapId": "",
        "name": "",
    }
    path = path_define.map_path

    def checkAddOrUpdate(self, db_input):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GameMaps.__map_list)
                    if item["mapId"] == db_input["mapId"]), None)
        if row is None:
            self.addDB(db_input)
            return "Add"
        else:
            self.updateDB(row, db_input)
            return "Update"

    @staticmethod
    def addDB(db_input):
        GameMaps.__map_list.append(db_input)

    @staticmethod
    def updateDB(row, db_input):
        GameMaps.__map_list[row] = db_input

    @classmethod
    def saveDB(cls):
        with open(cls.path, 'wb') as file_out:
            pickle.dump(GameMaps.__map_list, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.path, 'rb') as file_in:
                GameMaps.__map_list = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__map_list
