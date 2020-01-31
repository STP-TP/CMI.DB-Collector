import pickle
import DB_class.user_param.param_path as path_define


class GameCharacters:
    __character_list = []
    __db_init = False
    __character = {
        "characterId": "",
        "characterName": "",
    }
    __path = path_define.character_path

    def __init__(self):
        if GameCharacters.__db_init is False:
            GameCharacters.loadDB()
            GameCharacters.__db_init = True

    def checkAddOrUpdate(self, db_input):
        # DB와 id 존재 유무 체크
        row = next((index for (index, char) in enumerate(GameCharacters.__character_list)
                    if char["characterId"] == db_input["characterId"]), None)
        if row is None:
            self.addDB(db_input)
            return "Add"
        else:
            self.updateDB(row, db_input)
            return "Update"

    @staticmethod
    def addDB(db_input):
        GameCharacters.__character_list.append(db_input)

    @staticmethod
    def updateDB(row, db_input):
        GameCharacters.__character_list[row] = db_input

    @classmethod
    def saveDB(cls):
        with open(cls.__path, 'wb') as file_out:
            pickle.dump(GameCharacters.__character_list, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.__path, 'rb') as file_in:
                GameCharacters.__character_list = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__character_list

