import json
import api_comm as comm
import DB_class.DB_character as characterDb
import DB_class.DB_item as itemDb
import DB_class.DB_user as userDb
import datetime


class CollectDbFlow:
    db_char = characterDb.GameCharacters()
    db_item = itemDb.GameItems()
    db_user = userDb.User()
    __db_collect_mode = False

    def __init__(self):
        self.__com = comm.CommToApiServer()

    def setCollectMode(self, mode):
        self.__db_collect_mode = mode

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
        res = self.__com.lookup_totalRatingRanking(rank_min, rank_max)
        body = json.loads(res["body"])
        for ranker_id in body["rows"]:
            res = self.__com.lookup_playerInfo(ranker_id["playerId"])
            body_id = json.loads(res["body"])
            self.db_user.checkAddOrUpdate(body_id)
        self.db_user.saveDB()

    def trigger_rating_based(self, rank_min, rank_max, days):
        if self.__db_collect_mode:
            res = self.__com.lookup_totalRatingRanking(rank_min, rank_max)
            body = json.loads(res["body"])
            for ranker_id in body["rows"]:
                # user list
                res = self.__com.lookup_playerInfo(ranker_id["playerId"])
                body_id = json.loads(res["body"])
                self.db_user.checkAddOrUpdate(body_id)
            self.db_user.saveDB()
        user_list = self.db_user.getDB()
        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)
        player_id = user_list[1]["playerId"]

        res = self.__com.lookup_playerMatch(player_id, "rating", 100, day_start, day_end)
        body = json.loads(res["body"])
        print(body)

        """for user in user_list:
            
            user["playerId"]"""


a = CollectDbFlow()
"""a.setCollectMode(True)
a.collectItems()
a.collectCharacterDB()"""

a.setCollectMode(False)

a. trigger_rating_based(1, 150, 1)

