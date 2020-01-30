import pickle
import DB_class.user_param.param_path as path_define


class GamePositions:
    __position_list = []
    __db_init = False
    __position = {
        "attributeId": "",
        "attributeName": "",
        "explain": "",
    }
    __path = path_define.position_path

    def __init__(self):
        if GamePositions.__db_init is False:
            GamePositions.loadDB()
            GamePositions.__db_init = True

    def checkAddOrUpdate(self, db_input):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GamePositions.__position_list)
                    if item["attributeId"] == db_input["attributeId"]), None)
        if row is None:
            self.addDB(db_input)
            return "Add"
        else:
            self.updateDB(row, db_input)
            return "Update"

    @staticmethod
    def addDB(db_input):
        GamePositions.__position_list.append(db_input)

    @staticmethod
    def updateDB(row, db_input):
        GamePositions.__position_list[row] = db_input

    @classmethod
    def saveDB(cls):
        with open(cls.__path, 'wb') as file_out:
            pickle.dump(GamePositions.__position_list, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.__path, 'rb') as file_in:
                GamePositions.__position_list = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__position_list

