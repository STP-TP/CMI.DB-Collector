import pickle
import os


class Positions:
    position_list = []
    __position = {
        "attributeId": "",
        "attributeName": "",
        "explain": "",
    }

    def checkAddOrUpdate(self, position):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(Positions.position_list)
                    if item["attributeId"] == position["attributeId"]), None)
        if row is None:
            self.addPositionDB(position)
            return "Add"
        else:
            self.updatePositionDB(row, position)
            return "Update"

    def addPositionDB(self, position):
        Positions.position_list.append(position)

    def updatePositionDB(self, row, position):
        Positions.position_list[row]["attributeName"] = position["attributeName"]
        Positions.position_list[row]["explain"] = position["explain"]

    def saveDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\position.pkl'
        with open(path, 'wb') as fout:
            pickle.dump(Positions.position_list, fout)

    def loadDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\position.pkl'
        with open(path, 'rb') as fin:
            Positions.position_list = pickle.load(fin)

