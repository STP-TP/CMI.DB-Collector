import json
from DB_class.DB_user import *
from DB_class.DB_match import *
from DB_class.DB_match_detail import *
from DB_class.DB_other import *
from DB_class.user_param.param_db import *
import datetime
import copy


def convert_str_to_datetime(param_date: str):
    return datetime.datetime.strptime(param_date, "%Y-%m-%d %H:%M")


class ApiParser:
    __user = User()
    __match_rating = MatchList(rating)
    __match_normal = MatchList(normal)
    __detail = MatchDetailList()

    __position = GamePositions()
    __item = GameItems()
    __character = GameCharacters()
    __attribute = GameAttribute()

    __api_number = {
        1: "플레이어 검색",
        2: "플레이어 정보 조회",
        3: "플레이어 매칭기록 조회",
        4: "매칭 상세 정보 조회",
        5: "통합 랭킹 조회",
        6: "캐릭터 랭킹 조회",
        7: "투신전 랭킹 조회",
        8: "아이템 검색",
        9: "아이템 상세 정보 조회",
        10: "다중 아이템 상세 정보 조회",
        11: "캐릭터 정보",
        12: "포지션 특성 조회",
    }

    @staticmethod
    def player_search(body):
        return body["rows"][player_id[api]]

    @staticmethod
    def player_info(body):
        temp_user_db = copy.deepcopy(user_db)
        for key, val in body.items():
            if key == "records":
                for game_record in val:
                    if game_record[game_type_id[api]] == rating:
                        temp_user_db[rating_win[sql]] = game_record[win_count[api]]
                        temp_user_db[rating_lose[sql]] = game_record[lose_count[api]]
                        temp_user_db[rating_stop[sql]] = game_record[stop_count[api]]
                    elif game_record[game_type_id[api]] == normal:
                        temp_user_db[normal_win[sql]] = game_record[win_count[api]]
                        temp_user_db[normal_lose[sql]] = game_record[lose_count[api]]
                        temp_user_db[normal_stop[sql]] = game_record[stop_count[api]]
            elif (key == tier_name[api]) and (val is None):
                temp_user_db[tier_name[sql]] = "Unranked"
            elif val is None:
                if type(temp_user_db[key]) is int:
                    temp_user_db[key] = 0
                elif type(temp_user_db[key]) is str:
                    temp_user_db[key] = ""
            else:
                temp_user_db[key] = val
        return temp_user_db

    @staticmethod
    def player_matching_record(body):  # return match id list
        matches = body["matches"]
        temp_match_list = []
        for match in matches["rows"]:
            temp_match_list.append(match[match_id[api]])
        return [temp_match_list, matches["next"]]

    @staticmethod
    def match_detail_info(param_match_id, body):
        local_match_db = copy.deepcopy(match_db)
        if body[game_type_id[api]] == normal:
            local_match_db[game_type_id[sql]] = normal
        elif body[game_type_id[api]] == rating:
            local_match_db[game_type_id[sql]] = rating
        local_match_db[match_id[sql]] = param_match_id
        local_match_db[date[sql]] = convert_str_to_datetime(body[date[api]])
        local_match_db[game_type_id[sql]] = body[game_type_id[api]]
        local_player_list = []
        for team in body["teams"]:
            for user in team[players[api]]:
                local_player_list.append(user)
        local_match_db[players[sql]] = local_player_list
        local_match_db[map_id[sql]] = body[players[api]][0]["map"][map_id[api]]
        local_match_db[map_name[sql]] = body[players[api]][0]["map"][map_name[api]]

        local_match_detail_db = []
        for inx, user in enumerate(body[players[api]]):
            temp_match_detail_db = copy.deepcopy(match_detail_db)
            temp_match_detail_db[match_id[sql]] = param_match_id
            temp_match_detail_db[player_id[sql]] = user[player_id[api]]
            if inx < 5:
                temp_match_detail_db[result[sql]] = "win"
            else:
                temp_match_detail_db[result[sql]] = "lose"
            play_info = user["playInfo"]
            for key, val in play_info.items():
                if key == character_name[api]:
                    continue
                temp_match_detail_db[key] = val
            pos = user[position[api]]
            temp_match_detail_db[position_name[sql]] = pos[position_name[api]]
            temp_attribute_list = []
            for attributes in pos[attribute[api]]:
                temp_attribute_list.append(attributes[attribute_id[api]])
            temp_match_detail_db[attribute[sql]] = temp_attribute_list
            item_temp_dict = copy.deepcopy(item_slot)
            for item in user[items[api]]:
                item_temp_dict[int(item[equip_slot_code[sql]])] = item[item_id[api]]
            temp_item_list = list(sorted(item_temp_dict.items()))
            temp_match_detail_db[items[sql]] = temp_item_list
            local_match_detail_db.append(temp_match_detail_db)

        # one match, ten match_details
        return [local_match_db, local_match_detail_db, local_player_list]

    def total_ranking(self, body):
        pass

    @staticmethod
    def character_ranking(body):
        user_list = []
        for user in body["rows"]:
            user_list.append(user[player_id[api]])
        return user_list

    def battle_arena_ranking(self, body):
        pass

    def item_search(self, body):
        pass

    def item_info(self, body):
        pass

    def item_multi_info(self, body):
        pass

    @staticmethod
    def character_info(body):
        char_db = []
        for character in body["rows"]:
            char_db.append(character)
        return char_db

    def position_info(self, body):
        pass

    def execute_api_number(self, number):
        if number is 1:
            pass
        elif number is 2:
            pass
        elif number is 3:
            pass
        elif number is 4:
            pass
        elif number is 5:
            pass
        elif number is 6:
            pass
        elif number is 7:
            pass
        elif number is 8:
            pass
        elif number is 9:
            pass
        elif number is 10:
            pass
        elif number is 11:
            pass
        elif number is 12:
            pass
