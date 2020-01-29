import pickle
import DB_class.user_param.param_path as path_define


class GameMaps:
    map_list = []
    __map = {
        "mapId": "",
        "name": "",
    }
    path = path_define.map_path

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
        with open(self.path, 'wb') as file_out:
            pickle.dump(GameMaps.map_list, file_out)

    def loadDB(self):
        with open(self.path, 'rb') as file_in:
            GameMaps.map_list = pickle.load(file_in)

