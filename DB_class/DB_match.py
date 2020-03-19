from DB_class.DB_manager import *
from DB_class.user_param.param_db import *


class MatchList(DbManager):
    db = match_db
    __game_type = {
        "rating": path_define.match_rating_path,
        "normal": path_define.match_normal_path
    }
    __option: str
    primary_key = match_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = self.__game_type.get(option)
        self.__option = option
