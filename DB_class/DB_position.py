import pickle
import DB_class.user_param.param_path as path_define


class GamePositions:
    position_list = []
    __position = {
        "attributeId": "",
        "attributeName": "",
        "explain": "",
    }
    __path = path_define.position_path

    def checkAddOrUpdate(self, position):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GamePositions.position_list)
                    if item["attributeId"] == position["attributeId"]), None)
        if row is None:
            self.addDB(position)
            return "Add"
        else:
            self.updateDB(row, position)
            return "Update"

    def addDB(self, position):
        GamePositions.position_list.append(position)

    def updateDB(self, row, position):
        GamePositions.position_list[row] = position

    def saveDB(self):
        with open(self.__path, 'wb') as file_out:
            pickle.dump(GamePositions.position_list, file_out)

    def loadDB(self):
        with open(self.__path, 'rb') as file_in:
            GamePositions.position_list = pickle.load(file_in)

