import api_comm as comm
import json
from DB_class.user_param.param_db import *
import DB_class.user_param.param_path as path_define
from DB_class.DB_parser import *
from DB_class.DB_config import *
from DB_class.user_param.param_private import *


class CollectDbFlow:
    __db_collect_mode = False

    def __init__(self, param_ip, param_id, param_pw, param_db, param_api_key: list):
        self.__com = comm.CommToApiServer(param_api_key[0])
        self.__sub_com = comm.CommToApiServer(param_api_key[1])
        self.__sql = MysqlController(param_ip, param_id, param_pw, param_db)
        self.parser = ApiParser()

    def get_api_com_error_list(self, save_enabled=False):
        err_list = self.__com.get_api_error_list()
        if save_enabled:
            path_define.make_dir(path_define.log_path)
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
            print(loop_user_count+1, "/", len(user_list))
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

    def collect_items(self, save_on_off=False):
        item_id_list = self.__sql.select_item_id()
        item_id_list_set = []
        temp_id_list = []
        for local_id in item_id_list:
            temp_id_list.append(local_id)
            if len(temp_id_list) == 30:
                item_id_list_set.append(copy.deepcopy(temp_id_list))
                temp_id_list = []
        if len(temp_id_list) > 0:
            item_id_list_set.append(copy.deepcopy(temp_id_list))

        local_item_id_list = []
        for item_id_lst in item_id_list_set:
            res = self.response_code(self.__com.lookup_item_multi_info(item_id_lst))
            local_item_id_list += self.parser.item_multi_info(res)

        if save_on_off:
            for item_database in local_item_id_list:
                self.__sql.insert_item(item_database)
            print("Item Db save complete!!")
        return local_item_id_list

    def collect_attributes(self, save_on_off=False):
        attribute_id_list = self.__sql.select_attribute_id()
        local_attribute_db_list = []
        for local_id in attribute_id_list:
            res = self.response_code(self.__com.lookup_position_attribute(local_id))
            local_attribute_db_list.append((self.parser.attribute_info(res)))

        if save_on_off:
            for attribute_database in local_attribute_db_list:
                self.__sql.insert_attribute(attribute_database)
            print("Attribute Db save complete!!")
        return local_attribute_db_list

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
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            print("DB Save End")

    def trigger_normal_based(self, rank_min, rank_max, days):
        temp_day_end = datetime.datetime.now()
        temp_day_start = datetime.datetime.now() - datetime.timedelta(days)

        user_list = self.collect_normal_ranker_id(rank_min, rank_max)
        [local_user_db, local_match_db, local_match_detail_db] = \
            self.collect_game_information(user_list, temp_day_start, temp_day_end, normal)

        if self.__db_collect_mode:
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
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            print("DB Save End")

    def continuous_collecting(self, rating_tier, search_direction,
                              ref_early_date: datetime.timedelta = datetime.timedelta(minutes=10)):
        player_id_list = self.__sql.select_by_rating(rating_tier)
        if len(player_id_list) is 0:
            return

        search_date = self.__sql.select_search_date()
        ref_date: datetime
        other_date: datetime
        if search_direction == "past":
            early_date = search_date[rating_tier][0] - ref_early_date
            later_date = search_date[rating_tier][0] + datetime.timedelta(minutes=1)
            search_date[rating_tier][0] -= ref_early_date
        elif search_direction == "recent":
            if search_date[rating_tier][1] - ref_early_date < datetime.datetime.now():
                early_date = search_date[rating_tier][1] - datetime.timedelta(minutes=1)
                later_date = search_date[rating_tier][1] + ref_early_date
                search_date[rating_tier][1] += ref_early_date
            else:
                return
        else:
            return

        [local_user_db, local_match_db, local_match_detail_db] = \
            self.collect_game_information(player_id_list, early_date, later_date, rating)

        if self.__db_collect_mode:
            self.save_play_info_to_sql(local_user_db, local_match_db, local_match_detail_db)
            self.__sql.update_search_date(rating_tier, search_date[rating_tier][0], search_date[rating_tier][1])
            print("DB Save End")

    def get_collecting_date(self):
        return self.__sql.select_search_date()


