import json
from DB_class.DB_user import *
from DB_class.DB_match import *
from DB_class.DB_match_detail import *
from DB_class.DB_other import *
import DB_class.user_param.param_db as db_naming
import datetime
import copy


def convert_str_to_datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")


class ApiParser:
    __user = User()
    __match_rating = MatchList("rating")
    __match_normal = MatchList("normal")
    __detail = MatchDetailList()

    __position = GamePositions()
    __item = GameItems()
    __character = GameCharacters()
    __attribute = GameAttribute()
    __map = GameMaps()

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
        return body["rows"][db_naming.player_id]

    def player_info(self, body):
        for key, val in body.items():
            if key == "records":
                self.__user.db[db_naming.rating_win] = val[0][db_naming.win_count]
                self.__user.db[db_naming.rating_lose] = val[0][db_naming.lose_count]
                self.__user.db[db_naming.rating_stop] = val[0][db_naming.stop_count]
                self.__user.db[db_naming.normal_win] = val[1][db_naming.win_count]
                self.__user.db[db_naming.normal_lose] = val[0][db_naming.lose_count]
                self.__user.db[db_naming.normal_stop] = val[0][db_naming.stop_count]
            self.__user.db[key] = val
        return self.__user.db

    @staticmethod
    def player_matching_record(body):  # return match id list
        matches = body["matches"]
        match_list = []
        for match in matches["rows"]:
            match_list.append(match[db_naming.match_id])
        return match_list

    def match_detail_info(self, match_id, body):
        match = copy.deepcopy(self.__match_normal.db)
        if body[db_naming.game_type_id] == db_naming.normal:
            match[db_naming.game_type_id] = db_naming.normal
        elif body[db_naming.game_type_id] == db_naming.rating:
            match[db_naming.game_type_id] = db_naming.rating
        match[db_naming.match_id] = match_id
        match[db_naming.date] = convert_str_to_datetime(body[db_naming.date])
        match[db_naming.game_type_id] = body[db_naming.game_type_id]
        player_list = []
        for result in body["teams"]:
            for user in result[db_naming.players]:
                player_list.append(user)
        match[db_naming.players] = player_list

        match_detail_db = []
        for inx, user in enumerate(body[db_naming.players]):
            db = copy.deepcopy(self.__detail.db)
            db[db_naming.match_id] = match_id
            db[db_naming.player_id] = user[db_naming.player_id]
            if inx < 5:
                db[db_naming.result] = "win"
            else:
                db[db_naming.result] = "lose"
            play_info = user["playInfo"]
            for key, val in play_info.items():
                if key == db_naming.character_name:
                    continue
                db[key] = val
            pos = user[db_naming.position]
            db[db_naming.position] = pos[db_naming.name]
            attribute_list = []
            for attribute in pos[db_naming.attribute]:
                attribute_list.append(attribute["id"])
            db[db_naming.attribute] = attribute_list
            item_list = []
            for item in user[db_naming.items]:
                item_list.append(item[db_naming.item_id])
            db[db_naming.items] = item_list
            match_detail_db.append(db)

        # one match, ten match_details
        return [match, match_detail_db, player_list]

    def total_ranking(self, body):
        pass

    def character_ranking(self, body):
        pass

    def battle_arena_ranking(self, body):
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
