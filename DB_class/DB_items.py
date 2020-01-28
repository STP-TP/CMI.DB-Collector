import pickle
import os

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
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\item.pkl'
        with open(path, 'wb') as fout:
            pickle.dump(GameItems.item_list, fout)

    def loadDB(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '\DB\item.pkl'
        with open(path, 'rb') as fin:
            GameItems.item_list = pickle.load(fin)

