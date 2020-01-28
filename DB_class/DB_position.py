import pickle
import os


class GamePositions:
    position_list = []
    __position = {
        "attributeId": "",
        "attributeName": "",
        "explain": "",
    }

    def checkAddOrUpdate(self, position):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GamePositions.position_list)
                    if item["attributeId"] == position["attributeId"]), None)
        if row is None:
            self.addPositionDB(position)
            return "Add"
        else:
            self.updatePositionDB(row, position)
            return "Update"

    def addDB(self, position):
        GamePositions.position_list.append(position)

    def updateDB(self, row, position):
        GamePositions.position_list[row] = position

    def saveDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\position.pkl'
        with open(path, 'wb') as fout:
            pickle.dump(GamePositions.position_list, fout)

    def loadDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\position.pkl'
        with open(path, 'rb') as fin:
            GamePositions.position_list = pickle.load(fin)

