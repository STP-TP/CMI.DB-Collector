import pickle
import DB_class.user_param.param_path as path_define


class GameItems:
    item_list = []
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
    path = path_define.item_path

    def checkAddOrUpdate(self, item):
        # DB와 id 존재 유무 체크
        row = next((index for (index, item) in enumerate(GameItems.item_list)
                    if item["itemId"] == item["itemId"]), None)
        if row is None:
            self.addDB(item)
            return "Add"
        else:
            self.updateDB(row, item)
            return "Update"

    def addDB(self, item):
        GameItems.item_list.append(item)

    def updateDB(self, row, item):
        GameItems.item_list[row] = item

    def saveDB(self):
        with open(self.path, 'wb') as file_out:
            pickle.dump(GameItems.item_list, file_out)

    def loadDB(self):
        with open(self.path, 'rb') as file_in:
            GameItems.item_list = pickle.load(file_in)

