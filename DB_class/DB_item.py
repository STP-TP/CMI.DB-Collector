import pickle
import DB_class.user_param.param_path as path_define


class GameItems:
    __item_list = []
    __db_init = False
    __item = {
        "itemId": "",
        "itemName": "",
        "slotCode": "",
        "slotName": "",
        "rarityCode": "",
        "rarityName": "",
        "equipSlotCode": "",
        "equipSlotName": ""
    }
    __path = path_define.item_path

    def __init__(self):
        if GameItems.__db_init is False:
            GameItems.loadDB()
            GameItems.__db_init = True

    def checkAddOrUpdate(self, db_input):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GameItems.__item_list)
                    if item["itemId"] == db_input["itemId"]), None)
        if row is None:
            self.addDB(db_input)
            return "Add"
        else:
            self.updateDB(row, db_input)
            return "Update"

    @staticmethod
    def addDB(db_input):
        GameItems.__item_list.append(db_input)

    @staticmethod
    def updateDB(row, db_input):
        GameItems.__item_list[row] = db_input

    @classmethod
    def saveDB(cls):
        with open(cls.__path, 'wb') as file_out:
            pickle.dump(GameItems.__item_list, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.__path, 'rb') as file_in:
                GameItems.__item_list = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__item_list

