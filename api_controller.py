import json
import api_comm as comm
import DB_class.DB_characters as character_db
import DB_class.DB_items as item_db


class CollectDbFlow:
    db_char = character_db.GameCharacters()
    db_item = item_db.GameItems()

    def __init__(self):
        self.__com = comm.CommToApiServer()

    # Collect character DB
    def collectCharacterDB(self):
        res = self.__com.get_characterInform()
        body = json.loads(res["body"])
        for chars in body.get("rows"):
            self.db_char.checkAddOrUpdate(chars)
        self.db_char.saveDB()

    def collectItems(self):
        char = self.db_char.getDB()
        for char_id in char:
            res = self.__com.search_item("E ", "front", 100, [char_id["characterId"]])
            body = json.loads(res["body"])
            print(body)
            for item in body.get("rows"):
                self.db_item.checkAddOrUpdate(item)
        self.db_item.saveDB()


a = CollectDbFlow()
a.collectItems()
# print(a.db_item.getDB())
# a.collectCharacterDB()
