import json
import api_comm as comm
import DB_class.DB_other as otherDb
import DB_class.DB_user as userDb
import DB_class.DB_match as matchDb
import DB_class.DB_match_detail as matchDetailDb
import DB_class.user_param.param_db as db_naming
import datetime
from DB_class.DB_parser import *


class CollectDbFlow:
    db_char = otherDb.GameCharacters()
    db_item = otherDb.GameItems()
    db_user = userDb.User()
    db_match_normal = matchDb.MatchList(db_naming.normal)
    db_match_rating = matchDb.MatchList(db_naming.rating)
    db_match_detail = matchDetailDb.MatchDetailList()
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

    def collect_game_information(self, user_list, day_start, day_end, game_type=db_naming.rating):
        match_list = []
        user_db = []
        match_db = []
        match_detail_db = []
        player_dict = {}
        match_dict = {}

        loop_user_count = 0
        loop_match_count = 0
        while True:
            if len(user_list) <= loop_user_count:
                break
            print(loop_user_count, "/", len(user_list))
            player_id = user_list[loop_user_count]
            loop_user_count += 1
            if player_id in player_dict:
                continue
            # get player info
            body = self.response_code(self.__com.lookup_player_info(player_id))
            if body is None:
                continue
            user_db.append(body)
            body = self.response_code(self.__com.lookup_player_match(player_id, game_type, 100, day_start, day_end))
            player_dict[player_id] = True
            if body is None:
                continue
            match_list = match_list + self.parser.player_matching_record(body)
            while True:
                if len(match_list) <= loop_match_count:
                    break
                match_id = match_list[loop_match_count]
                loop_match_count += 1
                if match_id in match_dict:
                    continue
                body = self.response_code(self.__com.lookup_match_info(match_id))
                match_dict[match_id] = True
                if body is None:
                    continue
                else:
                    res = self.parser.match_detail_info(match_id, body)
                    match_db.append(res[0])
                    match_detail_db = match_detail_db + res[1]
                    user_list = user_list + res[2]
        return user_db, match_db, match_detail_db

    def save_play_info_to_pickle(self, user_db, match_db, match_detail_db):
        self.db_user.update_new_db_list(user_db)
        self.db_user.save_db()
        self.db_match_rating.update_new_db_list(match_db)
        self.db_match_rating.save_db()
        self.db_match_detail.update_new_db_list(match_detail_db)
        self.db_match_detail.save_db()

    def collect_character_db(self, save_on_off=False):
        """ return: character db list """
        body = self.response_code(self.__com.get_character_info())
        if body is None:
            return
        character_db = self.parser.character_info(body)
        return character_db

    def collect_items(self):
        char = self.db_char.get_db()
        for char_id in char:
            res = self.__com.search_item("E ", "front", 100, [char_id[db_naming.character_id]])
            body = json.loads(res["body"])
            for item in body.get("rows"):
                self.db_item.overlap_check(item)
        self.db_item.save_db()

    def collect_rating_ranker_id(self, rank_min, rank_max):
        user_list = []
        body = self.response_code(self.__com.lookup_total_rating_ranking(rank_min, rank_max))
        if body is None:
            return
        for ranker_id in body["rows"]:
            user_list.append(ranker_id[db_naming.player_id])

        return user_list

    def collect_normal_ranker_id(self, rank_min, rank_max):
        user_list = []
        character_db = self.collect_character_db()
        for character in character_db:
            char_id = character[db_naming.character_id]
            body = self.response_code(self.__com.lookup_total_character_ranking(char_id, "exp", rank_min, rank_max))
            if body is None:
                return
            char_rank_id = self.parser.character_ranking(body)
            user_list += char_rank_id

        return user_list

    def trigger_rating_based(self, rank_min, rank_max, days):
        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)

        user_list = self.collect_rating_ranker_id(rank_min, rank_max)
        [user_db, match_db, match_detail_db] = self.collect_game_information(user_list,
                                                                             day_start, day_end, db_naming.rating)

        if self.__db_collect_mode:
            self.save_play_info_to_pickle(user_db, match_db, match_detail_db)
            print("DB Save End")

    def trigger_normal_based(self, rank_min, rank_max, days):
        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)

        user_list = self.collect_normal_ranker_id(rank_min, rank_max)
        [user_db, match_db, match_detail_db] = self.collect_game_information(user_list,
                                                                             day_start, day_end, db_naming.normal)

        if self.__db_collect_mode:
            self.save_play_info_to_pickle(user_db, match_db, match_detail_db)
            print("DB Save End")

    def trigger_nickname(self, nickname, game_type=db_naming.rating, days=7):
        day_end = datetime.datetime.now()
        day_start = datetime.datetime.now() - datetime.timedelta(days)

        body = self.response_code(self.__com.lookup_nickname(nickname))
        if body is None:
            return
        user_list = self.parser.player_search(body)

        [user_db, match_db, match_detail_db] = self.collect_game_information(user_list,
                                                                             day_start, day_end, game_type)

        if self.__db_collect_mode:
            self.save_play_info_to_pickle(user_db, match_db, match_detail_db)
            print("DB Save End")


a = CollectDbFlow()
"""a.set_collect_mode(True)
a.collect_items()
a.collect_character_db()"""

a.set_collect_mode(True)

# a. trigger_rating_based(0, 20, 1)
a.trigger_normal_based(0, 5, 1)
# a.trigger_nickname("Papico", "normal")
