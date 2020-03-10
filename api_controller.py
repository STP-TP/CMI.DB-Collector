import json
import api_comm as comm
import DB_class.DB_other as DbOther
import DB_class.DB_user as userDb
import datetime
from DB_class.DB_parser import *


class CollectDbFlow:
    db_char = DbOther.GameCharacters()
    db_item = DbOther.GameItems()
    db_user = userDb.User()
    __db_collect_mode = False
    parser = ApiParser()

    def __init__(self):
        self.__com = comm.CommToApiServer()

    def set_collect_mode(self, mode):
        self.__db_collect_mode = mode

    @staticmethod
    def response_code(response):
        if response["code"] == 200:
            return json.loads(response["body"])
        else:
            print(response["explain"])
            return None

    # Collect character DB
    def collect_character_db(self):
        body = self.response_code(self.__com.get_character_info())
        if body is None:
            return

        for chars in body.get("rows"):
            self.db_char.overlap_check(chars)
        self.db_char.save_db()

    def collect_items(self):
        char = self.db_char.get_db()
        for char_id in char:
            res = self.__com.search_item("E ", "front", 100, [char_id["characterId"]])
            body = json.loads(res["body"])
            print(body)
            for item in body.get("rows"):
                self.db_item.overlap_check(item)
        self.db_item.save_db()

    def collect_ranker_id_tier_score(self, rank_min, rank_max):
        res = self.__com.lookup_total_rating_ranking(rank_min, rank_max)
        body = json.loads(res["body"])
        for ranker_id in body["rows"]:
            res = self.__com.lookup_player_info(ranker_id["playerId"])
            body_id = json.loads(res["body"])
            self.db_user.overlap_check(body_id)
        self.db_user.save_db()

    def trigger_rating_based(self, rank_min, rank_max, days):
        if self.__db_collect_mode:
            res = self.__com.lookup_total_rating_ranking(rank_min, rank_max)
            body = json.loads(res["body"])
            for ranker_id in body["rows"]:
                # user list
                res = self.__com.lookup_player_info(ranker_id["playerId"])
                body_id = json.loads(res["body"])
                self.db_user.overlap_check(body_id)
            self.db_user.save_db()
        user_list = self.db_user.get_db()
        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)
        player_id = "b4e521441196692b1030ab83a7350ad7"

        body = self.response_code(self.__com.lookup_player_match(player_id, "normal", 100, day_start, day_end))
        if body is None:
            return
        match_id_list = self.parser.player_matching_record(body)

        match_id = match_id_list[0]
        body = self.response_code(self.__com.lookup_match_info(match_id))
        if body is None:
            return
        self.parser.match_detail_info(match_id, body)
        # for match_id in match_id_list:

    def trigger_normal_based(self, rank_min, rank_max, days):
        for char in CollectDbFlow.db_char.get_db():
            res = self.__com.lookup_total_character_ranking(char["characterId"], "exp", rank_min, rank_max)
            body = json.loads(res["body"])
            rows = body["rows"]
            for ranker_id in rows:
                # user list
                res = self.__com.lookup_player_info(ranker_id["playerId"])
                body_id = json.loads(res["body"])
                self.db_user.overlap_check(body_id)

                # user match info
                day_end = datetime.datetime.now()
                day_start = datetime.datetime.now() - datetime.timedelta(days)
                player_id = ranker_id["playerId"]
                res = self.__com.lookup_player_match(player_id, "normal", 100, day_start, day_end)
                body = json.loads(res["body"])
                rows = body["matches"]["rows"]
                print(rows)
            self.db_user.save_db()

    def trigger_nickname(self, nickname, game_type="rating", days=7):
        res = self.__com.lookup_nickname(nickname)
        body = json.loads(res["body"])
        rows = body["rows"]
        if len(rows) == 0:
            pass

        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)
        res = self.__com.lookup_player_match(rows[0]["playerId"], game_type, 100, day_start, day_end)
        body = json.loads(res["body"])
        rows = body["matches"]["rows"]
        print(rows)  # match info save

        for match in rows:
            res = self.__com.lookup_match_info(match["matchId"])
            body = json.loads(res["body"])
            print(body)
            # rows_match = body["rows"]
            # print(rows_match)


a = CollectDbFlow()
"""a.set_collect_mode(True)
a.collect_items()
a.collect_character_db()"""

a.set_collect_mode(False)

a. trigger_rating_based(0, 150, 1)
# a.trigger_normal_based(0, 5, 1)
# a.trigger_nickname("Papico", "normal")
