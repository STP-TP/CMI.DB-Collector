import json
import api_comm as comm
import DB_class.DB_character as characterDb
import DB_class.DB_item as itemDb


class CollectDbFlow:
    db_char = characterDb.GameCharacters()
    db_item = itemDb.GameItems()

    def __init__(self):
        self.__com = comm.CommToApiServer()

    # Collect character DB
    def collectCharacterDB(self):
        res = self.__com.get_characterInfo()
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

    def collectRankerId_tierScore(self, rank_min, rank_max):
        self.__com.lookup_totalRatingRanking(0, 100)


a = CollectDbFlow()
a.collectItems()
# print(a.db_item.getDB())
# a.collectCharacterDB()
