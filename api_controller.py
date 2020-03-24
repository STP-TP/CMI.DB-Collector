import api_comm as comm
import json
import DB_class.DB_other as otherDb
import DB_class.DB_user as userDb
import DB_class.DB_match as matchDb
import DB_class.DB_match_detail as matchDetailDb
from DB_class.user_param.param_db import *
import DB_class.user_param.param_path as path_define
from DB_class.DB_parser import *
from DB_class.DB_config import *
from DB_class.user_param.param_private import *


class CollectDbFlow:
    db_char = otherDb.GameCharacters()
    db_item = otherDb.GameItems()
    db_user = userDb.User()
    db_match_normal = matchDb.MatchList(normal)
    db_match_rating = matchDb.MatchList(rating)
    db_match_detail = matchDetailDb.MatchDetailList()
    __db_collect_mode = False
    __sql = MysqlController(server_ip, server_id, server_pw, server_database)
    parser = ApiParser()

    def __init__(self):
        self.__com = comm.CommToApiServer()

    def get_api_com_error_list(self, save_enabled=False):
        err_list = self.__com.get_api_error_list()
        if save_enabled:
            # error save code
            with open(path_define.log_path + path_define.api_log, 'w') as outfile:
                json.dump(err_list, outfile)
            pass
        return err_list

    def set_collect_mode(self, mode):
        self.__db_collect_mode = mode

    @staticmethod
    def response_code(response):
        if response["code"] == 200:
            return json.loads(response["body"])
        else:
            print(response["explain"])
            return None

    def collect_game_information(self, user_list, day_start, day_end, game_type=rating):
        local_user_db = []
        local_match_db = []
        local_match_detail_db = []
        match_list = []
        player_dict = {}
        match_dict = {}

        loop_user_count = 0
        loop_match_count = 0
        while True:
            if len(user_list) <= loop_user_count:
                break
            print(loop_user_count, "/", len(user_list))
            temp_player_id = user_list[loop_user_count]
            loop_user_count += 1
            if temp_player_id in player_dict:
                continue
            # get player info
            body = self.response_code(self.__com.lookup_player_info(temp_player_id))
            if body is None:
                continue
            local_user_db.append(self.parser.player_info(body))
            body = self.response_code(
                self.__com.lookup_player_match(temp_player_id, game_type, 100, day_start, day_end))
            player_dict[temp_player_id] = True
            if body is None:
                continue
            res = self.parser.player_matching_record(body)
            match_list = match_list + res[0]
            while res[1]:
                body = self.response_code(self.__com.lookup_player_match_next(temp_player_id, res[1]))
                res = self.parser.player_matching_record(body)
                match_list = match_list + res[0]

            while True:
                if len(match_list) <= loop_match_count:
                    break
                temp_match_id = match_list[loop_match_count]
                loop_match_count += 1
                if temp_match_id in match_dict:
                    continue
                body = self.response_code(self.__com.lookup_match_info(temp_match_id))
                match_dict[temp_match_id] = True
                if body is None:
                    continue
                else:
                    res = self.parser.match_detail_info(temp_match_id, body)
                    local_match_db.append(res[0])
                    local_match_detail_db = local_match_detail_db + res[1]
                    user_list = user_list + res[2]
        return local_user_db, local_match_db, local_match_detail_db

    def save_play_info_to_sql(self, param_user_db, param_match_db, param_match_detail_db):
        for save_target in param_user_db:
            self.__sql.insert_user(save_target)
        for save_target in param_match_db:
            self.__sql.insert_match(save_target)
        for save_target in param_match_detail_db:
            self.__sql.insert_match_detail(save_target)

    def save_play_info_to_pickle(self, param_user_db, param_match_db, param_match_detail_db):
        self.db_user.update_new_db_list(param_user_db)
        self.db_user.save_db()
        self.db_match_rating.update_new_db_list(param_match_db)
        self.db_match_rating.save_db()
        self.db_match_detail.update_new_db_list(param_match_detail_db)
        self.db_match_detail.save_db()

    def load_play_info_from_pickle(self):
        self.db_user.load_db()
        self.db_match_normal.load_db()
        self.db_match_rating.load_db()
        self.db_match_detail.load_db()

    def collect_character_db(self, save_on_off=False):
        """return: character db list """
        body = self.response_code(self.__com.get_character_info())
        if body is None:
            return
        local_character_db = self.parser.character_info(body)
        if save_on_off:
            for char in local_character_db:
                self.__sql.insert_character(char)
            print("DB saved complete")
        return local_character_db

    def collect_items(self):
        char = self.db_char.get_db()
        for char_id in char:
            res = self.__com.search_item("E ", "front", 100, [char_id[character_id[api]]])
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
            user_list.append(ranker_id[player_id[api]])

        return user_list

    def collect_normal_ranker_id(self, rank_min, rank_max):
        user_list = []
        temp_character_db = self.collect_character_db()
        for character in temp_character_db:
            char_id = character[character_id[api]]
            body = self.response_code(self.__com.lookup_total_character_ranking(char_id, "exp", rank_min, rank_max))
            if body is None:
                return
            char_rank_id = self.parser.character_ranking(body)
            user_list += char_rank_id

        return user_list

    def trigger_rating_based(self, rank_min, rank_max, days):
        temp_day_end = datetime.datetime.now()
        temp_day_start = datetime.datetime.now() - datetime.timedelta(days)

        user_list = self.collect_rating_ranker_id(rank_min, rank_max)
        [local_user_db, local_match_db, local_match_detail_db] = \
            self.collect_game_information(user_list, temp_day_start, temp_day_end, rating)

        if self.__db_collect_mode:
            # self.save_play_info_to_pickle(local_user_db, local_match_db, local_match_detail_db)
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            print("DB Save End")

    def trigger_normal_based(self, rank_min, rank_max, days):
        temp_day_end = datetime.datetime.now()
        temp_day_start = datetime.datetime.now() - datetime.timedelta(days)

        user_list = self.collect_normal_ranker_id(rank_min, rank_max)
        [local_user_db, local_match_db, local_match_detail_db] = \
            self.collect_game_information(user_list, temp_day_start, temp_day_end, normal)

        if self.__db_collect_mode:
            # self.save_play_info_to_pickle(local_user_db, local_match_db, local_match_detail_db)
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            print("DB Save End")

    def trigger_nickname(self, param_nickname, param_game_type=rating, days=7):
        temp_day_end = datetime.datetime.now()
        temp_day_start = datetime.datetime.now() - datetime.timedelta(days)

        body = self.response_code(self.__com.lookup_nickname(param_nickname))
        if body is None:
            return
        user_list = self.parser.player_search(body)

        [local_user_db, local_match_db, local_match_detail_db] = \
            self.collect_game_information(user_list, temp_day_start, temp_day_end, param_game_type)

        if self.__db_collect_mode:
            # self.save_play_info_to_pickle(local_user_db, local_match_db, local_match_detail_db)
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            print("DB Save End")