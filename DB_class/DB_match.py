import pickle
import DB_class.user_param.param_path as path_define
import datetime
import json
from DB_class.DB_manager import *


def convert_str_to_datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")


class MatchList(DbManager):
    db = {
        "date": type(datetime),
        "gameTypeId": str,
        "matchId": str,
        "players": list,  # player id 0-4 are win players, 5-9 are lose players
    }
    result = {
        "win": list,
        "lose": list
    }
    __game_type = {
        "rating": path_define.match_rating_path,
        "normal": path_define.match_normal_path
    }
    __option: str

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["matchId"] == db_input["matchId"]), None)
        return row

    def init_path(self, option):
        self._path = self.__game_type.get(option)
        self.__option = option

