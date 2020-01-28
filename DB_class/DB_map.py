import pickle
import os


class GameMaps:
    map_list = []
    __map = {
        "mapId": "",
        "name": "",
    }

    def checkAddOrUpdate(self, item):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GameMaps.map_list)
                    if item["mapId"] == item["mapId"]), None)
        if row is None:
            self.addDB(item)
            return "Add"
        else:
            self.updateDB(row, item)
            return "Update"

    def addDB(self, item):
        GameMaps.map_list.append(item)

    def updateDB(self, row, item):
        GameMaps.map_list[row] = item

    def saveDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\map.pkl'
        with open(path, 'wb') as fout:
            pickle.dump(GameMaps.map_list, fout)

    def loadDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\map.pkl'
        with open(path, 'rb') as fin:
            GameMaps.map_list = pickle.load(fin)

